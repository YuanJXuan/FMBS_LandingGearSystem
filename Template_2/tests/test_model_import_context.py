# -*- coding: utf-8 -*-

import sys
import tempfile
import unittest
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))

import ModelImportRunner


class Settings:
    def __init__(self):
        self.values = {}
        self.sync_count = 0

    def setValue(self, key, value):
        self.values[key] = value

    def value(self, key, default=""):
        return self.values.get(key, default)

    def remove(self, key):
        self.values.pop(key, None)

    def sync(self):
        self.sync_count += 1


class ModelImportContextTests(unittest.TestCase):
    def test_selected_adm_uses_configuration_from_its_own_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            model_dir = Path(temp_dir) / "another_case"
            model_dir.mkdir(parents=True)
            adm_path = model_dir / "custom_model.adm"
            adm_path.write_text("Adams View model name: custom_model", encoding="utf-8")
            structure_path = model_dir / "custom_model_structure_parameters.json"
            structure_path.write_text('{"parameters": []}', encoding="utf-8")

            context = ModelImportRunner.build_model_context(str(adm_path))

        self.assertEqual(context["adm_path"], str(adm_path.resolve()))
        self.assertEqual(context["model_dir"], str(model_dir.resolve()))
        self.assertEqual(
            context["structure_parameter_file"],
            str(structure_path.resolve()),
        )

    def test_each_adm_resolves_only_its_own_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            first_dir = root / "first"
            second_dir = root / "second"
            first_dir.mkdir()
            second_dir.mkdir()
            first_adm = first_dir / "first.adm"
            second_adm = second_dir / "second.adm"
            first_adm.write_text("first", encoding="utf-8")
            second_adm.write_text("second", encoding="utf-8")
            first_structure = first_dir / "structure_parameters.json"
            first_structure.write_text('{"parameters": []}', encoding="utf-8")

            first_context = ModelImportRunner.build_model_context(str(first_adm))
            second_context = ModelImportRunner.build_model_context(str(second_adm))

        self.assertEqual(
            first_context["structure_parameter_file"],
            str(first_structure.resolve()),
        )
        self.assertEqual(second_context["structure_parameter_file"], "")

    def test_context_lists_tire_and_road_files_beside_adm(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            model_dir = Path(temp_dir)
            adm_path = model_dir / "case.adm"
            tire_path = model_dir / "wheel.tir"
            road_path = model_dir / "ground.rdf"
            ignored_path = model_dir / "outside.txt"
            adm_path.write_text("case", encoding="utf-8")
            tire_path.write_text("tire", encoding="utf-8")
            road_path.write_text("road", encoding="utf-8")
            ignored_path.write_text("ignored", encoding="utf-8")

            context = ModelImportRunner.build_model_context(str(adm_path))

        self.assertEqual(context["tire_files"], [str(tire_path.resolve())])
        self.assertEqual(context["road_files"], [str(road_path.resolve())])

    def test_saved_context_is_restored_for_the_same_active_scene(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            model_dir = Path(temp_dir)
            adm_path = model_dir / "case.adm"
            adm_path.write_text("case", encoding="utf-8")
            information_path = model_dir / "信息配置表.xlsx"
            information_path.write_bytes(b"configuration")
            settings = Settings()

            saved = ModelImportRunner.save_model_context(
                settings,
                str(adm_path),
                "Unknown",
            )
            restored = ModelImportRunner.restore_model_context(
                settings,
                ".Unknown",
            )

        self.assertTrue(saved)
        self.assertEqual(restored["adm_path"], str(adm_path.resolve()))
        self.assertEqual(restored["model_dir"], str(model_dir.resolve()))
        self.assertEqual(restored["model_name"], "Unknown")

    def test_generated_adm_restores_resources_from_its_source_package(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            generated_dir = root / "generated"
            resource_dir = root / "source_package"
            generated_dir.mkdir()
            resource_dir.mkdir()
            adm_path = generated_dir / "combined.adm"
            adm_path.write_text("combined", encoding="utf-8")
            structure_path = resource_dir / "source_structure_parameters.json"
            structure_path.write_text('{"parameters": []}', encoding="utf-8")
            (resource_dir / "wheel.tir").write_text("tire", encoding="utf-8")
            settings = Settings()

            saved = ModelImportRunner.save_model_context(
                settings,
                str(adm_path),
                "Combined",
                resource_dir=str(resource_dir),
            )
            restored = ModelImportRunner.restore_model_context(
                settings,
                "Combined",
            )

        self.assertTrue(saved)
        self.assertEqual(restored["adm_path"], str(adm_path.resolve()))
        self.assertEqual(restored["model_dir"], str(resource_dir.resolve()))
        self.assertEqual(
            restored["structure_parameter_file"],
            str(structure_path.resolve()),
        )
        self.assertEqual(restored["tire_files"], [str((resource_dir / "wheel.tir").resolve())])

    def test_same_unknown_name_does_not_restore_a_different_model_tree(self):
        class Proxy:
            def __init__(self, node_type):
                self.Type = node_type

        class Node:
            def __init__(self, name, node_type):
                self.Name = name
                self.Proxy = Proxy(node_type)

        class Scene:
            Name = "Unknown"

            def __init__(self, objects):
                self.Objects = objects

        first_scene = Scene([Node(".Unknown.part_a", "Part")])
        second_scene = Scene([Node(".Unknown.part_b", "Part")])
        with tempfile.TemporaryDirectory() as temp_dir:
            adm_path = Path(temp_dir) / "case.adm"
            adm_path.write_text("case", encoding="utf-8")
            settings = Settings()
            ModelImportRunner.save_model_context(
                settings,
                str(adm_path),
                "Unknown",
                ModelImportRunner.scene_signature(first_scene),
                ModelImportRunner.scene_inventory(first_scene),
            )

            restored = ModelImportRunner.restore_model_context(
                settings,
                "Unknown",
                ModelImportRunner.scene_signature(second_scene),
                ModelImportRunner.scene_inventory(second_scene),
            )

        self.assertIsNone(restored)

    def test_same_model_context_survives_additional_runtime_objects(self):
        class Proxy:
            def __init__(self, node_type):
                self.Type = node_type

        class Node:
            def __init__(self, name, node_type):
                self.Name = name
                self.Proxy = Proxy(node_type)

        class Scene:
            Name = "Unknown"

            def __init__(self, objects):
                self.Objects = objects

        original = Scene(
            [
                Node(".Unknown.ground", "Part"),
                Node(".Unknown.strut", "Part"),
                Node(".Unknown.joint", "Joint"),
            ]
        )
        after_simulation = Scene(
            original.Objects
            + [Node(".Unknown.runtime_result", "Result")]
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            adm_path = Path(temp_dir) / "case.adm"
            adm_path.write_text("case", encoding="utf-8")
            settings = Settings()
            ModelImportRunner.save_model_context(
                settings,
                str(adm_path),
                "Unknown",
                ModelImportRunner.scene_signature(original),
                ModelImportRunner.scene_inventory(original),
            )

            restored = ModelImportRunner.restore_model_context(
                settings,
                "Unknown",
                ModelImportRunner.scene_signature(after_simulation),
                ModelImportRunner.scene_inventory(after_simulation),
            )

        self.assertIsNotNone(restored)
        self.assertEqual(restored["adm_path"], str(adm_path.resolve()))

    def test_saved_context_is_not_used_for_another_active_scene(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            adm_path = Path(temp_dir) / "case.adm"
            adm_path.write_text("case", encoding="utf-8")
            settings = Settings()
            ModelImportRunner.save_model_context(
                settings,
                str(adm_path),
                "FirstModel",
            )

            restored = ModelImportRunner.restore_model_context(
                settings,
                "SecondModel",
            )

        self.assertIsNone(restored)


if __name__ == "__main__":
    unittest.main()
