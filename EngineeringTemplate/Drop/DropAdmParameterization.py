"""ADM imported Drop model hardpoint parameterization.

This module intentionally supports only the ``template_2_drop`` ADM template.
The ADM supplies the model topology, while ``template_2_drop_patch.py`` remains
the single source of truth for the CMD formulas used by markers and geometry.
"""

from __future__ import print_function

import importlib.util
import math
import os
import re

import Jusme
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils


MODEL_NAME = "template_2_drop"
SOURCE_ROOT = "." + MODEL_NAME
MODEL_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Model", MODEL_NAME)
)
PATCH_FILE = os.path.join(MODEL_FOLDER, MODEL_NAME + "_patch.py")
CMD_FILE = os.path.join(MODEL_FOLDER, MODEL_NAME + ".cmd")
EPSILON = 1.0e-6
LOCKED_AXIS_TOLERANCE = 1.0e-6

TRANSACTION_PROPERTIES = (
    "location",
    "orientation",
    "length",
    "function",
    "commands",
    "string_value",
    "string",
    "value",
    "initial_condition",
    "variable_name",
    "sim_script_name",
    "adams_id",
    "marker_name",
    "cylinder_name",
    "part_name",
    "relative_to",
)


# The enabled coordinates are deliberately narrow.  They match the structural
# parameter fields presented by the Drop dialog and prevent accidental motion
# outside the intended landing-gear plane.
HARDPOINT_RULES = {
    "hps_uc_top": ("z",),
    "hps_uc_bot": ("z",),
    "hps_lc_top": ("z",),
    "hps_lc_bot": ("z",),
    "hps_db_sf_atch": ("x", "z"),
    "hps_db_uc_atch": ("x", "z"),
    "hps_lta_uta_atch": ("x", "z"),
    "hps_uta_uc_atch": ("x", "z"),
    "hps_lta_lc_atch": ("x", "z"),
    "hpl_wheel_center1": ("y",),
    "hpr_wheel_center1": ("y",),
}

HARDPOINT_ALIASES = {
    "hpl_wheel_center": "hpl_wheel_center1",
    "hpr_wheel_center": "hpr_wheel_center1",
}

CORE_HARDPOINTS = (
    "hps_uc_top",
    "hps_uc_bot",
    "hps_lc_top",
    "hps_lc_bot",
    "hps_db_sf_atch",
    "hps_db_uc_atch",
    "hps_uta_uc_atch",
    "hps_lta_uta_atch",
    "hps_lta_lc_atch",
    "hps_uc_sf_atch_l",
    "hps_uc_sf_atch_r",
    "hpl_wheel_center1",
    "hpr_wheel_center1",
    "hpl_ob_axle1",
    "hpr_ob_axle1",
)

MOVING_PARTS = (
    "ges_upper_cylinder",
    "ges_lower_cylinder",
    "ges_collar",
    "ges_upper_torque_arm",
    "ges_lower_torque_arm",
    "ges_dragbrace",
)

REQUIRED_PARTS = MOVING_PARTS + (
    "mts_body_mount_2",
)

# These parts exist in some exported Adams variants, but the Jasmine ADM
# importer may legitimately omit them.  When present they still participate in
# updates and rollback; when absent they must not disable hardpoint editing.
OPTIONAL_PARTS = (
    "ges_subframe_2",
    "luntai1_2.wheel_part",
    "luntai2_2.wheel_part",
)

OPTIONAL_PATCH_PATH_FRAGMENTS = tuple("." + path for path in OPTIONAL_PARTS)

STATIC_REQUIRED_MARKERS = (
    "ges_upper_cylinder.MARKER_2",
    "ges_upper_cylinder.MARKER_405",
    "ges_upper_cylinder.MARKER_407",
    "ges_upper_cylinder.MARKER_409",
    "ges_dragbrace.MARKER_429",
    "mts_body_mount_2.MARKER_430",
    "ges_lower_cylinder.MARKER_1",
    "ges_lower_cylinder.MARKER_406",
    "ges_lower_cylinder.MARKER_408",
    "ges_lower_cylinder.MARKER_410",
    "ges_lower_cylinder.MARKER_6",
    "ges_lower_cylinder.MARKER_8",
)

