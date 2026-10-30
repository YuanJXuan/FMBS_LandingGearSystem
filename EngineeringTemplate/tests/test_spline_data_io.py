# -*- coding: utf-8 -*-

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))

import SplineDataIO


WORKBOOK_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets><sheet name="曲线数据" sheetId="1" r:id="rId1"/></sheets>
</workbook>
"""

WORKBOOK_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
   Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"
   Target="worksheets/sheet1.xml"/>
</Relationships>
"""


def _worksheet_xml(points):
    rows = [
        '<row r="1"><c r="A1" t="inlineStr"><is><t>X</t></is></c>'
        '<c r="B1" t="inlineStr"><is><t>Y</t></is></c></row>'
    ]
    for row_number, (x_value, y_value) in enumerate(points, 2):
        rows.append(
            '<row r="{0}"><c r="A{0}"><v>{1}</v></c>'
            '<c r="B{0}"><v>{2}</v></c></row>'.format(
                row_number, x_value, y_value
            )
        )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<sheetData>{}</sheetData></worksheet>'.format("".join(rows))
    )


def _write_xlsx(file_path, points):
    with zipfile.ZipFile(str(file_path), "w") as archive:
        archive.writestr("xl/workbook.xml", WORKBOOK_XML)
        archive.writestr("xl/_rels/workbook.xml.rels", WORKBOOK_RELS_XML)
        archive.writestr("xl/worksheets/sheet1.xml", _worksheet_xml(points))


class SplineDataIOTests(unittest.TestCase):
    def test_reads_first_two_columns_and_skips_header(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "curve.xlsx"
            _write_xlsx(file_path, [(0, 10), (0.5, 20), (1, 30)])

            self.assertEqual(SplineDataIO.list_xlsx_sheets(str(file_path)), ["曲线数据"])
            self.assertEqual(
                SplineDataIO.read_spline_points(str(file_path), "曲线数据"),
                [(0.0, 10.0), (0.5, 20.0), (1.0, 30.0)],
            )

    def test_rejects_x_values_that_are_not_strictly_increasing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "curve.xlsx"
            _write_xlsx(file_path, [(0, 10), (0, 20)])

            with self.assertRaisesRegex(SplineDataIO.SplineDataError, "严格递增"):
                SplineDataIO.read_spline_points(str(file_path))

    def test_finds_splines_in_flat_and_nested_model_trees(self):
        class Proxy:
            def __init__(self, node_type):
                self.Type = node_type

        class Node:
            def __init__(self, name, node_type, children=None):
                self.Name = name
                self.Label = name.rsplit(".", 1)[-1]
                self.Proxy = Proxy(node_type)
                self.PropertiesList = []
                self._children = children or []

            def getObjects(self):
                return self._children

        nested_spline = Node(".GCMB.SPLINE_stopper", "Fmbs::Spline")
        group = Node(".GCMB.DataElements", "App::DocumentObjectGroup", [nested_spline])
        flat_spline = Node(".GCMB.SPLINE_airspring", "Spline")
        ordinary_node = Node(".GCMB.ground", "Fmbs::Part")

        class Scene:
            Name = "GCMB"
            Objects = [group, flat_spline, ordinary_node]

            def getObjects(self):
                return []

            def getObject(self, _name):
                return None

        self.assertEqual(
            [node.Name for node in SplineDataIO.find_scene_splines(Scene())],
            [".GCMB.SPLINE_airspring", ".GCMB.SPLINE_stopper"],
        )

    def test_every_engineering_template_exposes_spline_import_dialog(self):
        page_names = (
            "template_2_brake.py",
            "template_2_drop.py",
            "template_2_retract.py",
            "template_2_turn.py",
            "template_4_cosim.py",
            "template_6_force.py",
            "template_6_motion.py",
            "template_7_swing.py",
        )
        for page_name in page_names:
            with self.subTest(page=page_name):
                page_path = TEMPLATE_DIR / page_name
                page_text = page_path.read_text(encoding="utf-8")
                compile(page_text, str(page_path), "exec")

                self.assertIn('QPushButton("修改样条曲线"', page_text)
                self.assertIn("import SplineImportDialog", page_text)
                self.assertIn("def openSplineImportDialog(self):", page_text)
                self.assertIn(
                    "SplineImportDialog.show_spline_import_dialog(self)",
                    page_text,
                )


if __name__ == "__main__":
    unittest.main()
