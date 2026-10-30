"""Shared transaction layer for ADM hardpoint parameterization.

Each ADM template may provide a compact ``structure_updater`` containing its
topology rules.  The shared layer executes that updater and the generated CMD
overlay as one checked transaction: validate, snapshot, update, recompute,
verify, and roll the scene back when any critical step fails.

``adjust_factory`` remains available only for older callers.  New ADM
templates should use ``structure_updater`` so their runtime no longer depends
on the historical one-file-per-hardpoint adjustors.
"""

from __future__ import print_function

import importlib.util
import inspect
import ast
import math
import os
import re
import textwrap

import Jusme


EPSILON = 1.0e-6
LOCKED_AXIS_TOLERANCE = 1.0e-6

TRANSACTION_PROPERTIES = (
    "location",
    "orientation",
    "length",
    "radius",
    "function",
    "commands",
    "string_value",
    "string",
    "value",
    "real_value",
    "initial_condition",
    "variable_name",
    "sim_script_name",
    "adams_id",
    "marker_name",
    "cylinder_name",
    "part_name",
    "relative_to",
)


class AdjustmentResult(object):
    def __init__(self, success, message, updated=0, changed=False, errors=None):
        self.success = bool(success)
        self.message = message
        self.updated = int(updated or 0)
        self.changed = bool(changed)
        self.errors = list(errors or [])


class TemplateContract(object):
    """Declarative description of one imported engineering template."""

    def __init__(
        self,
        model_name,
        model_folder,
        hardpoint_rules,
        adjust_factory=None,
        core_hardpoints=(),
        required_paths=(),
        aliases=None,
        length_pairs=(),
        vertical_pairs=(),
        wheel_pair=None,
        optional_patch_fragments=(),
        label=None,
        structure_updater=None,
        post_patch_updater=None,
        transaction_paths=(),
        recompute_paths=(),
    ):
        self.model_name = str(model_name)
        self.source_root = "." + self.model_name
        self.model_folder = os.path.abspath(model_folder)
        self.patch_file = os.path.join(
            self.model_folder, self.model_name + "_patch.py"
        )
        self.cmd_file = os.path.join(
            self.model_folder, self.model_name + ".cmd"
        )
        self.hardpoint_rules = dict(hardpoint_rules)
        self.adjust_factory = adjust_factory
        self.core_hardpoints = tuple(core_hardpoints)
        self.required_paths = tuple(required_paths)
        self.aliases = dict(aliases or {})
        self.length_pairs = tuple(length_pairs)
        self.vertical_pairs = tuple(vertical_pairs)
        self.wheel_pair = tuple(wheel_pair) if wheel_pair else None
        self.optional_patch_fragments = tuple(optional_patch_fragments)
        self.label = label or self.model_name
        self.structure_updater = structure_updater
        self.post_patch_updater = post_patch_updater
        self.transaction_paths = tuple(transaction_paths)
        self.recompute_paths = tuple(recompute_paths)


def canonical_hardpoint_name(contract, name_or_path):
    name = str(name_or_path or "").rstrip(".").split(".")[-1]
    return contract.aliases.get(name, name)


def get_rule(contract, name_or_path):
    return contract.hardpoint_rules.get(
        canonical_hardpoint_name(contract, name_or_path)
    )


def _model_root(scene):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    return "." + model_name if model_name else ""


def _resolve_path(contract, scene, path):
    model_root = _model_root(scene)
    if path == contract.source_root or path.startswith(contract.source_root + "."):
        return model_root + path[len(contract.source_root):] if model_root else path
    if path.startswith("."):
        return path
    return model_root + "." + path if model_root else path


def _get(contract, scene, path):
    try:
        return scene.getObject(_resolve_path(contract, scene, path))
    except Exception:
        return None


def hardpoint_path(contract, name_or_path, scene=None):
    scene = scene if scene is not None else getattr(Jusme, "ActiveUSScene", None)
    root = _model_root(scene) or contract.source_root
    return "{}.ground.{}".format(
        root,
        canonical_hardpoint_name(contract, name_or_path),
    )