DEPENDENT_GEOMETRY = (
    "ges_dragbrace.gralin_dragbrace_geom",
    "ges_upper_cylinder.gralin_upper_cylinder_geom1",
    "ges_upper_cylinder.gralin_upper_cylinder_geom2",
    "ges_upper_cylinder.gralin_upper_cylinder_geom3",
    "ges_lower_cylinder.gralin_geom1",
    "ges_lower_cylinder.gralin_geom2",
    "ges_upper_torque_arm.gralin_upper_torque_arm_geom",
    "ges_lower_torque_arm.gralin_lower_torque_arm_geom",
    "ges_collar.gralin_collar",
)

DEPENDENT_CONNECTORS = (
    "JOINT_51",
    "JOINT_57",
    "JOINT_56",
    "josrev_lta_uta_joint",
    "josrev_uta_uc_joint",
    "joscyl_lc_uc_joint",
    "jossph_db_uc_joint",
    "josrev_collar_uc_joint",
    "JOINT_1",
    "JOINT_2",
    "JOINT_15",
)

class AdjustmentResult(object):
    def __init__(self, success, message, updated=0, changed=False, errors=None):
        self.success = bool(success)
        self.message = message
        self.updated = int(updated or 0)
        self.changed = bool(changed)
        self.errors = list(errors or [])


def canonical_hardpoint_name(name_or_path):
    name = str(name_or_path or "").rstrip(".").split(".")[-1]
    return HARDPOINT_ALIASES.get(name, name)


def get_rule(name_or_path):
    """Return the editable axes for a supported hardpoint, or ``None``."""
    return HARDPOINT_RULES.get(canonical_hardpoint_name(name_or_path))


def hardpoint_path(name_or_path, scene=None):
    scene = scene if scene is not None else getattr(Jusme, "ActiveUSScene", None)
    root = _model_root(scene) or SOURCE_ROOT
    return "{}.ground.{}".format(
        root,
        canonical_hardpoint_name(name_or_path),
    )


def _model_root(scene):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    return "." + model_name if model_name else ""


def _resolve_path(scene, path):
    model_root = _model_root(scene)
    if path == SOURCE_ROOT or path.startswith(SOURCE_ROOT + "."):
        return model_root + path[len(SOURCE_ROOT):] if model_root else path
    if path.startswith("."):
        return path
    return model_root + "." + path if model_root else path


def _get(scene, relative_path):
    path = _resolve_path(scene, relative_path)
    try:
        return scene.getObject(path)
    except Exception:
        return None


def _xyz(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        return float(value.x), float(value.y), float(value.z)
    return float(value[0]), float(value[1]), float(value[2])


def _vector(value):
    x, y, z = _xyz(value)
    return Jusme.Vector(x, y, z)


def _midpoint(first, second):
    ax, ay, az = _xyz(first)
    bx, by, bz = _xyz(second)
    return Jusme.Vector((ax + bx) / 2.0, (ay + by) / 2.0, (az + bz) / 2.0)


def _centroid(first, second, third):
    ax, ay, az = _xyz(first)
    bx, by, bz = _xyz(second)
    cx, cy, cz = _xyz(third)
    return Jusme.Vector(
        (ax + bx + cx) / 3.0,
        (ay + by + cy) / 3.0,
        (az + bz + cz) / 3.0,
    )


def _distance(first, second):
    ax, ay, az = _xyz(first)
    bx, by, bz = _xyz(second)
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2)


def _cross(first, second, third):
    """Return (first - second) x (third - second)."""
    ax, ay, az = _xyz(first)
    bx, by, bz = _xyz(second)
    cx, cy, cz = _xyz(third)
    ux, uy, uz = ax - bx, ay - by, az - bz
    vx, vy, vz = cx - bx, cy - by, cz - bz
    return Jusme.Vector(
        uy * vz - uz * vy,
        uz * vx - ux * vz,
        ux * vy - uy * vx,
    )


def _all_finite(value):
    return all(math.isfinite(number) for number in _xyz(value))


