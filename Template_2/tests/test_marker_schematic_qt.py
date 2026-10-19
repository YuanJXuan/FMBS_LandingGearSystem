# -*- coding: utf-8 -*-
"""Real Qt interaction checks. Skip on hosts without PySide2 (no widget stubs)."""
import os
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Share"))
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
try:
    from PySide2.QtCore import QPoint, Qt
    from PySide2.QtTest import QTest
    from PySide2.QtWidgets import QApplication
    import MarkerSchematic
    import MarkerSchematicWidget
    QT_AVAILABLE = True
except ImportError:
    QT_AVAILABLE = False


@unittest.skipUnless(QT_AVAILABLE, "PySide2 is not installed")
class MarkerSchematicQtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        # Only the external engineering host is replaced; every widget is real Qt.
        with patch.dict(sys.modules, {name: types.ModuleType(name) for name in ("Jusme", "JusmeGui")}):
            import DedicatedCaseDialog
        cls.module = DedicatedCaseDialog

    def setUp(self):
        module = self.module
        class PreviewDialog(module.DedicatedCaseDialog):
            def _restoreSavedModelContext(self):
                return False
            def refreshVariableTables(self):
                pass
            def refreshPostprocessingConfiguration(self, clear_curve=False):
                pass
        self.nodes = {}
        scene = types.SimpleNamespace(Name="template_nlg_drop", getObject=lambda path: self.nodes.get(path))
        self.scene_patch = patch.object(module.SelectionMonitor, "get_active_scene", return_value=scene)
        self.scene_patch.start()
        self.addCleanup(self.scene_patch.stop)
        with patch.object(module.SelectionMonitor.SelectionMonitor, "start"), patch.object(
            module.StructuralParameterization, "available_parameters", return_value=([], [])
        ):
            self.dialog = PreviewDialog({"model_dir": str(ROOT / "Model/template_nlg_drop")})
            for entry in self.dialog.informationConfiguration["markers"]:
                self.nodes[entry["target"]] = object()
            self.dialog.refreshMarkerList()
        self.dialog.show()
        self.app.processEvents()

    def tearDown(self):
        self.dialog.close()
        self.dialog.deleteLater()
        self.app.processEvents()

    def test_all_fourteen_badges_select_correct_marker_and_coordinates(self):
        self.dialog.markerSchematicPanel.open_enlarged()
        self.app.processEvents()
        view = self.dialog.markerSchematicPanel._large_view
        for marker in view.markers:
            point = MarkerSchematic.screen_position(marker["badge_normalized"], view.image_rect())
            QTest.mouseClick(view, Qt.LeftButton, pos=QPoint(round(point[0]), round(point[1])))
            self.assertEqual(marker["index"], self.dialog.hpSelector.currentIndex())
            self.assertEqual(marker["target"], self.dialog.hpName.text())
            entry = self.dialog.markerItems[marker["index"] - 1]["configuration_entry"]
            self.assertEqual(tuple(entry["coordinates"]), tuple(float(e.text()) for e in (
                self.dialog.xMarker, self.dialog.yMarker, self.dialog.zMarker)))
            self.assertEqual(marker["number"], self.dialog.markerSchematicPanel.view.selected)

    def test_dropdown_highlight_and_repeat_click_preserve_unsaved_input(self):
        self.dialog.hpSelector.setCurrentIndex(2)
        self.assertEqual("02", self.dialog.markerSchematicPanel.view.selected)
        self.dialog.xMarker.setText("123.45")
        self.dialog._selectSchematicMarker("02")
        self.assertEqual("123.45", self.dialog.xMarker.text())
        self.dialog.hpSelector.setCurrentIndex(0)
        self.assertEqual("", self.dialog.markerSchematicPanel.view.selected)
        self.assertFalse(self.dialog.markOkButton.isEnabled())

    def test_model_missing_or_locked_point_does_not_change_selection(self):
        self.dialog.hpSelector.setCurrentIndex(2)
        self.dialog.hpSelector.setEnabled(False)
        self.dialog._syncMarkerSchematic()
        self.dialog._selectSchematicMarker("01")
        self.assertEqual(2, self.dialog.hpSelector.currentIndex())
        self.assertTrue(self.dialog.markerSchematicPanel.view.locked)
        self.dialog.hpSelector.setEnabled(True)
        self.nodes.pop(self.dialog.markerItems[0]["path"])
        self.dialog._selectSchematicMarker("01")
        self.assertEqual(2, self.dialog.hpSelector.currentIndex())
        self.assertFalse(self.dialog.markerSchematicPanel.view.markers[0]["available"])

    def test_minimum_window_and_collapse_keep_forms_horizontal(self):
        self.dialog.resize(1250, 660)
        self.app.processEvents()
        self.assertLessEqual(self.dialog.width(), 1250)
        self.assertLessEqual(self.dialog.height(), 660)
        self.assertLess(self.dialog.markOkButton.mapTo(self.dialog, QPoint()).x(),
                        self.dialog.dimensionOkButton.mapTo(self.dialog, QPoint()).x())
        self.assertEqual(self.dialog.markOkButton.mapTo(self.dialog, QPoint()).y(),
                         self.dialog.dimensionOkButton.mapTo(self.dialog, QPoint()).y())
        self.dialog.schematicToggleButton.setChecked(False)
        self.assertTrue(self.dialog.markerSchematicPanel.isHidden())
        self.dialog.schematicToggleButton.setChecked(True)
        self.assertFalse(self.dialog.markerSchematicPanel.isHidden())

    def test_switching_case_clears_sidebar_and_enlarged_view(self):
        self.dialog.markerSchematicPanel.open_enlarged()
        self.dialog.currentModelDir = str(ROOT / "Model/template_nlg_retract")
        self.dialog._refreshMarkerSchematic()
        self.assertIsNone(self.dialog.schematicData)
        self.assertTrue(self.dialog.markerSchematicPanel.isHidden())
        self.assertTrue(self.dialog.schematicToggleButton.isHidden())
        self.assertFalse(self.dialog.markerSchematicPanel._large_dialog.isVisible())
        self.assertEqual([], self.dialog.markerSchematicPanel._large_view.markers)


if __name__ == "__main__":
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    unittest.main()
