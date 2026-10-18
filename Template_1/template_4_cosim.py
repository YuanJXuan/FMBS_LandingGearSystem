# 引入窗体
from PySide2.QtGui import QBrush,QColor
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Cosim_dir = os.path.join(script_dir, "Cosim")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
sys.path.append(Share_dir)
sys.path.append(Cosim_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import Common
import CosimFactory 
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable

# 构建插件对话框窗体
class CosimDialog(QDialog):
    
    def __init__(self, parent=None):
        super(CosimDialog, self).__init__(parent)
        print("开启cosim对话框构造函数")
        self.initUI()

    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        self.Parameterize = None
        self.strModelName = Common.getModelName()

        #--------------创建对话框主布局：左右结构[cite: 7]
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        # ================= 1. 左侧区域：图片交互区 + 底部按钮[cite: 7] =================
        leftLayout = QVBoxLayout()

        #----------------------定义图片中各硬点区域的位置和名称
        rect_list = []
        hp_name_list = []
        
        rect = QRect(42, 35, 78, 27); rect_list.append(rect); hp_name_list.append("hps_uc_top")
        rect = QRect(42, 82, 78, 27); rect_list.append(rect); hp_name_list.append("hps_lc_top")
        rect = QRect(5, 160, 78, 27); rect_list.append(rect); hp_name_list.append("hsg_1")
        rect = QRect(5, 213, 78, 27); rect_list.append(rect); hp_name_list.append("hsg_2")
        rect = QRect(5, 275, 78, 27); rect_list.append(rect); hp_name_list.append("hps_uc_bot")
        rect = QRect(5, 322, 78, 27); rect_list.append(rect); hp_name_list.append("hps_lc_bot")
        rect = QRect(98, 323, 110, 27); rect_list.append(rect); hp_name_list.append("hpl_wheel_center")
        rect = QRect(267, 27, 110, 27); rect_list.append(rect); hp_name_list.append("hps_db_sf_atch")
        rect = QRect(380, 190, 110, 27); rect_list.append(rect); hp_name_list.append("hps_db_uc_atch")
        rect = QRect(380, 253, 110, 27); rect_list.append(rect); hp_name_list.append("hps_lta_uta_atch")
        rect = QRect(380, 287, 110, 27); rect_list.append(rect); hp_name_list.append("hps_uta_uc_atch")
        rect = QRect(380, 322, 110, 27); rect_list.append(rect); hp_name_list.append("hps_lta_lc_atch")

        # 创建图片显示控件[cite: 7]
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
        
        self.hpName = QLineEdit(self)
        sub2FormLayout.addRow("硬点名称：", self.hpName)
        self.xMarker = QLineEdit(self)
        sub2FormLayout.addRow("X坐标：", self.xMarker)
        self.yMarker = QLineEdit(self)
        sub2FormLayout.addRow("Y坐标：", self.yMarker)
        self.zMarker = QLineEdit(self)
        sub2FormLayout.addRow("Z坐标：", self.zMarker)
        self.markOkButton = QPushButton("设置硬点坐标")
        sub2FormLayout.addRow("", self.markOkButton)
        self.markOkButton.setEnabled(False)

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
            ("阻力系数(/)", "NLG_DRAG_COEFF"),
            ("投影面积(㎡)", "NLG_PROJ_AREA"),
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
            ("前起收起载荷(N)", "NLG_RETRACT_FORCE"),
            ("前起收起载荷增压时间(s)", "NLG_RETRACT_RAMP_UP"),
            ("前起收起载荷持续时间(s)", "NLG_RETRACT_HOLD_TIME"),
            ("前起收起载荷泄压时间(s)", "NLG_RETRACT_RETRACT_RAMP_DOWN"),
            ("前起放下载荷(N)", "NLG_EXTEND_FORCE"),
            ("前起放下载荷增压时间(s)", "NLG_EXTEND_RAMP_UP"),
            ("前起放下载荷持续时间(s)", "NLG_EXTEND_HOLD_TIME"),
            ("前起放下载荷泄压时间(s)", "NLG_EXTEND_RETRACT_RAMP_DOWN"),
        ], self.travelTab)
        travelLayout.addWidget(self.travelVariableTable)
        self.ret_disp_edit = self.travelVariableTable.editor("NLG_ACTUATOR_STROKE")
        self.up_F_edit = self.travelVariableTable.editor("NLG_RETRACT_FORCE")
        self.up_t1_edit = self.travelVariableTable.editor("NLG_RETRACT_RAMP_UP")
        self.up_t2_edit = self.travelVariableTable.editor("NLG_RETRACT_HOLD_TIME")
        self.up_t3_edit = self.travelVariableTable.editor("NLG_RETRACT_RETRACT_RAMP_DOWN")
        self.down_F_edit = self.travelVariableTable.editor("NLG_EXTEND_FORCE")
        self.down_t1_edit = self.travelVariableTable.editor("NLG_EXTEND_RAMP_UP")
        self.down_t2_edit = self.travelVariableTable.editor("NLG_EXTEND_HOLD_TIME")
        self.down_t3_edit = self.travelVariableTable.editor("NLG_EXTEND_RETRACT_RAMP_DOWN")

        self.okParamTimeButton = QPushButton("设置行程参数", self)
        travelButtonLayout = QHBoxLayout()
        travelButtonLayout.addStretch()
        travelButtonLayout.addWidget(self.okParamTimeButton)
        travelLayout.addLayout(travelButtonLayout)

        self.tabs.addTab(self.travelTab, "行程参数")


        # ================= 数据读取与变量初始化[cite: 7] =================
        var_list = Common.getDesignVariable("NLG_DRAG_COEFF")
        if var_list : self.c0Edit.setText("{:.8f}".format(var_list[0]))
      
        var_list = Common.getDesignVariable("NLG_PROJ_AREA")
        if var_list : self.paEdit.setText("{:.4f}".format(var_list[0]))

        var_list = Common.getDesignVariable("AIR_DENSITY")
        if var_list : self.mi_duEdit.setText("{:.4f}".format(var_list[0]))

        var_list = Common.getDesignVariable("AIR_VELOCITY")
        if var_list : self.windVEdit.setText("{:.4f}".format(var_list[0]))

        # 行程参数读取
        var_list = Common.getDesignVariable("NLG_ACTUATOR_STROKE")
        if var_list: self.ret_disp_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_RETRACT_FORCE")
        if var_list: self.up_F_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_RETRACT_RAMP_UP")
        if var_list: self.up_t1_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_RETRACT_HOLD_TIME")
        if var_list: self.up_t2_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_RETRACT_RETRACT_RAMP_DOWN")
        if var_list: self.up_t3_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_EXTEND_FORCE")
        if var_list: self.down_F_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_EXTEND_RAMP_UP")
        if var_list: self.down_t1_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_EXTEND_HOLD_TIME")
        if var_list: self.down_t2_edit.setText("{:.4f}".format(var_list[0]))
        var_list = Common.getDesignVariable("NLG_EXTEND_RETRACT_RAMP_DOWN")
        if var_list: self.down_t3_edit.setText("{:.4f}".format(var_list[0]))


        # ================= 绑定信号和槽[cite: 7] =================
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.okPushButton.clicked.connect(self.okClickButton)
        self.okParamTimeButton.clicked.connect(self.okParamTime)

        # 自定义槽函数
        self.view.mySignal.connect(self.mouseEventSlot)

        MouseEventGraphicsView.apply_standard_dialog(self)

        # 在 Qt 主线程中监听宿主选择集，避免跨线程访问场景对象。
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.selectionSlot)
        self.selectionMonitor.start()

        pass

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

        self.strSelFullName = ".{}.ground.{}".format(self.strModelName, hp_name)
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if node :
            self.hpName.setText(hp_name)
            self.xMarker.setText("{:.4f}".format(node.location.x))
            self.yMarker.setText("{:.4f}".format(node.location.y))
            self.zMarker.setText("{:.4f}".format(node.location.z))

            self.Parameterize = CosimFactory.CosimAdjustFactory(self.strSelFullName)

            if hp_name == "hps_lta_uta_atch" or \
                hp_name == "hps_lta_lc_atch" or \
                hp_name == "hps_uta_uc_atch" :
                self.xMarker.setEnabled(True); self.yMarker.setEnabled(False); self.zMarker.setEnabled(True)
            elif hp_name == "hps_uc_top" or \
                hp_name == "hps_uc_bot" :
                self.xMarker.setEnabled(False); self.yMarker.setEnabled(False); self.zMarker.setEnabled(True)
            elif hp_name == "hps_db_sf_atch" or \
                hp_name == "hps_db_uc_atch" :
                self.xMarker.setEnabled(True); self.yMarker.setEnabled(False); self.zMarker.setEnabled(True)
            elif hp_name == "hpr_wheel_center" or \
                hp_name == "hpl_wheel_center" :
                self.xMarker.setEnabled(False); self.yMarker.setEnabled(True); self.zMarker.setEnabled(False)
            elif hp_name == "hps_lc_top" or \
                hp_name == "hps_lc_bot" :
                self.xMarker.setEnabled(False); self.yMarker.setEnabled(False); self.zMarker.setEnabled(True)
            else :
                self.xMarker.setEnabled(False); self.yMarker.setEnabled(False); self.zMarker.setEnabled(False)

            self.markOkButton.setEnabled(True)
        else :
            self.hpName.setText("")
            self.xMarker.setText("")
            self.yMarker.setText("")
            self.zMarker.setText("")
            self.markOkButton.setEnabled(False)
            self.Parameterize = None
        pass

    #---------------------定义文件浏览槽函数
    def modelGenerate(self) :
        ModelScriptRunner.generate_model_from_dialog(
            self,
            os.path.join(AutoGenerater_dir, "model_template_4_cosim.py"),
            "retract_suo_force_nlg_mlg",
            globals(),
        )

    #---------------------ADM主体 + 硬点CMD + 公式补丁导入
    def modelImport(self) :
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_4_retract"),
            "template_4_retract",
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
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if ascene is None or node is None:
            return
        if  node :
            if SelectionMonitor.get_node_type(node) == "Fmbs::Point" :
                if self.Parameterize :
                    node.location = Jusme.Vector(float(strX), float(strY), float(strZ))
                    self.Parameterize.Adjust()
                    ascene.recompute()
                else :
                    msgBox = QMessageBox(self)
                    msgBox.setText("该硬点在联合仿真模板中不支持调整")
                    msgBox.exec_()
                    self.xMarker.setText(""); self.yMarker.setText(""); self.zMarker.setText("")
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
        Common.setDesignVariable("NLG_DRAG_COEFF", float(self.c0Edit.text()))
        Common.setDesignVariable("NLG_PROJ_AREA", float(self.paEdit.text()))
        Common.setDesignVariable("AIR_DENSITY", float(self.mi_duEdit.text()))
        Common.setDesignVariable("AIR_VELOCITY", float(self.windVEdit.text()))
        pass

    #--------------行程参数设置槽函数
    def okParamTime(self):
        if not self.travelVariableTable.validate_values(self):
            return
        Common.setDesignVariable("NLG_ACTUATOR_STROKE", float(self.ret_disp_edit.text()))
        Common.setDesignVariable("NLG_RETRACT_FORCE", float(self.up_F_edit.text()))
        Common.setDesignVariable("NLG_RETRACT_RAMP_UP", float(self.up_t1_edit.text()))
        Common.setDesignVariable("NLG_RETRACT_HOLD_TIME", float(self.up_t2_edit.text()))
        Common.setDesignVariable("NLG_RETRACT_RETRACT_RAMP_DOWN", float(self.up_t3_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_FORCE", float(self.down_F_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_RAMP_UP", float(self.down_t1_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_HOLD_TIME", float(self.down_t2_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_RETRACT_RAMP_DOWN", float(self.down_t3_edit.text()))
        pass

    #----------------------退出按钮点击事件
    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)


def show_cosim_dialog(parent=None):
    dialog = CosimDialog(parent)
    dialog.setWindowTitle("联合仿真对话框")
    dialog.show()
    return dialog


if __name__ == '__main__':
    _cosim_dialog = show_cosim_dialog()

    
