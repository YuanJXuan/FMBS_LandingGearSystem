# -*- coding: utf-8 -*-
"""Read and apply the case information workbook.

The workbook is intentionally treated as data rather than executable input.
Its sections describe Marker coordinates, simulation parameters,
post-processing requests, work diagrams and spline data files.
"""

from __future__ import print_function

import math
import os

import MarkerCoordinateSystem
import SplineDataIO
import StructuralParameterization


SECTION_TITLES = {
    "几何参数化信息": "markers",
    "仿真参数化信息": "simulation_parameters",
    "缓冲器参数信息": "buffer_parameters",
    "其他参数信息": "other_parameters",
    "结构参数信息": "structure_property_parameters",
    "后处理信息": "postprocessing",
    "功量图信息": "work_diagrams",
    "样条曲线信息": "splines",
}

PARAMETER_SECTION_KEYS = (
    "buffer_parameters",
    "other_parameters",
    "structure_property_parameters",
)

PARAMETER_ID_PREFIXES = {
    "simulation_parameters": "simulation",
    "buffer_parameters": "buffer",
    "other_parameters": "other",
    "structure_property_parameters": "structure_property",
}


class InformationConfigurationError(ValueError):
    """Raised when the case information workbook cannot be read."""


def _text(value):
    if value is None:
        return ""
    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))
        return "{:.15g}".format(value)
    return str(value).strip()


def _number(value, row_number, column_name):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise InformationConfigurationError(
            "第 {} 行{}不是有效数字".format(row_number, column_name)
        )
    if not math.isfinite(number):
        raise InformationConfigurationError(
            "第 {} 行{}不能是NaN或无穷大".format(row_number, column_name)
        )
    return number


def find_information_workbook(case_model_dir):
    """Locate the information workbook in or directly below a case folder."""
    case_model_dir = os.path.abspath(str(case_model_dir or ""))
    candidates = (
        os.path.join(case_model_dir, "信息配置表.xlsx"),
        os.path.join(case_model_dir, "信息配置.xlsx"),
        os.path.join(case_model_dir, "信息配置", "信息配置表.xlsx"),
        os.path.join(case_model_dir, "信息配置", "信息配置.xlsx"),
    )
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate

    discovered = []
    for folder in (case_model_dir, os.path.join(case_model_dir, "信息配置")):
        if not os.path.isdir(folder):
            continue
        for file_name in os.listdir(folder):
            lower_name = file_name.lower()
            if (
                not file_name.startswith("~$")
                and lower_name.endswith(".xlsx")
                and "配置" in file_name
            ):
                discovered.append(os.path.join(folder, file_name))
    return sorted(discovered)[0] if discovered else ""


def _is_header_row(section, values):
    first = _text(values.get(1)).replace(" ", "")
    second = _text(values.get(2)).replace(" ", "")
    if section == "markers":
        return "标记点用户名" in first or "标记点变量名" in second
    if section == "simulation_parameters" or section in PARAMETER_SECTION_KEYS:
        return "参数用户名" in first or "参数变量名" in second
    if section == "postprocessing":
        return "后处理用户名" in first or "后处理变量名" in second
    if section == "work_diagrams":
        return "功量图名称" in first or "x轴曲线" in second.lower()
    if section == "splines":
        return "样条曲线用户名" in first or "样条曲线名" in second
    return False


def _is_section_heading(values, fill_rgb):
    """Only standalone, green-filled labels are presentation headings."""
    if not _text(values.get(1)) or any(_text(values.get(col)) for col in range(2, 6)):
        return False
    if not fill_rgb:
        return False
    red, green, blue = (int(fill_rgb[index:index + 2], 16) for index in (0, 2, 4))
    # Accept dark/light and custom greens, excluding yellow, cyan and gray.
    return green > red + 8 and green > blue + 8


