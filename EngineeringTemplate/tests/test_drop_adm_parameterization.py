# -*- coding: utf-8 -*-

import importlib.util
import math
import sys
import types
import unittest
from pathlib import Path
from unittest import mock


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
MODULE_PATH = TEMPLATE_DIR / "Drop" / "DropAdmParameterization.py"
ROAD_MODULE_PATH = TEMPLATE_DIR / "Drop" / "DropRoadPosition.py"

road_spec = importlib.util.spec_from_file_location(
    "DropRoadPositionForTests",
    ROAD_MODULE_PATH,
)
DropRoadPosition = importlib.util.module_from_spec(road_spec)
road_spec.loader.exec_module(DropRoadPosition)


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class FakeNode:
    def __init__(self, name, location=None):
        self.Name = name
        self.location = location or Vector(0.0, 0.0, 0.0)
        self.orientation = Vector(0.0, 0.0, 0.0)
        self.length = 1.0
        self.Objects = []
        self.recompute_count = 0

    def recompute(self):
        self.recompute_count += 1


class FakeScene:
    def __init__(self, name="template_2_drop"):
        self.Name = name
        self.nodes = {}
        self.Objects = []
        self.recompute_count = 0

    def add(self, path, location=None):
        node = FakeNode(path, location)
        self.nodes[path] = node
        self.Objects.append(node)
        return node

    def getObject(self, path):
        return self.nodes.get(path)

    def recompute(self):
        self.recompute_count += 1


def _loc_along_line(first, second, distance):
    dx = second.x - first.x
    dy = second.y - first.y
    dz = second.z - first.z
    magnitude = math.sqrt(dx * dx + dy * dy + dz * dz)
    return Vector(
        first.x + distance * dx / magnitude,
        first.y + distance * dy / magnitude,
        first.z + distance * dz / magnitude,
    )


