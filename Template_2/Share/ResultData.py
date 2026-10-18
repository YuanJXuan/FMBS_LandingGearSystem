# -*- coding: utf-8 -*-
"""Read configured curves from Jasmine ``object_data`` result folders."""

from __future__ import print_function

import json
import math
import os


class ResultDataError(ValueError):
    """Raised when a simulation result cannot be loaded or interpreted."""


def normalize_result_directory(path):
    """Accept either ``object_data`` itself or its direct parent folder."""
    path = os.path.abspath(str(path or ""))
    nested = os.path.join(path, "object_data")
    if os.path.isdir(nested):
        return nested
    return path


def _jusme_work_directory():
    try:
        import Jusme

        getter = getattr(Jusme, "getWorkDir", None)
        return str(getter() or "").strip() if callable(getter) else ""
    except Exception:
        return ""


def default_result_directory(template_path="", work_directory=None):
    """Return Jasmine's default ``fmbs_workdir/result/object_data`` folder.

    The runtime work root returned by ``Jusme.getWorkDir()`` is authoritative.
    ``template_path`` remains as a fallback for tests and older platform builds
    that do not expose ``getWorkDir``.

    The installed layout is::

        <root>/bin/Template/Template_2
        <root>/fmbs_workdir/result/object_data

    ``template_path`` may point at Template_2 itself or any file/folder below it.
    The returned path is useful before the first simulation creates the folder.
    """
    work_directory = (
        _jusme_work_directory()
        if work_directory is None
        else str(work_directory or "").strip()
    )
    if work_directory:
        work_directory = os.path.abspath(work_directory)
        if os.path.basename(work_directory).lower() == "fmbs_workdir":
            return os.path.join(work_directory, "result", "object_data")
        return os.path.join(
            work_directory,
            "fmbs_workdir",
            "result",
            "object_data",
        )

    current = os.path.abspath(str(template_path or ""))
    if os.path.isfile(current):
        current = os.path.dirname(current)
    while current:
        if os.path.basename(current).lower() == "bin":
            return os.path.join(
                os.path.dirname(current),
                "fmbs_workdir",
                "result",
                "object_data",
            )
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    return ""


def parse_result_target(target):
    """Parse ``ObjectType.ObjectName.DataIndex.Component``."""
    parts = [part.strip() for part in str(target or "").split(".")]
    if len(parts) != 4 or not all(parts):
        raise ResultDataError(
            "后处理变量名应为 对象类型.对象名.数据项.分量：{}".format(target)
        )
    return tuple(parts)


def _mapping_value(mapping, key, description):
    if not isinstance(mapping, dict):
        raise ResultDataError("结果元数据中缺少{}".format(description))
    if key in mapping:
        return mapping[key]
    normalized = str(key).strip().lower()
    for candidate, value in mapping.items():
        if str(candidate).strip().lower() == normalized:
            return value
    raise ResultDataError("结果元数据中找不到{}：{}".format(description, key))


def resolve_result_offset(model_info, target):
    """Resolve a configured variable name to the numeric data offset."""
    object_type, object_name, data_index, component = parse_result_target(target)
    object_group = _mapping_value(model_info, object_type, "对象类型")
    if not isinstance(object_group, dict):
        raise ResultDataError("对象类型 {} 的元数据格式无效".format(object_type))

    matched = None
    normalized_name = object_name.lower()
    for object_key, value in object_group.items():
        if not isinstance(value, dict):
            continue
        names = (value.get("name"), object_key)
        if any(str(name or "").strip().lower() == normalized_name for name in names):
            matched = value
            break
    if matched is None:
        raise ResultDataError("找不到结果对象：{}.{}".format(object_type, object_name))

    data_indices = matched.get("data_indices")
    data_entry = _mapping_value(data_indices, data_index, "数据项")
    if not isinstance(data_entry, dict):
        raise ResultDataError("数据项 {} 的元数据格式无效".format(data_index))

    # Jasmine's current result schema uses the singular key ``component``.
    component_map = data_entry.get("component")
    return _mapping_value(component_map, component, "结果分量")


def _series_values(value, description):
    if hasattr(value, "tolist"):
        value = value.tolist()
    if isinstance(value, tuple):
        value = list(value)
    if not isinstance(value, list):
        try:
            value = list(value)
        except (TypeError, ValueError):
            raise ResultDataError("{}不是有效序列".format(description))
    return value


def _default_loader():
    try:
        from FmbsShortcut.Processer.post.data_loader import DataLoader
    except Exception as exc:
        raise ResultDataError("无法加载茉莉结果读取接口：{}".format(exc))
    return DataLoader()


def load_configured_results(result_directory, entries, data_loader=None):
    """Load time and every valid post-processing entry independently.

    One missing curve does not prevent other configured curves from being
    displayed.  Fatal result-folder errors raise :class:`ResultDataError`.
    """
    result_directory = normalize_result_directory(result_directory)
    if not os.path.isdir(result_directory):
        raise ResultDataError("找不到仿真结果目录：{}".format(result_directory))

    loader = data_loader or _default_loader()
    try:
        result_handle = loader.load_result_json(result_directory)
    except Exception as exc:
        raise ResultDataError("仿真结果加载失败：{}".format(exc))
    if result_handle is None:
        raise ResultDataError("仿真结果加载失败，DataLoader 未返回数据")

    try:
        raw_info = result_handle.getDataInfo()
        result_info = raw_info if isinstance(raw_info, dict) else json.loads(raw_info)
        model_info = result_info.get("model_info", {})
        time_values = _series_values(loader.getdata(0, result_handle), "时间数据")
    except ResultDataError:
        raise
    except Exception as exc:
        raise ResultDataError("无法解析仿真结果元数据：{}".format(exc))

    curves = []
    errors = []
    for entry in entries or []:
        target = str(entry.get("target") or "").strip()
        if not target:
            continue
        try:
            offset = resolve_result_offset(model_info, target)
            values = _series_values(
                loader.getdata(offset, result_handle),
                "{} 数据".format(target),
            )
            count = min(len(time_values), len(values))
            if count <= 0:
                raise ResultDataError("结果曲线没有数据点")
            curves.append(
                {
                    "id": entry.get("id") or target,
                    "row": entry.get("row"),
                    "label": entry.get("label") or target,
                    "target": target,
                    "x_unit": entry.get("x_unit") or "s",
                    "y_unit": entry.get("y_unit") or "",
                    "x": time_values[:count],
                    "y": values[:count],
                }
            )
        except Exception as exc:
            errors.append("{}：{}".format(entry.get("label") or target, exc))

    return {
        "result_directory": result_directory,
        "curves": curves,
        "errors": errors,
    }


