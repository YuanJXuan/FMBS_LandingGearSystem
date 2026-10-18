# -*- coding: utf-8 -*-

import importlib.util
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
SHARED_MODULE = TEMPLATE_DIR / "Share" / "AdmHardpointParameterization.py"


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class FakeNode:
    def __init__(self, name, location=None):
        self.Name = name
        self.location = location or Vector(0, 0, 0)
        self.orientation = Vector(0, 0, 0)
        self.length = 1.0
        self.radius = 1.0
        self.recompute_count = 0

    def recompute(self):
        self.recompute_count += 1


class FakeScene:
    def __init__(self, name="Unknown1"):
        self.Name = name
        self.nodes = {}
        self.recompute_count = 0

    def add(self, path, location=None):
        node = FakeNode(path, location)
        self.nodes[path] = node
        return node

    def getObject(self, path):
        return self.nodes.get(path)

    def recompute(self):
        self.recompute_count += 1


def _load_shared(scene):
    jusme = types.ModuleType("Jusme")
    jusme.Vector = Vector
    jusme.ActiveUSScene = scene
    with mock.patch.dict(sys.modules, {"Jusme": jusme}):
        spec = importlib.util.spec_from_file_location(
            "adm_hardpoint_parameterization_under_test", SHARED_MODULE
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


class FakeAdjustor:
    def __init__(self, scene, full_path, fail=False):
        self.scene = scene
        self.full_path = full_path
        self.fail = fail

    def Adjust(self):
        model_name = self.scene.Name
        target = self.scene.getObject(self.full_path)
        part = self.scene.getObject(".{}.part".format(model_name))
        part.location = Vector(target.location.x, 0, target.location.z)
        if self.fail:
            raise RuntimeError("simulated adjustor failure")


class AdmHardpointParameterizationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.model_folder = Path(self.temp_dir.name)
        (self.model_folder / "sample_patch.py").write_text(
            "def apply_patch(model_dir=None, model_name=None):\n"
            "    return {'updated': 1, 'errors': [], 'warnings': []}\n",
            encoding="utf-8",
        )
        (self.model_folder / "sample.cmd").write_text(
            "constraint create joint revolute &\n"
            "  joint_name = .sample.joint_1\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def _scene(self, name="Unknown1"):
        scene = FakeScene(name)
        root = "." + name
        scene.add(root + ".ground.upper", Vector(0, 0, 10))
        scene.add(root + ".ground.lower", Vector(0, 0, 0))
        scene.add(root + ".part", Vector(1, 2, 3))
        scene.add(root + ".joint_1")
        return scene

    def _contract(self, module, scene, fail=False):
        return module.TemplateContract(
            model_name="sample",
            model_folder=str(self.model_folder),
            hardpoint_rules={"upper": ("z",)},
            adjust_factory=lambda path: FakeAdjustor(scene, path, fail),
            core_hardpoints=("upper", "lower"),
            required_paths=("part",),
            length_pairs=(("upper", "lower", "test member"),),
            vertical_pairs=(("upper", "lower", "test member"),),
            label="Sample",
        )

    def test_actual_adm_scene_name_and_connector_recompute_are_supported(self):
        scene = self._scene("Unknown1")
        module = _load_shared(scene)
        contract = self._contract(module, scene)

        with mock.patch.object(module, "_run_formula_patch", return_value=(8, [])):
            result = module.adjust_hardpoint(
                contract, "upper", 0, 0, 12, scene=scene
            )

        self.assertTrue(result.success, result.message)
        self.assertEqual(
            module.hardpoint_path(contract, "upper", scene),
            ".Unknown1.ground.upper",
        )
        self.assertEqual(scene.getObject(".Unknown1.joint_1").recompute_count, 1)
        self.assertEqual(scene.getObject(".Unknown1.part").location.z, 12)

    def test_locked_axis_is_rejected_before_model_mutation(self):
        scene = self._scene()
        module = _load_shared(scene)
        contract = self._contract(module, scene)

        result = module.adjust_hardpoint(
            contract, "upper", 1, 0, 12, scene=scene
        )

        self.assertFalse(result.success)
        self.assertEqual(scene.getObject(".Unknown1.ground.upper").location.z, 10)
        self.assertEqual(scene.recompute_count, 0)

    def test_adjustor_failure_restores_hardpoint_and_dependent_part(self):
        scene = self._scene()
        module = _load_shared(scene)
        contract = self._contract(module, scene, fail=True)

        result = module.adjust_hardpoint(
            contract, "upper", 0, 0, 12, scene=scene
        )

        self.assertFalse(result.success)
        self.assertIn("已恢复", result.message)
        self.assertEqual(scene.getObject(".Unknown1.ground.upper").location.z, 10)
        part = scene.getObject(".Unknown1.part")
        self.assertEqual((part.location.x, part.location.y, part.location.z), (1, 2, 3))

    def test_missing_adjustor_dependency_is_rejected_before_mutation(self):
        scene = self._scene()
        scene.nodes.pop(".Unknown1.part")
        module = _load_shared(scene)
        contract = module.TemplateContract(
            model_name="sample",
            model_folder=str(self.model_folder),
            hardpoint_rules={"upper": ("z",)},
            adjust_factory=lambda path: FakeAdjustor(scene, path),
            core_hardpoints=("upper", "lower"),
            length_pairs=(("upper", "lower", "test member"),),
            vertical_pairs=(("upper", "lower", "test member"),),
            label="Sample",
        )

        result = module.adjust_hardpoint(
            contract, "upper", 0, 0, 12, scene=scene
        )

        self.assertFalse(result.success)
        self.assertIn("联动结构不完整", result.message)
        self.assertEqual(scene.getObject(".Unknown1.ground.upper").location.z, 10)
        self.assertEqual(scene.recompute_count, 0)

    def test_self_contained_structure_updater_does_not_need_legacy_factory(self):
        scene = self._scene()
        module = _load_shared(scene)

        def update_structure(active_scene, points, changed_name):
            self.assertEqual(changed_name, "upper")
            part = active_scene.getObject(".Unknown1.part")
            part.location = Vector(points["upper"].x, 0, points["upper"].z)

        contract = module.TemplateContract(
            model_name="sample",
            model_folder=str(self.model_folder),
            hardpoint_rules={"upper": ("z",)},
            core_hardpoints=("upper", "lower"),
            required_paths=("part",),
            length_pairs=(("upper", "lower", "test member"),),
            vertical_pairs=(("upper", "lower", "test member"),),
            structure_updater=update_structure,
            label="Sample",
        )

        with mock.patch.object(module, "_run_formula_patch", return_value=(3, [])):
            result = module.adjust_hardpoint(
                contract, "upper", 0, 0, 12, scene=scene
            )

        self.assertTrue(result.success, result.message)
        self.assertEqual(scene.getObject(".Unknown1.part").location.z, 12)

    def test_self_contained_updater_failure_rolls_back_all_direct_changes(self):
        scene = self._scene()
        module = _load_shared(scene)

        def failing_update(active_scene, points, changed_name):
            del points, changed_name
            active_scene.getObject(".Unknown1.part").location = Vector(9, 9, 9)
            raise RuntimeError("simulated topology failure")

        contract = module.TemplateContract(
            model_name="sample",
            model_folder=str(self.model_folder),
            hardpoint_rules={"upper": ("z",)},
            core_hardpoints=("upper", "lower"),
            required_paths=("part",),
            length_pairs=(("upper", "lower", "test member"),),
            vertical_pairs=(("upper", "lower", "test member"),),
            structure_updater=failing_update,
            label="Sample",
        )

        result = module.adjust_hardpoint(
            contract, "upper", 0, 0, 12, scene=scene
        )

        self.assertFalse(result.success)
        self.assertEqual(scene.getObject(".Unknown1.ground.upper").location.z, 10)
        part = scene.getObject(".Unknown1.part")
        self.assertEqual((part.location.x, part.location.y, part.location.z), (1, 2, 3))

    def test_template_pages_use_transactional_adm_entry_points(self):
        pages = {
            "template_2_turn.py": "TurnAdmParameterization",
            "template_7_swing.py": "SwingAdmParameterization",
            "template_2_retract.py": "RetractionAdmParameterization",
            "template_2_retract_semirocker.py": "SemiRockerAdmParameterization",
        }
        for file_name, module_name in pages.items():
            with self.subTest(page=file_name):
                page_text = (TEMPLATE_DIR / file_name).read_text(encoding="utf-8")
                compile(page_text, file_name, "exec")
                self.assertIn(module_name + ".adjust_hardpoint", page_text)
                self.assertIn("QDoubleValidator", page_text)
                self.assertIn("hpStatusLabel", page_text)
                self.assertNotIn("self.Parameterize.Adjust()", page_text)

        retract_text = (TEMPLATE_DIR / "template_2_retract.py").read_text(
            encoding="utf-8"
        )
        self.assertIn('"hps_rod_top"', retract_text)
        self.assertIn('"hps_rod_bot"', retract_text)
        self.assertIn("self.hpSelector.currentTextChanged", retract_text)
        self.assertNotIn('hp_name_list.append("hps_rod_top")', retract_text)
        self.assertNotIn("RetractAdjustFactory", retract_text)

        swing_text = (TEMPLATE_DIR / "template_7_swing.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("self.view.mySignal.connect(self.mouseEventSlot)", swing_text)
        self.assertIn('hp_name_list.append("hps_db_sf_atch")', swing_text)

        topology_modules = (
            TEMPLATE_DIR / "Turn" / "TurnAdmParameterization.py",
            TEMPLATE_DIR / "Swing" / "SwingAdmParameterization.py",
            TEMPLATE_DIR / "Retraction" / "RetractionAdmParameterization.py",
            TEMPLATE_DIR / "Retraction" / "SemiRockerAdmParameterization.py",
        )
        for module_path in topology_modules:
            with self.subTest(topology_module=module_path.name):
                module_text = module_path.read_text(encoding="utf-8")
                compile(module_text, module_path.name, "exec")
                self.assertIn("structure_updater=_update_structure", module_text)
                self.assertNotIn("Factory", module_text)
                self.assertNotIn(".Adjust()", module_text)


if __name__ == "__main__":
    unittest.main()