def _xyz(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        return float(value.x), float(value.y), float(value.z)
    return float(value[0]), float(value[1]), float(value[2])


def _vector(value):
    x_coord, y_coord, z_coord = _xyz(value)
    return Jusme.Vector(x_coord, y_coord, z_coord)


def _distance(first, second):
    ax, ay, az = _xyz(first)
    bx, by, bz = _xyz(second)
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2)


def _all_finite(value):
    return all(math.isfinite(number) for number in _xyz(value))


def _read_hardpoints(contract, scene, replacement_name=None, replacement=None):
    points = {}
    for name in contract.core_hardpoints:
        node = _get(contract, scene, "ground." + name)
        if node is None:
            raise RuntimeError("缺少硬点 ground.{}".format(name))
        points[name] = _vector(node.location)
    if replacement_name:
        points[replacement_name] = _vector(replacement)
    return points


def _validate_geometry(contract, points):
    for name, value in points.items():
        if not _all_finite(value):
            return "硬点 {} 包含无效数值".format(name)

    for pair in contract.length_pairs:
        first, second = pair[:2]
        label = pair[2] if len(pair) > 2 else "{}与{}".format(first, second)
        if first in points and second in points:
            if _distance(points[first], points[second]) <= EPSILON:
                return "{}的两个定义点不能重合".format(label)

    for pair in contract.vertical_pairs:
        upper, lower = pair[:2]
        label = pair[2] if len(pair) > 2 else "{}与{}".format(upper, lower)
        if points[upper].z <= points[lower].z + EPSILON:
            return "{}的上端点必须高于下端点".format(label)

    if contract.wheel_pair:
        left_name, right_name = contract.wheel_pair[:2]
        left = points[left_name]
        right = points[right_name]
        if left.y >= right.y - EPSILON:
            return "左、右轮心位置交叉或重合"
        if left.y >= -EPSILON:
            return "左轮心必须位于模型中心面的左侧"
        if right.y <= EPSILON:
            return "右轮心必须位于模型中心面的右侧"
    return ""


def _validate_scene(contract, scene):
    if scene is None:
        return "当前没有活动模型"
    scene_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    if not scene_name:
        return "当前活动场景没有有效名称"

    missing = []
    for name in contract.core_hardpoints:
        if _get(contract, scene, "ground." + name) is None:
            missing.append("ground." + name)
    for path in contract.required_paths:
        if _get(contract, scene, path) is None:
            missing.append(path)
    if missing:
        preview = "、".join(missing[:6])
        if len(missing) > 6:
            preview += " 等{}项".format(len(missing))
        return "场景 {} 的{}结构不完整，缺少：{}".format(
            scene_name, contract.label, preview
        )
    if not os.path.isfile(contract.patch_file):
        return "未找到{}公式补丁：{}".format(contract.label, contract.patch_file)
    if not os.path.isfile(contract.cmd_file):
        return "未找到{}参考CMD：{}".format(contract.label, contract.cmd_file)
    return ""


def compatibility_error(contract, scene=None):
    scene = scene if scene is not None else getattr(Jusme, "ActiveUSScene", None)
    return _validate_scene(contract, scene)


def is_compatible_scene(contract, scene=None):
    return not compatibility_error(contract, scene)


