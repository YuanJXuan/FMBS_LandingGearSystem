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


TEMPLATE_CASES = {
    "template_2_drop": {
        "page": "template_2_drop.py",
        "converted": 85,
        "resources": 4,
        "required_patch_text": ("measure modify function", "differential_equation"),
    },
    "template_2_retract": {
        "page": "template_2_retract.py",
        "converted": 48,
        "resources": 0,
        "required_patch_text": ("MOTION_disp", "x_force_function"),
    },
    "template_2_retract_semirocker": {
        "page": "template_2_retract_semirocker.py",
        "converted": 60,
        "resources": 0,
        "required_patch_text": (
            "MOTION_1",
            "SFORCE_1",
            "Last_Sim",
            "CYLINDER_14.length = 155.715",
        ),
    },
    "template_2_turn": {
        "page": "template_2_turn.py",
        "converted": 100,
        "resources": 4,
        "required_patch_text": ("measure modify function", "differential_equation"),
    },
    "template_4_retract": {
        "page": "template_4_cosim.py",
        "converted": 64,
        "resources": 0,
        "required_patch_text": ("x_force_function", "Last_Sim"),
    },
    "template_5_brake": {
        "page": "template_5_brake.py",
        "converted": 232,
        "resources": 8,
        "required_patch_text": ("MLG_Tb", "Last_Sim"),
    },
    "template_5_turn_force": {
        "page": "template_5_turn_force.py",
        "converted": 309,
        "resources": 8,
        "required_patch_text": ("turning_force", "differential_equation"),
    },
    "template_5_turn_motion": {
        "page": "template_5_turn_motion.py",
        "converted": 309,
        "resources": 8,
        "required_patch_text": ("angle_drive", "differential_equation"),
    },
    "template_6_force": {
        "page": "template_6_force.py",
        "converted": 176,
        "resources": 0,
        "required_patch_text": ("x_force_function", "Last_Sim"),
    },
    "template_6_motion": {
        "page": "template_6_motion.py",
        "converted": 198,
        "resources": 0,
        "required_patch_text": ("MOTION_LEFT", "x_force_function"),
    },
    "template_7_swing": {
        "page": "template_7_swing.py",
        "converted": 102,
        "resources": 4,
        "required_patch_text": ("measure modify function", "differential_equation"),
    },
}


