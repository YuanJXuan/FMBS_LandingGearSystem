# -*- coding: utf-8 -*-

import ast
import re
import sys
import types
import unittest
from pathlib import Path
from unittest import mock


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))
sys.path.insert(0, str(TEMPLATE_DIR / "CMDToPy"))

import JusmeModel_v5
import ModelImportRunner


class BrakeAdmImportTests(unittest.TestCase):
    def test_patch_converter_accepts_model_unit_cylinder_radius(self):
        source = """!
model create &
   model_name = radius_units
!
geometry modify shape cylinder &
   cylinder_name = .radius_units.part.CYLINDER_1 &
   radius = (2.2E-02meter)
!
"""
        patch_text, report = JusmeModel_v5.convert_patch_text(source)

        self.assertEqual(report.warnings, [])
        self.assertIn("CYLINDER_1.radius = 0.022", patch_text)

    def test_patch_resolves_adm_flattened_road_and_tire_ude_paths(self):
        source = """!
model create &
   model_name = sample
!
ude create instance &
   instance_name = .sample.lm &
   definition_name = .MDI.Forces.vpg_road &
   location = 1, 2, 3
!
ude create instance &
   instance_name = .sample.lt_l &
   definition_name = .MDI.Forces.vpg_tire &
   location = 4, 5, 6
!
marker modify &
   marker_name = .sample.ground.lm_ref_1 &
   location = (.sample.lm.location) &
   orientation = (.sample.lm.orientation)
!
marker modify &
   marker_name = .sample.lt_l.wheel_part.MARKER_1 &
   location = (LOC_RELATIVE_TO({0, 0, 0}, .sample.ground.wheel_point)) &
   relative_to = .sample.lt_l.wheel_part
!
"""
        patch_text, report = JusmeModel_v5.convert_patch_text(source)
        self.assertEqual(report.converted_blocks, 2)
        self.assertIn("'lm': 'road'", patch_text)
        self.assertIn("'lt_l': 'tire'", patch_text)

        class FakeNode:
            def __init__(self, name, location=None, orientation=None):
                self.Name = name
                self.location = location or [0.0, 0.0, 0.0]
                self.orientation = orientation or [0.0, 0.0, 0.0]

        class FakeScene:
            Name = "Unknown"

            def __init__(self):
                self.nodes = {}

            def add(self, name, location=None, orientation=None):
                node = FakeNode(name, location, orientation)
                self.nodes[name] = node
                return node

            def getObject(self, name):
                return self.nodes.get(name)

        scene = FakeScene()
        road_ref = scene.add(".Unknown.ground.lm_ref_1")
        scene.add(
            ".Unknown.lm_road_part",
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
        )
        scene.add(".Unknown.ground.wheel_point", [7.0, 8.0, 9.0])
        scene.add(".Unknown.lt_l_wheel_part")
        wheel_marker = scene.add(".Unknown.lt_l_wheel_part.MARKER_1")

        jusme = types.ModuleType("Jusme")
        jusme.ActiveUSScene = scene
        vec_utils = types.ModuleType("FmbsShortcut.SCcmd.utils.VecUtils")
        vec_utils.LOC_RELATIVE_TO = lambda offset, node: list(node.location)
        vec_utils.global2local = lambda *args: (args[2], args[3])
        fmbs = types.ModuleType("Fmbs")
        fmbs.__path__ = []
        import_all_node = types.ModuleType("Fmbs.import_all_node")
        import_all_node.MakeSceneNodeByType = lambda node_type, name: None
        shortcut = types.ModuleType("FmbsShortcut")
        shortcut.__path__ = []
        sccmd = types.ModuleType("FmbsShortcut.SCcmd")
        sccmd.__path__ = []
        utils = types.ModuleType("FmbsShortcut.SCcmd.utils")
        utils.__path__ = []
        fake_modules = {
            "Jusme": jusme,
            "Fmbs": fmbs,
            "Fmbs.import_all_node": import_all_node,
            "FmbsShortcut": shortcut,
            "FmbsShortcut.SCcmd": sccmd,
            "FmbsShortcut.SCcmd.utils": utils,
            "FmbsShortcut.SCcmd.utils.VecUtils": vec_utils,
        }
        namespace = {}
        with mock.patch.dict(sys.modules, fake_modules):
            exec(compile(patch_text, "flattened_ude_patch.py", "exec"), namespace)
            result = namespace["apply_patch"](model_name="Unknown")

        self.assertEqual(result["errors"], [])
        self.assertEqual(road_ref.location, [1.0, 2.0, 3.0])
        self.assertEqual(road_ref.orientation, [4.0, 5.0, 6.0])
        self.assertEqual(tuple(wheel_marker.location), (7.0, 8.0, 9.0))

    def setUp(self):
        self.model_dir = TEMPLATE_DIR / "Model" / "template_2_brake"

    def test_hps_bootstrap_is_safe_and_complete(self):
        hps_path = self.model_dir / "template_2_brake_hps.cmd"
        ModelImportRunner._validate_hps_source_file(
            str(hps_path),
            "template_2_brake",
        )
        source = hps_path.read_text(
            encoding="utf-8-sig"
        ).lower()

        self.assertEqual(source.count("point create"), 18)
        self.assertEqual(source.count("variable create"), 20)
        self.assertEqual(source.count("model create"), 1)
        self.assertNotIn("part create", source)
        self.assertNotIn("constraint create", source)

    def test_brake_dialog_lists_every_hps_design_variable(self):
        hps_text = (self.model_dir / "template_2_brake_hps.cmd").read_text(
            encoding="utf-8-sig"
        )
        hps_names = re.findall(
            r"variable_name\s*=\s*\.template_2_brake\.([A-Za-z0-9_]+)",
            hps_text,
        )

        dialog_tree = ast.parse(
            (TEMPLATE_DIR / "template_2_brake.py").read_text(encoding="utf-8")
        )
        rows = None
        for statement in dialog_tree.body:
            if (
                isinstance(statement, ast.Assign)
                and any(
                    isinstance(target, ast.Name)
                    and target.id == "BRAKE_DESIGN_VARIABLES"
                    for target in statement.targets
                )
            ):
                rows = ast.literal_eval(statement.value)
                break

        self.assertIsNotNone(rows)
        self.assertEqual([variable_name for _meaning, variable_name in rows], hps_names)

    def test_patch_mode_is_safe_and_complete_for_brake_reference(self):
        source = (self.model_dir / "template_2_brake.cmd").read_text(
            encoding="utf-8",
            errors="ignore",
        )
        patch_text, report = JusmeModel_v5.convert_patch_text(source)

        compile(patch_text, "template_2_brake_patch.py", "exec")
        self.assertEqual(report.converted_blocks, 86)
        self.assertEqual(report.unsupported_count, 0)
        self.assertEqual(report.deferred_count, 0)
        self.assertNotIn("MakeSceneNodeByType('Part", patch_text)
        self.assertNotIn("MakeSceneNodeByType('Joint", patch_text)
        self.assertNotIn("ude create instance", patch_text.lower())
        self.assertNotIn("VecUtils.ORI_LOCAL", patch_text)
        self.assertNotIn("VecUtils.ORI_ALIGN_AXIS", patch_text)
        self.assertIn(
            "jxl_joint_j_14.orientation = "
            "_template_2_brake_ground_cfl_plane_ref_2.orientation",
            patch_text,
        )
        self.assertIn("VecUtils.global2local", patch_text)
        self.assertNotIn(".global_loc", patch_text)
        self.assertIn("MLG.tir", patch_text)
        self.assertIn("2d_flat.rdf", patch_text)

    def test_generated_patch_runs_with_the_expected_platform_contract(self):
        source = (self.model_dir / "template_2_brake.cmd").read_text(
            encoding="utf-8",
            errors="ignore",
        )
        patch_text, _ = JusmeModel_v5.convert_patch_text(source)

        class FakeNode:
            def __init__(self, name):
                self.Name = name
                self.location = [0.0, 0.0, 0.0]
                self.orientation = [0.0, 0.0, 0.0]
                self.string_value = ""
                self.PropertiesList = ["string_value"]

            def __setattr__(self, key, value):
                if (
                    key == "function"
                    and getattr(self, "Name", "").endswith(".MLG_Vw")
                ):
                    raise RuntimeError("expected patch-step failure")
                object.__setattr__(self, key, value)

        class FakeScene:
            Name = "template_2_brake"

            def __init__(self):
                self.nodes = {}

            def getObject(self, name):
                return self.nodes.setdefault(name, FakeNode(name))

        scene = FakeScene()
        jusme = types.ModuleType("Jusme")
        jusme.ActiveUSScene = scene

        vec_utils = types.ModuleType("FmbsShortcut.SCcmd.utils.VecUtils")
        for name in (
            "LOC_RELATIVE_TO",
            "LOC_ALONG_LINE",
            "ORI_RELATIVE_TO",
            "ORI_ALONG_AXIS",
            "ORI_IN_PLANE",
        ):
            setattr(vec_utils, name, lambda *args: [0.0, 0.0, 0.0])
        vec_utils.DM = lambda *args: 1.0
        vec_utils.global2local = lambda *args: (
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        )

        fmbs = types.ModuleType("Fmbs")
        fmbs.__path__ = []
        import_all_node = types.ModuleType("Fmbs.import_all_node")
        import_all_node.MakeSceneNodeByType = (
            lambda node_type, name: scene.getObject(name)
        )
        shortcut = types.ModuleType("FmbsShortcut")
        shortcut.__path__ = []
        sccmd = types.ModuleType("FmbsShortcut.SCcmd")
        sccmd.__path__ = []
        utils = types.ModuleType("FmbsShortcut.SCcmd.utils")
        utils.__path__ = []

        fake_modules = {
            "Jusme": jusme,
            "Fmbs": fmbs,
            "Fmbs.import_all_node": import_all_node,
            "FmbsShortcut": shortcut,
            "FmbsShortcut.SCcmd": sccmd,
            "FmbsShortcut.SCcmd.utils": utils,
            "FmbsShortcut.SCcmd.utils.VecUtils": vec_utils,
        }
        namespace = {}
        with mock.patch.dict(sys.modules, fake_modules):
            exec(compile(patch_text, "template_2_brake_patch.py", "exec"), namespace)
            result = namespace["apply_patch"](
                str(self.model_dir),
                "template_2_brake",
            )

        self.assertEqual(result["updated"], 87)
        self.assertEqual(result["warnings"], [])
        self.assertEqual(len(result["errors"]), 1)
        self.assertIn("MLG_Vw", result["errors"][0]["step"])
        self.assertTrue(hasattr(scene.getObject(".template_2_brake.thrust"), "function"))


if __name__ == "__main__":
    unittest.main()
