# -*- coding: utf-8 -*-
"""Dialog for replacing a model spline with X/Y data from an XLSX file."""

import os

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

import Jusme
import ResultCurveWidget
import ResponsiveTableColumns
import SplineDataIO


def _active_scene():
    try:
        return Jusme.ActiveUSScene
    except Exception:
        return None


def show_spline_import_dialog(parent=None):
    """Open the shared spline importer for the current active scene."""
    if _active_scene() is None:
        QMessageBox.warning(parent, "无法修改样条曲线", "当前没有活动模型。")
        return None
    dialog = SplineImportDialog(parent)
    dialog.exec_()
    return dialog


class SplineImportDialog(QDialog):
    """Select a scene spline and replace its points from an XLSX worksheet."""

    PREVIEW_LIMIT = 200

    def __init__(self, parent=None):
        super(SplineImportDialog, self).__init__(parent)
        if parent is not None:
            self.setFont(parent.font())
        self.points = []
        self.spline_details = {}
        self._init_ui()
        self.refresh_splines()

    def _init_ui(self):
        self.setWindowTitle("导入样条曲线数据")
        self.setMinimumSize(1000, 600)

        description = QLabel(
            "Excel 前两列分别为 X、Y；允许在数据前保留表头。"
            "X 必须严格递增，写入时保留样条原有单位和外插设置。"
            "当前仅覆盖一维 X/Y 样条。"
        )
        description.setWordWrap(True)

        form_layout = QFormLayout()

        self.spline_combo = QComboBox(self)
        self.spline_combo.currentIndexChanged.connect(self.update_spline_details)
        self.refresh_button = QPushButton("刷新模型树", self)
        self.refresh_button.clicked.connect(self.refresh_splines)
        spline_layout = QHBoxLayout()
        spline_layout.addWidget(self.spline_combo, 1)
        spline_layout.addWidget(self.refresh_button)
        form_layout.addRow("目标 Spline：", spline_layout)

        self.spline_detail_label = QLabel(self)
        self.spline_detail_label.setWordWrap(True)
        form_layout.addRow("当前数据：", self.spline_detail_label)

        self.file_path_edit = QLineEdit(self)
        self.file_path_edit.setReadOnly(True)
        self.file_path_edit.setPlaceholderText("请选择包含 X、Y 两列的 .xlsx 文件")
        self.file_button = QPushButton("选择 Excel…", self)
        self.file_button.clicked.connect(self.select_excel_file)
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_path_edit, 1)
        file_layout.addWidget(self.file_button)
        form_layout.addRow("Excel 文件：", file_layout)

        self.sheet_combo = QComboBox(self)
        self.sheet_combo.setEnabled(False)
        self.sheet_combo.currentTextChanged.connect(self.load_selected_sheet)
        form_layout.addRow("工作表：", self.sheet_combo)

        self.preview_table = QTableWidget(0, 2, self)
        self.preview_table.setHorizontalHeaderLabels(["X", "Y"])
        self.preview_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.preview_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        ResponsiveTableColumns.install(
            self.preview_table,
            self.preview_table.horizontalHeader(),
            (180, 180),
            (100, 100),
        )

        self.preview_table_title = QLabel("当前 Spline 数据", self)
        table_panel = QWidget(self)
        table_layout = QVBoxLayout(table_panel)
        table_layout.setContentsMargins(0, 0, 0, 0)
        table_layout.addWidget(self.preview_table_title)
        table_layout.addWidget(self.preview_table, 1)

        self.preview_curve_title = QLabel("Spline 曲线", self)
        self.preview_curve = ResultCurveWidget.ResultCurveWidget(self)
        self.preview_curve.clear_curve("当前 Spline 没有可显示的 X/Y 数据")
        curve_panel = QWidget(self)
        curve_layout = QVBoxLayout(curve_panel)
        curve_layout.setContentsMargins(0, 0, 0, 0)
        curve_layout.addWidget(self.preview_curve_title)
        curve_layout.addWidget(self.preview_curve, 1)

        self.preview_splitter = QSplitter(Qt.Horizontal, self)
        self.preview_splitter.addWidget(table_panel)
        self.preview_splitter.addWidget(curve_panel)
        self.preview_splitter.setStretchFactor(0, 1)
        self.preview_splitter.setStretchFactor(1, 1)
        self.preview_splitter.setSizes([440, 560])

        self.status_label = QLabel("等待选择 Excel 文件", self)
        self.status_label.setWordWrap(True)

        self.apply_button = QPushButton("写入选中 Spline", self)
        self.apply_button.setEnabled(False)
        self.apply_button.clicked.connect(self.apply_points)
        close_button = QPushButton("关闭", self)
        close_button.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(close_button)

        layout = QVBoxLayout(self)
        layout.addWidget(description)
        layout.addLayout(form_layout)
        layout.addWidget(self.preview_splitter, 1)
        layout.addWidget(self.status_label)
        layout.addLayout(button_layout)

    def _selected_spline(self):
        scene = _active_scene()
        spline_path = self.spline_combo.currentData()
        if scene is None or not spline_path:
            return None
        try:
            return scene.getObject(spline_path)
        except Exception:
            return None

    @staticmethod
    def _xy_points(spline):
        if spline is None:
            return []
        try:
            x_values = list(getattr(spline, "x", []) or [])
            y_values = list(getattr(spline, "y", []) or [])
        except Exception:
            return []
        return list(zip(x_values[: min(len(x_values), len(y_values))], y_values))

    def _show_points(self, points, source_label):
        points = list(points or [])
        preview_points = points[: self.PREVIEW_LIMIT]
        self.preview_table.setRowCount(len(preview_points))
        for row, (x_value, y_value) in enumerate(preview_points):
            self.preview_table.setItem(row, 0, QTableWidgetItem(str(x_value)))
            self.preview_table.setItem(row, 1, QTableWidgetItem(str(y_value)))

        table_note = "{}（{} 个点）".format(source_label, len(points))
        if len(points) > self.PREVIEW_LIMIT:
            table_note += "，表格显示前 {} 个".format(self.PREVIEW_LIMIT)
        self.preview_table_title.setText(table_note)
        self.preview_curve_title.setText("{}曲线".format(source_label))

        details = self.spline_details.get(self.spline_combo.currentData(), {})
        if points:
            self.preview_curve.set_curve(
                [point[0] for point in points],
                [point[1] for point in points],
                source_label,
                details.get("x_units", ""),
                details.get("y_units", ""),
            )
        else:
            self.preview_curve.clear_curve(
                "{}没有可显示的 X/Y 数据".format(source_label)
            )

    def _show_selected_spline(self):
        self._show_points(
            self._xy_points(self._selected_spline()),
            "当前 Spline 数据",
        )

    def refresh_splines(self):
        scene = _active_scene()
        splines = SplineDataIO.find_scene_splines(scene)
        selected_path = self.spline_combo.currentData()

        self.spline_details = {}
        self.spline_combo.clear()
        selected_index = -1
        for index, spline in enumerate(splines):
            full_name = getattr(spline, "Name", "")
            label = getattr(spline, "Label", "") or full_name.rsplit(".", 1)[-1]
            self.spline_combo.addItem("{}  ({})".format(label, full_name), full_name)
            try:
                x_count = len(getattr(spline, "x", []) or [])
                y_count = len(getattr(spline, "y", []) or [])
                z_count = len(getattr(spline, "z", []) or [])
            except Exception:
                x_count = y_count = z_count = 0
            self.spline_details[full_name] = {
                "x_count": x_count,
                "y_count": y_count,
                "z_count": z_count,
                "x_units": str(getattr(spline, "x_units", "") or "").strip('"'),
                "y_units": str(getattr(spline, "y_units", "") or "").strip('"'),
            }
            if full_name == selected_path:
                selected_index = index
        if selected_index >= 0:
            self.spline_combo.setCurrentIndex(selected_index)

        if splines:
            self.status_label.setText(
                "已在当前模型中找到 {} 条样条曲线。".format(len(splines))
            )
        else:
            self.status_label.setText("当前模型树中没有找到 Spline。")
        self.update_spline_details()
        self._update_apply_button()

    def update_spline_details(self, _index=None):
        details = self.spline_details.get(self.spline_combo.currentData(), {})
        if not details:
            self.spline_detail_label.setText("—")
            self._show_points([], "当前 Spline 数据")
            self._update_apply_button()
            return

        units = "未设置单位"
        if details["x_units"] or details["y_units"]:
            units = "X：{}，Y：{}".format(
                details["x_units"] or "未设置",
                details["y_units"] or "未设置",
            )
        text = "X {} 项，Y {} 项；{}".format(
            details["x_count"], details["y_count"], units
        )
        if details["z_count"]:
            text += "；该样条含 Z 数据，当前的 X/Y 导入不能覆盖它"
        self.spline_detail_label.setText(text)
        if self.points:
            self._show_points(self.points, "待导入 Excel 数据")
        else:
            self._show_selected_spline()
        self._update_apply_button()

    def select_excel_file(self):
        current_path = self.file_path_edit.text().strip()
        initial_dir = os.path.dirname(current_path) if current_path else os.getcwd()
        file_path, _selected_filter = QFileDialog.getOpenFileName(
            self,
            "选择样条曲线 Excel",
            initial_dir,
            "Excel 工作簿 (*.xlsx);;所有文件 (*.*)",
        )
        if not file_path:
            return

        try:
            sheet_names = SplineDataIO.list_xlsx_sheets(file_path)
        except SplineDataIO.SplineDataError as exc:
            QMessageBox.warning(self, "Excel 文件无效", str(exc))
            return

        self.file_path_edit.setText(os.path.normpath(file_path))
        self.sheet_combo.blockSignals(True)
        self.sheet_combo.clear()
        self.sheet_combo.addItems(sheet_names)
        self.sheet_combo.blockSignals(False)
        self.sheet_combo.setEnabled(True)
        self.load_selected_sheet(self.sheet_combo.currentText())

    def load_selected_sheet(self, sheet_name):
        file_path = self.file_path_edit.text().strip()
        if not file_path or not sheet_name:
            return
        try:
            self.points = SplineDataIO.read_spline_points(file_path, sheet_name)
        except SplineDataIO.SplineDataError as exc:
            self.points = []
            self._show_selected_spline()
            self.status_label.setText(str(exc))
            self._update_apply_button()
            QMessageBox.warning(self, "样条数据无效", str(exc))
            return

        self._show_points(self.points, "待导入 Excel 数据")

        preview_note = "，预览前 {} 条".format(self.PREVIEW_LIMIT)
        if len(self.points) <= self.PREVIEW_LIMIT:
            preview_note = ""
        self.status_label.setText(
            "读取 {} 个数据点{}；X 范围：{} ～ {}。".format(
                len(self.points),
                preview_note,
                self.points[0][0],
                self.points[-1][0],
            )
        )
        self._update_apply_button()

    def _update_apply_button(self):
        details = self.spline_details.get(self.spline_combo.currentData(), {})
        self.apply_button.setEnabled(
            self.spline_combo.count() > 0 and len(self.points) >= 2
            and not details.get("z_count", 0)
        )

    def apply_points(self):
        scene = _active_scene()
        spline_path = self.spline_combo.currentData()
        if scene is None or not spline_path:
            QMessageBox.warning(self, "无法写入", "当前没有活动模型或目标 Spline。")
            return
        try:
            spline = scene.getObject(spline_path)
        except Exception:
            spline = None
        if spline is None:
            QMessageBox.warning(self, "无法写入", "目标 Spline 已不存在，请刷新模型树。")
            return
        if len(getattr(spline, "z", []) or []):
            QMessageBox.warning(
                self,
                "暂不支持该 Spline",
                "目标 Spline 含有 Z 数据；当前 Excel 格式仅支持一维 X/Y 样条。",
            )
            return

        answer = QMessageBox.question(
            self,
            "确认写入样条曲线",
            "将用 {} 个数据点覆盖：\n{}\n\n是否继续？".format(
                len(self.points), spline_path
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return

        old_x_value = getattr(spline, "x", None)
        old_y_value = getattr(spline, "y", None)
        old_x = list(old_x_value) if old_x_value is not None else None
        old_y = list(old_y_value) if old_y_value is not None else None
        try:
            spline.x = [point[0] for point in self.points]
            spline.y = [point[1] for point in self.points]
            scene.recompute()
        except Exception as exc:
            try:
                if old_x is not None:
                    spline.x = old_x
                if old_y is not None:
                    spline.y = old_y
                scene.recompute()
            except Exception as rollback_exc:
                print(
                    "样条曲线回滚失败：{}: {}".format(
                        type(rollback_exc).__name__, rollback_exc
                    )
                )
            QMessageBox.critical(
                self,
                "写入失败",
                "样条曲线写入失败，已尝试恢复原数据：\n{}: {}".format(
                    type(exc).__name__, exc
                ),
            )
            return

        QMessageBox.information(
            self,
            "写入完成",
            "已向 {} 写入 {} 个数据点。".format(spline_path, len(self.points)),
        )
        self._show_selected_spline()
