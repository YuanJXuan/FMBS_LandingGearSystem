# 引入窗体
from PySide2.QtGui import QBrush,QColor
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Turn_dir = os.path.join(script_dir, "Turn")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Image_dir = os.path.join(script_dir, "Image")
Model_dir = os.path.join(script_dir, "Model")

sys.path.append(Share_dir)
sys.path.append(Turn_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import Common
import TurnFactory
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable


TURN_FORCE_SIMULATION_VARIABLES = [
    ("前起低压腔有效面积", "NLG_Aa"),
    ("前起低压腔初始体积", "NLG_V0"),
    ("前起低压腔初始压力", "NLG_P0"),
    ("气体多变指数", "n_Poly"),
    ("大气压力", "Patm"),
    ("油液密度", "rho_Oil"),
    ("前起主腔油液面积", "NLG_A_MAIN_OIL"),
    ("前起回油腔油液面积", "NLG_A_RET_OIL"),
    ("前起主腔正向节流面积", "NLG_A_MAIN_POS"),
    ("前起主腔负向节流面积", "NLG_A_MAIN_NEG"),
    ("前起回油腔正向节流面积", "NLG_A_RET_POS"),
    ("前起回油腔负向节流面积", "NLG_A_RET_NEG"),
    ("前起主腔流量系数", "NLG_MAIN_Cd"),
    ("前起回油腔流量系数", "NLG_RET_Cd"),
    ("主起低压腔有效面积", "MLG_Aa"),
    ("主起低压腔初始体积", "MLG_V0"),
    ("主起低压腔初始压力", "MLG_P0"),
    ("主起主腔油液面积", "MLG_A_MAIN_OIL"),
    ("主起回油腔油液面积", "MLG_A_RET_OIL"),
    ("主起主腔正向节流面积", "MLG_A_MAIN_POS"),
    ("主起主腔负向节流面积", "MLG_A_MAIN_NEG"),
    ("主起回油腔正向节流面积", "MLG_A_RET_POS"),
    ("主起回油腔负向节流面积", "MLG_A_RET_NEG"),
    ("主起主腔流量系数", "MLG_MAIN_Cd"),
    ("主起回油腔流量系数", "MLG_RET_Cd"),
    ("目标滑行速度", "V_sheding"),
    ("转弯开始时间(s)", "T_1"),
    ("转弯结束时间(s)", "T_2"),
    ("目标转弯角度(deg)", "angle"),
    ("前起轮胎质量", "NLG_m"),
    ("前起轮胎横向转动惯量", "NLG_Ixx_Iyy"),
    ("前起轮胎纵向转动惯量", "NLG_Izz"),
    ("主起轮胎质量", "MLG_m"),
    ("主起轮胎横向转动惯量", "MLG_Ixx_Iyy"),
    ("主起轮胎纵向转动惯量", "MLG_Izz"),
]



# 构建转弯插件对话框窗体
class Template5TurnForceDialog(QDialog):
    def __init__(self, parent=None):
        super(Template5TurnForceDialog, self).__init__(parent)
        print("开启Template5TurnForceDialog对话框构造函数")
        self.initUI()
        pass

    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        self.Parameterize = None
        self.strModelName = Common.getModelName()

        #--------------创建对话框主布局：左右结构[cite: 6]
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        # ================= 1. 左侧区域：图片交互区 + 底部按钮[cite: 6] =================
        leftLayout = QVBoxLayout()

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

        # 创建图片显示控件[cite: 6]
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
        self.modelGenerateButton.setEnabled(False)
        self.modelGenerateButton.setToolTip("该模板仅提供 ADM 模型导入")
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


        # ================= 2. 右侧区域：两个标签页 =================
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
        self.simVariableTable = VariableInputTable.VariableInputTable(
            TURN_FORCE_SIMULATION_VARIABLES,
            self.simTab,
        )
        simLayout.addWidget(self.simVariableTable)

        simButtonLayout = QHBoxLayout()
        simButtonLayout.addStretch()
        self.simOkButton = QPushButton("设置仿真参数")
        simButtonLayout.addWidget(self.simOkButton)
        simLayout.addLayout(simButtonLayout)

        self.tabs.addTab(self.simTab, "仿真变量")


        # ================= 数据读取与变量初始化[cite: 6] =================
        for row in TURN_FORCE_SIMULATION_VARIABLES:
            variable_name = row[1]
            editor = self.simVariableTable.editor(variable_name)
            read_only = bool(row[2]) if len(row) > 2 else False
            if read_only:
                node = SelectionMonitor.get_active_node(
                    ".{}.{}".format(self.strModelName, variable_name)
                )
                function = str(getattr(node, "function", "") or "")
                editor.setText(function or "由模型函数定义")
                editor.setToolTip(function)
                continue
            var_list = Common.getDesignVariable(variable_name)
            if var_list:
                editor.setText("{:.4f}".format(var_list[0]))


        # ================= 绑定信号和槽[cite: 6] =================
        self.okPushButton.clicked.connect(self.okClickButton)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        
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

            self.Parameterize = TurnFactory.TurnAdjustFactory(self.strSelFullName)

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

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)

    #--------------仿真参数设置按钮槽函数
    def okSimClickButton(self):
        if not self.simVariableTable.validate_values(self):
            return
        for row in TURN_FORCE_SIMULATION_VARIABLES:
            read_only = bool(row[2]) if len(row) > 2 else False
            if read_only:
                continue
            variable_name = row[1]
            Common.setDesignVariable(
                variable_name,
                float(self.simVariableTable.editor(variable_name).text()),
            )
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

    #-----------------定义文件浏览槽函数
    def modelGenerate(self) :
        QMessageBox.information(
            self,
            "模型生成",
            "template_5_turn_force 仅支持 ADM 模型导入。",
        )

    def modelImport(self):
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_5_turn_force"),
            "template_5_turn_force",
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
                    msgBox.setText("该硬点在转弯模板中不支持调整")
                    msgBox.exec_()
                    self.xMarker.setText(""); self.yMarker.setText(""); self.zMarker.setText("")
        pass

    #----------------------退出按钮点击事件
    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()


def show_template_5_turn_force_dialog(parent=None):
    dialog = Template5TurnForceDialog(parent)
    dialog.setWindowTitle("三点式转弯仿真（载荷驱动）")
    dialog.show()
    return dialog


if __name__ == '__main__':
    _template_5_turn_force_dialog = show_template_5_turn_force_dialog()

    