def _validate_scene(scene):
    if scene is None:
        return "当前没有活动模型"
    scene_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    if not scene_name:
        return "当前活动场景没有有效名称"

    missing = []
    for name in CORE_HARDPOINTS:
        if _get(scene, "ground." + name) is None:
            missing.append("ground." + name)
    for name in REQUIRED_PARTS:
        if _get(scene, name) is None:
            missing.append(name)
    if _get(scene, "ground.cfs_collar_top") is None:
        missing.append("ground.cfs_collar_top")
    if _get(scene, "ground.origo1") is None:
        missing.append("ground.origo1")
    for path in STATIC_REQUIRED_MARKERS:
        if _get(scene, path) is None:
            missing.append(path)
    for path in DEPENDENT_GEOMETRY:
        if _get(scene, path) is None:
            missing.append(path)
    for path in DEPENDENT_CONNECTORS:
        if _get(scene, path) is None:
            missing.append(path)
    if missing:
        preview = "、".join(missing[:6])
        if len(missing) > 6:
            preview += " 等{}项".format(len(missing))
        return "场景 {} 的Drop结构不完整，缺少：{}".format(
            scene_name,
            preview,
        )
    if not os.path.isfile(PATCH_FILE):
        return "未找到Drop公式补丁：{}".format(PATCH_FILE)
    if not os.path.isfile(CMD_FILE):
        return "未找到Drop参考CMD：{}".format(CMD_FILE)
    return ""


def compatibility_error(scene=None):
    """Return an empty string when the active model matches the Drop contract."""
    scene = scene if scene is not None else getattr(Jusme, "ActiveUSScene", None)
    return _validate_scene(scene)


def is_compatible_scene(scene=None):
    return not compatibility_error(scene)


def _read_hardpoints(scene, replacement_name=None, replacement=None):
    values = {}
    for name in CORE_HARDPOINTS:
        node = _get(scene, "ground." + name)
        values[name] = _vector(node.location)
    if replacement_name:
        values[replacement_name] = _vector(replacement)
    return values


def _validate_geometry(points):
    for name, value in points.items():
        if not _all_finite(value):
            return "硬点 {} 包含无效数值".format(name)

    length_pairs = (
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
        ("hps_db_sf_atch", "hps_db_uc_atch", "斜撑杆"),
        ("hps_uta_uc_atch", "hps_lta_uta_atch", "上扭力臂"),
        ("hps_lta_lc_atch", "hps_lta_uta_atch", "下扭力臂"),
        ("hpl_wheel_center1", "hpl_ob_axle1", "左轮轴"),
        ("hpr_wheel_center1", "hpr_ob_axle1", "右轮轴"),
    )
    for first, second, label in length_pairs:
        if _distance(points[first], points[second]) <= EPSILON:
            return "{}的两个定义点不能重合".format(label)

    if points["hps_uc_top"].z <= points["hps_uc_bot"].z + EPSILON:
        return "上支柱上端点必须高于下端点"
    if points["hps_lc_top"].z <= points["hps_lc_bot"].z + EPSILON:
        return "下支柱上端点必须高于下端点"
    if points["hpl_wheel_center1"].y >= points["hpr_wheel_center1"].y - EPSILON:
        return "左、右轮心位置交叉或重合"
    if points["hpl_wheel_center1"].y >= -EPSILON:
        return "左轮心必须位于模型中心面的左侧"
    if points["hpr_wheel_center1"].y <= EPSILON:
        return "右轮心必须位于模型中心面的右侧"
    if points["hpl_ob_axle1"].y >= points["hpl_wheel_center1"].y - EPSILON:
        return "左轮外轴点必须位于左轮心外侧"
    if points["hpr_ob_axle1"].y <= points["hpr_wheel_center1"].y + EPSILON:
        return "右轮外轴点必须位于右轮心外侧"

    normal = _cross(
        points["hps_uc_sf_atch_l"],
        points["hps_uc_sf_atch_r"],
        points["hps_db_sf_atch"],
    )
    if _distance(normal, Jusme.Vector(0.0, 0.0, 0.0)) <= EPSILON:
        return "机架三个定位点共线，无法计算机架姿态"
    return ""


