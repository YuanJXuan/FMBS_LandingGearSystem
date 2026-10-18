"""Transactional hardpoint parameterization for ``template_2_retract``."""

import os

import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils

import AdmHardpointParameterization as _adm


MODEL_NAME = "template_2_retract"
MODEL_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Model", MODEL_NAME)
)

HARDPOINT_RULES = {
    "hps_db_sf_atch": ("x", "z"),
    "hps_db_uc_atch": ("x", "z"),
    "hps_rod_top": ("x", "z"),
    "hps_rod_bot": ("x", "z"),
}

CORE_HARDPOINTS = (
    "hps_db_sf_atch",
    "hps_db_uc_atch",
    "hps_rod_top",
    "hps_rod_bot",
    "hps_uc_sf_atch_l",
    "hps_uc_sf_atch_r",
    "hps_uc_geompt",
    "hps_uc_top",
    "hps_uc_bot",
    "hps_lc_top",
    "hps_lc_bot",
    "hps_lta_uta_atch",
    "hps_uta_uc_atch",
    "hps_lta_lc_atch",
    "hpl_wheel_center",
    "hpr_wheel_center",
    "hpl_ob_axle",
    "hpr_ob_axle",
    "hps_aeroforceN",
)


def _get(scene, path, required=True):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    node = scene.getObject(".{}.{}".format(model_name, path))
    if node is None and required:
        raise RuntimeError("缺少Retract结构对象 {}".format(path))
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


def _distance(first, second):
    return float(VecUtils.DM(first, second))


def _along(first, second, length):
    if _distance(first, second) <= _adm.EPSILON:
        raise RuntimeError("收放机构方向定义点不能重合")
    return _vector(VecUtils.LOC_ALONG_LINE(first, second, float(length)))


def _set_part_pose(scene, path, first, second, axis="z"):
    if _distance(first, second) <= _adm.EPSILON:
        raise RuntimeError("{}的两个定义点不能重合".format(path))
    part = _get(scene, path)
    part.location = _midpoint(first, second)
    part.orientation = VecUtils.ORI_ALONG_AXIS(first, second, axis)
    cm = _get(scene, path + ".cm", required=False)
    if cm is not None:
        cm.location = Jusme.Vector(0.0, 0.0, 0.0)
        cm.orientation = Jusme.Vector(0.0, 0.0, 0.0)


def _set_marker_global(
    scene, marker_path, parent_path, location, orientation, required=True
):
    marker = _get(scene, marker_path, required=required)
    parent = _get(scene, parent_path, required=required)
    if marker is None or parent is None:
        return
    local_location, local_orientation = VecUtils.global2local(
        parent.location,
        parent.orientation,
        location,
        orientation,
    )
    marker.location = _vector(local_location)
    marker.orientation = _vector(local_orientation)


def _set_child_global_location(scene, child_path, parent_path, location):
    child = _get(scene, child_path)
    parent = _get(scene, parent_path)
    local_location, unused_orientation = VecUtils.global2local(
        parent.location,
        parent.orientation,
        location,
        Jusme.Vector(0.0, 0.0, 0.0),
    )
    del unused_orientation
    child.location = _vector(local_location)


def _set_hardpoint(scene, points, name, value):
    points[name] = _vector(value)
    _get(scene, "ground." + name).location = _vector(value)