class TemplateAdmImportTests(unittest.TestCase):
    def test_turn_and_swing_dialogs_match_parameter_workbook(self):
        expected_rows = {
            "template_2_turn.py": (
                "TURN_SIMULATION_VARIABLES",
                [
                    ("油液刚度", "stiffness_oil"),
                    ("限制力刚度", "stiffness_stop"),
                    ("空气弹簧力刚度", "stiffness_air"),
                    ("油液阻尼", "damping_oil"),
                    ("限制力阻尼", "damping_stop"),
                    ("空气弹簧力阻尼", "damping_air"),
                    ("减摆阻尼系数", "damping_coefficient"),
                    ("初始速度", "initial_vel"),
                    ("减摆阻尼力", "damping_force", True),
                    ("转弯开始时间(s)", "T_1"),
                    ("转弯结束时间(s)", "T_2"),
                    ("转弯角度(deg)", "angle"),
                ],
            ),
            "template_7_swing.py": (
                "SWING_SIMULATION_VARIABLES",
                [
                    ("油液刚度", "stiffness_oil"),
                    ("限制力刚度", "stiffness_stop"),
                    ("空气弹簧力刚度", "stiffness_air"),
                    ("油液阻尼", "damping_oil"),
                    ("限制力阻尼", "damping_stop"),
                    ("空气弹簧力阻尼", "damping_air"),
                    ("减摆阻尼系数", "damping_coefficient"),
                    ("初始速度", "initial_vel"),
                    ("减摆阻尼力", "damping_force", True),
                    ("激励力矩", "excitation_torque", True),
                    ("速度驱动", "speed_setting", True),
                    ("转弯开始时间(s)", "T_1"),
                    ("转弯结束时间(s)", "T_2"),
                    ("转弯角度(deg)", "angle"),
                ],
            ),
        }

        for page_name, (constant_name, expected) in expected_rows.items():
            with self.subTest(page=page_name):
                page_path = TEMPLATE_DIR / page_name
                page_tree = ast.parse(page_path.read_text(encoding="utf-8"))
                actual = None
                for statement in page_tree.body:
                    if (
                        isinstance(statement, ast.Assign)
                        and any(
                            isinstance(target, ast.Name)
                            and target.id == constant_name
                            for target in statement.targets
                        )
                    ):
                        actual = ast.literal_eval(statement.value)
                        break
                self.assertEqual(actual, expected)

                template_name = page_path.stem
                hps_text = (
                    TEMPLATE_DIR
                    / "Model"
                    / template_name
                    / "{}_hps.cmd".format(template_name)
                ).read_text(encoding="utf-8-sig", errors="ignore")
                hps_names = set(
                    re.findall(
                        r"variable_name\s*=\s*\.{}\.([A-Za-z0-9_]+)".format(
                            template_name
                        ),
                        hps_text,
                    )
                )
                editable_names = {
                    row[1] for row in actual if len(row) < 3 or not row[2]
                }
                self.assertTrue(editable_names.issubset(hps_names))

        table_source = (
            TEMPLATE_DIR / "Share" / "VariableInputTable.py"
        ).read_text(encoding="utf-8")
        self.assertIn("if editor.isReadOnly():", table_source)

    def test_import_keeps_one_adm_scene_then_applies_hps_overlay(self):
        events = []

        class FakeNode:
            pass

        class FakeScene:
            def __init__(self):
                self.Name = "Unknown1"
                self.Objects = []
                self.nodes = {
                    ".Unknown1.ground": FakeNode(),
                    ".Unknown1._cv_part": FakeNode(),
                    ".Unknown1.ges_dragbrace": FakeNode(),
                    ".Unknown1.ges_upper_cylinder": FakeNode(),
                    ".Unknown1.ges_lower_cylinder": FakeNode(),
                }
                self.recompute_count = 0

            def getObject(self, path):
                return self.nodes.get(path)

            def recompute(self):
                self.recompute_count += 1

        scene = FakeScene()
        jusme = types.ModuleType("Jusme")
        jusme.ActiveUSScene = None

        class FakeCMDIO:
            def import_cmd(self, cmd_fp, ref_adm_fn, py_fn):
                overlay_text = Path(cmd_fp).read_text(encoding="utf-8")
                events.append(
                    (
                        "hps_overlay",
                        Path(cmd_fp).name.endswith("_hps_import.cmd")
                        and ".Unknown1.ground." in overlay_text
                        and "model create" not in overlay_text.lower(),
                    )
                )

        class FakeADMIO:
            def import_adm(self, adm_path):
                events.append(("adm", Path(adm_path).name))
                jusme.ActiveUSScene = scene

        class FakePatch:
            @staticmethod
            def apply_patch(model_dir, model_name):
                events.append(("patch", model_name))
                return {"updated": 1, "warnings": [], "errors": []}

        fmbs = types.ModuleType("Fmbs")
        fmbs.__path__ = []
        fmbs_file = types.ModuleType("Fmbs.File")
        fmbs_file.__path__ = []
        sceneio = types.ModuleType("Fmbs.File.sceneio")
        sceneio.__path__ = []
        cmd_module = types.ModuleType("Fmbs.File.sceneio.scene_cmd_io")
        cmd_module.SceneCMDIO = FakeCMDIO
        adm_module = types.ModuleType("Fmbs.File.sceneio.scene_adm_io")
        adm_module.SceneADMIO = FakeADMIO
        fake_modules = {
            "Jusme": jusme,
            "Fmbs": fmbs,
            "Fmbs.File": fmbs_file,
            "Fmbs.File.sceneio": sceneio,
            "Fmbs.File.sceneio.scene_cmd_io": cmd_module,
            "Fmbs.File.sceneio.scene_adm_io": adm_module,
        }
        model_dir = TEMPLATE_DIR / "Model" / "template_2_drop"

        with mock.patch.dict(sys.modules, fake_modules):
            with mock.patch.object(
                ModelImportRunner,
                "_load_patch_module",
                return_value=FakePatch,
            ):
                model_name, result = ModelImportRunner.import_adm_cmd_model(
                    str(model_dir),
                    "template_2_drop",
                )

        self.assertEqual(model_name, "Unknown1")
        self.assertEqual(result["updated"], 1)
        self.assertEqual(
            events,
            [
                ("adm", "template_2_drop.adm"),
                ("hps_overlay", True),
                ("patch", "Unknown1"),
            ],
        )

    def test_drop_dialog_contains_all_design_variables_and_yellow_rows(self):
        page_path = TEMPLATE_DIR / "template_2_drop.py"
        page_tree = ast.parse(page_path.read_text(encoding="utf-8"))
        rows = None
        for statement in page_tree.body:
            if (
                isinstance(statement, ast.Assign)
                and any(
                    isinstance(target, ast.Name)
                    and target.id == "DROP_SIMULATION_VARIABLES"
                    for target in statement.targets
                )
            ):
                rows = ast.literal_eval(statement.value)
                break

        self.assertIsNotNone(rows)
        dialog_names = {row[1] for row in rows}
        yellow_names = {
            "NLG_P_HIGH",
            "NLG_V_HIGH",
            "NLG_A_HIGH",
            "NLG_RET_Cd",
            "NLG_m",
            "NLG_Ixx_Iyy",
            "NLG_Izz",
        }
        self.assertTrue(yellow_names.issubset(dialog_names))

        hps_text = (
            TEMPLATE_DIR
            / "Model"
            / "template_2_drop"
            / "template_2_drop_hps.cmd"
        ).read_text(encoding="utf-8-sig", errors="ignore")
        hps_names = set(
            re.findall(
                r"variable_name\s*=\s*\.template_2_drop\."
                r"([A-Za-z0-9_]+)\s*&",
                hps_text,
            )
        )
        self.assertEqual(dialog_names, hps_names)

    def test_cmd_converter_exposes_a_separate_patch_action(self):
        page_path = TEMPLATE_DIR / "CMDContertor.py"
        page_text = page_path.read_text(encoding="utf-8")
        compile(page_text, str(page_path), "exec")

        self.assertIn('QPushButton("生成完整 PY")', page_text)
        self.assertIn('QPushButton("生成 ADM 补丁")', page_text)
        self.assertIn("def convert_patch_file(self):", page_text)
        self.assertIn("JusmeModel_v5.convert_patch_file", page_text)
        self.assertIn('os.path.splitext(file_path)[0] + "_patch.py"', page_text)
        self.assertIn("不能选择 *_hps.cmd", page_text)

    def test_semirocker_dialog_edits_the_actual_model_functions(self):
        page_path = TEMPLATE_DIR / "template_2_retract_semirocker.py"
        page_text = page_path.read_text(encoding="utf-8")
        tree = ast.parse(page_text)
        constants = {}
        for statement in tree.body:
            if not isinstance(statement, ast.Assign):
                continue
            for target in statement.targets:
                if isinstance(target, ast.Name) and target.id in (
                    "SEMIROCKER_SIMULATION_PARAMETERS",
                    "SEMIROCKER_TRAVEL_PARAMETERS",
                ):
                    constants[target.id] = ast.literal_eval(statement.value)

        self.assertEqual(len(constants["SEMIROCKER_SIMULATION_PARAMETERS"]), 5)
        self.assertEqual(len(constants["SEMIROCKER_TRAVEL_PARAMETERS"]), 4)
        self.assertIn('_scene_object(scene, "MOTION_1")', page_text)
        self.assertIn('_scene_object(scene, "SFORCE_1")', page_text)
        self.assertIn('_scene_object(scene, "Last_Sim")', page_text)
        self.assertIn("SemiRockerAdmParameterization.adjust_hardpoint", page_text)
        self.assertIn(
            "template_2_retract_semirocker,半摇臂收放",
            (TEMPLATE_DIR / "toolbarconfig").read_text(encoding="utf-8"),
        )
        self.assertTrue(
            (TEMPLATE_DIR / "template_2_retract_semirocker.png").is_file()
        )

    def test_each_new_template_has_a_complete_import_bundle_and_ui_entry(self):
        for template_name, case in TEMPLATE_CASES.items():
            with self.subTest(template=template_name):
                model_dir = TEMPLATE_DIR / "Model" / template_name
                paths = ModelImportRunner._validate_template_files(
                    str(model_dir), template_name
                )
                self.assertTrue(all(Path(path).is_file() for path in paths.values()))
                self.assertTrue(ModelImportRunner._adm_part_probes(paths["adm"]))

                page_text = (TEMPLATE_DIR / case["page"]).read_text(encoding="utf-8")
                self.assertIn("模型生成（PY）", page_text)
                self.assertIn("模型导入（ADM）", page_text)
                self.assertIn("import ModelImportRunner", page_text)
                if template_name.startswith("template_5_"):
                    self.assertNotIn("EngineeringTemplateDialog", page_text)
                    self.assertGreater(len(page_text.splitlines()), 300)
                self.assertIn(
                    'os.path.join(Model_dir, "{}")'.format(template_name),
                    page_text,
                )

    def test_template_5_pages_expose_every_actual_design_variable(self):
        cases = {
            "template_5_brake": (
                "BRAKE_SIMULATION_VARIABLES",
                29,
            ),
            "template_5_turn_force": (
                "TURN_FORCE_SIMULATION_VARIABLES",
                35,
            ),
            "template_5_turn_motion": (
                "TURN_MOTION_SIMULATION_VARIABLES",
                35,
            ),
        }
        toolbar_text = (TEMPLATE_DIR / "toolbarconfig").read_text(encoding="utf-8")

        for template_name, (constant_name, expected_count) in cases.items():
            with self.subTest(template=template_name):
                page_path = TEMPLATE_DIR / "{}.py".format(template_name)
                tree = ast.parse(page_path.read_text(encoding="utf-8"))
                rows = None
                for statement in tree.body:
                    if (
                        isinstance(statement, ast.Assign)
                        and any(
                            isinstance(target, ast.Name)
                            and target.id == constant_name
                            for target in statement.targets
                        )
                    ):
                        rows = ast.literal_eval(statement.value)
                        break

                self.assertIsNotNone(rows)
                self.assertEqual(len(rows), expected_count)
                dialog_names = [row[1] for row in rows]
                self.assertEqual(len(dialog_names), len(set(dialog_names)))

                hps_text = (
                    TEMPLATE_DIR
                    / "Model"
                    / template_name
                    / "{}_hps.cmd".format(template_name)
                ).read_text(encoding="utf-8-sig", errors="ignore")
                hps_names = re.findall(
                    r"variable_name\s*=\s*\.{}\.([A-Za-z0-9_]+)".format(
                        template_name
                    ),
                    hps_text,
                )
                self.assertEqual(set(dialog_names), set(hps_names))
                self.assertIn(template_name + ",", toolbar_text)
                self.assertTrue((TEMPLATE_DIR / "{}.png".format(template_name)).is_file())

    def test_hps_bootstrap_files_are_named_and_contain_no_physical_creation(self):
        for template_name in TEMPLATE_CASES:
            with self.subTest(template=template_name):
                model_dir = TEMPLATE_DIR / "Model" / template_name
                hps_path = model_dir / "{}_hps.cmd".format(template_name)
                ModelImportRunner._validate_hps_source_file(
                    str(hps_path),
                    template_name,
                )
                source = hps_path.read_text(
                    encoding="utf-8-sig", errors="ignore"
                ).lower()
                self.assertIn("model create", source)
                self.assertIn("point create", source)
                self.assertNotIn("part create", source)
                self.assertNotIn("constraint create", source)

    def test_checked_in_patches_are_current_safe_and_complete(self):
        for template_name, case in TEMPLATE_CASES.items():
            with self.subTest(template=template_name):
                model_dir = TEMPLATE_DIR / "Model" / template_name
                cmd_text = (model_dir / "{}.cmd".format(template_name)).read_text(
                    encoding="utf-8", errors="ignore"
                )
                generated_text, report = JusmeModel_v5.convert_patch_text(cmd_text)
                patch_text = (
                    model_dir / "{}_patch.py".format(template_name)
                ).read_text(encoding="utf-8")

                self.assertEqual(patch_text, generated_text)
                compile(patch_text, "{}_patch.py".format(template_name), "exec")
                self.assertEqual(report.converted_blocks, case["converted"])
                self.assertEqual(report.unsupported_count, 0)
                self.assertEqual(report.deferred_count, 0)
                self.assertEqual(report.warnings, [])
                self.assertEqual(patch_text.count("if set_resource("), case["resources"])
                self.assertNotIn("MakeSceneNodeByType('Part", patch_text)
                self.assertNotIn("MakeSceneNodeByType('Joint", patch_text)
                self.assertNotIn("ude create instance", patch_text.lower())
                for required_text in case["required_patch_text"]:
                    self.assertIn(required_text, patch_text)

    def test_all_new_patches_run_and_normalize_simulation_model_names(self):
        class FakeNode:
            def __init__(self, name):
                self.Name = name
                self.location = [0.0, 0.0, 0.0]
                self.orientation = [0.0, 0.0, 0.0]
                self.string_value = ""
                self.PropertiesList = ["string_value"]

        class FakeScene:
            def __init__(self, name):
                self.Name = name
                self.nodes = {}

            def getObject(self, name):
                return self.nodes.setdefault(name, FakeNode(name))

        for template_name, case in TEMPLATE_CASES.items():
            with self.subTest(template=template_name):
                model_dir = TEMPLATE_DIR / "Model" / template_name
                patch_text = (
                    model_dir / "{}_patch.py".format(template_name)
                ).read_text(encoding="utf-8")
                scene = FakeScene(template_name)

                jusme = types.ModuleType("Jusme")
                jusme.ActiveUSScene = scene
                vec_utils = types.ModuleType("FmbsShortcut.SCcmd.utils.VecUtils")
                vec_names = set(re.findall(r"VecUtils\.([A-Za-z_][A-Za-z0-9_]*)", patch_text))
                for name in vec_names:
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
                    exec(
                        compile(
                            patch_text,
                            "{}_patch.py".format(template_name),
                            "exec",
                        ),
                        namespace,
                    )
                    result = namespace["apply_patch"](
                        str(model_dir), template_name
                    )

                self.assertEqual(result["errors"], [])
                self.assertEqual(result["warnings"], [])
                self.assertEqual(
                    result["updated"], case["converted"] + case["resources"]
                )
                scripts = [
                    node.commands
                    for node in scene.nodes.values()
                    if getattr(node, "commands", "")
                ]
                self.assertTrue(scripts)
                for command in scripts:
                    self.assertIn("model_name=.{}".format(template_name), command)


if __name__ == "__main__":
    unittest.main()
