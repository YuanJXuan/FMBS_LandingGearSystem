# -*- coding: utf-8 -*-
"""Modal UI for generating and importing one combined NLG/MLG ADM model."""

from __future__ import print_function

import os
import traceback

from PySide2.QtCore import Qt
from PySide2.QtGui import QDoubleValidator
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import FullModelGenerator
import ModelImportRunner


class FullModelGenerateDialog(QDialog):
    """Collect two world points, generate one ADM and import it once."""

    def __init__(self, model_full_dir, parent=None):
        super(FullModelGenerateDialog, self).__init__(parent)
        self.model_full_dir = os.path.abspath(str(model_full_dir or ""))
        self.configuration = FullModelGenerator.load_configuration(
            self.model_full_dir
        )
        self.source_paths = {
            key: self.configuration["assemblies"][key]["source_adm"]
            for key in ("nlg", "mlg")
        }
        self.anchor_positions = FullModelGenerator.read_anchor_positions(
            self.model_full_dir,
            self.source_paths["nlg"],
            self.source_paths["mlg"],
        )
        self.imported_context = None
        self.setWindowTitle("生成完整起落架模型")
        self.setMinimumWidth(780)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        description = QLabel(
            "分别选择Model_Full目录中的前起和主起ADM，再输入两个定位点的"
            "世界坐标。程序将使用匹配的组合配置生成只含一个ground的完整模型。",
            self,
        )
        description.setWordWrap(True)
        layout.addWidget(description)

        input_panel = QWidget(self)
        grid = QGridLayout(input_panel)
        grid.addWidget(QLabel("模型类型", input_panel), 0, 0)
        grid.addWidget(QLabel("ADM模型", input_panel), 0, 1, 1, 2)
        for column, axis in enumerate(("X", "Y", "Z"), 1):
            grid.addWidget(QLabel(axis, input_panel), 0, column + 2)

        self.source_editors = {}
        self.coordinate_editors = {}
        for row, (key, label) in enumerate((("nlg", "前起位置"), ("mlg", "主起位置")), 1):
            grid.addWidget(QLabel(label, input_panel), row, 0)

            source_editor = QLineEdit(input_panel)
            source_editor.setReadOnly(True)
            source_editor.setText(os.path.basename(self.source_paths[key]))
            source_editor.setToolTip(self.source_paths[key])
            grid.addWidget(source_editor, row, 1)
            self.source_editors[key] = source_editor

            browse_button = QPushButton("选择…", input_panel)
            browse_button.setAutoDefault(False)
            browse_button.setDefault(False)
            browse_button.clicked.connect(
                lambda checked=False, source_key=key: self._select_source_adm(source_key)
            )
            grid.addWidget(browse_button, row, 2)

            editors = []
            for column, value in enumerate(self.anchor_positions[key], 3):
                editor = QLineEdit(input_panel)
                validator = QDoubleValidator(-1.0e12, 1.0e12, 12, editor)
                validator.setNotation(QDoubleValidator.StandardNotation)
                editor.setValidator(validator)
                editor.setText("{:.12g}".format(value))
                grid.addWidget(editor, row, column)
                editors.append(editor)
            self.coordinate_editors[key] = editors
        grid.setColumnStretch(1, 1)
        layout.addWidget(input_panel)

        form = QFormLayout()
        self.model_name_editor = QLineEdit(self)
        self.model_name_editor.setText(self.configuration["output_model_name"])
        self.model_name_editor.setToolTip("仅允许英文字母、数字和下划线")
        form.addRow("输出模型名称：", self.model_name_editor)
        self.combination_label = QLabel(self.configuration["combination_name"], self)
        self.combination_label.setWordWrap(True)
        self.combination_label.setToolTip(self.configuration["base_adm"])
        form.addRow("组合方案：", self.combination_label)
        layout.addLayout(form)

        self.status_label = QLabel("", self)
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

        buttons = QHBoxLayout()
        buttons.addStretch()
        self.generate_button = QPushButton("生成并导入", self)
        self.cancel_button = QPushButton("取消", self)
        self.generate_button.clicked.connect(self.generate_and_import)
        self.cancel_button.clicked.connect(self.reject)
        for button in (self.generate_button, self.cancel_button):
            button.setAutoDefault(False)
            button.setDefault(False)
        buttons.addWidget(self.generate_button)
        buttons.addWidget(self.cancel_button)
        layout.addLayout(buttons)

    def _selected_pair_configuration(self):
        return FullModelGenerator.load_configuration(
            self.model_full_dir,
            self.source_paths["nlg"],
            self.source_paths["mlg"],
        )

    def _set_coordinates(self, key, values):
        for editor, value in zip(self.coordinate_editors[key], values):
            editor.setText("{:.12g}".format(value))

    def _select_source_adm(self, key):
        label = "前起" if key == "nlg" else "主起"
        selected_path, _selected_filter = QFileDialog.getOpenFileName(
            self,
            "选择{}ADM模型".format(label),
            self.model_full_dir,
            "ADM模型 (*.adm)",
        )
        if not selected_path:
            return
        selected_path = os.path.abspath(selected_path)
        try:
            selected_key = os.path.normcase(os.path.realpath(selected_path))
            model_full_key = os.path.normcase(
                os.path.realpath(self.model_full_dir)
            )
            if os.path.commonpath(
                [selected_key, model_full_key]
            ) != model_full_key:
                raise FullModelGenerator.FullModelGenerationError(
                    "只能选择Model_Full目录中的ADM模型"
                )
        except (OSError, ValueError):
            QMessageBox.warning(
                self,
                "模型选择错误",
                "只能选择Model_Full目录中的ADM模型",
            )
            return
        if os.path.splitext(selected_path)[1].lower() != ".adm":
            QMessageBox.warning(self, "模型选择错误", "请选择ADM模型文件")
            return

        self.source_paths[key] = selected_path
        self.source_editors[key].setText(os.path.basename(selected_path))
        self.source_editors[key].setToolTip(selected_path)
        try:
            configuration = self._selected_pair_configuration()
            anchors = FullModelGenerator.read_anchor_positions(
                self.model_full_dir,
                self.source_paths["nlg"],
                self.source_paths["mlg"],
            )
        except Exception as exc:
            self.status_label.setText(str(exc))
            self.combination_label.setText("未找到匹配的组合方案")
            self.combination_label.setToolTip("")
            return

        self.configuration = configuration
        self.anchor_positions = anchors
        self._set_coordinates(key, anchors[key])
        self.combination_label.setText(configuration["combination_name"])
        self.combination_label.setToolTip(configuration["base_adm"])
        self.status_label.setText(
            "已选择{}：{}".format(label, os.path.basename(selected_path))
        )

    def _coordinates(self, key, description):
        values = []
        for editor in self.coordinate_editors[key]:
            text = editor.text().strip()
            if not text:
                raise FullModelGenerator.FullModelGenerationError(
                    "{}的X、Y、Z坐标不能为空".format(description)
                )
            values.append(float(text))
        return tuple(values)

    @staticmethod
    def _close_active_scene():
        import Jusme

        scene = Jusme.ActiveUSScene
        if scene is None:
            return
        scene_name = str(getattr(scene, "Name", "") or "").strip()
        if scene_name:
            Jusme.closeUSScene(scene_name)

    @staticmethod
    def _verify_imported_scene(model_name, configuration):
        import Jusme

        scene = Jusme.ActiveUSScene
        if scene is None:
            raise RuntimeError("完整ADM导入后没有活动模型")
        root = "." + str(model_name).strip().lstrip(".")
        missing = []
        for assembly in configuration["assemblies"].values():
            object_path = root + "." + assembly["anchor_path"].lstrip(".")
            try:
                node = scene.getObject(object_path)
            except Exception:
                node = None
            if node is None:
                missing.append(object_path)
        if missing:
            raise RuntimeError("完整模型缺少定位Marker：{}".format("、".join(missing)))
        recompute = getattr(scene, "recompute", None)
        if callable(recompute):
            recompute()

    def generate_and_import(self):
        try:
            self.configuration = self._selected_pair_configuration()
            nlg_target = self._coordinates("nlg", "前起")
            mlg_target = self._coordinates("mlg", "主起")
        except Exception as exc:
            QMessageBox.warning(self, "完整模型输入错误", str(exc))
            return

        answer = QMessageBox.question(
            self,
            "确认生成完整模型",
            "将根据两个定位点生成一个完整ADM，并关闭当前活动模型后导入。\n\n"
            "前起模型：{}\n前起坐标：{}\n\n"
            "主起模型：{}\n主起坐标：{}\n\n是否继续？".format(
                os.path.basename(self.source_paths["nlg"]),
                nlg_target,
                os.path.basename(self.source_paths["mlg"]),
                mlg_target,
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return

        self.generate_button.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        QApplication.processEvents()
        try:
            generated = FullModelGenerator.generate_combined_adm(
                self.model_full_dir,
                nlg_target,
                mlg_target,
                output_model_name=self.model_name_editor.text(),
                nlg_adm_path=self.source_paths["nlg"],
                mlg_adm_path=self.source_paths["mlg"],
            )
            self._close_active_scene()
            model_name = ModelImportRunner.import_adm_model(generated["adm_path"])
            generated["model_name"] = model_name
            self._verify_imported_scene(model_name, self.configuration)
            self.imported_context = generated
        except Exception as exc:
            print("[完整模型生成失败]\n{}".format(traceback.format_exc()))
            QMessageBox.critical(
                self,
                "完整模型生成失败",
                "完整模型生成或导入失败：\n{}\n\n详细信息已写入软件控制台。".format(exc),
            )
            return
        finally:
            QApplication.restoreOverrideCursor()
            self.generate_button.setEnabled(True)

        QMessageBox.information(
            self,
            "完整模型生成",
            "完整模型已生成并导入。\n\n模型：{}\nADM：{}".format(
                self.imported_context["model_name"],
                self.imported_context["adm_path"],
            ),
        )
        self.accept()


def show_full_model_generate_dialog(model_full_dir, parent=None):
    """Show the modal generator and return its imported context on success."""
    try:
        dialog = FullModelGenerateDialog(model_full_dir, parent)
    except Exception as exc:
        QMessageBox.critical(parent, "完整模型配置错误", str(exc))
        return None
    dialog.exec_()
    return dialog.imported_context