def _copy_property(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        return _vector(value)
    if isinstance(value, list):
        return list(value)
    if isinstance(value, tuple):
        return tuple(value)
    return value


def _patch_objects(scene):
    try:
        with open(PATCH_FILE, "r", encoding="utf-8") as patch_file:
            patch_text = patch_file.read()
    except (OSError, UnicodeError):
        return []
    paths = set(
        re.findall(
            r"['\"](\.template_2_drop(?:\.[A-Za-z_][A-Za-z0-9_]*)+)['\"]",
            patch_text,
        )
    )
    return [node for node in (_get(scene, path) for path in paths) if node is not None]


def _snapshot_geometry(scene):
    snapshot = []
    # Only snapshot nodes that this transaction can touch.  Traversing and
    # copying the whole scene is slow for tire models and may invoke unrelated
    # proxy properties with side effects.
    nodes = _patch_objects(scene)
    direct_paths = ["ground." + name for name in CORE_HARDPOINTS]
    direct_paths.extend(REQUIRED_PARTS)
    direct_paths.extend(OPTIONAL_PARTS)
    direct_paths.extend(STATIC_REQUIRED_MARKERS)
    direct_paths.extend(DEPENDENT_GEOMETRY)
    direct_paths.extend(DEPENDENT_CONNECTORS)
    direct_paths.extend(
        ("ges_upper_cylinder.MARKER_116", "ground.cfs_collar_top")
    )
    nodes.extend(
        node
        for node in (_get(scene, path) for path in direct_paths)
        if node is not None
    )
    visited = set()
    for node in nodes:
        if id(node) in visited:
            continue
        visited.add(id(node))
        properties = set(getattr(node, "PropertiesList", []) or [])
        for property_name in TRANSACTION_PROPERTIES:
            if (
                properties
                and property_name not in properties
                and property_name not in ("location", "orientation", "length")
            ):
                # Platform objects do not consistently expose every attribute,
                # so avoid invoking unrelated property getters where a property
                # list is available.
                continue
            try:
                value = getattr(node, property_name)
            except Exception:
                continue
            snapshot.append((node, property_name, _copy_property(value)))
    return snapshot


def _restore_geometry(snapshot):
    restore_errors = []
    for node, property_name, value in reversed(snapshot):
        try:
            setattr(node, property_name, value)
        except Exception as exc:
            restore_errors.append("{}.{}: {}".format(
                getattr(node, "Name", "<unknown>"),
                property_name,
                exc,
            ))
    return restore_errors


def _set_part_pose(scene, part_name, first, second, axis="z"):
    part = _get(scene, part_name)
    part.location = _midpoint(first, second)
    part.orientation = VecUtils.ORI_ALONG_AXIS(first, second, axis)


def _set_marker_global_pose(scene, marker_path, parent_path, location, orientation):
    marker = _get(scene, marker_path)
    parent = _get(scene, parent_path)
    if marker is None or parent is None:
        raise RuntimeError("缺少标记点或所属部件：{}".format(marker_path))
    local_location, local_orientation = VecUtils.global2local(
        parent.location,
        parent.orientation,
        location,
        orientation,
    )
    marker.location = _vector(local_location)
    marker.orientation = _vector(local_orientation)


def _update_static_endpoint_markers(scene, points):
    """Refresh endpoint markers that are static in CMD and absent from patch."""
    origin = _get(scene, "ground.origo1")
    origin_orientation = VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origin)

    for marker_name in (
        "MARKER_2",
        "MARKER_405",
        "MARKER_407",
        "MARKER_409",
    ):
        _set_marker_global_pose(
            scene,
            "ges_upper_cylinder." + marker_name,
            "ges_upper_cylinder",
            points["hps_uc_top"],
            origin_orientation,
        )

    # MARKER_116 is not used by a connector or force, but follows the same
    # endpoint when the ADM version contains it.
    if _get(scene, "ges_upper_cylinder.MARKER_116") is not None:
        _set_marker_global_pose(
            scene,
            "ges_upper_cylinder.MARKER_116",
            "ges_upper_cylinder",
            points["hps_uc_top"],
            origin_orientation,
        )

    for marker_name in (
        "MARKER_1",
        "MARKER_406",
        "MARKER_408",
        "MARKER_410",
    ):
        _set_marker_global_pose(
            scene,
            "ges_lower_cylinder." + marker_name,
            "ges_lower_cylinder",
            points["hps_lc_top"],
            origin_orientation,
        )

    for marker_path, parent_path in (
        ("ges_dragbrace.MARKER_429", "ges_dragbrace"),
        ("mts_body_mount_2.MARKER_430", "mts_body_mount_2"),
    ):
        _set_marker_global_pose(
            scene,
            marker_path,
            parent_path,
            points["hps_db_sf_atch"],
            origin_orientation,
        )

    wheel_orientation = VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origin)
    _set_marker_global_pose(
        scene,
        "ges_lower_cylinder.MARKER_8",
        "ges_lower_cylinder",
        points["hpl_wheel_center1"],
        wheel_orientation,
    )
    _set_marker_global_pose(
        scene,
        "ges_lower_cylinder.MARKER_6",
        "ges_lower_cylinder",
        points["hpr_wheel_center1"],
        wheel_orientation,
    )