def _load_module(scene):
    jusme = types.ModuleType("Jusme")
    jusme.Vector = Vector
    jusme.ActiveUSScene = scene

    vec_utils = types.ModuleType("FmbsShortcut.SCcmd.utils.VecUtils")
    vec_utils.LOC_ALONG_LINE = _loc_along_line
    vec_utils.ORI_ALONG_AXIS = lambda *args: Vector(1.0, 2.0, 3.0)
    vec_utils.LOC_RELATIVE_TO = lambda _offset, node: Vector(
        node.location.x, node.location.y, node.location.z
    )
    vec_utils.ORI_RELATIVE_TO = lambda orientation, _node: Vector(*orientation)
    vec_utils.global2local = lambda _pl, _po, location, orientation: (
        [location.x, location.y, location.z],
        [orientation.x, orientation.y, orientation.z],
    )

    shortcut = types.ModuleType("FmbsShortcut")
    shortcut.__path__ = []
    sccmd = types.ModuleType("FmbsShortcut.SCcmd")
    sccmd.__path__ = []
    utils = types.ModuleType("FmbsShortcut.SCcmd.utils")
    utils.__path__ = []
    fake_modules = {
        "Jusme": jusme,
        "FmbsShortcut": shortcut,
        "FmbsShortcut.SCcmd": sccmd,
        "FmbsShortcut.SCcmd.utils": utils,
        "FmbsShortcut.SCcmd.utils.VecUtils": vec_utils,
    }

    with mock.patch.dict(sys.modules, fake_modules):
        spec = importlib.util.spec_from_file_location(
            "drop_adm_parameterization_under_test",
            MODULE_PATH,
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


def _complete_scene(name="template_2_drop", root_name=None):
    scene = FakeScene(name)
    root = ".{}".format(root_name or name)
    hardpoints = {
        "hps_uc_top": (6197.6, 0.0, 1625.6),
        "hps_uc_bot": (6197.6, 0.0, 762.0),
        "hps_lc_top": (6197.6, 0.0, 1197.0),
        "hps_lc_bot": (6197.6, 0.0, 308.0),
        "hps_db_sf_atch": (7484.11, 0.0, 1623.06),
        "hps_db_uc_atch": (6451.6, 0.0, 1016.0),
        "hps_uta_uc_atch": (6324.6, 0.0, 838.2),
        "hps_lta_uta_atch": (6654.8, 0.0, 611.2),
        "hps_lta_lc_atch": (6299.2, 0.0, 333.4),
        "hps_uc_sf_atch_l": (6314.44, -340.36, 1691.64),
        "hps_uc_sf_atch_r": (6314.44, 340.36, 1691.64),
        "hpl_wheel_center1": (6229.096, -209.55, 308.0),
        "hpr_wheel_center1": (6229.096, 209.55, 308.0),
        "hpl_ob_axle1": (6229.096, -285.75, 308.0),
        "hpr_ob_axle1": (6229.096, 285.75, 308.0),
    }
    for name, coordinates in hardpoints.items():
        scene.add(
            root + ".ground." + name,
            Vector(*coordinates),
        )
    for name in (
        "ges_upper_cylinder",
        "ges_collar",
        "ges_upper_torque_arm",
        "ges_lower_torque_arm",
        "ges_dragbrace",
        "ges_subframe_2",
    ):
        scene.add(root + "." + name)
    scene.add(root + ".ground.cfs_collar_top")
    scene.add(root + ".ground.origo1")
    for path in (
        "ges_upper_cylinder.MARKER_2",
        "ges_upper_cylinder.MARKER_405",
        "ges_upper_cylinder.MARKER_407",
        "ges_upper_cylinder.MARKER_409",
        "ges_upper_cylinder.MARKER_116",
        "ges_dragbrace.MARKER_429",
        "mts_body_mount_2.MARKER_430",
        "ges_lower_cylinder.MARKER_1",
        "ges_lower_cylinder.MARKER_406",
        "ges_lower_cylinder.MARKER_408",
        "ges_lower_cylinder.MARKER_410",
        "ges_lower_cylinder.MARKER_6",
        "ges_lower_cylinder.MARKER_8",
    ):
        scene.add(root + "." + path)
    scene.add(root + ".ges_lower_cylinder")
    scene.add(root + ".mts_body_mount_2")
    for name in (
        "NLG_V",
        "NLG_S",
        "x1",
        "x2",
        "VARIABLE_123",
        "VARIABLE_124",
        "_cv_solver_variable",
        "Last_Sim",
    ):
        scene.add(root + "." + name)
    for name in (
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
    ):
        scene.add(root + "." + name)
    scene.add(root + ".luntai1_2.wheel_part")
    scene.add(root + ".luntai2_2.wheel_part")
    for path in (
        "ges_dragbrace.gralin_dragbrace_geom",
        "ges_upper_cylinder.gralin_upper_cylinder_geom1",
        "ges_upper_cylinder.gralin_upper_cylinder_geom2",
        "ges_upper_cylinder.gralin_upper_cylinder_geom3",
        "ges_lower_cylinder.gralin_geom1",
        "ges_lower_cylinder.gralin_geom2",
        "ges_upper_torque_arm.gralin_upper_torque_arm_geom",
        "ges_lower_torque_arm.gralin_lower_torque_arm_geom",
        "ges_collar.gralin_collar",
    ):
        scene.add(root + "." + path)
    return scene


class DropAdmParameterizationTests(unittest.TestCase):
    def test_drop_road_position_uses_actual_adm_scene_name(self):
        scene = FakeScene("Unknown1")
        road = scene.add(
            ".Unknown1.lumian_road_part",
            Vector(12238.0, 1509.0, -560.0),
        )
        ground_reference = scene.add(
            ".Unknown1.ground.lumian_ref_1",
            Vector(12238.0, 1509.0, -560.0),
        )
        road_reference = scene.add(
            ".Unknown1.lumian_road_part.road_ref",
            Vector(0.0, 0.0, 0.0),
        )
        road_joint = scene.add(".Unknown1.lumian_road_joint")

        self.assertEqual(
            DropRoadPosition.get_location(scene),
            (12238.0, 1509.0, -560.0),
        )
        DropRoadPosition.set_location(scene, (12000, 1400, -500))

        self.assertEqual(road.location, (12000.0, 1400.0, -500.0))
        self.assertEqual(
            ground_reference.location,
            (12000.0, 1400.0, -500.0),
        )
        self.assertEqual(
            (road_reference.location.x, road_reference.location.y, road_reference.location.z),
            (0.0, 0.0, 0.0),
        )
        self.assertEqual(road_joint.recompute_count, 1)
        self.assertEqual(scene.recompute_count, 2)

    def test_drop_road_position_supports_legacy_python_model(self):
        scene = FakeScene("GCMB")
        scene.add(".GCMB.road", Vector(1, 2, 3))
        scene.add(".GCMB.ground.lumian_ref_1", Vector(1, 2, 3))
        self.assertEqual(DropRoadPosition.get_location(scene), (1.0, 2.0, 3.0))

    def test_drop_road_position_requires_tire_reference_marker(self):
        scene = FakeScene("Unknown")
        scene.add(".Unknown.lumian_road_part", Vector(1, 2, 3))
        with self.assertRaisesRegex(RuntimeError, "lumian_ref_1"):
            DropRoadPosition.set_location(scene, (4, 5, 6))

    def test_drop_dialog_contains_three_road_location_editors(self):
        page_text = (TEMPLATE_DIR / "template_2_drop.py").read_text(
            encoding="utf-8"
        )
        for parameter_name in (
            "lumian_road_part.location.x",
            "lumian_road_part.location.y",
            "lumian_road_part.location.z",
        ):
            self.assertIn(parameter_name, page_text)
        self.assertIn("DropRoadPosition.set_location", page_text)

    def test_cmd_patch_modes_cover_partial_marker_updates(self):
        scene = _complete_scene()
        location_only = scene.add(
            ".template_2_drop.mts_body_mount_2.MARKER_427",
            Vector(1.0, 2.0, 3.0),
        )
        orientation_only = scene.add(
            ".template_2_drop.luntai1_2.wheel_part.gfo_i",
            Vector(4.0, 5.0, 6.0),
        )
        module = _load_module(scene)
        modes = module._partial_marker_patch_modes()

        self.assertEqual(
            modes[".template_2_drop.mts_body_mount_2.MARKER_427"],
            (True, False),
        )
        self.assertEqual(
            modes[".template_2_drop.luntai1_2.wheel_part.gfo_i"],
            (False, True),
        )
        self.assertEqual(
            modes[".template_2_drop.ges_upper_cylinder.gralin_2"],
            (True, True),
        )

        captured = module._capture_partial_marker_properties(scene)
        location_only.orientation = Vector(10.0, 20.0, 30.0)
        orientation_only.location = Vector(40.0, 50.0, 60.0)
        module._restore_partial_marker_properties(captured)
        self.assertAlmostEqual(location_only.orientation.x, 0.0)
        self.assertAlmostEqual(orientation_only.location.x, 4.0)

    def test_every_supported_hardpoint_completes_the_same_transaction(self):
        changes = {
            "hps_uc_top": (6197.6, 0.0, 1640.0),
            "hps_uc_bot": (6197.6, 0.0, 750.0),
            "hps_lc_top": (6197.6, 0.0, 1210.0),
            "hps_lc_bot": (6197.6, 0.0, 295.0),
            "hps_db_sf_atch": (7490.0, 0.0, 1630.0),
            "hps_db_uc_atch": (6460.0, 0.0, 1020.0),
            "hps_uta_uc_atch": (6330.0, 0.0, 840.0),
            "hps_lta_uta_atch": (6660.0, 0.0, 615.0),
            "hps_lta_lc_atch": (6305.0, 0.0, 335.0),
            "hpl_wheel_center1": (6229.096, -220.0, 308.0),
            "hpr_wheel_center1": (6229.096, 220.0, 308.0),
        }
        for name, coordinates in changes.items():
            with self.subTest(hardpoint=name):
                scene = _complete_scene()
                module = _load_module(scene)
                with mock.patch.object(
                    module, "_run_formula_patch", return_value=(89, [])
                ):
                    result = module.adjust_hardpoint(
                        name, *coordinates, scene=scene
                    )
                self.assertTrue(result.success, result.message)
                self.assertTrue(result.changed)

    def test_adjustment_updates_base_pose_and_formula_patch(self):
        scene = _complete_scene()
        module = _load_module(scene)

        with mock.patch.object(module, "_run_formula_patch", return_value=(89, [])):
            result = module.adjust_hardpoint(
                "hps_uc_top", 6197.6, 0.0, 1700.0, scene=scene
            )

        self.assertTrue(result.success)
        self.assertTrue(result.changed)
        self.assertEqual(result.updated, 89)
        self.assertAlmostEqual(
            scene.getObject(
                ".template_2_drop.ground.hps_uc_top"
            ).location.z,
            1700.0,
        )
        self.assertAlmostEqual(
            scene.getObject(
                ".template_2_drop.ges_upper_cylinder"
            ).location.z,
            (1700.0 + 762.0) / 2.0,
        )
        self.assertAlmostEqual(
            scene.getObject(
                ".template_2_drop.ges_upper_cylinder.MARKER_405"
            ).location.z,
            1700.0,
        )
        self.assertEqual(scene.recompute_count, 1)

    def test_static_joint_markers_and_wheel_part_follow_hardpoints(self):
        scene = _complete_scene()
        module = _load_module(scene)
        with mock.patch.object(module, "_run_formula_patch", return_value=(89, [])):
            brace_result = module.adjust_hardpoint(
                "hps_db_sf_atch", 7500.0, 0.0, 1640.0, scene=scene
            )
            wheel_result = module.adjust_hardpoint(
                "hpl_wheel_center1", 6229.096, -220.0, 308.0, scene=scene
            )

        self.assertTrue(brace_result.success, brace_result.message)
        self.assertTrue(wheel_result.success, wheel_result.message)
        for path in (
            ".template_2_drop.ges_dragbrace.MARKER_429",
            ".template_2_drop.mts_body_mount_2.MARKER_430",
        ):
            marker = scene.getObject(path)
            self.assertAlmostEqual(marker.location.x, 7500.0)
            self.assertAlmostEqual(marker.location.z, 1640.0)
        self.assertAlmostEqual(
            scene.getObject(
                ".template_2_drop.luntai1_2.wheel_part"
            ).location.y,
            -220.0,
        )
        self.assertAlmostEqual(
            scene.getObject(
                ".template_2_drop.ges_lower_cylinder.MARKER_8"
            ).location.y,
            -220.0,
        )

    def test_lower_cylinder_follows_lower_strut_hardpoints(self):
        scene = _complete_scene()
        module = _load_module(scene)

        with mock.patch.object(module, "_run_formula_patch", return_value=(89, [])):
            result = module.adjust_hardpoint(
                "hps_lc_top", 6197.6, 0.0, 1210.0, scene=scene
            )

        self.assertTrue(result.success, result.message)
        lower_cylinder = scene.getObject(
            ".template_2_drop.ges_lower_cylinder"
        )
        self.assertAlmostEqual(lower_cylinder.location.z, (1210.0 + 308.0) / 2.0)
        self.assertAlmostEqual(lower_cylinder.orientation.x, 1.0)

    def test_locked_axis_change_is_rejected_without_mutating_model(self):
        scene = _complete_scene()
        module = _load_module(scene)
        target = scene.getObject(".template_2_drop.ground.hps_uc_top")

        result = module.adjust_hardpoint(
            "hps_uc_top", 6200.0, 0.0, 1700.0, scene=scene
        )

        self.assertFalse(result.success)
        self.assertAlmostEqual(target.location.x, 6197.6)
        self.assertAlmostEqual(target.location.z, 1625.6)
        self.assertEqual(scene.recompute_count, 0)

    def test_invalid_geometry_is_rejected_before_snapshot_or_patch(self):
        scene = _complete_scene()
        module = _load_module(scene)
        target = scene.getObject(".template_2_drop.ground.hps_uc_top")

        with mock.patch.object(module, "_run_formula_patch") as patch_runner:
            result = module.adjust_hardpoint(
                "hps_uc_top", 6197.6, 0.0, 700.0, scene=scene
            )

        self.assertFalse(result.success)
        self.assertIn("必须高于", result.message)
        self.assertAlmostEqual(target.location.z, 1625.6)
        patch_runner.assert_not_called()

    def test_patch_failure_rolls_back_hardpoint_and_part_pose(self):
        scene = _complete_scene()
        module = _load_module(scene)
        target = scene.getObject(".template_2_drop.ground.hps_uc_top")
        upper_part = scene.getObject(".template_2_drop.ges_upper_cylinder")
        upper_part.location = Vector(10.0, 20.0, 30.0)

        with mock.patch.object(
            module,
            "_run_formula_patch",
            side_effect=RuntimeError("模拟补丁失败"),
        ):
            result = module.adjust_hardpoint(
                "hps_uc_top", 6197.6, 0.0, 1700.0, scene=scene
            )

        self.assertFalse(result.success)
        self.assertAlmostEqual(target.location.z, 1625.6)
        self.assertAlmostEqual(upper_part.location.x, 10.0)
        self.assertAlmostEqual(upper_part.location.y, 20.0)
        self.assertAlmostEqual(upper_part.location.z, 30.0)
        self.assertEqual(scene.recompute_count, 1)

    def test_compatible_model_can_use_the_adm_scene_name(self):
        scene = _complete_scene("Aircraft_template")
        module = _load_module(scene)

        with mock.patch.object(module, "_run_formula_patch", return_value=(89, [])):
            result = module.adjust_hardpoint(
                "hps_uc_top", 6197.6, 0.0, 1700.0, scene=scene
            )

        self.assertTrue(result.success, result.message)
        self.assertAlmostEqual(
            scene.getObject(".Aircraft_template.ground.hps_uc_top").location.z,
            1700.0,
        )

    def test_unknown_numbered_adm_scene_is_supported(self):
        scene = _complete_scene("Unknown1")
        module = _load_module(scene)

        self.assertEqual(
            module.hardpoint_path("hps_uc_top", scene),
            ".Unknown1.ground.hps_uc_top",
        )
        with mock.patch.object(module, "_run_formula_patch", return_value=(89, [])):
            result = module.adjust_hardpoint(
                "hps_uc_top", 6197.6, 0.0, 1700.0, scene=scene
            )

        self.assertTrue(result.success, result.message)

    def test_non_geometry_patch_nodes_do_not_disable_hardpoint_editing(self):
        scene = _complete_scene()
        for name in (
            "NLG_V",
            "NLG_S",
            "x1",
            "x2",
            "VARIABLE_123",
            "VARIABLE_124",
            "_cv_solver_variable",
            "Last_Sim",
        ):
            scene.nodes.pop(".template_2_drop." + name)
        module = _load_module(scene)

        self.assertEqual(module.compatibility_error(scene), "")

    def test_optional_subframe_and_wheel_parts_may_be_absent(self):
        scene = _complete_scene()
        for path in (
            ".template_2_drop.ges_subframe_2",
            ".template_2_drop.luntai1_2.wheel_part",
            ".template_2_drop.luntai2_2.wheel_part",
        ):
            scene.nodes.pop(path)
        module = _load_module(scene)

        self.assertEqual(module.compatibility_error(scene), "")
        with mock.patch.object(module, "_run_formula_patch", return_value=(89, [])):
            result = module.adjust_hardpoint(
                "hps_db_sf_atch", 7490.0, 0.0, 1630.0, scene=scene
            )

        self.assertTrue(result.success, result.message)

    def test_optional_patch_errors_are_warnings_not_transaction_failures(self):
        scene = _complete_scene()
        module = _load_module(scene)

        class FakePatch:
            @staticmethod
            def apply_patch(_model_folder, _model_name):
                return {
                    "updated": 80,
                    "warnings": [],
                    "errors": [
                        {
                            "step": (
                                "marker modify .template_2_drop."
                                "ges_subframe_2.graout_1"
                            ),
                            "error": "missing optional node",
                        },
                        {
                            "step": (
                                "marker modify .template_2_drop."
                                "luntai1_2.wheel_part.gfo_i"
                            ),
                            "error": "missing optional node",
                        },
                    ],
                }

        with mock.patch.object(module, "_load_patch_module", return_value=FakePatch):
            updated, warnings = module._run_formula_patch(scene)

        self.assertEqual(updated, 80)
        self.assertEqual(len(warnings), 2)

    def test_post_update_validation_failure_rolls_back_everything(self):
        scene = _complete_scene()
        module = _load_module(scene)
        target = scene.getObject(".template_2_drop.ground.hps_uc_top")
        geometry = scene.getObject(
            ".template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1"
        )

        def corrupt_geometry(_scene):
            geometry.length = 0.0
            return 89, []

        with mock.patch.object(module, "_run_formula_patch", side_effect=corrupt_geometry):
            result = module.adjust_hardpoint(
                "hps_uc_top", 6197.6, 0.0, 1700.0, scene=scene
            )

        self.assertFalse(result.success)
        self.assertIn("更新后校验失败", result.message)
        self.assertAlmostEqual(target.location.z, 1625.6)
        self.assertAlmostEqual(geometry.length, 1.0)

    def test_incompatible_model_is_rejected_by_structure(self):
        scene = FakeScene("unrelated_model")
        module = _load_module(scene)

        result = module.adjust_hardpoint(
            "hps_uc_top", 0.0, 0.0, 1.0, scene=scene
        )

        self.assertFalse(result.success)
        self.assertIn("缺少", result.message)

    def test_dialog_uses_adm_names_and_transactional_adjuster(self):
        page_text = (TEMPLATE_DIR / "template_2_drop.py").read_text(
            encoding="utf-8"
        )
        compile(page_text, "template_2_drop.py", "exec")
        self.assertIn('hp_name_list.append("hpl_wheel_center1")', page_text)
        self.assertNotIn('hp_name_list.append("hsg_1")', page_text)
        self.assertNotIn('hp_name_list.append("hsg_2")', page_text)
        self.assertIn("QDoubleValidator", page_text)
        self.assertIn("DropAdmParameterization.adjust_hardpoint", page_text)
        self.assertNotIn("self.Parameterize.Adjust()", page_text)


if __name__ == "__main__":
    unittest.main()
