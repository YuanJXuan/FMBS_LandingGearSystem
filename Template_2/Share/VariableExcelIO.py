# -*- coding: utf-8 -*-
"""Read and match batch state-variable updates from XLSX workbooks."""

from __future__ import print_function

import math

import SplineDataIO


class VariableExcelError(ValueError):
    """Raised when a variable update workbook is invalid or ambiguous."""


_PREFERRED_SHEETS = ("变量", "变量列表", "仿真变量", "variables", "parameters")
_HEADER_NAMES = {
    "变量",
    "变量名",
    "变量名称",
    "变量路径",
    "状态变量",
    "name",
    "variable",
    "variable name",
    "variable path",
}


def _text(value):
    if value is None:
        return ""
    if isinstance(value, float):
        if not math.isfinite(value):
            return str(value)
        return "{:.15g}".format(value)
    return str(value).strip()


def _select_sheet(file_path):
    try:
        sheets = SplineDataIO.list_xlsx_sheets(file_path)
    except SplineDataIO.SplineDataError as exc:
        raise VariableExcelError(str(exc))
    by_name = {name.strip().lower(): name for name in sheets}
    for preferred in _PREFERRED_SHEETS:
        if preferred.lower() in by_name:
            return by_name[preferred.lower()]
    return sheets[0]


def read_variable_updates(file_path, sheet_name=None):
    """Read ``variable path`` and ``function`` values from columns A and B.

    A header row is optional.  Blank rows are ignored, while partially filled
    rows are rejected so an accidental empty function cannot silently clear a
    model variable.
    """
    selected_sheet = sheet_name or _select_sheet(file_path)
    try:
        selected_sheet, rows = SplineDataIO.read_xlsx_rows(
            file_path,
            selected_sheet,
            max_columns=2,
            formula_columns=(2,),
        )
    except SplineDataIO.SplineDataError as exc:
        raise VariableExcelError(str(exc))

    updates = []
    errors = []
    for row_number, values in rows:
        variable_name = _text(values.get(1))
        function_value = _text(values.get(2))
        if not variable_name and not function_value:
            continue
        if variable_name.strip().lower() in _HEADER_NAMES:
            continue
        if not variable_name:
            errors.append("第 {} 行缺少变量名称/路径".format(row_number))
            continue
        if not function_value:
            errors.append("第 {} 行变量 {} 缺少 function 新值".format(
                row_number, variable_name
            ))
            continue
        updates.append(
            {
                "row": row_number,
                "identifier": variable_name,
                "function": function_value,
            }
        )

    if errors:
        raise VariableExcelError("\n".join(errors))
    if not updates:
        raise VariableExcelError(
            "Excel 中没有可导入的数据；请在 A 列填写变量名称/路径，在 B 列填写 function 新值。"
        )
    return selected_sheet, updates


def _normalize(value):
    return str(value or "").strip().lower()


def match_variable_updates(variables, updates):
    """Match workbook rows to currently displayed state variables.

    Relative paths shown in the interface are preferred.  A fully qualified
    model path is also accepted, and its model-root segment may differ so one
    workbook can be reused after importing an ADM under another scene name.
    A leaf variable name is accepted only when it is unique.
    """
    by_key = {}
    by_path = {}
    by_leaf = {}
    for item in variables:
        key = _normalize(item.get("key", item.get("name")))
        path = _normalize(item.get("path"))
        leaf = _normalize(item.get("name"))
        if key:
            by_key.setdefault(key, []).append(item)
        if path:
            by_path.setdefault(path, []).append(item)
        if leaf:
            by_leaf.setdefault(leaf, []).append(item)

    matched = []
    errors = []
    used_keys = {}
    for update in updates:
        identifier = _normalize(update["identifier"])
        candidates = by_key.get(identifier) or by_path.get(identifier)

        # Remove a leading scene/model segment from an absolute model path.
        if not candidates and identifier.startswith("."):
            path_parts = identifier.lstrip(".").split(".")
            if len(path_parts) > 1:
                candidates = by_key.get(".".join(path_parts[1:]))

        if not candidates:
            candidates = by_leaf.get(identifier)
        if not candidates:
            errors.append(
                "第 {} 行找不到变量：{}".format(
                    update["row"], update["identifier"]
                )
            )
            continue
        if len(candidates) != 1:
            errors.append(
                "第 {} 行变量名称不唯一：{}；请填写界面中显示的完整变量路径".format(
                    update["row"], update["identifier"]
                )
            )
            continue

        item = candidates[0]
        item_key = _normalize(item.get("key", item.get("path")))
        if item_key in used_keys:
            errors.append(
                "第 {} 行与第 {} 行重复修改变量：{}".format(
                    update["row"], used_keys[item_key], item.get("key", item["name"])
                )
            )
            continue
        used_keys[item_key] = update["row"]
        matched.append((item, update["function"], update["row"]))

    return matched, errors
