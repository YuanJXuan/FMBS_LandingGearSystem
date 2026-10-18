# 引入窗体
from PySide2.QtGui import QBrush,QColor,QDoubleValidator
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Retraction_dir = os.path.join(script_dir, "Retraction")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
sys.path.append(Share_dir)
sys.path.append(Retraction_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")


import Jusme
import Common
import RetractionAdmParameterization
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable

# 构建插件对话框窗体
class RetractionDialog(QDialog):
    
    def __init__(self, parent=None):
        super(RetractionDialog, self).__init__(parent)
        print("开启Retraction对话框构造函数")
        self.initUI()

    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        active_scene = SelectionMonitor.get_active_scene()
        self.strModelName = getattr(active_scene, "Name", "") if active_scene else ""

        #--------------创建对话框主布局：左右结构[cite: 4]
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        # ================= 1. 左侧区域：图片交互区 + 底部按钮[cite: 4] =================
        leftLayout = QVBoxLayout()

        # 定义图片中各硬点区域的位置和名称
        rect_list = []
        hp_name_list = []
        
        rect = QRect(267, 27, 110, 27); rect_list.append(rect); hp_name_list.append("hps_db_sf_atch")
        rect = QRect(380, 190, 110, 27); rect_list.append(rect); hp_name_list.append("hps_db_uc_atch")

        # 创建图片显示控件[cite: 4]
        self.view = MouseEventGraphicsView.mouseProcessView(
            image_path, rect_list, hp_name_list,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_WIDTH,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_HEIGHT
        )
        leftLayout.addWidget(self.view, 0, Qt.AlignTop | Qt.AlignHCenter)

        # 底部操作按钮
        btnLayout = QHBoxLayout()
        self.modelGenerateButton = QPushButton("模型生成（PY）", self)
        self.modelGenerateButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.modelImportButton = QPushButton("模型导入（ADM）", self)
        self.modelImportButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.splineImportButton = QPushButton("修改样条曲线", self)
        self.splineImportButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.okPushButton = QPushButton("退出", self)
        self.okPushButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btnLayout.addStretch()
        btnLayout.addWidget(self.modelGenerateButton)
        btnLayout.addWidget(self.modelImportButton)
        btnLayout.addWidget(self.splineImportButton)
        btnLayout.addWidget(self.okPushButton)
        leftLayout.addLayout(btnLayout)

        mainLayout.addLayout(leftLayout, 4)


        # ================= 2. 右侧区域：三个标签页 =================
        self.tabs = QTabWidget()
        mainLayout.addWidget(self.tabs, 5)

        # --- Tab 1: 结构参数 ---
        self.structTab = QWidget()
        sub2FormLayout = QFormLayout(self.structTab)

        self.hpSelector = QComboBox(self)
        self.hpSelector.addItem("请选择硬点")
        self.hpSelector.addItems([
            "hps_db_sf_atch",
            "hps_db_uc_atch",
            "hps_rod_top",
            "hps_rod_bot",
        ])
        sub2FormLayout.addRow("可调硬点：", self.hpSelector)
        
        self.hpName = QLineEdit(self)
        self.hpName.setReadOnly(True)
        sub2FormLayout.addRow("硬点名称：", self.hpName)
        self.xMarker = QLineEdit(self)
        self.xMarker.setEnabled(False)
        sub2FormLayout.addRow("X坐标：", self.xMarker)
        self.yMarker = QLineEdit(self)
        self.yMarker.setEnabled(False)
        sub2FormLayout.addRow("Y坐标：", self.yMarker)
        self.zMarker = QLineEdit(self)
        self.zMarker.setEnabled(False)
        sub2FormLayout.addRow("Z坐标：", self.zMarker)
        for editor in (self.xMarker, self.yMarker, self.zMarker):
            validator = QDoubleValidator(-1.0e9, 1.0e9, 12, editor)
            validator.setNotation(QDoubleValidator.StandardNotation)
            editor.setValidator(validator)
        self.markOkButton = QPushButton("设置硬点坐标")
        sub2FormLayout.addRow("", self.markOkButton)
        self.markOkButton.setEnabled(False)
        self.hpStatusLabel = QLabel("硬点参数化仅适用于template_2_retract的ADM导入模型")
        self.hpStatusLabel.setWordWrap(True)
        self.hpStatusLabel.setStyleSheet("color: #666666;")
        sub2FormLayout.addRow("", self.hpStatusLabel)

        sub2FormLayout.addRow(QLabel(""), QLabel(""))

        self.selGeo = QLineEdit(self)
        sub2FormLayout.addRow("几何体：", self.selGeo)
        self.doubleRadius = QLineEdit(self)
        sub2FormLayout.addRow("半径：", self.doubleRadius)
        self.doubleLength = QLineEdit(self)
        sub2FormLayout.addRow("长度：", self.doubleLength)
        self.doubleLength.setDisabled(True)
        self.dimensionOkButton = QPushButton("设置圆柱尺寸")
        sub2FormLayout.addRow("", self.dimensionOkButton)
        self.dimensionOkButton.setEnabled(False)

        self.tabs.addTab(self.structTab, "结构参数")


        # --- Tab 2: 仿真变量 ---
        self.simTab = QWidget()
        simLayout = QVBoxLayout(self.simTab)
        self.simVariableTable = VariableInputTable.VariableInputTable([
            ("前起阻力系数(/)", "NLG_DRAG_COEFF"),
            ("前起投影面积(㎡)", "NLG_PROJ_AREA"),
            ("空气密度(kg/m³)", "AIR_DENSITY"),
            ("气流速度(m/s)", "AIR_VELOCITY"),
        ], self.simTab)
        simLayout.addWidget(self.simVariableTable)
        self.c0Edit = self.simVariableTable.editor("NLG_DRAG_COEFF")
        self.paEdit = self.simVariableTable.editor("NLG_PROJ_AREA")
        self.mi_duEdit = self.simVariableTable.editor("AIR_DENSITY")
        self.windVEdit = self.simVariableTable.editor("AIR_VELOCITY")

        simButtonLayout = QHBoxLayout()
        simButtonLayout.addStretch()
        self.simOkButton = QPushButton("设置仿真参数")
        simButtonLayout.addWidget(self.simOkButton)
        simLayout.addLayout(simButtonLayout)

        self.tabs.addTab(self.simTab, "仿真变量")


        # --- Tab 3: 行程参数 ---
        self.travelTab = QWidget()
        travelLayout = QVBoxLayout(self.travelTab)
        self.travelVariableTable = VariableInputTable.VariableInputTable([
            ("前起作动筒行程(mm)", "NLG_ACTUATOR_STROKE"),
            ("前起收起时间(s)", "NLG_RETRACT_TIME"),
            ("前起上位保持时间(s)", "NLG_UP_HOLD_TIME"),
            ("前起放下时间(s)", "NLG_EXTEND_TIME"),
        ], self.travelTab)
        travelLayout.addWidget(self.travelVariableTable)
        self.NLG_ret_disp_edit = self.travelVariableTable.editor("NLG_ACTUATOR_STROKE")
        self.nlg_up_time_edit = self.travelVariableTable.editor("NLG_RETRACT_TIME")
        self.nlg_hold_time_edit = self.travelVariableTable.editor("NLG_UP_HOLD_TIME")
        self.nlg_down_time_edit = self.travelVariableTable.editor("NLG_EXTEND_TIME")

        self.okParamTimeButton = QPushButton("设置行程参数", self)
        travelButtonLayout = QHBoxLayout()
        travelButtonLayout.addStretch()
        travelButtonLayout.addWidget(self.okParamTimeButton)
        travelLayout.addLayout(travelButtonLayout)

        self.tabs.addTab(self.travelTab, "行程参数")


        # ================= 数据读取与变量初始化[cite: 4] =================
        print("开始----------读取设计变量C0")
        var_list = Common.getDesignVariable("NLG_DRAG_COEFF")
        if var_list :
            self.c0Edit.setText("{:.8f}".format(var_list[0]))
      
        print("开始----------读取设计变量pa")
        var_list = Common.getDesignVariable("NLG_PROJ_AREA")
        if var_list :
            self.paEdit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量mi_du")
        var_list = Common.getDesignVariable("AIR_DENSITY")
        if var_list :
            self.mi_duEdit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量windV")
        var_list = Common.getDesignVariable("AIR_VELOCITY")
        if var_list :
            self.windVEdit.setText("{:.4f}".format(var_list[0]))

        # 行程参数读取
        var_list = Common.getDesignVariable("NLG_ACTUATOR_STROKE")
        if var_list: self.NLG_ret_disp_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_RETRACT_TIME")
        if var_list: self.nlg_up_time_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_UP_HOLD_TIME")
        if var_list: self.nlg_hold_time_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_EXTEND_TIME")
        if var_list: self.nlg_down_time_edit.setText("{:.4f}".format(var_list[0]))


        # ================= 绑定信号和槽[cite: 4] =================
        print("开始定义按钮的槽函数")
        self.okPushButton.clicked.connect(self.okClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.okParamTimeButton.clicked.connect(self.okParamTime)
        self.hpSelector.currentTextChanged.connect(self.hpSelectorChanged)

        # 自定义槽函数
        self.view.mySignal.connect(self.mouseEventSlot)

        MouseEventGraphicsView.apply_standard_dialog(self)

        # 在 Qt 主线程中监听宿主选择集，避免跨线程访问场景对象。
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.selectionSlot)
        self.selectionMonitor.start()

        pass

    def hpSelectorChanged(self, hp_name):
        if hp_name and hp_name != "请选择硬点":
            self.mouseEventSlot(hp_name)

    #------------------------自定义监听茉莉平台鼠标消息槽函数
    def selectionSlot(self, node_name) :
        node = SelectionMonitor.get_active_node(node_name)
        if node is None :
            self.strSelGeoFullName = ""
            self.selGeo.setText("")
            self.doubleLength.setText("")
            self.doubleRadius.setText("")
            self.dimensionOkButton.setEnabled(False)
        else :
            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":
                # --- 选中几何体时自动跳转到结构参数标签页 ---
                self.tabs.setCurrentIndex(0)

                if self.strSelGeoFullName != node_name :
                    self.strSelGeoFullName = node_name
                    strSelGeoName = Common.splitStringLast(self.strSelGeoFullName)
                    self.selGeo.setText(strSelGeoName)
                    self.doubleLength.setText("{:.4f}".format(node.length))
                    self.doubleRadius.setText("{:.4f}".format(node.radius))
                    self.dimensionOkButton.setEnabled(True)
            else :
                self.selGeo.setText("")
                self.doubleLength.setText("")
                self.doubleRadius.setText("")
                self.dimensionOkButton.setEnabled(False)
        pass

    #---------------------自定义鼠标按下消息槽函数
    def mouseEventSlot(self, hp_name) :
        # --- 点击图片硬点时自动跳转到结构参数标签页 ---
        self.tabs.setCurrentIndex(0)

        ascene = SelectionMonitor.get_active_scene()
        self.strModelName = getattr(ascene, "Name", "") if ascene else ""
        compatibility_error = RetractionAdmParameterization.compatibility_error(ascene)
        hp_name = RetractionAdmParameterization.canonical_hardpoint_name(hp_name)
        selector_index = self.hpSelector.findText(hp_name)
        if selector_index >= 0 and selector_index != self.hpSelector.currentIndex():
            self.hpSelector.blockSignals(True)
            self.hpSelector.setCurrentIndex(selector_index)
            self.hpSelector.blockSignals(False)
        self.strSelFullName = RetractionAdmParameterization.hardpoint_path(
            hp_name,
            ascene,
        )
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if node :
            self.hpName.setText(hp_name)
            self.xMarker.setText("{:.12g}".format(node.location.x))
            self.yMarker.setText("{:.12g}".format(node.location.y))
            self.zMarker.setText("{:.12g}".format(node.location.z))

            axes = RetractionAdmParameterization.get_rule(hp_name)
            is_retract_model = not compatibility_error
            self.xMarker.setEnabled(bool(is_retract_model and axes and "x" in axes))
            self.yMarker.setEnabled(bool(is_retract_model and axes and "y" in axes))
            self.zMarker.setEnabled(bool(is_retract_model and axes and "z" in axes))
            self.markOkButton.setEnabled(bool(is_retract_model and axes))

            if not is_retract_model:
                self.hpStatusLabel.setText(compatibility_error)
                self.hpStatusLabel.setStyleSheet("color: #b05a00;")
            elif not axes:
                self.hpStatusLabel.setText("该硬点暂不支持参数化调整")
                self.hpStatusLabel.setStyleSheet("color: #b05a00;")
            else:
                self.hpStatusLabel.setText(
                    "可修改坐标：{}；其余坐标将保持不变".format(
                        "、".join(axis.upper() for axis in axes)
                    )
                )
                self.hpStatusLabel.setStyleSheet("color: #666666;")
        else :
            self.hpName.setText("")
            self.xMarker.setText("")
            self.yMarker.setText("")
            self.zMarker.setText("")
            self.xMarker.setEnabled(False)
            self.yMarker.setEnabled(False)
            self.zMarker.setEnabled(False)
            self.markOkButton.setEnabled(False)
            if compatibility_error:
                self.hpStatusLabel.setText(compatibility_error)
            else:
                self.hpStatusLabel.setText("模型中未找到该硬点")
            self.hpStatusLabel.setStyleSheet("color: #b05a00;")
        pass
   
    #---------------------定义文件浏览槽函数
    def modelGenerate(self) :
        ModelScriptRunner.generate_model_from_dialog(
            self,
            os.path.join(AutoGenerater_dir, "model_template_2_retract.py"),
            "retract_NLG_motion",
            globals(),
        )

    #---------------------ADM主体 + 硬点CMD + 公式补丁导入
    def modelImport(self) :
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_2_retract"),
            "template_2_retract",
        )

    def openSplineImportDialog(self):
        SplineImportDialog.show_spline_import_dialog(self)

    #---------------硬点点击设置按钮的槽函数
    def okMarkClickButton(self):
        strX = self.xMarker.text()
        strY = self.yMarker.text()
        strZ = self.zMarker.text()
        if not strX or not strY or not strZ :
            msgBox = QMessageBox(self)
            msgBox.setText("硬点坐标输入为空")
            msgBox.exec_()
            return

        ascene = SelectionMonitor.get_active_scene()
        if ascene is None:
            QMessageBox.warning(self, "硬点调整", "当前没有活动模型")
            return

        self.markOkButton.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        result = None
        try:
            result = RetractionAdmParameterization.adjust_hardpoint(
                self.strSelFullName,
                strX,
                strY,
                strZ,
                scene=ascene,
            )
        except Exception as exc:
            print("[Retract参数化异常] {}".format(exc))
            self.hpStatusLabel.setText("硬点调整发生未预期异常，模型未确认修改")
            self.hpStatusLabel.setStyleSheet("color: #b00020;")
            QMessageBox.critical(
                self,
                "硬点调整异常",
                "硬点参数化发生未预期异常：{}\n请重新导入模型后重试。".format(exc),
            )
        finally:
            QApplication.restoreOverrideCursor()

        axes = RetractionAdmParameterization.get_rule(self.strSelFullName)
        is_retract_model = RetractionAdmParameterization.is_compatible_scene(ascene)
        self.markOkButton.setEnabled(bool(is_retract_model and axes))
        if result is None:
            return
        if not result.success:
            self.hpStatusLabel.setText(result.message)
            self.hpStatusLabel.setStyleSheet("color: #b00020;")
            QMessageBox.warning(self, "硬点调整失败", result.message)
            for error in result.errors:
                print("[Retract参数化错误] {}".format(error))
        else:
            node = SelectionMonitor.get_active_node(self.strSelFullName)
            if node is not None:
                self.xMarker.setText("{:.12g}".format(node.location.x))
                self.yMarker.setText("{:.12g}".format(node.location.y))
                self.zMarker.setText("{:.12g}".format(node.location.z))
            self.hpStatusLabel.setText(result.message)
            self.hpStatusLabel.setStyleSheet("color: #0b7a2a;")
        pass

    #---------------圆柱体几何参数设置按钮槽函数
    def okDimClickButton(self):
        strRadius = self.doubleRadius.text()
        if not strRadius :
            msgBox = QMessageBox(self)
            msgBox.setText("圆柱体的半径尺寸输入为空")
            msgBox.exec_()
            return
        
        ascene = SelectionMonitor.get_active_scene()
        node = SelectionMonitor.get_active_node(self.strSelGeoFullName)
        if ascene is None or node is None:
            return
        if node :
            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":
                node.radius = float(strRadius)
                ascene.recompute()
        pass

    #--------------仿真参数设置按钮槽函数
    def okSimClickButton(self):
        if not self.simVariableTable.validate_values(self):
            return
        Common.setDesignVariable("NLG_DRAG_COEFF",float(self.c0Edit.text()))
        Common.setDesignVariable("NLG_PROJ_AREA",float(self.paEdit.text()))
        Common.setDesignVariable("AIR_DENSITY",float(self.mi_duEdit.text()))
        Common.setDesignVariable("AIR_VELOCITY",float(self.windVEdit.text()))

    #--------------行程参数设置槽函数
    def okParamTime(self):
        if not self.travelVariableTable.validate_values(self):
            return
        Common.setDesignVariable("NLG_ACTUATOR_STROKE",float(self.NLG_ret_disp_edit.text()))
        Common.setDesignVariable("NLG_RETRACT_TIME",float(self.nlg_up_time_edit.text()))
        Common.setDesignVariable("NLG_UP_HOLD_TIME",float(self.nlg_hold_time_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_TIME",float(self.nlg_down_time_edit.text()))
        pass

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)

    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()


def show_retraction_dialog(parent=None):
    dialog = RetractionDialog(parent)
    dialog.setWindowTitle("构造收放对话框")
    dialog.show()
    return dialog


if __name__ == '__main__':
    _retraction_dialog = show_retraction_dialog()

    