def _update_subframe(scene, points):
    orientation = VecUtils.ORI_IN_PLANE(
        points["hps_uc_sf_atch_r"],
        points["hps_uc_sf_atch_l"],
        points["hps_db_sf_atch"],
        "z_zx",
    )
    center = Jusme.Vector(
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
    subframe.location = center
    subframe.orientation = _vector(orientation)
    cm = _get(scene, "ges_subframe.cm", required=False)
    if cm is not None:
        cm.location = Jusme.Vector(0.0, 0.0, 0.0)
        cm.orientation = Jusme.Vector(0.0, 0.0, 0.0)

    midpoint = _get(scene, "ground.cfs_uc_sf_atch_mid")
    midpoint.location = _midpoint(
        points["hps_uc_sf_atch_l"], points["hps_uc_sf_atch_r"]
    )
    midpoint.orientation = _vector(orientation)


def _update_structure(scene, points, changed_name):
    """Apply the four-point retraction linkage rules used by this template."""
    rod_geometry = _get(scene, "ges_sf_rod.CYLINDER_30")
    preserved_rod_length = float(rod_geometry.length)
    if preserved_rod_length <= _adm.EPSILON:
        raise RuntimeError("收放活塞杆当前长度无效")

    db_sf = points["hps_db_sf_atch"]
    db_uc = points["hps_db_uc_atch"]
    rod_top = points["hps_rod_top"]
    rod_bot = points["hps_rod_bot"]

    if changed_name == "hps_db_sf_atch":
        top_offset = _distance(db_uc, rod_top)
        rod_top = _along(db_uc, db_sf, top_offset)
        rod_bot = _along(rod_top, db_uc, preserved_rod_length)
    elif changed_name == "hps_db_uc_atch":
        actuator_length = _distance(db_sf, db_uc)
        rod_bot = _along(db_sf, db_uc, actuator_length + 20.0)
        rod_top = _along(
            db_sf, db_uc, actuator_length + 20.0 - preserved_rod_length
        )
    elif changed_name == "hps_rod_top":
        actuator_length = _distance(db_sf, db_uc)
        db_uc = _along(db_sf, rod_top, actuator_length)
        rod_bot = _along(db_sf, rod_top, actuator_length + 20.0)
    elif changed_name == "hps_rod_bot":
        bot_distance = _distance(db_sf, rod_bot)
        if bot_distance <= 20.0 + _adm.EPSILON:
            raise RuntimeError("活塞杆下端点距机架端必须大于20 mm")
        db_uc = _along(db_sf, rod_bot, bot_distance - 20.0)
        rod_top = _along(rod_bot, db_sf, preserved_rod_length)
    else:
        raise RuntimeError("未定义的收放硬点联动规则：{}".format(changed_name))

    if _distance(db_sf, db_uc) <= 50.0 + _adm.EPSILON:
        raise RuntimeError("收放作动筒两端距离必须大于50 mm")
    if _distance(rod_top, rod_bot) <= _adm.EPSILON:
        raise RuntimeError("收放活塞杆两端点不能重合")

    _set_hardpoint(scene, points, "hps_db_sf_atch", db_sf)
    _set_hardpoint(scene, points, "hps_db_uc_atch", db_uc)
    _set_hardpoint(scene, points, "hps_rod_top", rod_top)
    _set_hardpoint(scene, points, "hps_rod_bot", rod_bot)

    _set_part_pose(scene, "ges_sf_actuator", db_sf, db_uc)
    _set_part_pose(scene, "ges_sf_rod", rod_bot, rod_top)
    _set_child_global_location(scene, "ges_sf_rod.PT3", "ges_sf_rod", rod_bot)
    _update_subframe(scene, points)


def _update_static_markers(scene, points, changed_name):
    """Update constant actuator/rod markers omitted by the CMD patch."""
    del changed_name
    zero = Jusme.Vector(0.0, 0.0, 0.0)
    rod_axis = VecUtils.ORI_ALONG_AXIS(
        points["hps_db_uc_atch"], points["hps_db_sf_atch"], "z"
    )
    rod_center = _midpoint(points["hps_rod_bot"], points["hps_rod_top"])

    _set_marker_global(
        scene,
        "ges_sf_actuator.MARKER_97",
        "ges_sf_actuator",
        points["hps_db_sf_atch"],
        zero,
    )
    _set_marker_global(
        scene,
        "ges_sf_rod.MARKER_84",
        "ges_sf_rod",
        rod_center,
        rod_axis,
    )
    _set_marker_global(
        scene,
        "ges_sf_actuator.MARKER_85",
        "ges_sf_actuator",
        rod_center,
        rod_axis,
    )

    # The spherical actuator-to-strut joint follows the rod bottom point.
    for marker_path, parent_path in (
        ("ges_sf_rod.MARKER_5", "ges_sf_rod"),
        ("ges_upper_cylinder.MARKER_4", "ges_upper_cylinder"),
    ):
        _set_marker_global(
            scene,
            marker_path,
            parent_path,
            points["hps_rod_bot"],
            zero,
        )

    for marker_path in (
        "MARKER_96",
        "MARKER_101",
        "MARKER_88",
        "MARKER_stopper_rod",
    ):
        _set_marker_global(
            scene,
            "ges_sf_rod." + marker_path,
            "ges_sf_rod",
            points["hps_rod_bot"],
            zero,
            required=False,
        )
    for marker_path in ("MARKER_100", "MARKER_89", "stopper_actuator"):
        _set_marker_global(
            scene,
            "ges_sf_actuator." + marker_path,
            "ges_sf_actuator",
            points["hps_rod_bot"],
            zero,
            required=False,
        )

CONTRACT = _adm.TemplateContract(
    model_name=MODEL_NAME,
    model_folder=MODEL_FOLDER,
    hardpoint_rules=HARDPOINT_RULES,
    core_hardpoints=CORE_HARDPOINTS,
    required_paths=(
        "ground.origo",
        "ges_sf_actuator",
        "ges_sf_rod",
        "ges_upper_cylinder",
        "ges_lower_cylinder",
        "ges_collar",
        "ges_upper_torque_arm",
        "ges_lower_torque_arm",
        "ges_subframe",
    ),
    length_pairs=(
        ("hps_db_sf_atch", "hps_db_uc_atch", "收放作动筒"),
        ("hps_rod_top", "hps_rod_bot", "收放活塞杆"),
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
    ),
    vertical_pairs=(
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
    ),
    wheel_pair=("hpl_wheel_center", "hpr_wheel_center"),
    label="Retract",
    structure_updater=_update_structure,
    post_patch_updater=_update_static_markers,
    transaction_paths=(
        "ground.cfs_uc_sf_atch_mid",
        "ges_sf_rod.PT3",
        "ges_sf_actuator.MARKER_97",
        "ges_sf_actuator.MARKER_85",
        "ges_sf_rod.MARKER_84",
        "ges_sf_rod.MARKER_5",
        "ges_upper_cylinder.MARKER_4",
        "ges_sf_rod.MARKER_96",
        "ges_sf_rod.MARKER_101",
        "ges_sf_rod.MARKER_88",
        "ges_sf_rod.MARKER_stopper_rod",
        "ges_sf_actuator.MARKER_100",
        "ges_sf_actuator.MARKER_89",
        "ges_sf_actuator.stopper_actuator",
    ),
    recompute_paths=(
        "joscyl_db_sf",
        "joscly_ac_rd",
        "jossph_rd_uc",
        "JOINT_14",
        "MOTION_disp",
        "disp_sf",
        "NLG_aeroforce",
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
