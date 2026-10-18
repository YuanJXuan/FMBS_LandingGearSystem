# -*- coding: utf-8 -*-
"""半摇臂收放工程模板界面。"""

import os
import re
import sys

from PySide2.QtCore import Qt, QRect
from PySide2.QtGui import QDoubleValidator
from PySide2.QtWidgets import *


script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Retraction_dir = os.path.join(script_dir, "Retraction")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
sys.path.append(Share_dir)
sys.path.append(Retraction_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import ModelImportRunner
import MouseEventGraphicsView
import SelectionMonitor
import SemiRockerAdmParameterization
import SplineImportDialog
import VariableInputTable


TEMPLATE_NAME = "template_2_retract_semirocker"

SEMIROCKER_SIMULATION_PARAMETERS = [
    ("弹簧刚度(N/mm)", "SPRING_STIFFNESS"),
    ("弹簧自由长度(mm)", "SPRING_FREE_LENGTH"),
    ("弹簧阻尼(N·s/mm)", "SPRING_DAMPING"),
    ("仿真结束时间(s)", "SIM_END_TIME"),
    ("仿真步数", "SIM_STEPS"),
]

SEMIROCKER_TRAVEL_PARAMETERS = [
    ("作动筒行程(mm)", "ACTUATOR_STROKE"),
    ("收起时间(s)", "RETRACT_TIME"),
    ("上位保持时间(s)", "UP_HOLD_TIME"),
    ("放下时间(s)", "EXTEND_TIME"),
]

DEFAULT_PARAMETERS = {
    "SPRING_STIFFNESS": 100.0,
    "SPRING_FREE_LENGTH": 25.0,
    "SPRING_DAMPING": 10.0,
    "SIM_END_TIME": 5.0,
    "SIM_STEPS": 500.0,
    "ACTUATOR_STROKE": 635.0,
    "RETRACT_TIME": 1.0,
    "UP_HOLD_TIME": 1.0,
    "EXTEND_TIME": 1.0,
}

HARDPOINT_NAMES = [
    "hps_db_sf_atch",
    "hps_uc_sf_atch_l",
    "hps_uc_sf_atch_r",
    "hps_lc_bot",
    "hps_uc_top",
    "hps_db_uc_atch",
    "hps_uc_geompt",
    "hps_uc_bot",
    "hps_lc_top",
    "hps_lb_uc_atch",
]


def _scene_object(scene, relative_path):
    if scene is None:
        return None
    model_name = str(getattr(scene, "Name", "") or "").strip().lstrip(".")
    if not model_name:
        return None
    try:
        return scene.getObject(".{}.{}".format(model_name, relative_path))
    except Exception:
        return None


def _format_number(value):
    return "{:.12g}".format(float(value))


class SemiRockerRetractionDialog(QDialog):

    def __init__(self, parent=None):
        super(SemiRockerRetractionDialog, self).__init__(parent)
        print("开启半摇臂收放对话框构造函数")
        self.initUI()

    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        self.strModelName = ""

        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        leftLayout = QVBoxLayout()
        rect_list = [QRect(267, 27, 110, 27), QRect(380, 190, 110, 27)]
        hp_name_list = ["hps_db_sf_atch", "hps_db_uc_atch"]
        self.view = MouseEventGraphicsView.mouseProcessView(
            image_path,
            rect_list,
            hp_name_list,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_WIDTH,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_HEIGHT,
        )
        leftLayout.addWidget(self.view, 0, Qt.AlignTop | Qt.AlignHCenter)

        btnLayout = QHBoxLayout()
        self.modelGenerateButton = QPushButton("模型生成（PY）", self)
        self.modelGenerateButton.setEnabled(False)
        self.modelGenerateButton.setToolTip("该模板仅提供 ADM 模型导入")
        self.modelImportButton = QPushButton("模型导入（ADM）", self)
        self.splineImportButton = QPushButton("修改样条曲线", self)
        self.okPushButton = QPushButton("退出", self)
        for button in (
            self.modelGenerateButton,
            self.modelImportButton,
            self.splineImportButton,
            self.okPushButton,
        ):
            button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btnLayout.addStretch()
        btnLayout.addWidget(self.modelGenerateButton)
        btnLayout.addWidget(self.modelImportButton)
        btnLayout.addWidget(self.splineImportButton)
        btnLayout.addWidget(self.okPushButton)
        leftLayout.addLayout(btnLayout)
        mainLayout.addLayout(leftLayout, 4)

        self.tabs = QTabWidget()
        mainLayout.addWidget(self.tabs, 5)
        self._create_structure_tab()
        self._create_simulation_tab()
        self._create_travel_tab()
        self._load_parameter_values()

        self.okPushButton.clicked.connect(self.okClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.okParamTimeButton.clicked.connect(self.okParamTime)
        self.hpSelector.currentTextChanged.connect(self.hpSelectorChanged)
        self.view.mySignal.connect(self.mouseEventSlot)

        MouseEventGraphicsView.apply_standard_dialog(self)
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.selectionSlot)
        self.selectionMonitor.start()

    def _create_structure_tab(self):
        self.structTab = QWidget()
        layout = QFormLayout(self.structTab)

        self.hpSelector = QComboBox(self)
        self.hpSelector.addItem("请选择硬点")
        self.hpSelector.addItems(HARDPOINT_NAMES)
        layout.addRow("可调硬点：", self.hpSelector)

        self.hpName = QLineEdit(self)
        self.hpName.setReadOnly(True)
        layout.addRow("硬点名称：", self.hpName)
        self.xMarker = QLineEdit(self)
        self.yMarker = QLineEdit(self)
        self.zMarker = QLineEdit(self)
        layout.addRow("X坐标：", self.xMarker)
        layout.addRow("Y坐标：", self.yMarker)
        layout.addRow("Z坐标：", self.zMarker)
        for editor in (self.xMarker, self.yMarker, self.zMarker):
            editor.setEnabled(False)
            validator = QDoubleValidator(-1.0e9, 1.0e9, 12, editor)
            validator.setNotation(QDoubleValidator.StandardNotation)
            editor.setValidator(validator)

        self.markOkButton = QPushButton("设置硬点坐标")
        self.markOkButton.setEnabled(False)
        layout.addRow("", self.markOkButton)
        self.hpStatusLabel = QLabel("硬点参数化仅适用于半摇臂收放的 ADM 导入模型")
        self.hpStatusLabel.setWordWrap(True)
        self.hpStatusLabel.setStyleSheet("color: #666666;")
        layout.addRow("", self.hpStatusLabel)

        layout.addRow(QLabel(""), QLabel(""))
        self.selGeo = QLineEdit(self)
        self.selGeo.setReadOnly(True)
        layout.addRow("几何体：", self.selGeo)
        self.doubleRadius = QLineEdit(self)
        layout.addRow("半径：", self.doubleRadius)
        self.doubleLength = QLineEdit(self)
        self.doubleLength.setDisabled(True)
        layout.addRow("长度：", self.doubleLength)
        self.dimensionOkButton = QPushButton("设置圆柱尺寸")
        self.dimensionOkButton.setEnabled(False)
        layout.addRow("", self.dimensionOkButton)
        self.tabs.addTab(self.structTab, "结构参数")

    def _create_simulation_tab(self):
        self.simTab = QWidget()
        layout = QVBoxLayout(self.simTab)
        self.simVariableTable = VariableInputTable.VariableInputTable(
            SEMIROCKER_SIMULATION_PARAMETERS, self.simTab
        )
        layout.addWidget(self.simVariableTable)
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        self.simOkButton = QPushButton("设置仿真参数")
        buttonLayout.addWidget(self.simOkButton)
        layout.addLayout(buttonLayout)
        self.tabs.addTab(self.simTab, "仿真变量")

    def _create_travel_tab(self):
        self.travelTab = QWidget()
        layout = QVBoxLayout(self.travelTab)
        self.travelVariableTable = VariableInputTable.VariableInputTable(
            SEMIROCKER_TRAVEL_PARAMETERS, self.travelTab
        )
        layout.addWidget(self.travelVariableTable)
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        self.okParamTimeButton = QPushButton("设置行程参数")
        buttonLayout.addWidget(self.okParamTimeButton)
        layout.addLayout(buttonLayout)
        self.tabs.addTab(self.travelTab, "行程参数")

    def _set_parameter(self, name, value):
        tables = (self.simVariableTable, self.travelVariableTable)
        for table in tables:
            editors = table.editors()
            if name in editors:
                editors[name].setText(_format_number(value))
                return

    def _parameter(self, table, name):
        return float(table.editor(name).text().strip())

    def _load_parameter_values(self):
        values = dict(DEFAULT_PARAMETERS)
        scene = SelectionMonitor.get_active_scene()
        if not SemiRockerAdmParameterization.compatibility_error(scene):
            motion = _scene_object(scene, "MOTION_1")
            force = _scene_object(scene, "SFORCE_1")
            simulation = _scene_object(scene, "Last_Sim")
            self._read_motion_parameters(getattr(motion, "function", ""), values)
            self._read_force_parameters(getattr(force, "function", ""), values)
            self._read_simulation_parameters(
                getattr(simulation, "commands", ""), values
            )
        for name, value in values.items():
            self._set_parameter(name, value)

    @staticmethod
    def _read_motion_parameters(function, values):
        number = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eEdD][-+]?\d+)?"
        pattern = re.compile(
            r"STEP\s*\(\s*time\s*,\s*0\s*,\s*0\s*,\s*(%s)\s*,\s*(%s)\s*\)"
            r"\s*-\s*STEP\s*\(\s*time\s*,\s*(%s)\s*,\s*0\s*,\s*(%s)\s*,\s*(%s)\s*\)"
            % (number, number, number, number, number),
            re.I,
        )
        match = pattern.search(str(function or ""))
        if not match:
            return
        retract_time, first_stroke, extend_start, extend_end, _ = [
            float(value.replace("D", "E").replace("d", "e"))
            for value in match.groups()
        ]
        values["ACTUATOR_STROKE"] = abs(first_stroke)
        values["RETRACT_TIME"] = retract_time
        values["UP_HOLD_TIME"] = max(0.0, extend_start - retract_time)
        values["EXTEND_TIME"] = max(0.0, extend_end - extend_start)

    @staticmethod
    def _read_force_parameters(function, values):
        text = str(function or "")
        number = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eEdD][-+]?\d+)?"
        stiffness = re.search(r"^\s*-(%s)\s*\*\s*\(\s*DM\(" % number, text, re.I)
        free_length = re.search(r"\)\s*-\s*(%s)\s*\)" % number, text, re.I)
        damping = re.search(r"\)\s*-\s*(%s)\s*\*\s*VR\(" % number, text, re.I)
        if stiffness:
            values["SPRING_STIFFNESS"] = float(stiffness.group(1))
        if free_length:
            values["SPRING_FREE_LENGTH"] = float(free_length.group(1))
        if damping:
            values["SPRING_DAMPING"] = float(damping.group(1))

    @staticmethod
    def _read_simulation_parameters(commands, values):
        text = str(commands or "")
        end_time = re.search(r"\bend_time\s*=\s*([^\s]+)", text, re.I)
        steps = re.search(r"\bnumber_of_steps\s*=\s*([^\s]+)", text, re.I)
        try:
            if end_time:
                values["SIM_END_TIME"] = float(end_time.group(1))
            if steps:
                values["SIM_STEPS"] = float(steps.group(1))
        except ValueError:
            pass

    def hpSelectorChanged(self, hp_name):
        if hp_name and hp_name != "请选择硬点":
            self.mouseEventSlot(hp_name)

    def selectionSlot(self, node_name):
        node = SelectionMonitor.get_active_node(node_name)
        if node is None or SelectionMonitor.get_node_type(node) != "Fmbs::ShapeCylinder":
            self.strSelGeoFullName = ""
            self.selGeo.clear()
            self.doubleLength.clear()
            self.doubleRadius.clear()
            self.dimensionOkButton.setEnabled(False)
            return
        self.tabs.setCurrentIndex(0)
        self.strSelGeoFullName = node_name
        self.selGeo.setText(str(node_name).split(".")[-1])
        self.doubleLength.setText(_format_number(node.length))
        self.doubleRadius.setText(_format_number(node.radius))
        self.dimensionOkButton.setEnabled(True)

    def mouseEventSlot(self, hp_name):
        self.tabs.setCurrentIndex(0)
        scene = SelectionMonitor.get_active_scene()
        compatibility_error = SemiRockerAdmParameterization.compatibility_error(scene)
        hp_name = SemiRockerAdmParameterization.canonical_hardpoint_name(hp_name)
        selector_index = self.hpSelector.findText(hp_name)
        if selector_index >= 0 and selector_index != self.hpSelector.currentIndex():
            self.hpSelector.blockSignals(True)
            self.hpSelector.setCurrentIndex(selector_index)
            self.hpSelector.blockSignals(False)

        self.strSelFullName = SemiRockerAdmParameterization.hardpoint_path(
            hp_name, scene
        )
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        axes = SemiRockerAdmParameterization.get_rule(hp_name)
        if node is None:
            self.hpName.clear()
            for editor in (self.xMarker, self.yMarker, self.zMarker):
                editor.clear()
                editor.setEnabled(False)
            self.markOkButton.setEnabled(False)
            self.hpStatusLabel.setText(compatibility_error or "模型中未找到该硬点")
            self.hpStatusLabel.setStyleSheet("color: #b05a00;")
            return

        self.hpName.setText(hp_name)
        self.xMarker.setText(_format_number(node.location.x))
        self.yMarker.setText(_format_number(node.location.y))
        self.zMarker.setText(_format_number(node.location.z))
        compatible = not compatibility_error
        self.xMarker.setEnabled(bool(compatible and axes and "x" in axes))
        self.yMarker.setEnabled(bool(compatible and axes and "y" in axes))
        self.zMarker.setEnabled(bool(compatible and axes and "z" in axes))
        self.markOkButton.setEnabled(bool(compatible and axes))
        if not compatible:
            self.hpStatusLabel.setText(compatibility_error)
            self.hpStatusLabel.setStyleSheet("color: #b05a00;")
        else:
            self.hpStatusLabel.setText(
                "可修改坐标：{}；关联公式、几何和运动副将同步刷新".format(
                    "、".join(axis.upper() for axis in axes)
                )
            )
            self.hpStatusLabel.setStyleSheet("color: #666666;")

    def modelGenerate(self):
        QMessageBox.information(
            self,
            "模型生成",
            "template_2_retract_semirocker 仅支持 ADM 模型导入。",
        )

    def modelImport(self):
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_2_retract_semirocker"),
            TEMPLATE_NAME,
        )

    def openSplineImportDialog(self):
        SplineImportDialog.show_spline_import_dialog(self)

    def okMarkClickButton(self):
        if not all(editor.text().strip() for editor in (self.xMarker, self.yMarker, self.zMarker)):
            QMessageBox.warning(self, "硬点调整", "硬点坐标输入为空")
            return
        scene = SelectionMonitor.get_active_scene()
        if scene is None:
            QMessageBox.warning(self, "硬点调整", "当前没有活动模型")
            return

        self.markOkButton.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            result = SemiRockerAdmParameterization.adjust_hardpoint(
                self.strSelFullName,
                self.xMarker.text(),
                self.yMarker.text(),
                self.zMarker.text(),
                scene=scene,
            )
        except Exception as exc:
            print("[半摇臂收放参数化异常] {}".format(exc))
            QMessageBox.critical(self, "硬点调整异常", str(exc))
            return
        finally:
            QApplication.restoreOverrideCursor()
            axes = SemiRockerAdmParameterization.get_rule(self.strSelFullName)
            self.markOkButton.setEnabled(
                bool(SemiRockerAdmParameterization.is_compatible_scene(scene) and axes)
            )

        if not result.success:
            self.hpStatusLabel.setText(result.message)
            self.hpStatusLabel.setStyleSheet("color: #b00020;")
            QMessageBox.warning(self, "硬点调整失败", result.message)
            for error in result.errors:
                print("[半摇臂收放参数化错误] {}".format(error))
            return

        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if node is not None:
            self.xMarker.setText(_format_number(node.location.x))
            self.yMarker.setText(_format_number(node.location.y))
            self.zMarker.setText(_format_number(node.location.z))
        self.hpStatusLabel.setText(result.message)
        self.hpStatusLabel.setStyleSheet("color: #0b7a2a;")

    def okDimClickButton(self):
        try:
            radius = float(self.doubleRadius.text().strip())
        except ValueError:
            QMessageBox.warning(self, "圆柱尺寸", "请输入有效的半径")
            return
        if radius <= 0.0:
            QMessageBox.warning(self, "圆柱尺寸", "半径必须大于0")
            return
        scene = SelectionMonitor.get_active_scene()
        node = SelectionMonitor.get_active_node(self.strSelGeoFullName)
        if scene is None or node is None:
            return
        if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":
            node.radius = radius
            scene.recompute()

    def _compatible_scene_or_warn(self):
        scene = SelectionMonitor.get_active_scene()
        error = SemiRockerAdmParameterization.compatibility_error(scene)
        if error:
            QMessageBox.warning(self, "参数设置", error)
            return None
        return scene

    def okSimClickButton(self):
        if not self.simVariableTable.validate_values(self):
            return
        scene = self._compatible_scene_or_warn()
        if scene is None:
            return
        stiffness = self._parameter(self.simVariableTable, "SPRING_STIFFNESS")
        free_length = self._parameter(self.simVariableTable, "SPRING_FREE_LENGTH")
        damping = self._parameter(self.simVariableTable, "SPRING_DAMPING")
        end_time = self._parameter(self.simVariableTable, "SIM_END_TIME")
        step_value = self._parameter(self.simVariableTable, "SIM_STEPS")
        steps = int(round(step_value))
        if min(stiffness, free_length, damping, end_time) < 0.0 or end_time == 0.0:
            QMessageBox.warning(self, "参数设置", "刚度、自由长度、阻尼不能为负，仿真时间必须大于0")
            return
        if steps <= 0 or abs(step_value - steps) > 1.0e-9:
            QMessageBox.warning(self, "参数设置", "仿真步数必须是正整数")
            return

        force = _scene_object(scene, "SFORCE_1")
        simulation = _scene_object(scene, "Last_Sim")
        if force is None or simulation is None:
            QMessageBox.warning(self, "参数设置", "模型中缺少 SFORCE_1 或 Last_Sim")
            return
        root = ".{}".format(str(scene.Name).strip().lstrip("."))
        force.function = (
            "-{k}*(DM({root}.ges_upper_cylinder.MARKER_69,"
            "{root}.ges_lower_cylinder.MARKER_70)-{length})"
            "-{damping}*VR({root}.ges_upper_cylinder.MARKER_69,"
            "{root}.ges_lower_cylinder.MARKER_70)"
        ).format(
            k=_format_number(stiffness),
            root=root,
            length=_format_number(free_length),
            damping=_format_number(damping),
        )
        simulation.commands = (
            "simulation single_run transient type=auto_select initial_static=no "
            "end_time={} number_of_steps={} model_name={}"
        ).format(_format_number(end_time), steps, root)
        for node in (force, simulation):
            recompute = getattr(node, "recompute", None)
            if callable(recompute):
                recompute()
        scene.recompute()

    def okParamTime(self):
        if not self.travelVariableTable.validate_values(self):
            return
        scene = self._compatible_scene_or_warn()
        if scene is None:
            return
        stroke = self._parameter(self.travelVariableTable, "ACTUATOR_STROKE")
        retract_time = self._parameter(self.travelVariableTable, "RETRACT_TIME")
        hold_time = self._parameter(self.travelVariableTable, "UP_HOLD_TIME")
        extend_time = self._parameter(self.travelVariableTable, "EXTEND_TIME")
        if stroke <= 0.0 or retract_time <= 0.0 or hold_time < 0.0 or extend_time <= 0.0:
            QMessageBox.warning(
                self,
                "行程参数",
                "行程、收起时间和放下时间必须大于0，保持时间不能为负",
            )
            return
        motion = _scene_object(scene, "MOTION_1")
        if motion is None:
            QMessageBox.warning(self, "行程参数", "模型中缺少 MOTION_1")
            return
        extend_start = retract_time + hold_time
        extend_end = extend_start + extend_time
        motion.function = (
            "STEP(time,0,0,{retract},-{stroke})"
            "-STEP(time,{start},0,{end},-{stroke})"
        ).format(
            retract=_format_number(retract_time),
            stroke=_format_number(stroke),
            start=_format_number(extend_start),
            end=_format_number(extend_end),
        )
        recompute = getattr(motion, "recompute", None)
        if callable(recompute):
            recompute()
        scene.recompute()

    def closeEvent(self, event):
        self.selectionMonitor.stop()
        super(SemiRockerRetractionDialog, self).closeEvent(event)

    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()


def show_template_2_retract_semirocker_dialog(parent=None):
    dialog = SemiRockerRetractionDialog(parent)
    dialog.setWindowTitle("半摇臂收放仿真对话框")
    dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    dialog.show()
    return dialog


if __name__ == "__main__":
    _semirocker_dialog = show_template_2_retract_semirocker_dialog()
