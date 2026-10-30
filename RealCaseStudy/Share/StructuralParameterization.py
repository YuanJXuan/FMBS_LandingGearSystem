# -*- coding: utf-8 -*-
"""Configuration-driven structural parameterization for ADM models.

The engine deliberately knows nothing about a particular landing-gear model.
Each case can provide a small JSON file that describes a driver Marker,
editable axes and optional dependent objects.  Models without such a file
keep the generic single-Marker editing workflow.
"""

from __future__ import print_function

import json
import math
import os


SUPPORTED_OPERATIONS = ("delta", "copy", "mirror", "offset")
VALID_AXES = ("x", "y", "z")
LOCKED_AXIS_TOLERANCE = 1.0e-7


class ConfigurationError(ValueError):
    """Raised when a structural-parameter JSON file is invalid."""


class AdjustmentResult(object):
    def __init__(self, success, message, updated=0, changed=False, errors=None):
        self.success = bool(success)
        self.message = str(message)
        self.updated = int(updated or 0)
        self.changed = bool(changed)
        self.errors = list(errors or [])


def _normalize_axes(value, field_name):
    if isinstance(value, str):
        value = [value]
    axes = []
    for axis in value or []:
        normalized = str(axis).strip().lower()
        if normalized not in VALID_AXES:
            raise ConfigurationError(
                "{} 包含无效方向：{}".format(field_name, axis)
            )
        if normalized not in axes:
            axes.append(normalized)
    if not axes:
        raise ConfigurationError("{} 至少需要一个方向".format(field_name))
    return tuple(axes)


def _normalize_follower(raw_follower, parameter_id, index):
    if not isinstance(raw_follower, dict):
        raise ConfigurationError(
            "参数 {} 的第 {} 个联动对象格式错误".format(parameter_id, index)
        )
    follower = dict(raw_follower)
    path = str(follower.get("path", "")).strip()
    if not path:
        raise ConfigurationError(
            "参数 {} 的第 {} 个联动对象缺少 path".format(parameter_id, index)
        )
    operation = str(follower.get("operation", "delta")).strip().lower()
    if operation not in SUPPORTED_OPERATIONS:
        raise ConfigurationError(
            "参数 {} 的联动对象 {} 使用了不支持的 operation：{}".format(
                parameter_id, path, operation
            )
        )
    follower["path"] = path
    follower["operation"] = operation
    follower["required"] = bool(follower.get("required", True))
    target_type = str(follower.get("target_type", "marker")).strip().lower()
    if target_type not in ("marker", "part"):
        raise ConfigurationError(
            "参数 {} 的联动对象 {} 使用了不支持的 target_type：{}".format(
                parameter_id, path, target_type
            )
        )
    follower["target_type"] = target_type
    if "axes" in follower:
        follower["axes"] = _normalize_axes(
            follower["axes"], "参数 {} 的 follower.axes".format(parameter_id)
        )
    return follower


def _finite_float(value, field_name):
    try:
        result = float(value)
    except (TypeError, ValueError):
        raise ConfigurationError("{} 必须是有效数字".format(field_name))
    if not math.isfinite(result):
        raise ConfigurationError("{} 不能是NaN或无穷大".format(field_name))
    return result