def _copy_property(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        return _vector(value)
    if isinstance(value, list):
        return list(value)
    if isinstance(value, tuple):
        return tuple(value)
    return value


def _read_text(path):
    with open(path, "r", encoding="utf-8-sig", errors="ignore") as source_file:
        return source_file.read()


def _patch_paths(contract):
    try:
        patch_text = _read_text(contract.patch_file)
    except (OSError, UnicodeError):
        return set()
    pattern = r"['\"](" + re.escape(contract.source_root) + (
        r"(?:\.[A-Za-z_][A-Za-z0-9_]*)+)['\"]"
    )
    return set(re.findall(pattern, patch_text))


def _adjustor_paths(adjustor):
    """Extract model-relative getObject paths from the selected legacy class."""
    try:
        source = textwrap.dedent(inspect.getsource(adjustor.__class__))
        tree = ast.parse(source)
    except (OSError, IOError, TypeError, SyntaxError):
        return set()
    paths = set()
    for node in ast.walk(tree):
        value = getattr(node, "value", None)
        if not isinstance(value, str):
            # Python 3.7 represents string literals as ast.Str.  Reading the
            # instance dictionary avoids the deprecated ast.Str compatibility
            # accessor on newer runtimes.
            value = getattr(node, "__dict__", {}).get("s")
        if not isinstance(value, str):
            continue
        match = re.match(r"^\.\{\}\.([A-Za-z_][A-Za-z0-9_.]*)$", value)
        if match:
            paths.add(match.group(1))
    return paths


def _missing_adjustor_paths(contract, scene, adjustor):
    return sorted(
        path
        for path in _adjustor_paths(adjustor)
        if _get(contract, scene, path) is None
    )


def _connector_paths(contract):
    try:
        cmd_text = _read_text(contract.cmd_file)
    except (OSError, UnicodeError):
        return set()
    paths = set(
        re.findall(
            r"(?im)^\s*joint_name\s*=\s*(\.{}(?:\.[A-Za-z_][A-Za-z0-9_]*)+)".format(
                re.escape(contract.model_name)
            ),
            cmd_text,
        )
    )
    paths.update(contract.recompute_paths)
    return paths


def _snapshot_geometry(contract, scene, adjustor=None):
    paths = set(_patch_paths(contract))
    if adjustor is not None:
        paths.update(_adjustor_paths(adjustor))
    paths.update(_connector_paths(contract))
    paths.update("ground." + name for name in contract.core_hardpoints)
    paths.update(contract.required_paths)
    paths.update(contract.transaction_paths)

    nodes = []
    visited = set()
    for path in paths:
        node = _get(contract, scene, path)
        if node is None or id(node) in visited:
            continue
        visited.add(id(node))
        nodes.append(node)

    snapshot = []
    for node in nodes:
        properties = set(getattr(node, "PropertiesList", []) or [])
        for property_name in TRANSACTION_PROPERTIES:
            if (
                properties
                and property_name not in properties
                and property_name not in ("location", "orientation", "length", "radius")
            ):
                continue
            try:
                value = getattr(node, property_name)
            except Exception:
                continue
            snapshot.append((node, property_name, _copy_property(value)))
    return snapshot


def _restore_geometry(snapshot):
    restore_errors = []
    for node, property_name, value in reversed(snapshot):
        try:
            setattr(node, property_name, value)
        except Exception as exc:
            restore_errors.append(
                "{}.{}: {}".format(
                    getattr(node, "Name", "<unknown>"), property_name, exc
                )
            )
    return restore_errors


def _split_cmd_blocks(cmd_text):
    blocks = []
    block = []
    for raw_line in cmd_text.splitlines():
        if raw_line.strip().startswith("!"):
            if block:
                blocks.append("\n".join(block))
                block = []
            continue
        if raw_line.strip():
            block.append(raw_line)
    if block:
        blocks.append("\n".join(block))
    return blocks


def _partial_marker_patch_modes(contract):
    try:
        cmd_text = _read_text(contract.cmd_file)
        patch_text = _read_text(contract.patch_file)
    except (OSError, UnicodeError):
        return {}
    patched_markers = set(
        re.findall(r"record_error\('marker modify ([^']+)'", patch_text)
    )
    modes = {}
    for block in _split_cmd_blocks(cmd_text):
        if not re.match(r"^\s*marker\s+modify\b", block, flags=re.I):
            continue
        name_match = re.search(
            r"(?im)^\s*marker_name\s*=\s*(\.[A-Za-z_][A-Za-z0-9_.]*)",
            block,
        )
        if not name_match or name_match.group(1) not in patched_markers:
            continue
        modes[name_match.group(1)] = (
            bool(re.search(r"(?im)^\s*location\s*=", block)),
            bool(re.search(r"(?im)^\s*orientation\s*=", block)),
        )
    return modes


def _capture_partial_marker_properties(contract, scene):
    captured = []
    for path, (has_location, has_orientation) in _partial_marker_patch_modes(
        contract
    ).items():
        marker = _get(contract, scene, path)
        if marker is None:
            continue
        if not has_location:
            captured.append((marker, "location", _copy_property(marker.location)))
        if not has_orientation:
            captured.append(
                (marker, "orientation", _copy_property(marker.orientation))
            )
    return captured


def _restore_partial_marker_properties(captured):
    for marker, property_name, value in captured:
        setattr(marker, property_name, value)


def _load_patch_module(contract):
    module_name = "_{}_runtime_patch".format(contract.model_name)
    spec = importlib.util.spec_from_file_location(module_name, contract.patch_file)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载{}公式补丁".format(contract.label))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _format_patch_error(detail):
    if isinstance(detail, dict):
        return "{}: {}".format(
            detail.get("step", "补丁步骤"),
            detail.get("error", detail.get("message", detail)),
        )
    return str(detail)


def _run_formula_patch(contract, scene):
    module = _load_patch_module(contract)
    if not hasattr(module, "apply_patch"):
        raise RuntimeError("{}公式补丁缺少apply_patch入口".format(contract.label))
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    if not model_name:
        raise RuntimeError("活动场景名为空")
    result = module.apply_patch(contract.model_folder, model_name) or {}
    errors = list(result.get("errors") or [])
    critical_errors = []
    warnings = list(result.get("warnings") or [])
    for detail in errors:
        step = detail.get("step", "") if isinstance(detail, dict) else ""
        is_geometry_error = (
            step.startswith("marker modify ")
            or step.startswith("geometry modify ")
            or step.startswith("part modify rigid_body ")
        )
        is_optional = any(
            fragment in step for fragment in contract.optional_patch_fragments
        )
        if is_geometry_error and not is_optional:
            critical_errors.append(detail)
        else:
            warnings.append(_format_patch_error(detail))
    if critical_errors:
        raise RuntimeError(
            "公式补丁执行失败：{}".format(_format_patch_error(critical_errors[0]))
        )
    return int(result.get("updated") or 0), warnings


def _recompute_connectors(contract, scene):
    errors = []
    for path in _connector_paths(contract):
        connector = _get(contract, scene, path)
        if connector is None:
            continue
        recompute = getattr(connector, "recompute", None)
        if callable(recompute):
            try:
                recompute()
            except Exception as exc:
                errors.append("{}: {}".format(path, exc))
    if errors:
        raise RuntimeError("关联运动副重算失败：{}".format(errors[0]))


def _validate_updated_structure(contract, scene, changed_name, expected_location):
    target = _get(contract, scene, "ground." + changed_name)
    if target is None:
        return "更新后硬点丢失：{}".format(changed_name)
    try:
        if _distance(target.location, expected_location) > LOCKED_AXIS_TOLERANCE:
            return "更新后硬点坐标与输入值不一致"
    except Exception as exc:
        return "无法校验更新后的硬点坐标：{}".format(exc)

    try:
        geometry_error = _validate_geometry(
            contract, _read_hardpoints(contract, scene)
        )
    except Exception as exc:
        return "更新后无法读取硬点结构：{}".format(exc)
    if geometry_error:
        return geometry_error

    for path in contract.required_paths:
        node = _get(contract, scene, path)
        for property_name in ("location", "orientation"):
            try:
                value = getattr(node, property_name)
            except Exception:
                continue
            if not _all_finite(value):
                return "更新后对象位姿无效：{}.{}".format(path, property_name)
    return ""


def adjust_hardpoint(
    contract, name_or_path, x_coord, y_coord, z_coord, scene=None
):
    scene = scene if scene is not None else getattr(Jusme, "ActiveUSScene", None)
    scene_error = _validate_scene(contract, scene)
    if scene_error:
        return AdjustmentResult(False, scene_error)

    name = canonical_hardpoint_name(contract, name_or_path)
    axes = get_rule(contract, name)
    if axes is None:
        return AdjustmentResult(False, "硬点 {} 不支持参数化调整".format(name))

    target = _get(contract, scene, "ground." + name)
    if target is None:
        return AdjustmentResult(False, "未找到硬点 {}".format(name))
    try:
        requested = Jusme.Vector(float(x_coord), float(y_coord), float(z_coord))
    except (TypeError, ValueError) as exc:
        return AdjustmentResult(False, "硬点坐标必须是有效数字：{}".format(exc))
    if not _all_finite(requested):
        return AdjustmentResult(False, "硬点坐标不能包含NaN或无穷大")

    old_location = _vector(target.location)
    for axis in ("x", "y", "z"):
        if axis not in axes and abs(
            getattr(requested, axis) - getattr(old_location, axis)
        ) > LOCKED_AXIS_TOLERANCE:
            return AdjustmentResult(
                False, "硬点 {} 的{}坐标不可修改".format(name, axis.upper())
            )
    new_location = Jusme.Vector(
        requested.x if "x" in axes else old_location.x,
        requested.y if "y" in axes else old_location.y,
        requested.z if "z" in axes else old_location.z,
    )
    if _distance(old_location, new_location) <= EPSILON:
        return AdjustmentResult(True, "硬点坐标没有变化", changed=False)

    try:
        points = _read_hardpoints(contract, scene, name, new_location)
        geometry_error = _validate_geometry(contract, points)
    except Exception as exc:
        return AdjustmentResult(False, "无法校验硬点结构：{}".format(exc))
    if geometry_error:
        return AdjustmentResult(False, geometry_error)

    adjustor = None
    if not callable(contract.structure_updater):
        if not callable(contract.adjust_factory):
            return AdjustmentResult(False, "硬点 {} 缺少结构联动规则".format(name))
        full_path = hardpoint_path(contract, name, scene)
        try:
            adjustor = contract.adjust_factory(full_path)
        except Exception as exc:
            return AdjustmentResult(
                False, "无法创建{}联动调整器：{}".format(name, exc)
            )
        if adjustor is None or not callable(getattr(adjustor, "Adjust", None)):
            return AdjustmentResult(False, "硬点 {} 缺少联动调整器".format(name))

        missing_adjustor_paths = _missing_adjustor_paths(contract, scene, adjustor)
        if missing_adjustor_paths:
            preview = "、".join(missing_adjustor_paths[:6])
            if len(missing_adjustor_paths) > 6:
                preview += " 等{}项".format(len(missing_adjustor_paths))
            return AdjustmentResult(
                False,
                "硬点 {} 的联动结构不完整，缺少：{}".format(name, preview),
            )

    snapshot = _snapshot_geometry(contract, scene, adjustor)
    if not snapshot:
        return AdjustmentResult(False, "无法创建模型回滚快照，已取消调整")

    try:
        partial_marker_properties = _capture_partial_marker_properties(
            contract, scene
        )
        target.location = new_location
        if callable(contract.structure_updater):
            contract.structure_updater(scene, points, name)
            geometry_error = _validate_geometry(
                contract, _read_hardpoints(contract, scene)
            )
            if geometry_error:
                raise RuntimeError("结构联动后校验失败：{}".format(geometry_error))
        else:
            adjustor.Adjust()
        updated, warnings = _run_formula_patch(contract, scene)
        _restore_partial_marker_properties(partial_marker_properties)
        if callable(contract.post_patch_updater):
            refreshed_points = _read_hardpoints(contract, scene)
            contract.post_patch_updater(scene, refreshed_points, name)
        _recompute_connectors(contract, scene)
        scene.recompute()
        post_error = _validate_updated_structure(
            contract, scene, name, new_location
        )
        if post_error:
            raise RuntimeError("结构更新后校验失败：{}".format(post_error))
        message = "硬点 {} 调整完成，共刷新{}项公式/几何数据".format(
            name, updated
        )
        if warnings:
            message += "；有{}条警告，请查看控制台".format(len(warnings))
            for warning in warnings:
                print("[{}参数化警告] {}".format(contract.label, warning))
        return AdjustmentResult(
            True, message, updated=updated, changed=True
        )
    except Exception as exc:
        restore_errors = _restore_geometry(snapshot)
        try:
            scene.recompute()
        except Exception:
            pass
        message = "硬点调整失败，模型已恢复：{}".format(exc)
        if restore_errors:
            message += "；但有{}项恢复失败，请重新导入模型".format(
                len(restore_errors)
            )
        return AdjustmentResult(
            False, message, errors=[str(exc)] + restore_errors
        )
