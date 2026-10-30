# -*- coding: utf-8 -*-
"""Model-name-independent discovery of ADM-imported physical parts."""

from __future__ import print_function


def scene_root(scene):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    return "." + model_name if model_name else ""


def children(container):
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


def _node_names(node):
    names = []
    for attribute in ("Name", "Label"):
        value = str(getattr(node, attribute, "") or "").strip()
        if value and value not in names:
            names.append(value)
    return names


def _matches_suffix(node, suffix):
    suffix = str(suffix or "").strip().lower().lstrip("._")
    if not suffix:
        return False
    for name in _node_names(node):
        normalized = name.lower().strip().rstrip(".")
        if (
            normalized == suffix
            or normalized.endswith("." + suffix)
            or normalized.endswith("_" + suffix)
        ):
            return True
    return False


def object_path(scene, node):
    """Return the best resolvable absolute path for a discovered node."""
    root = scene_root(scene)
    if not root:
        return ""
    model_name = root.lstrip(".")
    candidates = []
    for raw_name in _node_names(node):
        if raw_name.startswith("."):
            candidates.append(raw_name)
        elif raw_name.startswith(model_name + "."):
            candidates.append("." + raw_name)
        else:
            candidates.append(root + "." + raw_name)
            if "." in raw_name:
                # ADM imports commonly flatten UDE paths such as
                # ``tire.wheel_part`` to ``tire_wheel_part``.
                candidates.append(root + "." + raw_name.replace(".", "_"))

    for path in candidates:
        try:
            if scene.getObject(path) is not None:
                return path
        except Exception:
            pass
    return candidates[0] if candidates else ""


def discover_parts(scene, suffix):
    """Discover all nodes whose Name/Label ends in the requested suffix."""
    root = scene_root(scene)
    if not root:
        return []

    try:
        bodies = scene.getObject(root + ".Bodies")
    except Exception:
        bodies = None
    if bodies is not None:
        # Physical wheel/road parts are direct members of Bodies after ADM
        # import.  Staying in this group avoids walking every marker, force and
        # result object in a large model on each UI refresh.
        starts = [bodies]
    else:
        try:
            model_root = scene.getObject(root)
        except Exception:
            model_root = None
        starts = [node for node in (model_root, scene) if node is not None]

    queue = list(starts)
    visited = set()
    matches = []
    while queue:
        container = queue.pop(0)
        identity = id(container)
        if identity in visited:
            continue
        visited.add(identity)
        for node in children(container):
            node_identity = id(node)
            if node_identity not in visited:
                queue.append(node)
            if _matches_suffix(node, suffix):
                matches.append(
                    {
                        "node": node,
                        "path": object_path(scene, node),
                        "name": (_node_names(node) or [suffix])[0],
                    }
                )

    unique = []
    seen = set()
    for item in matches:
        key = item["path"].lower() if item["path"] else id(item["node"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    unique.sort(key=lambda item: (item["path"] or item["name"]).lower())
    return unique