def load_information_configuration(case_model_dir, file_path=None):
    """Parse the case workbook by section title rather than fixed row number."""
    file_path = file_path or find_information_workbook(case_model_dir)
    if not file_path:
        raise InformationConfigurationError(
            "在 {} 中找不到信息配置表.xlsx".format(case_model_dir)
        )
    try:
        sheet_name, rows, row_fills = SplineDataIO.read_xlsx_rows(
            file_path,
            max_columns=5,
            include_row_fills=True,
        )
    except SplineDataIO.SplineDataError as exc:
        raise InformationConfigurationError(str(exc))

    result = {
        "file_path": file_path,
        "base_dir": os.path.dirname(file_path),
        "sheet_name": sheet_name,
        "markers": [],
        "buffer_parameters": [],
        "other_parameters": [],
        "structure_property_parameters": [],
        "legacy_simulation_parameters": [],
        # Aggregate list retained for callers and old tests that still use the
        # original single-section contract.
        "simulation_parameters": [],
        "postprocessing": [],
        "work_diagrams": [],
        "splines": [],
        "section_headers": {},
        "errors": [],
        "warnings": [],
    }
    current_section = ""
    current_heading = None
    for row_number, values in rows:
        first_text = _text(values.get(1))
        if current_section and _is_section_heading(values, row_fills.get(row_number)):
            if current_heading is not None:
                current_heading["end_row"] = row_number
            current_heading = {
                "row": row_number,
                "title": str(values[1]),
                "end_row": None,
            }
            result["section_headers"].setdefault(current_section, []).append(current_heading)
            continue
        if first_text in SECTION_TITLES:
            if current_heading is not None:
                current_heading["end_row"] = row_number
            current_heading = None
            current_section = SECTION_TITLES[first_text]
            continue
        if not current_section or _is_header_row(current_section, values):
            continue
        if not any(_text(values.get(column)) for column in range(1, 6)):
            continue

        try:
            if current_section == "markers":
                label = _text(values.get(1))
                target = _text(values.get(2))
                if not label or not target:
                    raise InformationConfigurationError(
                        "第 {} 行缺少标记点用户名或ADM变量名".format(row_number)
                    )
                coordinates = tuple(
                    _number(values.get(column), row_number, axis + "坐标")
                    for column, axis in zip((3, 4, 5), ("X", "Y", "Z"))
                )
                result["markers"].append(
                    {
                        "id": "config.marker.{}".format(len(result["markers"]) + 1),
                        "row": row_number,
                        "label": label,
                        "target": target,
                        "coordinates": coordinates,
                    }
                )
            elif (
                current_section == "simulation_parameters"
                or current_section in PARAMETER_SECTION_KEYS
            ):
                label = _text(values.get(1))
                target = _text(values.get(2))
                value = values.get(3)
                unit = _text(values.get(4))
                if not label or not target or value is None or _text(value) == "":
                    raise InformationConfigurationError(
                        "第 {} 行缺少参数用户名、ADM变量名或参数值".format(row_number)
                    )
                section_entries = (
                    result["legacy_simulation_parameters"]
                    if current_section == "simulation_parameters"
                    else result[current_section]
                )
                entry = {
                    "id": "config.{}.{}".format(
                        PARAMETER_ID_PREFIXES[current_section],
                        len(section_entries) + 1,
                    ),
                    "row": row_number,
                    "label": label,
                    "target": target,
                    "value": value,
                    "unit": unit,
                }
                section_entries.append(entry)
                result["simulation_parameters"].append(entry)
            elif current_section == "postprocessing":
                label = _text(values.get(1))
                target = _text(values.get(2))
                # A display-name-only row is a harmless workbook placeholder.
                # It becomes active as soon as a result variable is supplied.
                if not target:
                    continue
                result["postprocessing"].append(
                    {
                        "id": "config.postprocessing.{}".format(
                            len(result["postprocessing"]) + 1
                        ),
                        "row": row_number,
                        "label": label or target,
                        "target": target,
                        "x_unit": _text(values.get(3)),
                        "y_unit": _text(values.get(4)),
                    }
                )
            elif current_section == "work_diagrams":
                label = _text(values.get(1))
                x_source = _text(values.get(2))
                y_source = _text(values.get(3))
                if not label or not x_source or not y_source:
                    raise InformationConfigurationError(
                        "第 {} 行缺少功量图名称、X轴曲线或Y轴曲线".format(
                            row_number
                        )
                    )
                result["work_diagrams"].append(
                    {
                        "id": "config.work_diagram.{}".format(
                            len(result["work_diagrams"]) + 1
                        ),
                        "row": row_number,
                        "label": label,
                        "x_source": x_source,
                        "y_source": y_source,
                        "x_unit": _text(values.get(4)),
                        "y_unit": _text(values.get(5)),
                    }
                )
            elif current_section == "splines":
                label = _text(values.get(1))
                target = _text(values.get(2))
                file_name = _text(values.get(3))
                if not label or not target or not file_name:
                    raise InformationConfigurationError(
                        "第 {} 行缺少样条曲线用户名、ADM名称或文件名称".format(
                            row_number
                        )
                    )
                result["splines"].append(
                    {
                        "id": "config.spline.{}".format(
                            len(result["splines"]) + 1
                        ),
                        "row": row_number,
                        "label": label,
                        "target": target,
                        "file_name": file_name,
                    }
                )
        except InformationConfigurationError as exc:
            result["errors"].append(str(exc))

    for section_name, label in (
        ("markers", "Marker"),
        ("simulation_parameters", "仿真参数"),
        ("postprocessing", "后处理变量"),
        ("splines", "样条曲线"),
    ):
        seen_targets = {}
        for entry in result[section_name]:
            target_key = _normalize(entry.get("target"))
            if target_key in seen_targets:
                result["warnings"].append(
                    "配置表第 {} 行与第 {} 行重复指向{}：{}".format(
                        entry.get("row"),
                        seen_targets[target_key],
                        label,
                        entry.get("target"),
                    )
                )
            else:
                seen_targets[target_key] = entry.get("row")

    seen_diagram_labels = {}
    for entry in result["work_diagrams"]:
        label_key = _normalize(entry.get("label"))
        if label_key in seen_diagram_labels:
            result["warnings"].append(
                "配置表第 {} 行与第 {} 行的功量图名称重复：{}".format(
                    entry.get("row"),
                    seen_diagram_labels[label_key],
                    entry.get("label"),
                )
            )
        else:
            seen_diagram_labels[label_key] = entry.get("row")

    return result


def empty_configuration(case_model_dir, error_message=""):
    return {
        "file_path": "",
        "base_dir": os.path.abspath(str(case_model_dir or "")),
        "sheet_name": "",
        "markers": [],
        "buffer_parameters": [],
        "other_parameters": [],
        "structure_property_parameters": [],
        "legacy_simulation_parameters": [],
        "simulation_parameters": [],
        "postprocessing": [],
        "work_diagrams": [],
        "splines": [],
        "section_headers": {},
        "errors": [error_message] if error_message else [],
        "warnings": [],
    }


def _normalize(value):
    return str(value or "").strip().lower()