def _normalized_reference(value):
    return str(value or "").strip().lower()


def _resolve_curve_reference(curves, reference):
    wanted = _normalized_reference(reference)
    matches = []
    for curve in curves or []:
        aliases = {
            _normalized_reference(curve.get("id")),
            _normalized_reference(curve.get("label")),
            _normalized_reference(curve.get("target")),
        }
        if wanted and wanted in aliases:
            matches.append(curve)
    if not matches:
        raise ResultDataError("找不到功量图来源曲线：{}".format(reference))
    if len(matches) > 1:
        raise ResultDataError("功量图来源曲线名称不唯一：{}".format(reference))
    return matches[0]


def _finite_time_series(curve):
    samples = []
    for raw_time, raw_value in zip(curve.get("x") or [], curve.get("y") or []):
        try:
            time_value = float(raw_time)
            result_value = float(raw_value)
        except (TypeError, ValueError):
            continue
        if math.isfinite(time_value) and math.isfinite(result_value):
            if samples and time_value < samples[-1][0]:
                raise ResultDataError(
                    "曲线 {} 的时间数据不是递增序列".format(
                        curve.get("label") or curve.get("target")
                    )
                )
            if samples and time_value == samples[-1][0]:
                samples[-1] = (time_value, result_value)
            else:
                samples.append((time_value, result_value))
    if len(samples) < 2:
        raise ResultDataError(
            "曲线 {} 的有效数据点不足".format(
                curve.get("label") or curve.get("target")
            )
        )
    return samples


def _interpolate_at(samples, query_time, start_index=0):
    index = max(0, min(start_index, len(samples) - 2))
    while index + 1 < len(samples) and samples[index + 1][0] < query_time:
        index += 1
    if index + 1 >= len(samples):
        return samples[-1][1], len(samples) - 2
    first_time, first_value = samples[index]
    second_time, second_value = samples[index + 1]
    if query_time == first_time or second_time == first_time:
        return first_value, index
    if query_time == second_time:
        return second_value, index
    fraction = (query_time - first_time) / (second_time - first_time)
    return first_value + fraction * (second_value - first_value), index


def _aligned_y_values(x_curve, y_curve):
    """Return the two result series evaluated at the same simulation times."""
    x_samples = _finite_time_series(x_curve)
    y_samples = _finite_time_series(y_curve)
    if len(x_samples) == len(y_samples) and all(
        abs(x_item[0] - y_item[0]) <= 1.0e-12
        for x_item, y_item in zip(x_samples, y_samples)
    ):
        return (
            [item[1] for item in x_samples],
            [item[1] for item in y_samples],
        )

    overlap_start = max(x_samples[0][0], y_samples[0][0])
    overlap_end = min(x_samples[-1][0], y_samples[-1][0])
    if overlap_end <= overlap_start:
        raise ResultDataError("两条功量图来源曲线没有共同时间范围")

    x_values = []
    y_values = []
    y_index = 0
    for time_value, x_value in x_samples:
        if time_value < overlap_start or time_value > overlap_end:
            continue
        y_value, y_index = _interpolate_at(y_samples, time_value, y_index)
        x_values.append(x_value)
        y_values.append(y_value)
    if len(x_values) < 2:
        raise ResultDataError("两条功量图来源曲线的共同采样点不足")
    return x_values, y_values


def build_work_diagrams(curves, definitions):
    """Build configured force-displacement style XY curves.

    The source curve Y values form the new X/Y coordinates.  Source order is
    kept in simulation-time order so hysteresis loops are not distorted.
    """
    diagrams = []
    errors = []
    for definition in definitions or []:
        label = definition.get("label") or "功量图"
        try:
            x_curve = _resolve_curve_reference(
                curves, definition.get("x_source")
            )
            y_curve = _resolve_curve_reference(
                curves, definition.get("y_source")
            )
            if x_curve is y_curve:
                raise ResultDataError("功量图的X轴和Y轴不能使用同一条曲线")
            x_values, y_values = _aligned_y_values(x_curve, y_curve)
            diagrams.append(
                {
                    "id": definition.get("id") or label,
                    "row": definition.get("row"),
                    "label": label,
                    "title": label,
                    "plot_type": "work_diagram",
                    "x_label": x_curve.get("label") or definition.get("x_source"),
                    "y_label": y_curve.get("label") or definition.get("y_source"),
                    "x_unit": definition.get("x_unit") or x_curve.get("y_unit") or "",
                    "y_unit": definition.get("y_unit") or y_curve.get("y_unit") or "",
                    "x": x_values,
                    "y": y_values,
                }
            )
        except Exception as exc:
            errors.append("{}：{}".format(label, exc))
    return {"curves": diagrams, "errors": errors}
