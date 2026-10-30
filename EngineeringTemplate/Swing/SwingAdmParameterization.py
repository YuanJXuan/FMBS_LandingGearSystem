"""Transactional hardpoint parameterization for ``template_7_swing``."""

import os

import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils

import AdmHardpointParameterization as _adm


MODEL_NAME = "template_7_swing"
MODEL_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Model", MODEL_NAME)
)

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
    "hpl_wheel_center": ("y",),
    "hpr_wheel_center": ("y",),
}

CORE_HARDPOINTS = (
    "hps_uc_top",
    "hps_uc_bot",
    "hps_lc_top",
    "hps_lc_bot",
    "hps_db_sf_atch",
    "hps_db_uc_atch",
    "hps_lta_uta_atch",
    "hps_uta_uc_atch",
    "hps_lta_lc_atch",
    "hps_uc_sf_atch_l",
    "hps_uc_sf_atch_r",
    "hps_uc_geompt",
    "hpl_wheel_center",
    "hpr_wheel_center",
    "hpl_ob_axle",
    "hpr_ob_axle",
    "hps_nlg_axle_lowpoint",
    "hsg_1",
    "hsg_2",
    "zdt1",
    "zdt2",
)


def _get(scene, path, required=True):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    node = scene.getObject(".{}.{}".format(model_name, path))
    if node is None and required:
        raise RuntimeError("缺少Swing结构对象 {}".format(path))
    return node


