# -*- coding: utf-8 -*-
"""Discover and edit physical parameters on imported ``wheel_part`` nodes."""

from __future__ import print_function

import math

import ModelPartDiscovery


TIRE_PROPERTIES = (
    ("mass", "质量"),
    ("ixx", "X轴转动惯量"),
    ("iyy", "Y轴转动惯量"),
    ("izz", "Z轴转动惯量"),
    ("vx", "X方向初始速度"),
    ("vy", "Y方向初始速度"),
    ("vz", "Z方向初始速度"),
)


def _actual_property_name(node, requested_name):
    try:
        getattr(node, requested_name)
        return requested_name
    except Exception:
        pass
    for property_name in getattr(node, "PropertiesList", []) or []:
        if str(property_name).lower() == requested_name.lower():
            return str(property_name)
    return ""


def _display_name(part):
    path = str(part.get("path") or "").strip()
    if path:
        pieces = path.lstrip(".").split(".")
        if len(pieces) > 1:
            return ".".join(pieces[1:])
        return pieces[0]
    return str(part.get("name") or "wheel_part")


def discover_wheel_parameters(scene):
    """Return editable numeric properties from every ``wheel_part`` node."""
    parameters = []
    for part in ModelPartDiscovery.discover_parts(scene, "wheel_part"):
        node = part["node"]
        display_name = _display_name(part)
        for requested_name, meaning in TIRE_PROPERTIES:
            property_name = _actual_property_name(node, requested_name)
            if not property_name:
                continue
            try:
                value = float(getattr(node, property_name))
            except (AttributeError, TypeError, ValueError):
                continue
            if not math.isfinite(value):
                continue
            full_name = "{}.{}".format(display_name, requested_name)
            parameters.append(
                {
                    "name": full_name,
                    "label": "{} - {}".format(display_name, meaning),
                    "value": value,
                    "node": node,
                    "path": part["path"],
                    "property": property_name,
                }
            )
    return parameters


def table_rows(parameters):
    return [(item["label"], item["name"]) for item in parameters]


def populate_table(table, parameters):
    for item in parameters:
        editor = table.editor(item["name"])
        if editor is not None:
            editor.setText("{:.12g}".format(item["value"]))


def apply_table_values(scene, table, parameters):
    """Apply wheel-part values and return ``(updated_count, errors)``."""
    if not ModelPartDiscovery.scene_root(scene):
        return 0, ["当前没有活动模型"]

    updated = 0
    errors = []
    for item in parameters:
        editor = table.editor(item["name"])
        if editor is None:
            continue
        try:
            value = float(editor.text().strip())
            if not math.isfinite(value):
                raise ValueError("取值必须是有限数值")
            node = None
            if item.get("path"):
                try:
                    node = scene.getObject(item["path"])
                except Exception:
                    node = None
            if node is None:
                node = item.get("node")
            if node is None:
                raise RuntimeError("模型中已找不到该轮胎零件")
            setattr(node, item["property"], value)
            updated += 1
        except Exception as exc:
            errors.append("{}: {}".format(item["name"], exc))

    recompute = getattr(scene, "recompute", None)
    if updated and callable(recompute):
        try:
            recompute()
        except Exception as exc:
            errors.append("模型刷新失败: {}".format(exc))
    return updated, errors
