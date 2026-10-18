# -*- coding: utf-8 -*-
"""Synchronize the drop road body with its ground reference marker."""

import math


ROAD_PART_SUFFIXES = (
    ".lumian_road_part",  # ADM import: .Unknown.lumian_road_part
    ".lumian.road_part",  # Nested scene representation
    ".road",              # Legacy Python-generated drop model
)
GROUND_REFERENCE_SUFFIX = ".ground.lumian_ref_1"
ROAD_JOINT_SUFFIXES = (
    ".lumian_road_joint",  # ADM import: .Unknown.lumian_road_joint
    ".lumian.road_joint",  # Nested scene representation
    ".road_joint",         # Possible legacy representation
    ".road.road_joint",
)


def find_road_part(scene):
    if scene is None:
        return None
    scene_name = str(getattr(scene, "Name", "") or "").strip()
    if not scene_name:
        return None
    root = "." + scene_name
    for suffix in ROAD_PART_SUFFIXES:
        node = scene.getObject(root + suffix)
        if node is not None:
            return node
    return None


def find_ground_reference(scene):
    if scene is None:
        return None
    scene_name = str(getattr(scene, "Name", "") or "").strip()
    if not scene_name:
        return None
    return scene.getObject("." + scene_name + GROUND_REFERENCE_SUFFIX)


def find_road_joint(scene):
    if scene is None:
        return None
    scene_name = str(getattr(scene, "Name", "") or "").strip()
    if not scene_name:
        return None
    root = "." + scene_name
    for suffix in ROAD_JOINT_SUFFIXES:
        node = scene.getObject(root + suffix)
        if node is not None:
            return node
    return None


def _coordinates(node, description):
    location = getattr(node, "location", None)
    if location is None:
        raise RuntimeError("{}缺少 location 属性".format(description))
    if all(hasattr(location, axis) for axis in ("x", "y", "z")):
        return (float(location.x), float(location.y), float(location.z))
    try:
        return tuple(float(location[index]) for index in range(3))
    except (TypeError, ValueError, IndexError):
        raise RuntimeError("无法读取{}坐标".format(description))


def get_location(scene):
    road_part = find_road_part(scene)
    ground_reference = find_ground_reference(scene)
    if road_part is None:
        raise RuntimeError("当前模型中未找到路面零件 lumian_road_part")
    if ground_reference is None:
        raise RuntimeError("当前模型中未找到 ground.lumian_ref_1")
    # The tire forces use this ground marker as their road reference frame, so
    # it is the authoritative position shown in the dialog.
    return _coordinates(ground_reference, "路面参考点")


def set_location(scene, coordinates):
    road_part = find_road_part(scene)
    ground_reference = find_ground_reference(scene)
    road_joint = find_road_joint(scene)
    if road_part is None:
        raise RuntimeError("当前模型中未找到路面零件 lumian_road_part")
    if ground_reference is None:
        raise RuntimeError("当前模型中未找到 ground.lumian_ref_1")
    if len(coordinates) != 3:
        raise ValueError("路面位置必须包含 X、Y、Z 三个坐标")
    values = tuple(float(value) for value in coordinates)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("路面位置必须是有限数值")

    old_road_location = road_part.location
    old_reference_location = ground_reference.location
    recompute = getattr(scene, "recompute", None)
    try:
        # road_ref remains at the road part's local origin.  Moving its parent
        # and the fixed joint's ground marker to the same target keeps the
        # joint consistent while updating the tire solver reference frame.
        ground_reference.location = values
        road_part.location = values
        if callable(recompute):
            recompute()
        joint_recompute = getattr(road_joint, "recompute", None)
        if callable(joint_recompute):
            joint_recompute()
            if callable(recompute):
                recompute()
    except Exception as exc:
        road_part.location = old_road_location
        ground_reference.location = old_reference_location
        if callable(recompute):
            try:
                recompute()
            except Exception:
                pass
        raise RuntimeError("路面位置同步失败，已恢复原位置：{}".format(exc))
    return road_part, ground_reference
