# -*- coding: utf-8 -*-
"""Convert ADM/world Marker coordinates to Jasmine local coordinates."""

from __future__ import print_function

import math

import StructuralParameterization


class MarkerCoordinateError(ValueError):
    """Raised when a Marker coordinate frame cannot be resolved safely."""


def _xyz(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        result = tuple(float(getattr(value, axis)) for axis in ("x", "y", "z"))
    else:
        result = tuple(float(value[index]) for index in range(3))
    if len(result) != 3 or not all(math.isfinite(number) for number in result):
        raise MarkerCoordinateError("坐标包含NaN或无穷大")
    return result


def _resolve_relative_to(scene, value):
    if value is None:
        return None
    if not isinstance(value, str):
        return value
    path = StructuralParameterization.resolve_path(scene, value)
    try:
        return scene.getObject(path)
    except Exception:
        return None


def _owned_by_part(part, marker):
    try:
        return any(candidate is marker for candidate in part.part_owned_shapes_markers)
    except Exception:
        return False


def resolve_marker_parent(scene, marker, marker_path=""):
    """Resolve the Part whose coordinate system owns ``marker.location``."""
    try:
        parent = _resolve_relative_to(scene, getattr(marker, "relative_to", None))
    except Exception:
        parent = None
    if parent is not None and parent is not marker:
        return parent

    resolved_path = StructuralParameterization.resolve_path(scene, marker_path)
    if resolved_path and "." in resolved_path.lstrip("."):
        parent_path = resolved_path.rsplit(".", 1)[0]
        try:
            parent = scene.getObject(parent_path)
        except Exception:
            parent = None
        if parent is not None and parent is not marker:
            return parent

    # Fallback for platform builds where a Marker's Name is flattened or its
    # relative_to presentation property is unavailable after ADM import.
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    root = "." + model_name if model_name else ""
    try:
        bodies = scene.getObject(root + ".Bodies") if root else None
    except Exception:
        bodies = None
    containers = []
    if bodies is not None:
        getter = getattr(bodies, "getObjects", None)
        if callable(getter):
            try:
                containers.extend(list(getter() or []))
            except Exception:
                pass
    try:
        ground = scene.getObject(root + ".ground") if root else None
    except Exception:
        ground = None
    if ground is not None:
        containers.append(ground)
    for part in containers:
        if _owned_by_part(part, marker):
            return part
    return None


def world_pose_to_local(
    scene,
    marker,
    marker_path,
    world_coordinates,
    world_orientation,
):
    """Convert a Marker world pose to the owning Part's local coordinates."""
    world_values = _xyz(world_coordinates)
    orientation_values = _xyz(world_orientation)
    parent = resolve_marker_parent(scene, marker, marker_path)
    if parent is None:
        raise MarkerCoordinateError(
            "无法确定Marker所属零件，不能安全地把世界坐标转换为局部坐标：{}".format(
                marker_path
            )
        )
    try:
        parent_location = parent.location
        parent_orientation = parent.orientation
    except Exception as exc:
        raise MarkerCoordinateError(
            "Marker所属零件缺少位置或方向信息：{}".format(exc)
        )

    try:
        import Jusme
        import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils

        global_location = Jusme.Vector(*world_values)
        global_orientation = Jusme.Vector(*orientation_values)
        local_location, local_orientation = VecUtils.global2local(
            parent_location,
            parent_orientation,
            global_location,
            global_orientation,
        )
        return _xyz(local_location), _xyz(local_orientation)
    except MarkerCoordinateError:
        raise
    except Exception as exc:
        raise MarkerCoordinateError(
            "世界坐标转局部坐标失败：{}: {}".format(
                type(exc).__name__, exc
            )
        )


def world_to_local(scene, marker, marker_path, world_coordinates):
    """Return local coordinates suitable for assigning to ``marker.location``."""
    parent = resolve_marker_parent(scene, marker, marker_path)
    if parent is None:
        raise MarkerCoordinateError(
            "无法确定Marker所属零件，不能安全地把世界坐标转换为局部坐标：{}".format(
                marker_path
            )
        )
    try:
        parent_orientation = parent.orientation
    except Exception as exc:
        raise MarkerCoordinateError(
            "Marker所属零件缺少方向信息：{}".format(exc)
        )
    local_location, _local_orientation = world_pose_to_local(
        scene,
        marker,
        marker_path,
        world_coordinates,
        parent_orientation,
    )
    return local_location
