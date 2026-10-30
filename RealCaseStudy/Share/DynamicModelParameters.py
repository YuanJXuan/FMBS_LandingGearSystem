# -*- coding: utf-8 -*-
"""Discover and edit user-facing state parameters of the active ADM model.

The dedicated template dialogs use this module instead of maintaining a
different hard-coded variable list for every model revision.  Every
``DataElementVariable`` is displayed and edited exclusively through its
``function`` property, whether the function contains a constant or a formula.
"""

from __future__ import print_function

import math
import re


_TIRE_NAME_PATTERN = re.compile(
    r"^(?:nlg|mlg)(?:_[a-z0-9]+)*_(?:m|ixx_iyy|izz|lzz)$",
    re.IGNORECASE,
)


def _scene_root(scene):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    return "." + model_name if model_name else ""


def _children(container):
    if container is None:
        return []
    getter = getattr(container, "getObjects", None)
    if callable(getter):
        try:
            return list(getter())
        except Exception:
            pass
    try:
        return list(container)
    except Exception:
        return []


def _node_type(node):
    values = []
    proxy = getattr(node, "Proxy", None)
    for owner, attribute in ((proxy, "Type"), (node, "TypeId")):
        try:
            value = str(getattr(owner, attribute, "") or "").strip()
        except Exception:
            value = ""
        if value:
            values.append(value)
    return " ".join(values).lower()


def _node_properties(node):
    try:
        return set(getattr(node, "PropertiesList", []) or [])
    except Exception:
        return set()


def _variable_path(root, node, name):
    for attribute in ("variable_name", "Name"):
        try:
            raw_path = str(getattr(node, attribute, "") or "").strip()
        except Exception:
            raw_path = ""
        if not raw_path:
            continue
        if raw_path.startswith("."):
            return raw_path
        if "." in raw_path:
            return "." + raw_path.lstrip(".")
    return root + "." + name


def _variable_name(node):
    for attribute in ("variable_name", "Name", "Label"):
        try:
            raw_name = str(getattr(node, attribute, "") or "").strip()
        except Exception:
            raw_name = ""
        if raw_name:
            return raw_name.rsplit(".", 1)[-1]
    return ""


def _variable_label(node, name):
    try:
        label = str(getattr(node, "Label", "") or "").strip()
    except Exception:
        label = ""
    return label if label and label != name else name


def _state_function(node):
    """Return the state function text, or an empty string when it is unset."""
    properties = _node_properties(node)
    if "function" not in properties and not hasattr(node, "function"):
        return ""
    try:
        function = getattr(node, "function", "")
    except Exception:
        return ""
    return "" if function is None else str(function)


def _state_variable_candidates(scene, root):
    pending = []
    try:
        pending.extend(list(getattr(scene, "Objects", []) or []))
    except Exception:
        pass
    pending.extend(_children(scene))

    get_object = getattr(scene, "getObject", None)
    if callable(get_object):
        for group_name in (
            "DataElements",
            "Data_Elements",
            "Elements",
            "Variables",
        ):
            try:
                group = get_object(root + "." + group_name)
            except Exception:
                group = None
            if group is not None:
                pending.append(group)

    visited = set()
    while pending:
        node = pending.pop(0)
        identity = id(node)
        if identity in visited:
            continue
        visited.add(identity)
        yield node
        pending.extend(_children(node))


def _is_state_variable(node):
    node_type = _node_type(node).replace("_", "").replace(" ", "")
    if "dataelementvariable" in node_type:
        return True
    properties = _node_properties(node)
    return "function" in properties and "variable_name" in properties


