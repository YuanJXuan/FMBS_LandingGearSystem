# -*- coding: utf-8 -*-

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))

import DynamicModelParameters
import VariableExcelIO


WORKBOOK_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets><sheet name="变量" sheetId="1" r:id="rId1"/></sheets>
</workbook>
"""

WORKBOOK_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1"
   Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"
   Target="worksheets/sheet1.xml"/>
</Relationships>
"""

WORKSHEET_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <sheetData>
    <row r="1">
      <c r="A1" t="inlineStr"><is><t>变量名称</t></is></c>
      <c r="B1" t="inlineStr"><is><t>function</t></is></c>
    </row>
    <row r="2">
      <c r="A2" t="inlineStr"><is><t>speed</t></is></c>
      <c r="B2"><v>12.5</v></c>
    </row>
    <row r="3">
      <c r="A3" t="inlineStr"><is><t>force</t></is></c>
      <c r="B3" t="inlineStr"><is><t>VARVAL(.Model.speed)*2</t></is></c>
    </row>
    <row r="4">
      <c r="A4" t="inlineStr"><is><t>drive</t></is></c>
      <c r="B4"><f>SIN(TIME)</f><v>0</v></c>
    </row>
  </sheetData>
</worksheet>
"""


def _write_workbook(file_path):
    with zipfile.ZipFile(str(file_path), "w") as archive:
        archive.writestr("xl/workbook.xml", WORKBOOK_XML)
        archive.writestr("xl/_rels/workbook.xml.rels", WORKBOOK_RELS_XML)
        archive.writestr("xl/worksheets/sheet1.xml", WORKSHEET_XML)


class VariableExcelImportTests(unittest.TestCase):
    def test_reads_constants_text_and_formula_cells(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "variables.xlsx"
            _write_workbook(file_path)

            sheet, updates = VariableExcelIO.read_variable_updates(str(file_path))

        self.assertEqual(sheet, "变量")
        self.assertEqual(
            [(item["identifier"], item["function"]) for item in updates],
            [
                ("speed", "12.5"),
                ("force", "VARVAL(.Model.speed)*2"),
                ("drive", "SIN(TIME)"),
            ],
        )

    def test_matches_relative_and_model_independent_absolute_paths(self):
        first = {
            "name": "value",
            "key": "group1.value",
            "path": ".Current.group1.value",
        }
        second = {
            "name": "value",
            "key": "group2.value",
            "path": ".Current.group2.value",
        }
        speed = {"name": "speed", "key": "speed", "path": ".Current.speed"}
        matched, errors = VariableExcelIO.match_variable_updates(
            [first, second, speed],
            [
                {"row": 2, "identifier": ".Old.group1.value", "function": "1"},
                {"row": 3, "identifier": "speed", "function": "2"},
            ],
        )
        self.assertEqual(errors, [])
        self.assertEqual([item[0] for item in matched], [first, speed])

        matched, errors = VariableExcelIO.match_variable_updates(
            [first, second],
            [{"row": 2, "identifier": "value", "function": "1"}],
        )
        self.assertEqual(matched, [])
        self.assertIn("不唯一", errors[0])

    def test_batch_write_rolls_back_if_one_variable_fails(self):
        class Node:
            def __init__(self, value, reject=None):
                self._function = value
                self.reject = reject

            @property
            def function(self):
                return self._function

            @function.setter
            def function(self, value):
                if value == self.reject:
                    raise ValueError("rejected")
                self._function = value

        first = Node("old1")
        second = Node("old2", reject="bad")

        class Scene:
            Name = "Current"

            def getObject(self, path):
                return {
                    ".Current.first": first,
                    ".Current.second": second,
                }.get(path)

            def recompute(self):
                pass

        updates = [
            (
                {
                    "name": "first",
                    "key": "first",
                    "path": ".Current.first",
                    "value_property": "function",
                },
                "new1",
                2,
            ),
            (
                {
                    "name": "second",
                    "key": "second",
                    "path": ".Current.second",
                    "value_property": "function",
                },
                "bad",
                3,
            ),
        ]

        updated, errors = DynamicModelParameters.apply_function_updates(
            Scene(), updates
        )

        self.assertEqual(updated, 0)
        self.assertTrue(errors)
        self.assertEqual(first.function, "old1")
        self.assertEqual(second.function, "old2")


if __name__ == "__main__":
    unittest.main()
