"""ADM hardpoint parameterization for the semi-rocker retraction template."""

import os

import Jusme

import AdmHardpointParameterization as _adm


MODEL_NAME = "template_2_retract_semirocker"
MODEL_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Model", MODEL_NAME)
)

# The mechanism is symmetric about the XZ plane.  The exported reference
# model defines all structural points in that plane except the two subframe
# attachment points, so ordinary edits keep Y locked and mirror the paired
# attachment point automatically.
HARDPOINT_RULES = {
    "hps_db_sf_atch": ("x", "z"),
    "hps_uc_sf_atch_l": ("x", "z"),
    "hps_uc_sf_atch_r": ("x", "z"),
    "hps_lc_bot": ("x", "z"),
    "hps_uc_top": ("x", "z"),
    "hps_db_uc_atch": ("x", "z"),
    "hps_uc_geompt": ("x", "z"),
    "hps_uc_bot": ("x", "z"),
    "hps_lc_top": ("x", "z"),
    "hps_lb_uc_atch": ("x", "z"),
}

CORE_HARDPOINTS = tuple(HARDPOINT_RULES)

_preserved_runtime_parameters = {}


def _get(scene, path, required=True):
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    node = scene.getObject(".{}.{}".format(model_name, path))
    if node is None and required:
        raise RuntimeError("缺少半摇臂收放结构对象 {}".format(path))
    return node


def _vector(value):
    if all(hasattr(value, axis) for axis in ("x", "y", "z")):
        return Jusme.Vector(float(value.x), float(value.y), float(value.z))
    return Jusme.Vector(float(value[0]), float(value[1]), float(value[2]))


def _update_structure(scene, points, changed_name):
    """Keep the paired subframe attachments symmetric before patch replay."""
    global _preserved_runtime_parameters
    _preserved_runtime_parameters = {}
    for path, property_name in (
        ("MOTION_1", "function"),
        ("SFORCE_1", "function"),
        ("Last_Sim", "commands"),
    ):
        node = _get(scene, path, required=False)
        if node is not None:
            _preserved_runtime_parameters[(path, property_name)] = getattr(
                node, property_name, ""
            )

    mirror_names = {
        "hps_uc_sf_atch_l": "hps_uc_sf_atch_r",
        "hps_uc_sf_atch_r": "hps_uc_sf_atch_l",
    }
    mirror_name = mirror_names.get(changed_name)
    if mirror_name is None:
        return

    changed = points[changed_name]
    mirrored = points[mirror_name]
    new_mirrored = Jusme.Vector(changed.x, mirrored.y, changed.z)
    points[mirror_name] = _vector(new_mirrored)
    _get(scene, "ground." + mirror_name).location = _vector(new_mirrored)


def _restore_runtime_parameters(scene, points, changed_name):
    """Do not let formula replay discard values edited in the dialog."""
    del points, changed_name
    for (path, property_name), value in _preserved_runtime_parameters.items():
        node = _get(scene, path, required=False)
        if node is not None:
            setattr(node, property_name, value)


CONTRACT = _adm.TemplateContract(
    model_name=MODEL_NAME,
    model_folder=MODEL_FOLDER,
    hardpoint_rules=HARDPOINT_RULES,
    core_hardpoints=CORE_HARDPOINTS,
    required_paths=(
        "ground.origo",
        "ges_dragbrace",
        "ges_upper_cylinder",
        "ges_lower_cylinder",
        "ges_subframe",
        "ges_collar",
        "lunzhou",
        "luntai",
        "sf_rod",
        "MOTION_1",
        "SFORCE_1",
        "Last_Sim",
    ),
    length_pairs=(
        ("hps_db_sf_atch", "hps_db_uc_atch", "收放作动筒"),
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
    ),
    vertical_pairs=(
        ("hps_uc_top", "hps_uc_bot", "上支柱"),
        ("hps_lc_top", "hps_lc_bot", "下支柱"),
    ),
    label="SemiRockerRetract",
    structure_updater=_update_structure,
    post_patch_updater=_restore_runtime_parameters,
    transaction_paths=(
        "ground.hps_uc_sf_atch_l",
        "ground.hps_uc_sf_atch_r",
    ),
    recompute_paths=(
        "joscyl_lc_uc_joint",
        "josrev_uc_sf_joint",
        "mts_fixed_2",
        "josfix_subframe_to_body",
        "joscyl_db_sf",
        "josrev_collar_uc_joint",
        "JOINT_12",
        "JOINT_13",
        "JOINT_14",
        "JOINT_15",
        "JOINT_16",
        "JOINT_17",
        "MOTION_1",
        "SFORCE_1",
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