def _split_cmd_blocks(cmd_text):
    blocks = []
    block = []
    for raw_line in cmd_text.splitlines():
        if raw_line.strip().startswith("!"):
            if block:
                blocks.append("\n".join(block))
                block = []
            continue
        if raw_line.strip():
            block.append(raw_line)
    if block:
        blocks.append("\n".join(block))
    return blocks


def _partial_marker_patch_modes():
    """Return marker patch fields omitted by the authoritative CMD command."""
    try:
        with open(CMD_FILE, "r", encoding="utf-8-sig", errors="ignore") as cmd_file:
            cmd_text = cmd_file.read()
        with open(PATCH_FILE, "r", encoding="utf-8") as patch_file:
            patch_text = patch_file.read()
    except (OSError, UnicodeError):
        return {}

    patched_markers = set(
        re.findall(r"record_error\('marker modify ([^']+)'", patch_text)
    )
    modes = {}
    for block in _split_cmd_blocks(cmd_text):
        if not re.match(r"^\s*marker\s+modify\b", block, flags=re.I):
            continue
        name_match = re.search(
            r"(?im)^\s*marker_name\s*=\s*(\.[A-Za-z_][A-Za-z0-9_.]*)",
            block,
        )
        if not name_match:
            continue
        path = name_match.group(1)
        if path not in patched_markers:
            continue
        modes[path] = (
            bool(re.search(r"(?im)^\s*location\s*=", block)),
            bool(re.search(r"(?im)^\s*orientation\s*=", block)),
        )
    return modes


def _capture_partial_marker_properties(scene):
    """Capture local fields omitted by partial CMD marker-modify commands."""
    captured = []
    for path, (has_location, has_orientation) in _partial_marker_patch_modes().items():
        marker = _get(scene, path)
        if marker is None:
            continue
        if not has_location:
            captured.append((marker, "location", _copy_property(marker.location)))
        if not has_orientation:
            captured.append(
                (marker, "orientation", _copy_property(marker.orientation))
            )
    return captured


def _restore_partial_marker_properties(captured):
    """Preserve the CMD meaning of an omitted marker property on patch reruns."""
    for marker, property_name, value in captured:
        setattr(marker, property_name, value)


def _recompute_connectors(scene):
    for path in DEPENDENT_CONNECTORS:
        connector = _get(scene, path)
        recompute = getattr(connector, "recompute", None)
        if callable(recompute):
            recompute()