def discover_real_variables(scene):
    """Return design variables that expose a finite ``real_value``."""
    root = _scene_root(scene)
    if not root:
        return []
    try:
        design_tools = scene.getObject(root + ".DesignTools")
    except Exception:
        design_tools = None

    # ADM/CMD import normally exposes root variables through DesignTools.  A
    # few platform builds omit that presentation group, so fall back to the
    # model root without hard-coding a template-specific variable list.
    using_design_tools = design_tools is not None
    variable_container = design_tools
    if variable_container is None:
        try:
            variable_container = scene.getObject(root)
        except Exception:
            variable_container = None
    if variable_container is None:
        variable_container = scene

    variables = []
    seen_names = set()
    for node in _children(variable_container):
        raw_name = str(getattr(node, "Name", "") or "").strip()
        name = raw_name.rsplit(".", 1)[-1]
        if not name or name.startswith("_") or name in seen_names:
            continue
        try:
            value = float(getattr(node, "real_value"))
        except (AttributeError, TypeError, ValueError):
            continue
        if not math.isfinite(value):
            continue
        label = str(getattr(node, "Label", "") or "").strip()
        if "." in raw_name:
            node_path = "." + raw_name.lstrip(".")
        else:
            node_path = root + "." + name
        if (
            not using_design_tools
            and "." in raw_name
            and node_path.rsplit(".", 1)[0].lower() != root.lower()
        ):
            continue
        variables.append(
            {
                "name": name,
                "label": label if label and label != name else name,
                "value": value,
                "node": node,
                "path": node_path,
                "kind": "design",
                "value_property": "real_value",
            }
        )
        seen_names.add(name)
    return variables


def discover_state_variables(scene):
    """Return all non-internal state variables, including formula variables."""
    root = _scene_root(scene)
    if not root:
        return []

    variables = []
    seen_paths = set()
    for node in _state_variable_candidates(scene, root):
        if not _is_state_variable(node):
            continue
        name = _variable_name(node)
        if not name or name.startswith("_"):
            continue

        path = _variable_path(root, node, name)
        # Do not accidentally display variables belonging to another model in
        # platform builds whose scene.Objects collection is process-global.
        if path.startswith(".") and not path.lower().startswith(root.lower() + "."):
            continue
        relative_path = path[len(root) + 1:]
        if not relative_path or any(
            segment.startswith("_") for segment in relative_path.split(".")
        ):
            continue

        value = _state_function(node)

        path_key = path.lower()
        if path_key in seen_paths:
            continue
        seen_paths.add(path_key)
        variables.append(
            {
                "name": name,
                "key": relative_path,
                "label": _variable_label(node, name),
                "value": value,
                "node": node,
                "path": path,
                "kind": "state",
                "value_property": "function",
                "value_kind": "expression",
            }
        )
    return variables


def discover_model_variables(scene):
    """Return every state variable; design variables are ignored."""
    return discover_state_variables(scene)


def is_tire_or_road_variable_name(variable_name):
    name = str(variable_name or "").strip().lower()
    return bool(
        "tire" in name
        or "tyre" in name
        or "wheel" in name
        or "luntai" in name
        or "road" in name
        or "lumian" in name
        or "runway" in name
        or _TIRE_NAME_PATTERN.match(name)
    )


def is_tire_variable_name(variable_name):
    """Backward-compatible name for tire/road parameter classification."""
    return is_tire_or_road_variable_name(variable_name)


def partition_variables(variables):
    """Split variables into ordinary and tire/road parameter variables."""
    simulation_variables = []
    tire_variables = []
    for variable in variables:
        target = (
            tire_variables
            if is_tire_or_road_variable_name(
                variable.get("path") or variable.get("key") or variable["name"]
            )
            else simulation_variables
        )
        target.append(variable)
    return simulation_variables, tire_variables


def partition_tire_road_variables(variables):
    """Separate the existing tire/road selection without changing parameter keys."""
    tire_variables, road_variables = [], []
    for variable in variables:
        identifier = variable.get("key")
        if not identifier:
            path = str(variable.get("path") or "").strip()
            # An imported model name may itself contain "road" or "tire".
            identifier = (
                path.lstrip(".").partition(".")[2]
                if path.startswith(".") else path
            ) or variable["name"]
        name = str(identifier).lower()
        target = road_variables if any(
            word in name for word in ("road", "lumian", "runway", "路面", "跑道")
        ) else tire_variables
        target.append(variable)
    return tire_variables, road_variables