def _vector(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        return Jusme.Vector(float(value.x), float(value.y), float(value.z))
    return Jusme.Vector(float(value[0]), float(value[1]), float(value[2]))


def _midpoint(first, second):
    return Jusme.Vector(
        0.5 * (first.x + second.x),
        0.5 * (first.y + second.y),
        0.5 * (first.z + second.z),
    )


def _set_part_pose(scene, path, first, second, axis="z"):
    part = _get(scene, path)
    part.location = _midpoint(first, second)
    part.orientation = VecUtils.ORI_ALONG_AXIS(first, second, axis)
    cm = _get(scene, path + ".cm", required=False)
    if cm is not None:
        cm.location = Jusme.Vector(0.0, 0.0, 0.0)
        cm.orientation = Jusme.Vector(0.0, 0.0, 0.0)


def _set_marker_global(scene, marker_path, parent_path, location, orientation):
    marker = _get(scene, marker_path)
    parent = _get(scene, parent_path)
    local_location, local_orientation = VecUtils.global2local(
        parent.location,
        parent.orientation,
        location,
        orientation,
    )
    marker.location = _vector(local_location)
    marker.orientation = _vector(local_orientation)


def _mirror_wheel_hardpoint(scene, points, changed_name):
    if changed_name == "hpl_wheel_center":
        opposite_name = "hpr_wheel_center"
    elif changed_name == "hpr_wheel_center":
        opposite_name = "hpl_wheel_center"
    else:
        return
    changed = points[changed_name]
    opposite = points[opposite_name]
    mirrored = Jusme.Vector(opposite.x, -changed.y, opposite.z)
    points[opposite_name] = mirrored
    _get(scene, "ground." + opposite_name).location = mirrored


def _update_structure(scene, points, changed_name):
    """Update the Swing topology skeleton before replaying CMD formulas."""
    _mirror_wheel_hardpoint(scene, points, changed_name)

    _set_part_pose(
        scene, "ges_upper_cylinder", points["hps_uc_top"], points["hps_uc_bot"]
    )
    _set_part_pose(
        scene, "ges_lower_cylinder", points["hps_lc_top"], points["hps_lc_bot"]
    )

    collar_top = VecUtils.LOC_ALONG_LINE(
        points["hps_uc_bot"],
        points["hps_uc_top"],
        0.11 * VecUtils.DM(points["hps_uc_bot"], points["hps_uc_top"]),
    )
    collar_orientation = VecUtils.ORI_ALONG_AXIS(
        points["hps_uc_bot"], points["hps_uc_top"], "z"
    )
    cfs_collar_top = _get(scene, "ground.cfs_collar_top")
    cfs_collar_top.location = _vector(collar_top)
    cfs_collar_top.orientation = _vector(collar_orientation)
    _set_part_pose(scene, "ges_collar", points["hps_uc_bot"], collar_top)

    _set_part_pose(
        scene,
        "ges_upper_torque_arm",
        points["hps_uta_uc_atch"],
        points["hps_lta_uta_atch"],
    )
    _set_part_pose(
        scene,
        "ges_lower_torque_arm",
        points["hps_lta_lc_atch"],
        points["hps_lta_uta_atch"],
    )
    _set_part_pose(
        scene,
        "ges_dragbrace",
        points["hps_db_sf_atch"],
        points["hps_db_uc_atch"],
    )

    wheel_midpoint = _get(scene, "ground.cfs_wheel_centers_midpoint")
    wheel_midpoint.location = _midpoint(
        points["hpl_wheel_center"], points["hpr_wheel_center"]
    )
    wheel_midpoint.orientation = Jusme.Vector(0.0, 0.0, 0.0)

    subframe_orientation = VecUtils.ORI_IN_PLANE(
        points["hps_uc_sf_atch_r"],
        points["hps_uc_sf_atch_l"],
        points["hps_db_sf_atch"],
        "z_zx",
    )
    subframe_center = Jusme.Vector(
        (
            points["hps_uc_sf_atch_r"].x
            + points["hps_uc_sf_atch_l"].x
            + points["hps_db_sf_atch"].x
        )
        / 3.0,
        (
            points["hps_uc_sf_atch_r"].y
            + points["hps_uc_sf_atch_l"].y
            + points["hps_db_sf_atch"].y
        )
        / 3.0,
        (
            points["hps_uc_sf_atch_r"].z
            + points["hps_uc_sf_atch_l"].z
            + points["hps_db_sf_atch"].z
        )
        / 3.0,
    )
    subframe = _get(scene, "ges_subframe")
    subframe.location = subframe_center
    subframe.orientation = _vector(subframe_orientation)
    subframe_cm = _get(scene, "ges_subframe.cm", required=False)
    if subframe_cm is not None:
        subframe_cm.location = Jusme.Vector(0.0, 0.0, 0.0)
        subframe_cm.orientation = Jusme.Vector(0.0, 0.0, 0.0)

    uc_sf_mid = _get(scene, "ground.cfs_uc_sf_atch_mid")
    uc_sf_mid.location = _midpoint(
        points["hps_uc_sf_atch_l"], points["hps_uc_sf_atch_r"]
    )
    uc_sf_mid.orientation = _vector(subframe_orientation)
    body_point = _get(scene, "ground.cfs_subframe_to_body_point")
    body_point.location = _vector(subframe_center)
    body_point.orientation = _vector(subframe_orientation)

    hsg_length = VecUtils.DM(points["hsg_1"], points["hsg_2"])
    hsg_orientation = VecUtils.ORI_ALONG_AXIS(
        points["hsg_1"], points["hsg_2"], "z"
    )
    points["zdt1"] = _vector(
        VecUtils.LOC_ALONG_LINE(points["hsg_1"], points["hsg_2"], 0.6 * hsg_length)
    )
    points["zdt2"] = _vector(
        VecUtils.LOC_ALONG_LINE(points["hsg_1"], points["hsg_2"], 0.9 * hsg_length)
    )
    for point_name in ("zdt1", "zdt2"):
        point = _get(scene, "ground." + point_name)
        point.location = _vector(points[point_name])
        point.orientation = _vector(hsg_orientation)
    _set_part_pose(scene, "hsg", points["hsg_1"], points["hsg_2"])
    _set_part_pose(scene, "zdt", points["zdt1"], points["zdt2"])


def _update_static_markers(scene, points, changed_name):
    del changed_name
    _set_marker_global(
        scene,
        "ges_upper_cylinder.jxs_joint_j_11",
        "ges_upper_cylinder",
        points["hps_lc_top"],
        Jusme.Vector(180.0, 180.0, 0.0),
    )
    _set_marker_global(
        scene,
        "ges_collar.MARKER_166",
        "ges_collar",
        _get(scene, "ground.cfs_collar_top").location,
        Jusme.Vector(0.0, 0.0, 0.0),
    )

CONTRACT = _adm.TemplateContract(
    model_name=MODEL_NAME,
    model_folder=MODEL_FOLDER,
    hardpoint_rules=HARDPOINT_RULES,
    core_hardpoints=CORE_HARDPOINTS,
    required_paths=(
        "ground.origo",
        "ges_upper_cylinder",
        "ges_lower_cylinder",
        "ges_collar",
        "ges_upper_torque_arm",
        "ges_lower_torque_arm",
        "ges_dragbrace",
        "ges_subframe",
        "hsg",
        "zdt",
    ),
    length_pairs=(
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
        ("hps_db_sf_atch", "hps_db_uc_atch", "斜撑杆"),
        ("hps_uta_uc_atch", "hps_lta_uta_atch", "上扭力臂"),
        ("hps_lta_lc_atch", "hps_lta_uta_atch", "下扭力臂"),
        ("hsg_1", "hsg_2", "减摆器"),
    ),
    vertical_pairs=(
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
    ),
    wheel_pair=("hpl_wheel_center", "hpr_wheel_center"),
    optional_patch_fragments=(".lt_l.wheel_part", ".lt_r.wheel_part"),
    label="Swing",
    structure_updater=_update_structure,
    post_patch_updater=_update_static_markers,
    transaction_paths=(
        "ground.cfs_collar_top",
        "ground.cfs_wheel_centers_midpoint",
        "ground.cfs_uc_sf_atch_mid",
        "ground.cfs_subframe_to_body_point",
        "ges_upper_cylinder.jxs_joint_j_11",
        "ges_collar.MARKER_166",
    ),
    recompute_paths=(
        "js_wt",
        "zdt_upcylinder",
        "hsg_collar",
        "joint_lt_y",
        "joint_lt_z",
        "MOTION_4",
        "hcq_sd",
        "jbznl",
        "jgxzl",
        "jiaodu",
        "jsd",
        "kqthl",
        "lz_jili",
        "yyznl",
        "_cv_bushing",
    ),
)


def canonical_hardpoint_name(name_or_path):
    return _adm.canonical_hardpoint_name(CONTRACT, name_or_path)


def get_rule(name_or_path):
    return _adm.get_rule(CONTRACT, name_or_path)


def hardpoint_path(name_or_path, scene=None):
    return _adm.hardpoint_path(CONTRACT, name_or_path, scene)


def compatibility_error(scene=None):
    return _adm.compatibility_error(CONTRACT, scene)


def is_compatible_scene(scene=None):
    return _adm.is_compatible_scene(CONTRACT, scene)


def adjust_hardpoint(name_or_path, x_coord, y_coord, z_coord, scene=None):
    return _adm.adjust_hardpoint(
        CONTRACT, name_or_path, x_coord, y_coord, z_coord, scene
    )