def _update_base_poses(scene, points, changed_name):
    _set_part_pose(
        scene,
        "ges_upper_cylinder",
        points["hps_uc_top"],
        points["hps_uc_bot"],
        "z",
    )
    _set_part_pose(
        scene,
        "ges_lower_cylinder",
        points["hps_lc_top"],
        points["hps_lc_bot"],
        "z",
    )

    collar_top = VecUtils.LOC_ALONG_LINE(
        points["hps_uc_bot"],
        points["hps_uc_top"],
        0.11 * _distance(points["hps_uc_bot"], points["hps_uc_top"]),
    )
    collar_top_node = _get(scene, "ground.cfs_collar_top")
    collar_top_node.location = collar_top
    collar_top_node.orientation = VecUtils.ORI_ALONG_AXIS(
        points["hps_uc_bot"], points["hps_uc_top"], "z"
    )
    _set_part_pose(
        scene,
        "ges_collar",
        points["hps_uc_bot"],
        collar_top,
        "z",
    )

    _set_part_pose(
        scene,
        "ges_upper_torque_arm",
        points["hps_uta_uc_atch"],
        points["hps_lta_uta_atch"],
        "z",
    )
    _set_part_pose(
        scene,
        "ges_lower_torque_arm",
        points["hps_lta_lc_atch"],
        points["hps_lta_uta_atch"],
        "z",
    )
    _set_part_pose(
        scene,
        "ges_dragbrace",
        points["hps_db_sf_atch"],
        points["hps_db_uc_atch"],
        "z",
    )

    subframe_center = _centroid(
        points["hps_uc_sf_atch_l"],
        points["hps_uc_sf_atch_r"],
        points["hps_db_sf_atch"],
    )
    normal = _cross(
        points["hps_uc_sf_atch_l"],
        points["hps_uc_sf_atch_r"],
        points["hps_db_sf_atch"],
    )
    nx, ny, nz = _xyz(normal)
    normal_end = Jusme.Vector(
        subframe_center.x + nx,
        subframe_center.y + ny,
        subframe_center.z + nz,
    )
    subframe = _get(scene, "ges_subframe_2")
    if subframe is not None:
        subframe.location = subframe_center
        subframe.orientation = VecUtils.ORI_ALONG_AXIS(
            subframe_center, normal_end, "y"
        )

    wheel_part_by_hardpoint = {
        "hpl_wheel_center1": "luntai1_2.wheel_part",
        "hpr_wheel_center1": "luntai2_2.wheel_part",
    }
    wheel_part_path = wheel_part_by_hardpoint.get(changed_name)
    if wheel_part_path:
        wheel_part = _get(scene, wheel_part_path)
        if wheel_part is not None:
            wheel_part.location = _vector(points[changed_name])


def _load_patch_module():
    module_name = "_drop_runtime_patch"
    spec = importlib.util.spec_from_file_location(module_name, PATCH_FILE)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载Drop公式补丁")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run_formula_patch(scene):
    module = _load_patch_module()
    if not hasattr(module, "apply_patch"):
        raise RuntimeError("Drop公式补丁缺少apply_patch入口")
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    if not model_name:
        raise RuntimeError("活动场景名为空")
    result = module.apply_patch(MODEL_FOLDER, model_name) or {}
    errors = list(result.get("errors") or [])
    critical_errors = []
    noncritical_errors = []
    for error in errors:
        step = error.get("step", "") if isinstance(error, dict) else ""
        is_geometry_error = (
            step.startswith("marker modify ")
            or step.startswith("geometry modify ")
            or step.startswith("part modify rigid_body ")
        )
        is_optional_error = any(
            fragment in step for fragment in OPTIONAL_PATCH_PATH_FRAGMENTS
        )
        if is_geometry_error and not is_optional_error:
            critical_errors.append(error)
        else:
            noncritical_errors.append(error)
    if critical_errors:
        detail = critical_errors[0]
        if isinstance(detail, dict):
            detail = "{}: {}".format(
                detail.get("step", "补丁步骤"),
                detail.get("error", detail.get("message", detail)),
            )
        raise RuntimeError("公式补丁执行失败：{}".format(detail))
    warnings = list(result.get("warnings") or [])
    for detail in noncritical_errors:
        if isinstance(detail, dict):
            warnings.append(
                "{}: {}".format(
                    detail.get("step", "补丁步骤"),
                    detail.get("error", detail.get("message", detail)),
                )
            )
        else:
            warnings.append(str(detail))
    return int(result.get("updated") or 0), warnings


def _validate_updated_structure(scene, changed_name, expected_location):
    """Validate critical postconditions before committing the transaction."""
    target = _get(scene, "ground." + changed_name)
    if target is None:
        return "更新后硬点丢失：{}".format(changed_name)
    try:
        if _distance(target.location, expected_location) > LOCKED_AXIS_TOLERANCE:
            return "更新后硬点坐标与输入值不一致"
    except Exception as exc:
        return "无法校验更新后的硬点坐标：{}".format(exc)

    try:
        geometry_error = _validate_geometry(_read_hardpoints(scene))
    except Exception as exc:
        return "更新后无法读取硬点结构：{}".format(exc)
    if geometry_error:
        return geometry_error

    for path in REQUIRED_PARTS:
        node = _get(scene, path)
        try:
            if not _all_finite(node.location) or not _all_finite(node.orientation):
                return "更新后零件位姿无效：{}".format(path)
        except Exception as exc:
            return "无法校验零件位姿 {}: {}".format(path, exc)

    for path in STATIC_REQUIRED_MARKERS:
        node = _get(scene, path)
        try:
            if not _all_finite(node.location) or not _all_finite(node.orientation):
                return "更新后标记点位姿无效：{}".format(path)
        except Exception as exc:
            return "无法校验标记点位姿 {}: {}".format(path, exc)

    for path in DEPENDENT_GEOMETRY:
        node = _get(scene, path)
        try:
            length = float(node.length)
        except Exception as exc:
            return "无法校验几何长度 {}: {}".format(path, exc)
        if not math.isfinite(length) or length <= EPSILON:
            return "更新后几何长度无效：{}".format(path)
    return ""


