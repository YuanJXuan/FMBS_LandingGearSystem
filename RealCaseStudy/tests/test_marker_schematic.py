# -*- coding: utf-8 -*-
import copy
import ast
import json
import shutil
import sys
import tempfile
import types
import unittest
from unittest.mock import Mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Share"))
import InformationConfiguration
import MarkerSchematic as schematic


class MarkerSchematicTests(unittest.TestCase):
    case_model = "template_nlg_drop"

    def setUp(self):
        self.folder = ROOT / "Model" / self.case_model
        self.data = schematic.load_schematic(str(self.folder))
        entries = InformationConfiguration.load_information_configuration(str(self.folder))["markers"]
        self.items = [dict(configuration_entry=e, path=e["target"], display=e["label"], node=object()) for e in entries]

    def test_all_fourteen_points_match_workbook_even_after_reordering(self):
        items = list(reversed(self.items))
        matched = schematic.match_markers(self.data["markers"], items)
        self.assertEqual(len(self.items), len(matched))
        for marker in matched:
            self.assertTrue(marker["available"])
            self.assertEqual(marker["target"], items[marker["index"] - 1]["configuration_entry"]["target"])

    def test_renamed_model_and_flattened_runtime_path_use_configured_part(self):
        for item in self.items:
            item["configuration_entry"] = dict(item["configuration_entry"])
            item["configuration_entry"]["target"] = item["configuration_entry"]["target"].replace(self.case_model, "imported_copy")
            item["path"] = ".imported_copy.flattened_runtime_name"
        self.assertTrue(all(m["available"] for m in schematic.match_markers(self.data["markers"], self.items)))
        self.items[0]["configuration_entry"]["target"] = ".imported_copy.other_part.MARKER_K2"
        self.assertFalse(schematic.match_markers(self.data["markers"], self.items)[0]["available"])

    def test_missing_and_duplicate_targets_are_not_clickable(self):
        self.items[0]["node"] = None
        self.items.append(dict(self.items[1]))
        matched = schematic.match_markers(self.data["markers"], self.items)
        self.assertFalse(matched[0]["available"])
        self.assertIn("未找到", matched[0]["reason"])
        self.assertFalse(matched[1]["available"])
        self.assertEqual(0, matched[1]["index"])

    def test_other_cases_do_not_inherit_supported_schematics(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertIsNone(schematic.load_schematic(folder))
        self.assertIsNone(schematic.load_schematic(str(ROOT / "Model")))

    def test_case_identity_and_title_follow_its_own_resources(self):
        self.assertEqual(self.case_model, self.data["model"])
        self.assertEqual(schematic.SCHEMATIC_MODELS[self.case_model], self.data["title"])
        self.assertTrue(all(m["target"].startswith("." + self.case_model + ".") for m in self.data["markers"]))
        self.assertEqual(self.folder.resolve(), Path(self.data["image_path"]).parent)

    def test_copy_to_renamed_directory_and_ambiguous_configuration(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            filename = schematic.SCHEMATIC_FILES[self.case_model]
            shutil.copyfile(self.folder / filename, folder / filename)
            shutil.copyfile(self.data["image_path"], folder / self.data["image"])
            self.assertEqual(self.case_model, schematic.load_schematic(temp)["model"])
            other_file = next(name for model, name in schematic.SCHEMATIC_FILES.items() if model != self.case_model)
            (folder / other_file).write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "多套示意图"):
                schematic.load_schematic(temp)

    def test_point_and_badge_hit_testing_survives_resize_and_letterboxing(self):
        for size in ((240, 500), (360, 300), (1050, 790), (1448, 1086)):
            rect = schematic.fit_rect(self.data["image_size"], size)
            self.assertAlmostEqual(self.data["image_size"][0] / self.data["image_size"][1], rect[2] / rect[3])
            for marker in self.data["markers"]:
                for key in ("point_normalized", "badge_normalized"):
                    pos = schematic.screen_position(marker[key], rect)
                    hits = schematic.hit_candidates(pos, self.data["markers"], rect)
                    self.assertEqual(marker["number"], hits[0]["number"])
            self.assertEqual([], schematic.hit_candidates((0, 0), self.data["markers"], rect))

    def test_overlapping_targets_return_choices_without_duplicate_point_and_badge(self):
        markers = [dict(number=str(i), point_normalized=[.5,.5], badge_normalized=[.5,.5]) for i in (1,2)]
        self.assertEqual(2, len(schematic.hit_candidates((50,50), markers, (0,0,100,100))))
        self.assertEqual([], schematic.hit_candidates((0,0), markers, (0,0,0,0)))

    def test_invalid_metadata_fails_without_escaping_model_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            (folder / "image.png").write_bytes(b"placeholder")
            for mutation in ("outside", "duplicate", "nan", "wrong_model"):
                data = copy.deepcopy(self.data)
                data["image"] = "image.png"
                if mutation == "outside":
                    data["image"] = "../image.png"
                elif mutation == "duplicate":
                    data["markers"][1]["number"] = "01"
                elif mutation == "nan":
                    data["markers"][0]["point_normalized"][0] = float("nan")
                else:
                    data["model"] = "unsupported_model"
                (folder / schematic.SCHEMATIC_FILES[self.case_model]).write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaises(ValueError, msg=mutation):
                    schematic.load_schematic(str(folder))


class RetractMarkerSchematicTests(MarkerSchematicTests):
    case_model = "template_nlg_retract"


class SchematicSelectionTests(unittest.TestCase):
    """Exercise the production selection handlers without pretending to render Qt."""

    case_model = "template_nlg_drop"

    def setUp(self):
        data = schematic.load_schematic(str(ROOT / "Model" / self.case_model))
        entries = InformationConfiguration.load_information_configuration(
            str(ROOT / "Model" / self.case_model)
        )["markers"]
        self.nodes = {entry["target"]: object() for entry in entries}
        scene = types.SimpleNamespace(getObject=lambda path: self.nodes.get(path))
        namespace = {
            "MarkerSchematic": schematic,
            "SelectionMonitor": types.SimpleNamespace(get_active_scene=lambda: scene),
            "StructuralParameterization": types.SimpleNamespace(
                resolve_object=lambda scene, path: (path, scene.getObject(path))
            ),
        }
        names = {"_selectSchematicMarker", "_syncMarkerSchematic", "markerSelectorChanged"}
        tree = ast.parse((ROOT / "Share/DedicatedCaseDialog.py").read_text(encoding="utf-8-sig"))
        methods = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name in names]
        exec(compile(ast.Module(body=methods, type_ignores=[]), "DedicatedCaseDialog.py", "exec"), namespace)
        self.dialog = types.SimpleNamespace(
            schematicData=data,
            markerItems=[dict(configuration_entry=e, path=e["target"], display=e["label"],
                              node=self.nodes[e["target"]]) for e in entries],
            tabs=Mock(), hpStatusLabel=Mock(), markOkButton=Mock(), markerSchematicPanel=Mock(),
            _selectedStructureParameter=lambda: None,
        )
        for name in names:
            setattr(self.dialog, name, types.MethodType(namespace[name], self.dialog))

        class Field:
            value = ""
            enabled = True
            def setText(self, text): self.value = text
            def clear(self): self.value = ""
            def setEnabled(self, enabled): self.enabled = enabled

        class Selector:
            index = 0
            enabled = True
            def currentIndex(self): return self.index
            def isEnabled(self): return self.enabled
            def setCurrentIndex(selector, index):
                selector.index = index
                self.dialog.markerSelectorChanged(index)

        self.dialog.hpSelector = Selector()
        for name in ("hpName", "xMarker", "yMarker", "zMarker"):
            setattr(self.dialog, name, Field())

    def test_every_diagram_selection_updates_path_coordinates_and_highlight(self):
        for index, marker in enumerate(self.dialog.schematicData["markers"], 1):
            self.dialog._selectSchematicMarker(marker["number"])
            self.assertEqual(index, self.dialog.hpSelector.index)
            self.assertEqual(marker["target"], self.dialog.hpName.value)
            self.assertEqual(tuple(marker["configuration_world_coordinates_mm"]), tuple(
                float(getattr(self.dialog, axis + "Marker").value) for axis in "xyz"
            ))
            self.assertEqual(marker["number"], self.dialog.markerSchematicPanel.set_markers.call_args[0][1])

    def test_repeated_selection_keeps_unsubmitted_edits(self):
        self.dialog._selectSchematicMarker("01")
        self.dialog.xMarker.setText("999")
        self.dialog._selectSchematicMarker("01")
        self.assertEqual("999", self.dialog.xMarker.value)

    def test_locked_mode_or_removed_node_cannot_select_another_point(self):
        self.dialog._selectSchematicMarker("02")
        self.dialog.hpSelector.enabled = False
        self.dialog._selectSchematicMarker("01")
        self.assertEqual(2, self.dialog.hpSelector.index)
        self.dialog.hpSelector.enabled = True
        self.nodes.pop(self.dialog.markerItems[0]["path"])
        self.dialog._selectSchematicMarker("01")
        self.assertEqual(2, self.dialog.hpSelector.index)
        markers = self.dialog.markerSchematicPanel.set_markers.call_args[0][0]
        self.assertFalse(markers[0]["available"])

    def test_placeholder_clears_coordinates_and_highlight(self):
        self.dialog._selectSchematicMarker("01")
        self.dialog.hpSelector.setCurrentIndex(0)
        self.assertEqual("", self.dialog.xMarker.value)
        self.assertFalse(self.dialog.xMarker.enabled)
        self.assertEqual("", self.dialog.markerSchematicPanel.set_markers.call_args[0][1])


class RetractSchematicSelectionTests(SchematicSelectionTests):
    case_model = "template_nlg_retract"


for _case in ("template_nlg_turn", "template_mlg_drop", "template_full_drop", "template_full_brake"):
    for _base in (MarkerSchematicTests, SchematicSelectionTests):
        _name = _case + _base.__name__
        globals()[_name] = type(_name, (_base,), {"case_model": _case})
del _base, _case, _name


if __name__ == "__main__":
    unittest.main()
