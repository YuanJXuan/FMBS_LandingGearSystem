# -*- coding: utf-8 -*-
"""Excel-defined section headings must never become editable model records."""
import os
import sys
import tempfile
import types
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Share"))
import InformationConfiguration as configuration
import SplineDataIO

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"


def write_fixture(path, rows, with_styles=True):
    """Build small input fixtures, never save or edit a shipped workbook."""
    xml_rows = []
    for index, (values, style) in enumerate(rows, 1):
        cells = []
        for column, value in enumerate(values):
            cell_style = ' s="{}"'.format(style) if column == 0 else ""
            cells.append('<c r="{}{}"{} t="inlineStr"><is><t>{}</t></is></c>'.format(
                chr(65 + column), index, cell_style, escape(str(value))))
        xml_rows.append('<row r="{}">{}</row>'.format(index, "".join(cells)))
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("xl/workbook.xml", (
            '<workbook xmlns="{}" xmlns:r="{}"><sheets>'
            '<sheet name="Sheet1" sheetId="1" r:id="rId1"/>'
            '</sheets></workbook>').format(NS, REL))
        archive.writestr("xl/_rels/workbook.xml.rels", (
            '<Relationships xmlns="{}">'
            '<Relationship Id="rId1" Target="worksheets/sheet1.xml" Type="{}/worksheet"/>'
            '<Relationship Id="rId2" Target="theme/custom.xml" Type="{}/theme"/>'
            '</Relationships>').format(PKG_REL, REL, REL))
        archive.writestr("xl/worksheets/sheet1.xml", (
            '<worksheet xmlns="{}"><sheetData>{}</sheetData></worksheet>'
        ).format(NS, "".join(xml_rows)))
        if with_styles:
            colors = ('rgb="FF92D050"', 'theme="9" tint="0.3999755851924192"',
                      'indexed="17"', 'rgb="FFFFFF00"', 'rgb="FFBDD7EE"')
            fills = '<fill><patternFill patternType="none"/></fill>' + "".join(
                '<fill><patternFill patternType="solid"><fgColor {}/></patternFill></fill>'.format(color)
                for color in colors)
            archive.writestr("xl/styles.xml", (
                '<styleSheet xmlns="{}"><fills>{}</fills><cellXfs>{}</cellXfs></styleSheet>'
            ).format(NS, fills, "".join('<xf fillId="{}"/>'.format(i) for i in range(6))))
            archive.writestr("xl/theme/custom.xml", (
                '<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                '<a:themeElements><a:clrScheme name="Custom">'
                '<a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>'
                '<a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>'
                '<a:accent6><a:srgbClr val="70AD47"/></a:accent6>'
                '</a:clrScheme></a:themeElements></a:theme>'))


class ConfigurationSectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "信息配置表.xlsx"

    def load(self, rows, **kwargs):
        write_fixture(self.path, rows, **kwargs)
        return configuration.load_information_configuration(self.temp.name)

    def test_rgb_theme_and_indexed_greens_are_headings_not_parameters(self):
        config = self.load([
            (["几何参数化信息"], 4),
            (["参数组 RGB"], 1),
            (["点1", ".case.part.m1", 1, 2, 3], 0),
            (["参数组 主题"], 2),
            (["点2", ".case.part.m2", 4, 5, 6], 0),
            (["参数组 索引"], 3),
        ])
        self.assertEqual([], config["errors"])
        self.assertEqual(2, len(config["markers"]))
        self.assertEqual(["config.marker.1", "config.marker.2"], [e["id"] for e in config["markers"]])
        groups = configuration.section_entry_groups(config, "markers", config["markers"])
        self.assertEqual(["参数组 RGB", "参数组 主题", "参数组 索引"], [title for title, _ in groups])
        self.assertEqual([1, 1, 0], [len(entries) for _, entries in groups])
        self.assertIs(config["markers"][0], groups[0][1][0])

    def test_renaming_inserting_removing_and_moving_headings_on_reload(self):
        major = (["缓冲器参数信息"], 4)
        first = (["参数1", ".case.v1", 12, "mm"], 0)
        second = (["参数2", ".case.v2", 34, "N"], 0)
        before = self.load([major, (["原名称"], 1), first, second])
        after = self.load([major, first, (["其他参数信息"], 2), second, (["新增空组"], 3)])
        self.assertEqual([], after["errors"])
        groups = configuration.section_entry_groups(after, "buffer_parameters", after["buffer_parameters"])
        self.assertEqual([None, "其他参数信息", "新增空组"], [title for title, _ in groups])
        self.assertEqual([1, 1, 0], [len(entries) for _, entries in groups])
        for old, new in zip(before["buffer_parameters"], after["buffer_parameters"]):
            self.assertEqual({k: v for k, v in old.items() if k != "row"},
                             {k: v for k, v in new.items() if k != "row"})
        flat = self.load([major, first, second])
        self.assertEqual({}, flat["section_headers"])
        self.assertEqual([(None, flat["buffer_parameters"])],
                         configuration.section_entry_groups(flat, "buffer_parameters", flat["buffer_parameters"]))

    def test_green_data_row_is_still_data_and_non_green_invalid_row_still_reports_error(self):
        config = self.load([
            (["缓冲器参数信息"], 4),
            (["普通参数", ".case.var", 7], 1),
            (["蓝色不是小标题"], 5),
            (["无填充的缺失参数"], 0),
        ])
        self.assertEqual({}, config["section_headers"])
        self.assertEqual(7.0, float(config["buffer_parameters"][0]["value"]))
        self.assertEqual(2, len(config["errors"]))

    def test_all_supported_sections_accept_arbitrary_and_duplicate_heading_text(self):
        for title, section in configuration.SECTION_TITLES.items():
            with self.subTest(section=section):
                config = self.load([([title], 4), (["任意分组名称"], 2), (["任意分组名称"], 1)])
                self.assertEqual([], config["errors"])
                groups = configuration.section_entry_groups(config, section, [])
                self.assertEqual([("任意分组名称", []), ("任意分组名称", [])], groups)

    def test_legacy_and_modern_sections_do_not_leak_headings_across_boundaries(self):
        config = self.load([
            (["仿真参数化信息"], 4), (["旧格式分组"], 1), (["旧参数", "old", 1], 0),
            (["其他参数信息"], 4), (["新参数", "new", 2], 0),
            (["新格式分组"], 1), (["新参数2", "new2", 3], 0),
        ])
        params = configuration.simulation_parameter_groups(config)["other_parameters"]
        resolved = configuration.resolve_simulation_parameters(None, params, [])
        groups = configuration.section_entry_groups(config, "other_parameters", resolved)
        self.assertEqual(["旧格式分组", None, "新格式分组"], [title for title, _ in groups])
        self.assertEqual(["old", "new", "new2"], [items[0]["name"] for _, items in groups])
        self.assertEqual({id(e) for e in resolved}, {id(e) for _, items in groups for e in items})

    def test_value_only_reader_and_legacy_workbooks_without_styles_remain_compatible(self):
        config = self.load([
            (["几何参数化信息"], 0), (["点1", ".case.marker", 1, 2, 3], 0)
        ], with_styles=False)
        self.assertEqual([], config["errors"])
        self.assertEqual({}, config["section_headers"])
        name, rows = SplineDataIO.read_xlsx_rows(str(self.path))
        styled_name, styled_rows, fills = SplineDataIO.read_xlsx_rows(str(self.path), include_row_fills=True)
        self.assertEqual((name, rows), (styled_name, styled_rows))
        self.assertEqual({}, fills)

    def test_real_full_drop_sections_preserve_counts_and_exact_titles(self):
        config = configuration.load_information_configuration(str(ROOT / "Model" / "template_full_drop"))
        self.assertEqual([], config["errors"])
        expected = {
            "markers": [("轮胎", 2), ("撑杆与作动筒", 8), ("防扭臂", 3), ("质量块", 1)],
            "buffer_parameters": [("主起落架", 14), ("前起落架", 13)],
            "structure_property_parameters": [("质量", 2), ("转动惯量", 6)],
        }
        for section, counts in expected.items():
            groups = configuration.section_entry_groups(config, section, config[section])
            self.assertEqual(counts, [(title, len(entries)) for title, entries in groups])
            self.assertEqual(config[section], [entry for _, entries in groups for entry in entries])
        self.assertEqual(6, len(config["splines"]))


os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
try:
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QComboBox, QLabel, QListWidget, QPushButton, QWidget
    from MarkerConfigurationTable import MarkerConfigurationTable
    from VariableInputTable import VariableInputTable
    QT_AVAILABLE = True
except ImportError:
    QT_AVAILABLE = False