def _normalize_coaxial_group(raw_group, index):
    if not isinstance(raw_group, dict):
        raise ConfigurationError("第 {} 个共轴约束格式错误".format(index))
    group = dict(raw_group)
    group_id = str(group.get("id", "")).strip()
    start = str(group.get("start", "")).strip()
    end = str(group.get("end", "")).strip()
    if not group_id:
        raise ConfigurationError("第 {} 个共轴约束缺少 id".format(index))
    if not start or not end or start.lower() == end.lower():
        raise ConfigurationError("共轴约束 {} 的两个端点无效".format(group_id))

    axis = str(group.get("axis", "z")).strip().lower()
    if axis not in VALID_AXES:
        raise ConfigurationError(
            "共轴约束 {} 使用了无效轴向：{}".format(group_id, axis)
        )

    markers = []
    for marker_index, raw_marker in enumerate(group.get("markers") or [], 1):
        if not isinstance(raw_marker, dict):
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个Marker格式错误".format(
                    group_id, marker_index
                )
            )
        marker = dict(raw_marker)
        path = str(marker.get("path", "")).strip()
        if not path:
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个Marker缺少 path".format(
                    group_id, marker_index
                )
            )
        marker["path"] = path
        target_type = str(marker.get("target_type", "marker")).strip().lower()
        if target_type not in ("marker", "part"):
            raise ConfigurationError(
                "共轴约束 {} 的 {} 使用了不支持的 target_type：{}".format(
                    group_id, path, target_type
                )
            )
        marker["target_type"] = target_type
        has_fraction = marker.get("fraction") is not None
        has_distance = marker.get("distance") is not None
        cylinder_path = str(marker.get("cylinder", "")).strip()
        placement_count = sum(
            (bool(has_fraction), bool(has_distance), bool(cylinder_path))
        )
        if placement_count != 1:
            raise ConfigurationError(
                "共轴约束 {} 的 {} 必须且只能设置 fraction、distance 或 cylinder"
                " 中的一项".format(group_id, path)
            )
        if cylinder_path:
            marker["cylinder"] = cylinder_path
            marker["cylinder_scale"] = _finite_float(
                marker.get("cylinder_scale", 0.5),
                "共轴约束 {} 的 {}.cylinder_scale".format(group_id, path),
            )
            if marker["cylinder_scale"] <= 0.0:
                raise ConfigurationError(
                    "共轴约束 {} 的 {}.cylinder_scale 必须大于0".format(
                        group_id, path
                    )
                )
        elif has_distance:
            marker["distance"] = _finite_float(
                marker.get("distance"),
                "共轴约束 {} 的 {}.distance".format(group_id, path),
            )
            if marker["distance"] < 0.0:
                raise ConfigurationError(
                    "共轴约束 {} 的 {}.distance 不能小于0".format(
                        group_id, path
                    )
                )
        else:
            marker["fraction"] = _finite_float(
                marker.get("fraction"),
                "共轴约束 {} 的 {}.fraction".format(group_id, path),
            )
        if has_distance or cylinder_path:
            distance_from = str(
                marker.get("distance_from", "start")
            ).strip().lower()
            if distance_from not in ("start", "end"):
                raise ConfigurationError(
                    "共轴约束 {} 的 {}.distance_from 必须是 start 或 end".format(
                        group_id, path
                    )
                )
            marker["distance_from"] = distance_from
        marker["required"] = bool(marker.get("required", True))
        marker["reverse"] = bool(marker.get("reverse", False))
        marker["align_orientation"] = bool(
            marker.get("align_orientation", True)
        )
        if marker.get("offset") is not None:
            raw_offset = marker["offset"]
            if isinstance(raw_offset, dict):
                marker["offset"] = {
                    axis: _finite_float(
                        raw_offset.get(axis, 0.0),
                        "共轴约束 {} 的 {}.offset.{}".format(
                            group_id, path, axis
                        ),
                    )
                    for axis in VALID_AXES
                }
            elif isinstance(raw_offset, (list, tuple)) and len(raw_offset) == 3:
                marker["offset"] = {
                    axis: _finite_float(
                        raw_offset[index],
                        "共轴约束 {} 的 {}.offset.{}".format(
                            group_id, path, axis
                        ),
                    )
                    for index, axis in enumerate(VALID_AXES)
                }
            else:
                raise ConfigurationError(
                    "共轴约束 {} 的 {}.offset 必须是XYZ对象或三个数值".format(
                        group_id, path
                    )
                )
        markers.append(marker)

    length_targets = []
    for target_index, raw_target in enumerate(
        group.get("length_targets") or [], 1
    ):
        if not isinstance(raw_target, dict):
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个长度联动对象格式错误".format(
                    group_id, target_index
                )
            )
        target = dict(raw_target)
        path = str(target.get("path", "")).strip()
        if not path:
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个长度联动对象缺少 path".format(
                    group_id, target_index
                )
            )
        target["path"] = path
        target["scale"] = _finite_float(
            target.get("scale", 1.0),
            "共轴约束 {} 的 {}.scale".format(group_id, path),
        )
        target["offset"] = _finite_float(
            target.get("offset", 0.0),
            "共轴约束 {} 的 {}.offset".format(group_id, path),
        )
        if target["scale"] <= 0.0:
            raise ConfigurationError(
                "共轴约束 {} 的 {}.scale 必须大于0".format(group_id, path)
            )
        target["required"] = bool(target.get("required", True))
        length_targets.append(target)

    coincident_pairs = []
    for pair_index, raw_pair in enumerate(
        group.get("coincident_pairs") or [], 1
    ):
        if isinstance(raw_pair, (list, tuple)) and len(raw_pair) == 2:
            first, second = raw_pair
            tolerance = 1.0e-5
        elif isinstance(raw_pair, dict):
            first = raw_pair.get("first")
            second = raw_pair.get("second")
            tolerance = _finite_float(
                raw_pair.get("tolerance", 1.0e-5),
                "共轴约束 {} 的第 {} 个重合校验容差".format(
                    group_id, pair_index
                ),
            )
        else:
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个重合校验格式错误".format(
                    group_id, pair_index
                )
            )
        first = str(first or "").strip()
        second = str(second or "").strip()
        if not first or not second or first.lower() == second.lower():
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个重合校验对象无效".format(
                    group_id, pair_index
                )
            )
        if tolerance <= 0.0:
            raise ConfigurationError(
                "共轴约束 {} 的第 {} 个重合校验容差必须大于0".format(
                    group_id, pair_index
                )
            )
        coincident_pairs.append(
            {"first": first, "second": second, "tolerance": tolerance}
        )

    recompute = group.get("recompute") or []
    if isinstance(recompute, str):
        recompute = [recompute]
    group["id"] = group_id
    group["start"] = start
    group["end"] = end
    group["axis"] = axis
    group["start_reverse"] = bool(group.get("start_reverse", False))
    group["end_reverse"] = bool(group.get("end_reverse", True))
    group["align_start_orientation"] = bool(
        group.get("align_start_orientation", True)
    )
    group["align_end_orientation"] = bool(
        group.get("align_end_orientation", True)
    )
    group["markers"] = markers
    group["length_targets"] = length_targets
    group["coincident_pairs"] = coincident_pairs
    group["recompute"] = [
        str(path).strip() for path in recompute if str(path).strip()
    ]
    return group