def simulation_parameter_groups(configuration):
    """Return the three UI parameter groups with legacy workbook fallback.

    Workbooks that still contain the old ``仿真参数化信息`` section are
    intentionally displayed in ``其他参数信息``.  This keeps existing case
    folders operational while allowing new workbooks to use all three
    explicit sections.
    """
    configuration = configuration or {}
    groups = {
        key: list(configuration.get(key, []) or [])
        for key in PARAMETER_SECTION_KEYS
    }
    legacy = configuration.get("legacy_simulation_parameters")
    if legacy is None:
        # Compatibility with configuration dictionaries created by older
        # application versions or tests rather than by this parser.
        if not any(groups.values()):
            legacy = configuration.get("simulation_parameters", [])
        else:
            legacy = []
    groups["other_parameters"].extend(list(legacy or []))
    return groups


def section_entry_groups(configuration, section, entries):
    """Keep Excel heading/data order without adding headings to model records.

    ``None`` titles represent ungrouped rows.  Empty and repeated headings
    remain visible.  Section boundaries stop a preceding heading from leaking
    into ungrouped rows when modern and legacy parameter sections share a tab.
    """
    headers = (configuration or {}).get("section_headers", {})
    headings = list(headers.get(section, []))
    if section == "other_parameters":
        headings.extend(headers.get("simulation_parameters", []))
    entries = list(entries or [])
    if not headings:
        return [(None, entries)]

    events = []
    for heading in headings:
        events.append((heading["row"], 1, heading))
        if heading.get("end_row") is not None:
            events.append((heading["end_row"], 0, None))
    unlocated = []
    for entry in entries:
        row = entry.get("row", entry.get("config_row"))
        if row is None:
            unlocated.append(entry)
        else:
            events.append((row, 2, entry))
    groups = []
    current_rows = None
    for _row, kind, record in sorted(events, key=lambda event: event[:2]):
        if kind == 0:
            current_rows = None
        elif kind == 1:
            current_rows = []
            groups.append((record["title"], current_rows))
        else:
            if current_rows is None:
                current_rows = []
                groups.append((None, current_rows))
            current_rows.append(record)
    if unlocated:
        groups.append((None, unlocated))
    return groups


def _match_state_variable(target, state_variables):
    normalized = _normalize(target)
    target_aliases = {normalized}
    if normalized.startswith("."):
        target_parts = normalized.lstrip(".").split(".")
        if len(target_parts) > 1:
            target_aliases.add(".".join(target_parts[1:]))
    matches = []
    for item in state_variables or []:
        aliases = {
            _normalize(item.get("name")),
            _normalize(item.get("key")),
            _normalize(item.get("path")),
        }
        path = _normalize(item.get("path"))
        if path.startswith("."):
            parts = path.lstrip(".").split(".")
            if len(parts) > 1:
                aliases.add(".".join(parts[1:]))
        if target_aliases.intersection(aliases):
            matches.append(item)
    return matches


def _actual_property_name(node, requested_name):
    if node is None:
        return requested_name
    try:
        getattr(node, requested_name)
        return requested_name
    except Exception:
        pass
    for property_name in getattr(node, "PropertiesList", []) or []:
        if str(property_name).lower() == requested_name.lower():
            return str(property_name)
    return ""


def _configured_value_text(value):
    return _text(value)


def resolve_simulation_parameters(scene, configured_parameters, state_variables):
    """Resolve workbook rows to state functions or ordinary object properties."""
    resolved = []
    for entry in configured_parameters or []:
        target = entry["target"]
        item = {
            "name": target.rsplit(".", 1)[-1],
            "key": entry["id"],
            "display_name": target,
            "label": entry["label"],
            "unit": entry.get("unit", ""),
            "value": _configured_value_text(entry.get("value")),
            "node": None,
            "path": "",
            "kind": "configured",
            "value_property": "function",
            "value_kind": "expression",
            "config_row": entry.get("row"),
            "resolution_error": "",
        }
        state_matches = _match_state_variable(target, state_variables)
        if len(state_matches) == 1:
            state_item = state_matches[0]
            item.update(
                {
                    "name": state_item["name"],
                    "node": state_item.get("node"),
                    "path": state_item.get("path", ""),
                    "kind": "state",
                    "value_property": "function",
                    "value_kind": "expression",
                }
            )
        elif len(state_matches) > 1:
            item["resolution_error"] = "状态变量名称不唯一：{}".format(target)
        elif "." not in target.strip("."):
            item["resolution_error"] = "找不到状态变量：{}".format(target)
        else:
            object_reference, property_name = target.rsplit(".", 1)
            object_path = StructuralParameterization.resolve_path(
                scene, object_reference
            ) if scene is not None else object_reference
            try:
                node = scene.getObject(object_path) if scene is not None else None
            except Exception:
                node = None
            actual_property = _actual_property_name(node, property_name)
            item.update(
                {
                    "node": node,
                    "path": object_path,
                    "kind": "property",
                    "value_property": actual_property or property_name,
                    "value_kind": "numeric",
                }
            )
            if scene is not None and node is None:
                item["resolution_error"] = "找不到对象：{}".format(object_path)
            elif scene is not None and not actual_property:
                item["resolution_error"] = "对象 {} 没有属性 {}".format(
                    object_path, property_name
                )
        resolved.append(item)
    return resolved


def dynamic_simulation_parameters(state_variables, label_map=None):
    """Adapt discovered state variables to the configurable table contract."""
    label_map = label_map or {}
    parameters = []
    for variable in state_variables or []:
        item = dict(variable)
        key = item.get("key", item.get("name", ""))
        name = item.get("name", key)
        item["key"] = key
        item["display_name"] = key
        item["label"] = label_map.get(
            key,
            label_map.get(name, item.get("label", name)),
        )
        item["unit"] = ""
        item["config_row"] = None
        item["resolution_error"] = ""
        parameters.append(item)
    return parameters