def table_rows(variables, label_map=None):
    label_map = label_map or {}
    rows = []
    for item in variables:
        default_label = item["label"]
        if item.get("kind") == "state":
            default_label = "{}（状态变量函数）".format(default_label)
        rows.append(
            (
                label_map.get(
                    item.get("key", item["name"]),
                    label_map.get(item["name"], default_label),
                ),
                item.get("key", item["name"]),
                False,
                item.get("value_kind") != "expression",
            )
        )
    return rows


def populate_table(table, variables):
    for item in variables:
        editor = table.editor(item.get("key", item["name"]))
        if editor is not None:
            editor.setText(str(item["value"]))


def apply_table_values(scene, table, variables):
    """Apply editable values and return ``(updated_count, errors)``."""
    root = _scene_root(scene)
    if not root:
        return 0, ["当前没有活动模型"]

    updated = 0
    errors = []
    for item in variables:
        name = item["name"]
        key = item.get("key", name)
        editor = table.editor(key)
        if editor is None:
            continue
        try:
            text = editor.text().strip()
            if item.get("value_kind") == "expression":
                value = text
            else:
                value = float(text)
                if not math.isfinite(value):
                    raise ValueError("取值必须是有限数值")
            node = scene.getObject(item.get("path") or (root + "." + name))
            if node is None:
                node = item.get("node")
            if node is None:
                raise RuntimeError("模型中已找不到该变量")
            value_property = item.get("value_property", "function")
            setattr(node, value_property, value)
            updated += 1
        except Exception as exc:
            errors.append("{}: {}".format(key, exc))

    recompute = getattr(scene, "recompute", None)
    if updated and callable(recompute):
        try:
            recompute()
        except Exception as exc:
            errors.append("模型刷新失败: {}".format(exc))
    return updated, errors


def apply_function_updates(scene, matched_updates):
    """Atomically write imported ``function`` text to matched state variables.

    ``matched_updates`` contains ``(variable_item, function_text, row_number)``
    tuples.  Every target is resolved before the first write.  If one write or
    the model refresh fails, all values are restored to their previous state.
    """
    root = _scene_root(scene)
    if not root:
        return 0, ["当前没有活动模型"]
    if not matched_updates:
        return 0, ["没有可修改的变量"]

    targets = []
    errors = []
    for item, function_text, row_number in matched_updates:
        key = item.get("key", item.get("name", ""))
        try:
            node = scene.getObject(item.get("path") or (root + "." + item["name"]))
        except Exception:
            node = None
        if node is None:
            node = item.get("node")
        if node is None:
            errors.append(
                "第 {} 行变量 {} 已不在当前模型中".format(row_number, key)
            )
            continue
        if item.get("value_property", "function") != "function":
            errors.append(
                "第 {} 行变量 {} 不是可修改的状态变量".format(row_number, key)
            )
            continue
        try:
            old_function = getattr(node, "function")
        except Exception as exc:
            errors.append(
                "第 {} 行变量 {} 无法读取原 function：{}".format(
                    row_number, key, exc
                )
            )
            continue
        targets.append((node, old_function, str(function_text), key))

    if errors:
        return 0, errors

    recompute = getattr(scene, "recompute", None)
    try:
        for node, _old_function, new_function, _key in targets:
            node.function = new_function
        if callable(recompute):
            recompute()
    except Exception as exc:
        rollback_errors = []
        for node, old_function, _new_function, key in targets:
            try:
                node.function = old_function
            except Exception as rollback_exc:
                rollback_errors.append("{} 恢复失败：{}".format(key, rollback_exc))
        if callable(recompute):
            try:
                recompute()
            except Exception as rollback_exc:
                rollback_errors.append("模型恢复刷新失败：{}".format(rollback_exc))
        message = "批量修改失败，已恢复原值：{}".format(exc)
        if rollback_errors:
            message += "；" + "；".join(rollback_errors)
        return 0, [message]
    return len(targets), []