def normalize_parameter(raw_parameter, index=1):
    if not isinstance(raw_parameter, dict):
        raise ConfigurationError("第 {} 个结构参数不是对象".format(index))
    parameter = dict(raw_parameter)
    parameter_id = str(parameter.get("id", "")).strip()
    driver = str(parameter.get("driver", "")).strip()
    if not parameter_id:
        raise ConfigurationError("第 {} 个结构参数缺少 id".format(index))
    if not driver:
        raise ConfigurationError("参数 {} 缺少 driver".format(parameter_id))
    parameter["id"] = parameter_id
    parameter["label"] = str(parameter.get("label") or parameter_id).strip()
    parameter["description"] = str(parameter.get("description") or "").strip()
    parameter["driver"] = driver
    parameter["axes"] = _normalize_axes(
        parameter.get("axes"), "参数 {} 的 axes".format(parameter_id)
    )
    parameter["followers"] = [
        _normalize_follower(follower, parameter_id, follower_index)
        for follower_index, follower in enumerate(
            parameter.get("followers") or [], 1
        )
    ]
    raw_coincident_with = parameter.get("coincident_with") or []
    if isinstance(raw_coincident_with, str):
        raw_coincident_with = [raw_coincident_with]
    coincident_with = []
    seen_coincident_paths = set()
    driver_key = driver.lstrip(".").lower()
    for path_index, raw_path in enumerate(raw_coincident_with, 1):
        path = str(raw_path or "").strip()
        path_key = path.lstrip(".").lower()
        if not path or path_key == driver_key:
            raise ConfigurationError(
                "参数 {} 的第 {} 个同位置参数无效".format(
                    parameter_id, path_index
                )
            )
        if path_key in seen_coincident_paths:
            raise ConfigurationError(
                "参数 {} 重复引用同位置参数：{}".format(parameter_id, path)
            )
        seen_coincident_paths.add(path_key)
        coincident_with.append(path)
    parameter["coincident_with"] = coincident_with
    parameter["coincident_tolerance"] = _finite_float(
        parameter.get("coincident_tolerance", 1.0e-5),
        "参数 {} 的 coincident_tolerance".format(parameter_id),
    )
    if parameter["coincident_tolerance"] <= 0.0:
        raise ConfigurationError(
            "参数 {} 的 coincident_tolerance 必须大于0".format(parameter_id)
        )
    parameter["table_only"] = bool(parameter.get("table_only", False))
    recompute = parameter.get("recompute") or []
    if isinstance(recompute, str):
        recompute = [recompute]
    parameter["recompute"] = [str(path).strip() for path in recompute if str(path).strip()]
    raw_coaxial = parameter.get("coaxial") or []
    if isinstance(raw_coaxial, dict):
        raw_coaxial = [raw_coaxial]
    parameter["coaxial"] = [
        _normalize_coaxial_group(group, group_index)
        for group_index, group in enumerate(raw_coaxial, 1)
    ]
    return parameter