def adjust_hardpoint(name_or_path, x_coord, y_coord, z_coord, scene=None):
    """Adjust one Drop hardpoint as a validated, rollback-safe transaction."""
    scene = scene if scene is not None else getattr(Jusme, "ActiveUSScene", None)
    scene_error = _validate_scene(scene)
    if scene_error:
        return AdjustmentResult(False, scene_error)

    name = canonical_hardpoint_name(name_or_path)
    axes = get_rule(name)
    if axes is None:
        return AdjustmentResult(False, "硬点 {} 不支持参数化调整".format(name))

    target = _get(scene, "ground." + name)
    if target is None:
        return AdjustmentResult(False, "未找到硬点 {}".format(name))

    try:
        requested = Jusme.Vector(float(x_coord), float(y_coord), float(z_coord))
    except (TypeError, ValueError) as exc:
        return AdjustmentResult(False, "硬点坐标必须是有效数字：{}".format(exc))
    if not _all_finite(requested):
        return AdjustmentResult(False, "硬点坐标不能包含NaN或无穷大")

    old_location = _vector(target.location)
    for axis in ("x", "y", "z"):
        if axis not in axes and abs(
            getattr(requested, axis) - getattr(old_location, axis)
        ) > LOCKED_AXIS_TOLERANCE:
            return AdjustmentResult(
                False,
                "硬点 {} 的{}坐标不可修改".format(name, axis.upper()),
            )

    new_location = Jusme.Vector(
        requested.x if "x" in axes else old_location.x,
        requested.y if "y" in axes else old_location.y,
        requested.z if "z" in axes else old_location.z,
    )
    if _distance(old_location, new_location) <= EPSILON:
        return AdjustmentResult(True, "硬点坐标没有变化", changed=False)

    points = _read_hardpoints(scene, name, new_location)
    geometry_error = _validate_geometry(points)
    if geometry_error:
        return AdjustmentResult(False, geometry_error)

    snapshot = _snapshot_geometry(scene)
    if not snapshot:
        return AdjustmentResult(False, "无法创建模型回滚快照，已取消调整")

    try:
        partial_marker_properties = _capture_partial_marker_properties(scene)
        target.location = new_location
        _update_base_poses(scene, points, name)
        updated, warnings = _run_formula_patch(scene)
        _restore_partial_marker_properties(partial_marker_properties)
        _update_static_endpoint_markers(scene, points)
        _recompute_connectors(scene)
        scene.recompute()
        post_error = _validate_updated_structure(scene, name, new_location)
        if post_error:
            raise RuntimeError("结构更新后校验失败：{}".format(post_error))
        message = "硬点 {} 调整完成，共刷新{}项公式/几何数据".format(
            name,
            updated,
        )
        if warnings:
            message += "；有{}条警告，请查看控制台".format(len(warnings))
            for warning in warnings:
                print("[Drop参数化警告] {}".format(warning))
        return AdjustmentResult(
            True,
            message,
            updated=updated,
            changed=True,
        )
    except Exception as exc:
        restore_errors = _restore_geometry(snapshot)
        try:
            scene.recompute()
        except Exception:
            pass
        message = "硬点调整失败，模型已恢复：{}".format(exc)
        if restore_errors:
            message += "；但有{}项恢复失败，请重新导入模型".format(
                len(restore_errors)
            )
        return AdjustmentResult(
            False,
            message,
            errors=[str(exc)] + restore_errors,
        )