def simulation_table_rows(parameters):
    rows = []
    for item in parameters or []:
        label = item["label"]
        if item.get("unit"):
            label += " ({})".format(item["unit"])
        rows.append(
            (
                label,
                item["display_name"],
                False,
                item.get("value_kind") != "expression",
                item["key"],
            )
        )
    return rows


def populate_simulation_table(table, parameters):
    for item in parameters or []:
        editor = table.editor(item["key"])
        if editor is not None:
            editor.setText(str(item["value"]))
            if item.get("resolution_error"):
                editor.setToolTip(item["resolution_error"])
                editor.setStyleSheet("border: 1px solid #d8a000;")


def apply_simulation_table(scene, table, parameters):
    """Atomically apply the simulation rows currently displayed in the table."""
    if scene is None:
        return 0, ["当前没有活动模型"]
    targets = []
    errors = []
    seen = {}
    for item in parameters or []:
        editor = table.editor(item["key"])
        if editor is None:
            continue
        if item.get("resolution_error"):
            errors.append(item["resolution_error"])
            continue
        try:
            node = scene.getObject(item.get("path")) if item.get("path") else None
        except Exception:
            node = None
        if node is None:
            node = item.get("node")
        if node is None:
            errors.append("找不到参数对象：{}".format(item["display_name"]))
            continue
        property_name = item.get("value_property", "function")
        identity = (id(node), property_name.lower())
        if identity in seen:
            errors.append(
                "配置表第 {} 行与第 {} 行重复指向：{}".format(
                    item.get("config_row"),
                    seen[identity],
                    item["display_name"],
                )
            )
            continue
        seen[identity] = item.get("config_row")
        try:
            old_value = getattr(node, property_name)
            text = editor.text().strip()
            if item.get("value_kind") == "expression":
                if not text:
                    raise ValueError("function不能为空")
                new_value = text
            else:
                new_value = float(text)
                if not math.isfinite(new_value):
                    raise ValueError("取值必须是有限数值")
            targets.append(
                (node, property_name, old_value, new_value, item["display_name"])
            )
        except Exception as exc:
            errors.append("{}: {}".format(item["display_name"], exc))
    if errors:
        return 0, errors

    recompute = getattr(scene, "recompute", None)
    try:
        for node, property_name, _old_value, new_value, _label in targets:
            setattr(node, property_name, new_value)
        if callable(recompute):
            recompute()
    except Exception as exc:
        rollback_errors = []
        for node, property_name, old_value, _new_value, label in reversed(targets):
            try:
                setattr(node, property_name, old_value)
            except Exception as rollback_exc:
                rollback_errors.append("{} 恢复失败：{}".format(label, rollback_exc))
        if callable(recompute):
            try:
                recompute()
            except Exception as rollback_exc:
                rollback_errors.append("模型恢复刷新失败：{}".format(rollback_exc))
        message = "仿真参数写入失败，已恢复原值：{}".format(exc)
        if rollback_errors:
            message += "；" + "；".join(rollback_errors)
        return 0, [message]
    return len(targets), []


def _path_aliases(path):
    normalized = _normalize(path).lstrip(".")
    aliases = {normalized} if normalized else set()
    parts = normalized.split(".")
    if str(path or "").strip().startswith(".") and len(parts) > 2:
        aliases.add(".".join(parts[1:]))
    return aliases


def _linkage_matches(marker_entry, linkage_definitions):
    target_aliases = _path_aliases(marker_entry.get("target"))
    return [
        parameter
        for parameter in linkage_definitions or []
        if target_aliases.intersection(_path_aliases(parameter.get("driver")))
    ]


def count_marker_linkages(marker_entries, linkage_definitions):
    """Return how many configured Marker rows have exactly one linkage rule."""
    count = 0
    for entry in marker_entries or []:
        matches = _linkage_matches(entry, linkage_definitions)
        if len(matches) == 1 and (
            matches[0].get("followers")
            or matches[0].get("coaxial")
            or matches[0].get("coincident_with")
        ):
            count += 1
    return count


def marker_coordinates_for_selection(
    marker_entries,
    linkage_definitions,
    selected_entry_id,
    coordinates,
):
    """Build the connected Excel Marker batch for one dropdown edit.

    The information workbook remains the authoritative list.  A single edit
    is expanded only to the connected coaxial endpoints and coincident
    Markers required by the atomic linkage engine.  Unrelated configured
    Markers are deliberately excluded so one dropdown edit cannot reset a
    separate assembly.  Markers declared with ``coincident_with`` are assigned
    the same requested world coordinates, matching the synchronized editors
    in ``MarkerConfigurationTable``.
    """
    requested = _coordinates(coordinates)
    entries = list(marker_entries or [])
    entries_by_id = {entry.get("id"): entry for entry in entries}
    selected = entries_by_id.get(selected_entry_id)
    if selected is None:
        raise ValueError("信息配置表中找不到选中的Marker")

    def entry_ids_for_paths(paths):
        aliases = set()
        for path in paths:
            aliases.update(_path_aliases(path))
        return {
            entry["id"]
            for entry in entries
            if _path_aliases(entry.get("target")).intersection(aliases)
        }

    included_ids = {selected_entry_id}
    synchronized_ids = {selected_entry_id}

    # Treat coincident declarations as undirected, transitive groups.  This
    # allows selecting either side of a shared joint to keep both Excel rows
    # synchronized before the linkage transaction is validated.
    groups = []
    for parameter in linkage_definitions or []:
        coincident_paths = list(parameter.get("coincident_with") or [])
        if not coincident_paths:
            continue
        group_ids = entry_ids_for_paths(
            [parameter.get("driver")] + coincident_paths
        )
        if len(group_ids) > 1:
            groups.append(group_ids)

    changed = True
    while changed:
        changed = False
        for group_ids in groups:
            if synchronized_ids.intersection(group_ids) and not group_ids.issubset(
                synchronized_ids
            ):
                synchronized_ids.update(group_ids)
                changed = True

    included_ids.update(synchronized_ids)
    changed = True
    while changed:
        changed = False
        for parameter in linkage_definitions or []:
            driver_ids = entry_ids_for_paths([parameter.get("driver")])
            if not included_ids.intersection(driver_ids):
                continue
            dependency_paths = list(parameter.get("coincident_with") or [])
            dependency_paths.append(parameter.get("driver"))
            for group in parameter.get("coaxial", []):
                dependency_paths.extend((group.get("start"), group.get("end")))
            dependency_ids = entry_ids_for_paths(dependency_paths)
            if not dependency_ids.issubset(included_ids):
                included_ids.update(dependency_ids)
                changed = True

    batch_entries = [
        entry for entry in entries if entry["id"] in included_ids
    ]
    values = {
        entry["id"]: _coordinates(entry.get("coordinates", ()))
        for entry in batch_entries
    }
    for entry_id in synchronized_ids:
        values[entry_id] = requested
    return batch_entries, values, synchronized_ids


