# -*- coding: utf-8 -*-
"""Model-name-independent road position discovery and synchronization."""

import math

import ModelPartDiscovery


ROAD_PART_SUFFIXES = (
    ".lumian_road_part",
    ".lm_road_part",
    ".road_part",
    ".lumian.road_part",
    ".lm.road_part",
    ".road.road_part",
)

GROUND_REFERENCE_SUFFIXES = (
    ".ground.lumian_ref_1",
    ".ground.lm_ref_1",
    ".ground.road_ref_1",
    ".ground.road_ref",
)

ROAD_JOINT_SUFFIXES = (
    ".lumian_road_joint",
    ".lm_road_joint",
    ".road_joint",
    ".lumian.road_joint",
    ".lm.road_joint",
    ".road.road_joint",
)


def _root(scene):
    name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    return "." + name if name else ""


def _find(scene, suffixes):
    root = _root(scene)
    if not root:
        return None
    for suffix in suffixes:
        try:
            node = scene.getObject(root + suffix)
        except Exception:
            node = None
        if node is not None:
            return node
    return None


def find_road_part(scene):
    road_part = _find(scene, ROAD_PART_SUFFIXES)
    if road_part is not None:
        return road_part
    parts = ModelPartDiscovery.discover_parts(scene, "road_part")
    return parts[0]["node"] if parts else None


def _road_prefixes(scene):
    prefixes = []
    for part in ModelPartDiscovery.discover_parts(scene, "road_part"):
        for value in (part.get("name"), part.get("path")):
            name = str(value or "").strip().lstrip(".").split(".")[-1]
            lower_name = name.lower()
            if lower_name.endswith("_road_part"):
                prefix = name[: -len("_road_part")]
            elif lower_name == "road_part":
                prefix = "road"
            else:
                continue
            if prefix and prefix not in prefixes:
                prefixes.append(prefix)
    return prefixes


def find_ground_reference(scene):
    reference = _find(scene, GROUND_REFERENCE_SUFFIXES)
    if reference is not None:
        return reference
    dynamic_suffixes = []
    for prefix in _road_prefixes(scene):
        dynamic_suffixes.extend(
            (".ground.{}_ref_1".format(prefix), ".ground.{}_ref".format(prefix))
        )
    return _find(scene, dynamic_suffixes)


def find_road_joint(scene):
    joint = _find(scene, ROAD_JOINT_SUFFIXES)
    if joint is not None:
        return joint
    dynamic_suffixes = []
    for prefix in _road_prefixes(scene):
        dynamic_suffixes.extend(
            (".{}_road_joint".format(prefix), ".{}.road_joint".format(prefix))
        )
    return _find(scene, dynamic_suffixes)


def is_available(scene):
    return bool(
        find_road_part(scene) is not None
        and find_ground_reference(scene) is not None
    )


def _coordinates(node, description):
    location = getattr(node, "location", None)
    if location is None:
        raise RuntimeError("{}缺少 location 属性".format(description))
    if all(hasattr(location, axis) for axis in ("x", "y", "z")):
        return tuple(float(getattr(location, axis)) for axis in ("x", "y", "z"))
    try:
        return tuple(float(location[index]) for index in range(3))
    except (TypeError, ValueError, IndexError):
        raise RuntimeError("无法读取{}坐标".format(description))


def get_location(scene):
    reference = find_ground_reference(scene)
    if reference is None:
        raise RuntimeError("当前模型中未找到路面参考点")
    return _coordinates(reference, "路面参考点")


def set_location(scene, coordinates):
    road_part = find_road_part(scene)
    reference = find_ground_reference(scene)
    road_joint = find_road_joint(scene)
    if road_part is None or reference is None:
        raise RuntimeError("当前模型中未找到完整的路面零件和参考点")

    values = tuple(float(value) for value in coordinates)
    if len(values) != 3 or not all(math.isfinite(value) for value in values):
        raise ValueError("路面位置必须包含三个有限数值")

    old_part_location = road_part.location
    old_reference_location = reference.location
    recompute = getattr(scene, "recompute", None)
    try:
        reference.location = values
        road_part.location = values
        if callable(recompute):
            recompute()
        joint_recompute = getattr(road_joint, "recompute", None)
        if callable(joint_recompute):
            joint_recompute()
        if callable(recompute):
            recompute()
    except Exception as exc:
        road_part.location = old_part_location
        reference.location = old_reference_location
        if callable(recompute):
            try:
                recompute()
            except Exception:
                pass
        raise RuntimeError("路面位置同步失败，已恢复原位置：{}".format(exc))
    return road_part, reference