def load_parameter_file(file_path):
    """Return normalized parameter definitions from an optional JSON file."""
    if not file_path or not os.path.isfile(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8-sig") as stream:
            data = json.load(stream)
    except (OSError, ValueError) as exc:
        raise ConfigurationError("结构参数配置文件读取失败：{}".format(exc))

    raw_parameters = data.get("parameters") if isinstance(data, dict) else data
    if not isinstance(raw_parameters, list):
        raise ConfigurationError("结构参数配置必须包含 parameters 列表")

    raw_coaxial = (data.get("coaxial") or []) if isinstance(data, dict) else []
    if isinstance(raw_coaxial, dict):
        raw_coaxial = [raw_coaxial]
    coaxial_groups = [
        _normalize_coaxial_group(group, group_index)
        for group_index, group in enumerate(raw_coaxial, 1)
    ]
    coaxial_ids = set()
    for group in coaxial_groups:
        key = group["id"].lower()
        if key in coaxial_ids:
            raise ConfigurationError("共轴约束 id 重复：{}".format(group["id"]))
        coaxial_ids.add(key)

    parameters = []
    seen_ids = set()
    for index, raw_parameter in enumerate(raw_parameters, 1):
        parameter = normalize_parameter(raw_parameter, index)
        driver_key = parameter["driver"].strip().lstrip(".").lower()
        for group in coaxial_groups:
            endpoint_keys = {
                group["start"].strip().lstrip(".").lower(),
                group["end"].strip().lstrip(".").lower(),
            }
            if driver_key in endpoint_keys:
                parameter["coaxial"].append(group)
        key = parameter["id"].lower()
        if key in seen_ids:
            raise ConfigurationError("结构参数 id 重复：{}".format(parameter["id"]))
        seen_ids.add(key)
        parameters.append(parameter)
    return parameters


def _scene_root(scene):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    return "." + model_name if model_name else ""


def resolve_path(scene, path):
    """Resolve a relative or differently rooted path against the active scene."""
    root = _scene_root(scene)
    raw_path = str(path or "").strip()
    if not raw_path or not root:
        return raw_path
    if not raw_path.startswith("."):
        return root + "." + raw_path.lstrip(".")
    if raw_path.lower() == root.lower() or raw_path.lower().startswith(
        root.lower() + "."
    ):
        return raw_path
    parts = raw_path.lstrip(".").split(".")
    if len(parts) > 1:
        return root + "." + ".".join(parts[1:])
    return root + raw_path


def _get(scene, path):
    resolved_path = resolve_path(scene, path)
    candidates = [resolved_path]
    root = _scene_root(scene)
    if root and resolved_path.lower().startswith(root.lower() + "."):
        relative_path = resolved_path[len(root) + 1 :]
        flattened_path = root + "." + relative_path.replace(".", "_")
        if flattened_path not in candidates:
            candidates.append(flattened_path)
        relative_parts = relative_path.split(".")
        if len(relative_parts) > 2:
            flattened_owner_path = (
                root
                + "."
                + "_".join(relative_parts[:-1])
                + "."
                + relative_parts[-1]
            )
            if flattened_owner_path not in candidates:
                candidates.append(flattened_owner_path)
    for candidate in candidates:
        try:
            node = scene.getObject(candidate)
        except Exception:
            node = None
        if node is not None:
            return candidate, node
    return resolved_path, None


def resolve_object(scene, path):
    """Resolve a configured object, including flattened ADM UDE names."""
    return _get(scene, path)


def _xyz(value):
    if all(hasattr(value, axis) for axis in VALID_AXES):
        values = tuple(float(getattr(value, axis)) for axis in VALID_AXES)
    else:
        values = tuple(float(value[index]) for index in range(3))
    if not all(math.isfinite(number) for number in values):
        raise ValueError("坐标包含NaN或无穷大")
    return values


def _vector(values):
    import Jusme

    return Jusme.Vector(*values)


def _location_target(scene, path):
    resolved_path, node = _get(scene, path)
    if node is None:
        return resolved_path, None, None
    try:
        location = _xyz(node.location)
    except Exception:
        return resolved_path, node, None
    return resolved_path, node, location


def parameter_availability(scene, parameter):
    if scene is None:
        return "当前没有活动模型"
    driver_path, driver, driver_location = _location_target(
        scene, parameter["driver"]
    )
    if driver is None or driver_location is None:
        return "找不到主控Marker：{}".format(driver_path)
    for follower in parameter.get("followers", []):
        follower_path, follower_node, follower_location = _location_target(
            scene, follower["path"]
        )
        if follower.get("required", True) and (
            follower_node is None or follower_location is None
        ):
            return "找不到联动对象：{}".format(follower_path)
    for coincident_path in parameter.get("coincident_with", []):
        resolved_path, node, location = _location_target(scene, coincident_path)
        if node is None or location is None:
            return "找不到同位置参数：{}".format(resolved_path)
    return ""


def available_parameters(scene, parameters):
    available = []
    unavailable = []
    for parameter in parameters or []:
        error = parameter_availability(scene, parameter)
        if error:
            unavailable.append((parameter, error))
        else:
            available.append(parameter)
    return available, unavailable


def driver_path(scene, parameter):
    return resolve_path(scene, parameter.get("driver"))


def _axis_mapping(raw_value, default):
    if isinstance(raw_value, dict):
        return {
            axis: float(raw_value.get(axis, default)) for axis in VALID_AXES
        }
    if raw_value is None:
        return {axis: float(default) for axis in VALID_AXES}
    value = float(raw_value)
    return {axis: value for axis in VALID_AXES}


def _follower_location(follower, old_location, driver_new, driver_delta, default_axes):
    operation = follower["operation"]
    axes = tuple(follower.get("axes") or default_axes)
    result = list(old_location)
    if operation == "delta":
        scale = _axis_mapping(follower.get("scale"), 1.0)
        for index, axis in enumerate(VALID_AXES):
            if axis in axes:
                result[index] += driver_delta[index] * scale[axis]
    elif operation == "copy":
        for index, axis in enumerate(VALID_AXES):
            if axis in axes:
                result[index] = driver_new[index]
    elif operation == "mirror":
        origin = _axis_mapping(follower.get("origin"), 0.0)
        for index, axis in enumerate(VALID_AXES):
            if axis in axes:
                result[index] = 2.0 * origin[axis] - driver_new[index]
    elif operation == "offset":
        offset = _axis_mapping(follower.get("offset"), 0.0)
        for index, axis in enumerate(VALID_AXES):
            if axis in axes:
                result[index] = driver_new[index] + offset[axis]
    return tuple(result)


def _validate_limits(parameter, coordinates):
    limits = parameter.get("limits") or {}
    for index, axis in enumerate(VALID_AXES):
        if axis not in limits:
            continue
        bounds = limits[axis]
        if not isinstance(bounds, (list, tuple)) or len(bounds) != 2:
            return "参数 {} 的 {} 限值格式错误".format(parameter["label"], axis.upper())
        lower, upper = float(bounds[0]), float(bounds[1])
        if coordinates[index] < lower or coordinates[index] > upper:
            return "{}坐标必须位于 [{}, {}]".format(axis.upper(), lower, upper)
    return ""


def apply_parameter(scene, parameter, coordinates):
    """Apply one configured structure parameter as a rollback-safe transaction."""
    availability_error = parameter_availability(scene, parameter)
    if availability_error:
        return AdjustmentResult(False, availability_error)
    try:
        requested = _xyz(coordinates)
    except Exception as exc:
        return AdjustmentResult(False, "结构参数坐标无效：{}".format(exc))

    driver_resolved, driver_node, driver_old = _location_target(
        scene, parameter["driver"]
    )
    axes = tuple(parameter["axes"])
    for index, axis in enumerate(VALID_AXES):
        if axis not in axes and abs(requested[index] - driver_old[index]) > LOCKED_AXIS_TOLERANCE:
            return AdjustmentResult(
                False,
                "参数 {} 不允许修改{}坐标".format(parameter["label"], axis.upper()),
            )
    driver_new = tuple(
        requested[index] if axis in axes else driver_old[index]
        for index, axis in enumerate(VALID_AXES)
    )
    limit_error = _validate_limits(parameter, driver_new)
    if limit_error:
        return AdjustmentResult(False, limit_error)
    driver_delta = tuple(
        driver_new[index] - driver_old[index] for index in range(3)
    )
    if max(abs(value) for value in driver_delta) <= LOCKED_AXIS_TOLERANCE:
        return AdjustmentResult(True, "结构参数坐标没有变化", changed=False)

    targets = [(driver_resolved, driver_node, driver_old, driver_new)]
    seen_paths = {driver_resolved.lower()}
    for follower in parameter.get("followers", []):
        resolved_path, node, old_location = _location_target(scene, follower["path"])
        if node is None or old_location is None:
            if follower.get("required", True):
                return AdjustmentResult(False, "找不到联动对象：{}".format(resolved_path))
            continue
        if resolved_path.lower() in seen_paths:
            return AdjustmentResult(False, "结构参数重复引用对象：{}".format(resolved_path))
        seen_paths.add(resolved_path.lower())
        try:
            new_location = _follower_location(
                follower,
                old_location,
                driver_new,
                driver_delta,
                axes,
            )
            _xyz(new_location)
        except Exception as exc:
            return AdjustmentResult(
                False, "联动对象 {} 的规则无效：{}".format(resolved_path, exc)
            )
        targets.append((resolved_path, node, old_location, new_location))

    recompute_nodes = []
    for recompute_path in parameter.get("recompute", []):
        resolved_path, node = _get(scene, recompute_path)
        if node is not None:
            recompute_nodes.append((resolved_path, node))

    try:
        for _path, node, _old_location, new_location in targets:
            node.location = _vector(new_location)
        for _path, node in recompute_nodes:
            recompute = getattr(node, "recompute", None)
            if callable(recompute):
                recompute()
        scene_recompute = getattr(scene, "recompute", None)
        if callable(scene_recompute):
            scene_recompute()
        for path, node, _old_location, expected_location in targets:
            actual_location = _xyz(node.location)
            if any(
                abs(actual_location[index] - expected_location[index]) > 1.0e-5
                for index in range(3)
            ):
                raise RuntimeError("对象位置校验失败：{}".format(path))
    except Exception as exc:
        rollback_errors = []
        for path, node, old_location, _new_location in reversed(targets):
            try:
                node.location = _vector(old_location)
            except Exception as rollback_exc:
                rollback_errors.append("{} 恢复失败：{}".format(path, rollback_exc))
        try:
            scene_recompute = getattr(scene, "recompute", None)
            if callable(scene_recompute):
                scene_recompute()
        except Exception as rollback_exc:
            rollback_errors.append("模型恢复刷新失败：{}".format(rollback_exc))
        message = "结构参数调整失败，已恢复原坐标：{}".format(exc)
        if rollback_errors:
            message += "；" + "；".join(rollback_errors)
        return AdjustmentResult(False, message, errors=[str(exc)] + rollback_errors)

    return AdjustmentResult(
        True,
        "结构参数“{}”调整完成，已更新 {} 个对象".format(
            parameter["label"], len(targets)
        ),
        updated=len(targets),
        changed=True,
    )