def _linked_world_location(follower, driver_world):
    axes = tuple(follower.get("axes") or ("x", "y", "z"))
    if set(axes) != {"x", "y", "z"}:
        raise ValueError("结构参数表联动必须同时定义X、Y、Z三个世界坐标")
    operation = follower.get("operation", "copy")
    if operation == "copy":
        return tuple(driver_world)
    if operation == "offset":
        raw_offset = follower.get("offset") or {}
        if isinstance(raw_offset, dict):
            offset = tuple(float(raw_offset.get(axis, 0.0)) for axis in ("x", "y", "z"))
        else:
            offset = (float(raw_offset),) * 3
        return tuple(driver_world[index] + offset[index] for index in range(3))
    if operation == "mirror":
        raw_origin = follower.get("origin") or {}
        if isinstance(raw_origin, dict):
            origin = tuple(float(raw_origin.get(axis, 0.0)) for axis in ("x", "y", "z"))
        else:
            origin = (float(raw_origin),) * 3
        return tuple(2.0 * origin[index] - driver_world[index] for index in range(3))
    raise ValueError(
        "结构参数表的世界坐标联动不支持 operation={}；请使用copy、offset或mirror".format(
            operation
        )
    )


def _coordinates(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        result = tuple(float(getattr(value, axis)) for axis in ("x", "y", "z"))
    else:
        result = tuple(float(value[index]) for index in range(3))
    if not all(math.isfinite(number) for number in result):
        raise ValueError("坐标包含NaN或无穷大")
    return result


def _interpolate(start, end, fraction):
    return tuple(
        start[index] + float(fraction) * (end[index] - start[index])
        for index in range(3)
    )


def _coaxial_marker_location(scene, start, end, axis_length, marker):
    """Place a marker by ratio or by a fixed distance along the shared axis."""
    cylinder_path = marker.get("cylinder")
    if cylinder_path:
        resolved_path, cylinder = StructuralParameterization.resolve_object(
            scene, cylinder_path
        )
        if cylinder is None:
            raise ValueError("找不到圆柱几何体：{}".format(resolved_path))
        try:
            distance = float(cylinder.length) * float(
                marker.get("cylinder_scale", 0.5)
            )
        except Exception as exc:
            raise ValueError(
                "无法读取圆柱几何体 {} 的长度：{}".format(resolved_path, exc)
            )
        if not math.isfinite(distance) or distance <= 0.0:
            raise ValueError("圆柱几何体 {} 的长度必须大于0".format(resolved_path))
    elif marker.get("distance") is not None:
        distance = float(marker["distance"])
    else:
        location = _interpolate(start, end, marker["fraction"])
        offset = marker.get("offset") or {}
        return tuple(
            location[index] + float(offset.get(axis, 0.0))
            for index, axis in enumerate(("x", "y", "z"))
        )
    fraction = distance / float(axis_length)
    if marker.get("distance_from", "start") == "end":
        fraction = 1.0 - fraction
    location = _interpolate(start, end, fraction)
    offset = marker.get("offset") or {}
    return tuple(
        location[index] + float(offset.get(axis, 0.0))
        for index, axis in enumerate(("x", "y", "z"))
    )


def _coaxial_groups(parameters):
    groups = []
    seen = set()
    for parameter in parameters:
        for group in parameter.get("coaxial", []):
            key = group["id"].lower()
            if key in seen:
                continue
            seen.add(key)
            groups.append(group)
    return groups


def apply_marker_values(
    scene,
    marker_entries,
    coordinates_by_id,
    linkage_definitions=None,
):
    """Atomically set ADM/world Marker coordinates and configured followers."""
    if scene is None:
        return 0, ["当前没有活动模型"]
    try:
        import Jusme
    except Exception as exc:
        return 0, ["无法创建Marker坐标：{}".format(exc)]

    targets = []
    errors = []
    seen_nodes = {}
    targets_by_path = {}
    desired_world_by_path = {}
    property_targets = []
    seen_properties = set()
    recompute_nodes = []
    seen_recompute_nodes = set()
    active_parameters = []

    def add_recompute(path):
        resolved_path, node = StructuralParameterization.resolve_object(scene, path)
        if node is None or id(node) in seen_recompute_nodes:
            return
        seen_recompute_nodes.add(id(node))
        recompute_nodes.append((resolved_path, node))

    def add_target(
        node,
        path,
        target_type,
        world_location,
        row_number,
        label,
        world_orientation=None,
    ):
        if node is None:
            errors.append("第 {} 行找不到联动对象：{}".format(row_number, path))
            return
        if id(node) in seen_nodes:
            errors.append(
                "配置表第 {} 行与第 {} 行重复修改对象：{}".format(
                    row_number, seen_nodes[id(node)], path
                )
            )
            return
        try:
            old_location = _coordinates(node.location)
            desired_world = _coordinates(world_location)
            old_orientation = (
                _coordinates(node.orientation)
                if world_orientation is not None
                else None
            )
            desired_orientation = (
                _coordinates(world_orientation)
                if world_orientation is not None
                else None
            )
        except Exception as exc:
            errors.append("{}: {}".format(label, exc))
            return
        seen_nodes[id(node)] = row_number
        desired_world_by_path[path.lower()] = desired_world
        target = {
            "node": node,
            "old_location": old_location,
            "old_orientation": old_orientation,
            "world_location": desired_world,
            "world_orientation": desired_orientation,
            "path": path,
            "target_type": target_type,
        }
        targets.append(target)
        targets_by_path[path.lower()] = target

    def set_target_orientation(path, node, world_orientation, label):
        target = targets_by_path.get(path.lower())
        if target is None or target["node"] is not node:
            errors.append("{} 找不到待调整的轴线Marker：{}".format(label, path))
            return
        try:
            if target["old_orientation"] is None:
                target["old_orientation"] = _coordinates(node.orientation)
            target["world_orientation"] = _coordinates(world_orientation)
        except Exception as exc:
            errors.append("{}: {}".format(label, exc))

    def add_property_target(node, path, property_name, new_value, label):
        if node is None:
            errors.append("{} 找不到长度联动对象：{}".format(label, path))
            return
        identity = (id(node), property_name)
        if identity in seen_properties:
            errors.append("结构参数重复修改属性：{}.{}".format(path, property_name))
            return
        try:
            old_value = float(getattr(node, property_name))
            new_value = float(new_value)
            if not math.isfinite(old_value) or not math.isfinite(new_value):
                raise ValueError("属性值必须是有限数值")
            if new_value <= 0.0:
                raise ValueError("长度必须大于0")
        except Exception as exc:
            errors.append("{}: {}".format(label, exc))
            return
        seen_properties.add(identity)
        property_targets.append(
            {
                "node": node,
                "path": path,
                "property_name": property_name,
                "old_value": old_value,
                "new_value": new_value,
            }
        )

    for entry in marker_entries or []:
        try:
            world_location = tuple(
                float(value) for value in coordinates_by_id[entry["id"]]
            )
            if not all(math.isfinite(value) for value in world_location):
                raise ValueError("坐标必须是有限数值")
        except Exception as exc:
            errors.append("{}: {}".format(entry["label"], exc))
            continue

        linkage_matches = _linkage_matches(entry, linkage_definitions)
        if len(linkage_matches) > 1:
            errors.append(
                "第 {} 行Marker匹配到多个结构联动规则：{}".format(
                    entry["row"], entry["target"]
                )
            )
            continue
        parameter = linkage_matches[0] if linkage_matches else None
        if parameter is not None and parameter not in active_parameters:
            active_parameters.append(parameter)
        driver_path = parameter["driver"] if parameter else entry["target"]
        resolved_path, node = StructuralParameterization.resolve_object(
            scene, driver_path
        )
        if node is None:
            errors.append(
                "第 {} 行找不到Marker：{}".format(entry["row"], resolved_path)
            )
            continue
        add_target(
            node,
            resolved_path,
            "marker",
            world_location,
            entry["row"],
            entry["label"],
        )

        if parameter is None:
            continue
        for follower in parameter.get("followers", []):
            follower_path, follower_node = StructuralParameterization.resolve_object(
                scene, follower["path"]
            )
            if follower_node is None and not follower.get("required", True):
                continue
            try:
                follower_world = _linked_world_location(follower, world_location)
            except Exception as exc:
                errors.append(
                    "{} 的联动规则无效：{}".format(entry["label"], exc)
                )
                continue
            add_target(
                follower_node,
                follower_path,
                follower.get("target_type", "marker"),
                follower_world,
                entry["row"],
                "{} -> {}".format(entry["label"], follower_path),
            )

        for recompute_path in parameter.get("recompute", []):
            add_recompute(recompute_path)

    checked_coincident_pairs = set()
    for parameter in active_parameters:
        driver_path, driver_node = StructuralParameterization.resolve_object(
            scene, parameter["driver"]
        )
        driver_location = desired_world_by_path.get(driver_path.lower())
        for peer in parameter.get("coincident_with", []):
            peer_path, peer_node = StructuralParameterization.resolve_object(
                scene, peer
            )
            pair_key = tuple(sorted((driver_path.lower(), peer_path.lower())))
            if pair_key in checked_coincident_pairs:
                continue
            checked_coincident_pairs.add(pair_key)
            peer_location = desired_world_by_path.get(peer_path.lower())
            if driver_node is None or peer_node is None:
                errors.append(
                    "同位置参数 {} 找不到对象：{}、{}".format(
                        parameter["label"], driver_path, peer_path
                    )
                )
                continue
            if driver_location is None or peer_location is None:
                errors.append(
                    "同位置参数 {} 要求信息配置表同时包含：{}、{}".format(
                        parameter["label"], parameter["driver"], peer
                    )
                )
                continue
            separation = math.sqrt(
                sum(
                    (driver_location[index] - peer_location[index]) ** 2
                    for index in range(3)
                )
            )
            if separation > parameter.get("coincident_tolerance", 1.0e-5):
                errors.append(
                    "同位置参数 {} 与 {} 的坐标不一致，相差 {:.6g}".format(
                        parameter["driver"], peer, separation
                    )
                )

    coaxial_groups = _coaxial_groups(active_parameters)
    if coaxial_groups:
        try:
            import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils
        except Exception as exc:
            errors.append("无法加载共轴计算函数 ORI_ALONG_AXIS：{}".format(exc))
            VecUtils = None
    else:
        VecUtils = None

    for group in coaxial_groups:
        start_path, start_node = StructuralParameterization.resolve_object(
            scene, group["start"]
        )
        end_path, end_node = StructuralParameterization.resolve_object(
            scene, group["end"]
        )
        start = desired_world_by_path.get(start_path.lower())
        end = desired_world_by_path.get(end_path.lower())
        if start_node is None or end_node is None:
            errors.append("共轴约束 {} 找不到端点对象".format(group["id"]))
            continue
        if start is None or end is None:
            errors.append(
                "共轴约束 {} 要求信息配置表同时包含两个端点：{}、{}".format(
                    group["id"], group["start"], group["end"]
                )
            )
            continue
        axis_length = math.sqrt(
            sum((end[index] - start[index]) ** 2 for index in range(3))
        )
        if axis_length <= 1.0e-7:
            errors.append("共轴约束 {} 的两个端点不能重合".format(group["id"]))
            continue

        try:
            forward_orientation = _coordinates(
                VecUtils.ORI_ALONG_AXIS(
                    Jusme.Vector(*start),
                    Jusme.Vector(*end),
                    group["axis"],
                )
            )
            reverse_orientation = _coordinates(
                VecUtils.ORI_ALONG_AXIS(
                    Jusme.Vector(*end),
                    Jusme.Vector(*start),
                    group["axis"],
                )
            )
        except Exception as exc:
            errors.append(
                "共轴约束 {} 无法计算轴向：{}".format(group["id"], exc)
            )
            continue
        if group.get("align_start_orientation", True):
            set_target_orientation(
                start_path,
                start_node,
                reverse_orientation if group["start_reverse"] else forward_orientation,
                "共轴约束 {}".format(group["id"]),
            )
        if group.get("align_end_orientation", True):
            set_target_orientation(
                end_path,
                end_node,
                reverse_orientation if group["end_reverse"] else forward_orientation,
                "共轴约束 {}".format(group["id"]),
            )

        for marker in group.get("markers", []):
            marker_path, marker_node = StructuralParameterization.resolve_object(
                scene, marker["path"]
            )
            if marker_node is None and not marker.get("required", True):
                continue
            try:
                marker_location = _coaxial_marker_location(
                    scene, start, end, axis_length, marker
                )
            except Exception as exc:
                errors.append(
                    "共轴约束 {} 无法定位 {}：{}".format(
                        group["id"], marker_path, exc
                    )
                )
                continue
            add_target(
                marker_node,
                marker_path,
                marker.get("target_type", "marker"),
                marker_location,
                "共轴约束 {}".format(group["id"]),
                "共轴约束 {} -> {}".format(group["id"], marker_path),
                (
                    reverse_orientation
                    if marker["reverse"]
                    else forward_orientation
                )
                if marker["align_orientation"]
                else None,
            )
        for recompute_path in group.get("recompute", []):
            add_recompute(recompute_path)
        for length_target in group.get("length_targets", []):
            resolved_path, node = StructuralParameterization.resolve_object(
                scene, length_target["path"]
            )
            if node is None and not length_target.get("required", True):
                continue
            add_property_target(
                node,
                resolved_path,
                "length",
                axis_length * length_target["scale"]
                + length_target["offset"],
                "共轴约束 {}".format(group["id"]),
            )

    for group in coaxial_groups:
        for pair in group.get("coincident_pairs", []):
            first_path, first_node = StructuralParameterization.resolve_object(
                scene, pair["first"]
            )
            second_path, second_node = StructuralParameterization.resolve_object(
                scene, pair["second"]
            )
            first_location = desired_world_by_path.get(first_path.lower())
            second_location = desired_world_by_path.get(second_path.lower())
            if first_node is None or second_node is None:
                errors.append(
                    "共轴约束 {} 的重合校验找不到对象：{}、{}".format(
                        group["id"], first_path, second_path
                    )
                )
                continue
            if first_location is None or second_location is None:
                errors.append(
                    "共轴约束 {} 的重合校验对象未加入联动：{}、{}".format(
                        group["id"], first_path, second_path
                    )
                )
                continue
            separation = math.sqrt(
                sum(
                    (first_location[index] - second_location[index]) ** 2
                    for index in range(3)
                )
            )
            if separation > pair["tolerance"]:
                errors.append(
                    "共轴约束 {} 的副端点不重合：{} 与 {} 相差 {:.6g}".format(
                        group["id"], first_path, second_path, separation
                    )
                )
    if errors:
        return 0, errors

    recompute = getattr(scene, "recompute", None)
    try:
        converted_targets = []
        for target in targets:
            if target["target_type"] == "part":
                new_location = target["world_location"]
                new_orientation = target["world_orientation"]
            elif target["world_orientation"] is not None:
                new_location, new_orientation = (
                    MarkerCoordinateSystem.world_pose_to_local(
                        scene,
                        target["node"],
                        target["path"],
                        target["world_location"],
                        target["world_orientation"],
                    )
                )
            else:
                new_location = MarkerCoordinateSystem.world_to_local(
                    scene,
                    target["node"],
                    target["path"],
                    target["world_location"],
                )
                new_orientation = None
            converted_targets.append((target, new_location, new_orientation))
        for target, new_location, new_orientation in converted_targets:
            target["node"].location = Jusme.Vector(*new_location)
            if new_orientation is not None:
                target["node"].orientation = Jusme.Vector(*new_orientation)
        for target in property_targets:
            setattr(
                target["node"],
                target["property_name"],
                target["new_value"],
            )
        if callable(recompute):
            recompute()
        for _path, node in recompute_nodes:
            node_recompute = getattr(node, "recompute", None)
            if callable(node_recompute):
                node_recompute()
        if callable(recompute):
            recompute()
    except Exception as exc:
        rollback_errors = []
        for target in reversed(property_targets):
            try:
                setattr(
                    target["node"],
                    target["property_name"],
                    target["old_value"],
                )
            except Exception as rollback_exc:
                rollback_errors.append(
                    "{}.{} 恢复失败：{}".format(
                        target["path"],
                        target["property_name"],
                        rollback_exc,
                    )
                )
        for target in reversed(targets):
            try:
                target["node"].location = Jusme.Vector(*target["old_location"])
                if target["old_orientation"] is not None:
                    target["node"].orientation = Jusme.Vector(
                        *target["old_orientation"]
                    )
            except Exception as rollback_exc:
                rollback_errors.append(
                    "{} 恢复失败：{}".format(target["path"], rollback_exc)
                )
        if callable(recompute):
            try:
                recompute()
            except Exception as rollback_exc:
                rollback_errors.append("模型恢复刷新失败：{}".format(rollback_exc))
        for path, node in recompute_nodes:
            try:
                node_recompute = getattr(node, "recompute", None)
                if callable(node_recompute):
                    node_recompute()
            except Exception as rollback_exc:
                rollback_errors.append("{} 恢复刷新失败：{}".format(path, rollback_exc))
        if callable(recompute):
            try:
                recompute()
            except Exception as rollback_exc:
                rollback_errors.append("模型恢复刷新失败：{}".format(rollback_exc))
        message = "Marker批量修改失败，已恢复原位置和方向：{}".format(exc)
        if rollback_errors:
            message += "；" + "；".join(rollback_errors)
        return 0, [message]
    return len(targets) + len(property_targets), []


def _spline_aliases(spline):
    aliases = set()
    for attribute in ("Name", "Label", "spline_name"):
        value = _normalize(getattr(spline, attribute, ""))
        if not value:
            continue
        aliases.add(value)
        aliases.add(value.lstrip(".").rsplit(".", 1)[-1])
        parts = value.lstrip(".").split(".")
        if len(parts) > 1:
            aliases.add(".".join(parts[1:]))
    return aliases


def _configured_spline_file(configuration, file_name):
    base_dir = os.path.abspath(configuration.get("base_dir") or "")
    file_path = os.path.abspath(os.path.join(base_dir, file_name))
    try:
        if os.path.commonpath((base_dir, file_path)) != base_dir:
            raise ValueError("样条文件必须位于信息配置表同目录下")
    except ValueError as exc:
        raise InformationConfigurationError(str(exc))
    if not os.path.isfile(file_path):
        raise InformationConfigurationError("找不到样条数据文件：{}".format(file_path))
    return file_path


def apply_configured_splines(scene, configuration):
    """Atomically replace all splines listed in the information workbook."""
    if scene is None:
        return 0, ["当前没有活动模型"]
    splines = SplineDataIO.find_scene_splines(scene)
    targets = []
    errors = []
    used_splines = set()
    for entry in configuration.get("splines", []):
        target_name = _normalize(entry["target"])
        matches = [spline for spline in splines if target_name in _spline_aliases(spline)]
        if not matches:
            errors.append("找不到样条曲线：{}".format(entry["target"]))
            continue
        if len(matches) > 1:
            errors.append("样条曲线名称不唯一：{}".format(entry["target"]))
            continue
        spline = matches[0]
        if id(spline) in used_splines:
            errors.append("配置表重复指向样条曲线：{}".format(entry["target"]))
            continue
        used_splines.add(id(spline))
        try:
            if len(getattr(spline, "z", []) or []):
                raise InformationConfigurationError("目标样条包含Z数据，暂不支持覆盖")
            file_path = _configured_spline_file(configuration, entry["file_name"])
            points = SplineDataIO.read_spline_points(file_path)
            old_x_value = getattr(spline, "x", None)
            old_y_value = getattr(spline, "y", None)
            old_x = list(old_x_value) if old_x_value is not None else None
            old_y = list(old_y_value) if old_y_value is not None else None
            targets.append((spline, old_x, old_y, points, entry["target"]))
        except (InformationConfigurationError, SplineDataIO.SplineDataError) as exc:
            errors.append("{}: {}".format(entry["label"], exc))
    if errors:
        return 0, errors

    recompute = getattr(scene, "recompute", None)
    try:
        for spline, _old_x, _old_y, points, _label in targets:
            spline.x = [point[0] for point in points]
            spline.y = [point[1] for point in points]
        if callable(recompute):
            recompute()
    except Exception as exc:
        rollback_errors = []
        for spline, old_x, old_y, _points, label in reversed(targets):
            try:
                if old_x is not None:
                    spline.x = old_x
                if old_y is not None:
                    spline.y = old_y
            except Exception as rollback_exc:
                rollback_errors.append("{} 恢复失败：{}".format(label, rollback_exc))
        if callable(recompute):
            try:
                recompute()
            except Exception as rollback_exc:
                rollback_errors.append("模型恢复刷新失败：{}".format(rollback_exc))
        message = "样条曲线写入失败，已恢复原数据：{}".format(exc)
        if rollback_errors:
            message += "；" + "；".join(rollback_errors)
        return 0, [message]
    return len(targets), []