@unittest.skipUnless(QT_AVAILABLE, "PySide2 is not installed")
class ConfigurationSectionsQtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def close_widget(self, widget):
        widget.close()
        widget.deleteLater()
        self.app.processEvents()

    def test_marker_editors_and_coincident_linkage_remain_bound_to_original_ids(self):
        table = MarkerConfigurationTable()
        self.addCleanup(self.close_widget, table)
        entries = [dict(id="m1", label="点1", target=".case.p.m1", coordinates=(1, 2, 3)),
                   dict(id="m2", label="点2", target=".case.p.m2", coordinates=(1, 2, 3))]
        table.set_entries(entries, [[e["target"] for e in entries]],
                          groups=[("分组一", entries[:1]), ("空组", []), ("分组二", entries[1:])])
        model = table.markerModel
        self.assertEqual(5, model.rowCount())
        for row in (0, 2, 3):
            self.assertFalse(model.item(row, 0).flags() & (Qt.ItemIsEditable | Qt.ItemIsSelectable))
            self.assertIsNone(table.indexWidget(model.index(row, 2)))
        editor = table.indexWidget(model.index(1, 2))
        peer = table.indexWidget(model.index(4, 2))
        editor.setText("125")
        editor.textEdited.emit("125")
        self.assertEqual("125", peer.text())
        self.assertEqual({"m1": (125, 2, 3), "m2": (125, 2, 3)}, table.coordinate_values(entries))
        table.set_entries(entries)
        self.assertEqual(2, model.rowCount())
        self.assertTrue(table.uniformRowHeights())
        self.assertEqual({"m1": (1, 2, 3), "m2": (1, 2, 3)}, table.coordinate_values(entries))

    def test_ungrouped_rows_and_duplicate_headings_keep_parameter_editor_keys(self):
        table = VariableInputTable([])
        self.addCleanup(self.close_widget, table)
        rows = [("参数1", "path1", False, False, "id1"), ("参数2", "path2", False, False, "id2")]
        table.set_grouped_rows([(None, rows[:1]), ("重复标题", []), ("重复标题", rows[1:])])
        self.assertEqual(4, table.variableModel.rowCount())
        for row, key in ((0, "id1"), (3, "id2")):
            self.assertIs(table.editor(key), table.indexWidget(table.variableModel.index(row, 2)))
        table.set_grouped_rows([(None, rows)])
        self.assertEqual(2, table.variableModel.rowCount())
        self.assertTrue(table.uniformRowHeights())

    def test_postprocessing_headings_are_not_curves_and_reload_preserves_checks(self):
        with patch.dict(sys.modules, {name: types.ModuleType(name) for name in ("Jusme", "JusmeGui")}):
            from DedicatedCaseDialog import DedicatedCaseDialog
        owner = QWidget()
        self.addCleanup(self.close_widget, owner)
        config = configuration.empty_configuration(str(ROOT))
        config["section_headers"] = {"postprocessing": [dict(row=2, title="空组", end_row=None)]}
        state = types.SimpleNamespace(
            informationConfiguration=config,
            postprocessingCurveList=QListWidget(owner),
            postprocessingDiagramSelector=QComboBox(owner),
            postprocessingModeSelector=QComboBox(owner),
            postprocessingBrowseButton=QPushButton(owner),
            postprocessingReloadButton=QPushButton(owner),
            postprocessingStatus=QLabel(owner),
            postprocessingResultDirectory="",
            postprocessingCurves={},
            postprocessingCurveWidget=types.SimpleNamespace(clear_curve=lambda text: None),
            postprocessingDisplayModeChanged=lambda: None,
        )
        refresh = DedicatedCaseDialog.refreshPostprocessingConfiguration
        refresh(state)
        self.assertEqual(1, state.postprocessingCurveList.count())
        self.assertFalse(state.postprocessingBrowseButton.isEnabled())
        config["postprocessing"] = [dict(id="p1", row=3, label="曲线1", target="result1"),
                                    dict(id="p2", row=7, label="曲线2", target="result2")]
        config["section_headers"]["postprocessing"] = [dict(row=2, title="第一组", end_row=6),
                                                        dict(row=6, title="第二组", end_row=None)]
        refresh(state)
        items = state.postprocessingCurveList
        self.assertEqual(4, items.count())
        self.assertEqual(Qt.Checked, items.item(1).checkState())
        for row in (0, 2):
            self.assertIsNone(items.item(row).data(Qt.UserRole))
            self.assertFalse(items.item(row).flags() & (Qt.ItemIsUserCheckable | Qt.ItemIsSelectable))
        items.item(1).setCheckState(Qt.Unchecked)
        items.item(3).setCheckState(Qt.Checked)
        config["section_headers"]["postprocessing"] = [dict(row=6, title="重新命名", end_row=None)]
        refresh(state)
        self.assertEqual(3, items.count())
        self.assertEqual("重新命名", items.item(1).text())
        self.assertEqual(Qt.Unchecked, items.item(0).checkState())
        self.assertEqual(Qt.Checked, items.item(2).checkState())
        self.assertEqual({"p1", "p2"}, set(state.postprocessingEntriesById))


if __name__ == "__main__":
    unittest.main()
