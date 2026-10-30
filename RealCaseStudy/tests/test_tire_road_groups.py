# -*- coding: utf-8 -*-
"""Check parameter classification and editor identity across fixed section rows."""

import os
import sys
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Share"))
import DynamicModelParameters as parameters


class TireRoadGroupingTests(unittest.TestCase):
    def test_classification_ignores_model_name_and_keeps_original_records(self):
        variables = [
            {"name": "road_height", "key": "road_height", "path": ".tire_case.road_height"},
            {"name": "NLG_m", "key": "NLG_m", "path": ".road_case.NLG_m"},
            {"name": "lumian_speed", "path": ".case.lumian_speed"},
            {"name": "wheel_pressure", "path": ".road_case.wheel_pressure"},
            {"name": "runway_friction"},
        ]
        tire, road = parameters.partition_tire_road_variables(variables)
        self.assertEqual([variables[1], variables[3]], tire)
        self.assertEqual([variables[0], variables[2], variables[4]], road)
        self.assertEqual({id(v) for v in variables}, {id(v) for v in tire + road})

    def test_relative_object_path_identifies_road_parameter(self):
        variable = {"name": "height", "key": "road_part.height"}
        tire, road = parameters.partition_tire_road_variables([variable])
        self.assertEqual([], tire)
        self.assertIs(variable, road[0])

    def test_empty_model_has_two_empty_groups(self):
        self.assertEqual(([], []), parameters.partition_tire_road_variables([]))


os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
try:
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication
    from VariableInputTable import VariableInputTable
    QT_AVAILABLE = True
except ImportError:
    QT_AVAILABLE = False


@unittest.skipUnless(QT_AVAILABLE, "PySide2 is not installed")
class FixedParameterSectionsQtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.table = VariableInputTable([])

    def tearDown(self):
        self.table.close()
        self.table.deleteLater()
        self.app.processEvents()

    def test_heading_rows_cannot_redirect_edits_to_another_parameter(self):
        variables = [
            dict(name="road_speed", key="road.speed", path=".case.road.speed",
                 label="路面速度", value="1", value_kind="expression"),
            dict(name="wheel_mass", key="wheel.mass", path=".case.wheel.mass",
                 label="轮胎质量", value="2", value_kind="expression"),
        ]
        tire, road = parameters.partition_tire_road_variables(variables)
        self.table.set_grouped_rows((
            ("轮胎参数", parameters.table_rows(tire)),
            ("路面参数", parameters.table_rows(road)),
        ))
        parameters.populate_table(self.table, variables)
        model = self.table.variableModel
        self.assertEqual(4, model.rowCount())
        self.assertFalse(self.table.rootIsDecorated())
        for row in (0, 2):
            self.assertFalse(model.item(row, 0).flags() & Qt.ItemIsEditable)
            self.assertEqual(0, model.item(row, 0).rowCount())
            self.assertIsNone(self.table.indexWidget(model.index(row, 2)))
        for row, key, value in ((1, "wheel.mass", "125"), (3, "road.speed", "TIME * 2")):
            editor = self.table.indexWidget(model.index(row, 2))
            self.assertIs(self.table.editor(key), editor)
            self.assertGreaterEqual(model.item(row, 0).sizeHint().height(), editor.sizeHint().height())
            editor.setText(value)
        nodes = {v["path"]: types.SimpleNamespace(function=v["value"]) for v in variables}
        scene = types.SimpleNamespace(Name="case", getObject=nodes.get, recompute=lambda: None)
        updated, errors = parameters.apply_table_values(scene, self.table, variables)
        self.assertEqual((2, []), (updated, errors))
        self.assertEqual("125", nodes[".case.wheel.mass"].function)
        self.assertEqual("TIME * 2", nodes[".case.road.speed"].function)

    def test_empty_refresh_and_flat_tables_leave_no_stale_editors(self):
        self.table.set_grouped_rows((("轮胎参数", [("质量", "mass")]), ("路面参数", [])))
        self.table.set_grouped_rows((("轮胎参数", []), ("路面参数", [])))
        self.assertEqual({}, self.table.editors())
        self.assertEqual(2, self.table.variableModel.rowCount())
        self.assertEqual("暂无参数", self.table.variableModel.item(1, 2).text())
        self.table.set_rows([("普通参数", "ordinary")])
        self.assertEqual(1, self.table.variableModel.rowCount())
        self.assertEqual({"ordinary"}, set(self.table.editors()))
        self.assertTrue(self.table.uniformRowHeights())


if __name__ == "__main__":
    unittest.main()
