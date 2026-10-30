# -*- coding: utf-8 -*-
"""Discover and directly edit Marker nodes in the active ADM model."""

from __future__ import print_function

import math

import Jusme


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
            value = str(getattr(owner, attribute, "") or "")
        except Exception:
            value = ""
        if value:
            values.append(value)
    return " ".join(values).lower()


def _is_marker(node):
    node_type = _node_type(node)
    if "floating" in node_type:
        return False
    if "marker" in node_type and "floating" not in node_type:
        return True
    try:
        properties = set(getattr(node, "PropertiesList", []) or [])
    except Exception:
        properties = set()
    return "marker_name" in properties and "location" in properties


def _node_path(root, node):
    for attribute in ("marker_name", "Name"):
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
        return root + "." + raw_path
    return ""


def _finite_location(node):
    try:
        return all(
            math.isfinite(float(getattr(node.location, axis)))
            for axis in ("x", "y", "z")
        )
    except Exception:
        return False


def discover_markers(scene):
    """Return every editable non-internal Marker in the active model tree."""
    root = _scene_root(scene)
    if not root:
        return []

    pending = []
    try:
        pending.extend(list(getattr(scene, "Objects", []) or []))
    except Exception:
        pass
    pending.extend(_children(scene))

    get_object = getattr(scene, "getObject", None)
    if callable(get_object):
        for group_name in ("ground", "Bodies", "Parts", "Markers"):
            try:
                group = get_object(root + "." + group_name)
            except Exception:
                group = None
            if group is not None:
                pending.append(group)

    markers = []
    seen_paths = set()
    visited = set()
    while pending:
        node = pending.pop(0)
        identity = id(node)
        if identity in visited:
            continue
        visited.add(identity)
        pending.extend(_children(node))

        if not _is_marker(node) or not _finite_location(node):
            continue
        path = _node_path(root, node)
        if not path or not path.lower().startswith(root.lower() + "."):
            continue
        relative_path = path[len(root) + 1:]
        leaf_name = relative_path.rsplit(".", 1)[-1]
        if leaf_name.startswith("_") or "._cv" in path.lower():
            continue
        path_key = path.lower()
        if path_key in seen_paths:
            continue
        seen_paths.add(path_key)
        markers.append(
            {
                "name": leaf_name,
                "display": relative_path,
                "path": path,
                "node": node,
            }
        )

    return sorted(markers, key=lambda item: item["display"].lower())


def set_marker_location(scene, marker, coordinates):
    """Set one Marker location with rollback and return ``(success, message)``."""
    if scene is None:
        return False, "当前没有活动模型"
    try:
        values = tuple(float(value) for value in coordinates)
    except (TypeError, ValueError):
        return False, "Marker坐标必须是有效数字"
    if len(values) != 3 or not all(math.isfinite(value) for value in values):
        return False, "Marker坐标不能包含NaN或无穷大"

    path = marker.get("path", "") if isinstance(marker, dict) else str(marker or "")
    try:
        node = scene.getObject(path)
    except Exception:
        node = None
    if node is None and isinstance(marker, dict):
        node = marker.get("node")
    if node is None:
        return False, "当前模型中未找到Marker：{}".format(path)

    old_location = None
    try:
        old_location = Jusme.Vector(
            float(node.location.x),
            float(node.location.y),
            float(node.location.z),
        )
        node.location = Jusme.Vector(*values)
        recompute = getattr(scene, "recompute", None)
        if callable(recompute):
            recompute()
    except Exception as exc:
        if old_location is not None:
            try:
                node.location = old_location
                recompute = getattr(scene, "recompute", None)
                if callable(recompute):
                    recompute()
            except Exception:
                pass
        return False, "Marker修改失败，已恢复原坐标：{}: {}".format(
            type(exc).__name__,
            exc,
        )
    return True, "Marker坐标修改完成"
