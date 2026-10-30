# -*- coding: utf-8 -*-
"""Reload the real lists repeatedly without resetting or accumulating font sizes."""
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
    from PySide2.QtGui import QFont
    from PySide2.QtWidgets import QApplication
    QT_AVAILABLE = True
except ImportError:
    QT_AVAILABLE = False


@unittest.skipUnless(QT_AVAILABLE, "PySide2 is not installed")
class ListFontReloadQtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        with patch.dict(sys.modules, {name: types.ModuleType(name) for name in ("Jusme", "JusmeGui")}):
            import DedicatedCaseDialog
        cls.module = DedicatedCaseDialog

    def assert_list_fonts(self, dialog, expected):
        tables = [dialog.infoMarkerTable, dialog.tireRoadVariableTable]
        tables.extend(dialog.parameterTables.values())
        for table in tables:
            for widget in (table, table.viewport(), table.header()):
                self.assertEqual(expected, widget.font().pointSizeF())
            model = table.model()
            for row in range(model.rowCount()):
                self.assertEqual(expected, model.item(row, 0).font().pointSizeF())
                for column in range(model.columnCount()):
                    editor = table.indexWidget(model.index(row, column))
                    if editor is not None:
                        self.assertEqual(expected, editor.font().pointSizeF())
                        self.assertGreaterEqual(model.item(row, 0).sizeHint().height(),
                                                editor.sizeHint().height())
        curves = dialog.postprocessingCurveList
        self.assertEqual(expected, curves.font().pointSizeF())
        self.assertEqual(expected, curves.viewport().font().pointSizeF())
        for index in range(curves.count()):
            self.assertEqual(expected, curves.item(index).font().pointSizeF())

    def test_all_tabs_keep_font_size_after_reloading_configuration(self):
        module = self.module

        class PreviewDialog(module.DedicatedCaseDialog):
            def _restoreSavedModelContext(self):
                return False

        # One case supplies Excel section rows; the other supplies result curves
        # and the legacy parameter group. Only the external scene is absent.
        with patch.object(module.SelectionMonitor, "get_active_scene", return_value=None), \
                patch.object(module.SelectionMonitor.SelectionMonitor, "start"):
            for model_name in ("template_full_drop", "template_nlg_retract"):
                with self.subTest(model=model_name):
                    dialog = PreviewDialog({"model_dir": str(ROOT / "Model" / model_name)})
                    try:
                        dialog.ensurePolished()
                        self.app.processEvents()
                        expected = dialog.infoMarkerTable.font().pointSizeF()
                        self.assert_list_fonts(dialog, expected)
                        # Later host/parent font changes must not affect newly
                        # created value editors or the cached list font.
                        parent_font = QFont(dialog.font())
                        parent_font.setPointSizeF(max(1.0, expected - 3.0))
                        dialog.setFont(parent_font)
                        for _ in range(3):
                            dialog.reloadInformationConfiguration(show_message=False)
                            dialog._apply_list_font()
                            self.app.processEvents()
                            self.assert_list_fonts(dialog, expected)
                    finally:
                        dialog.close()
                        dialog.deleteLater()
                        self.app.processEvents()


if __name__ == "__main__":
    unittest.main()
