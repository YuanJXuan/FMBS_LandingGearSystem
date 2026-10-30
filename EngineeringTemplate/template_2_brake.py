# 引入窗体
from PySide2.QtGui import QBrush,QColor
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Brake_dir = os.path.join(script_dir, "Brake")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
sys.path.append(Share_dir)
sys.path.append(Brake_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import Common
import BrakeFactory 
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable


BRAKE_DESIGN_VARIABLES = [
    ("气体多变指数", "MLG_n_Poly"),
    ("大气压力", "Patm"),
    ("油液密度", "MLG_rho_Oil"),
    ("低压腔有效面积", "MLG_A_LOW"),
    ("低压腔初始体积", "MLG_V_LOW"),
    ("低压腔初始压力", "MLG_P_LOW"),
    ("主腔油液面积", "MLG_A_MAIN_OIL"),
    ("回油腔油液面积", "MLG_A_RET_OIL"),
    ("主腔正向节流面积", "MLG_A_MAIN_POS"),
    ("主腔负向节流面积", "MLG_A_MAIN_NEG"),
    ("回油腔正向节流面积", "MLG_A_RET_POS"),
    ("回油腔负向节流面积", "MLG_A_RET_NEG"),
    ("回油腔流量系数", "MLG_RET_Cd"),
    ("主腔流量系数", "MLG_MAIN_Cd"),
    ("刹车力矩", "MLG_Tb"),
    ("缓冲器初始长度", "MLG_S0"),
    ("初始前进速度", "MLG_Vx"),
    ("轮胎质量", "MLG_m"),
    ("轮胎横向转动惯量", "MLG_Ixx_Iyy"),
    ("轮胎纵向转动惯量", "MLG_lzz"),
]


# 旧 PY 模型使用过的变量名称，仅用于保留旧入口的兼容性。
BRAKE_DESIGN_VARIABLE_ALIASES = {
    "MLG_n_Poly": ("GAMA",),
    "MLG_rho_Oil": ("rou",),
    "MLG_A_LOW": ("MLG_Aa",),
    "MLG_V_LOW": ("MLG_V0",),
    "MLG_P_LOW": ("MLG_P0",),
    "MLG_A_MAIN_OIL": ("MLG_Ah",),
    "MLG_A_RET_OIL": ("MLG_As",),
    "MLG_A_MAIN_POS": ("MLG_Ahd",),
    "MLG_A_MAIN_NEG": ("MLG_Ahdl",),
    "MLG_A_RET_POS": ("MLG_Asd",),
    "MLG_A_RET_NEG": ("MLG_Asdl",),
    "MLG_RET_Cd": ("MLG_Ch",),
    "MLG_MAIN_Cd": ("MLG_Cs",),
    "MLG_Tb": ("M",),
    "MLG_Vx": ("V", "V_sheding"),
}


def _brake_design_variable_names(variable_name):
    return (variable_name,) + BRAKE_DESIGN_VARIABLE_ALIASES.get(variable_name, ())


def _get_brake_design_variable(*names):
    for name in names:
        values = Common.getDesignVariable(name)
        if values:
            return values
    return []


def _set_brake_design_variable(value, *names):
    for name in names:
        if Common.setDesignVariable(name, value):
            return True
    return False


# 构建插件对话框窗体
class BrakeDialog(QDialog):
    
    def __init__(self, parent=None):
        super(BrakeDialog, self).__init__(parent)
        print("开启Brake对话框构造函数")
        self.initUI()

    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        self.Parameterize = None
        self.strModelName = Common.getModelName()

        #--------------创建对话框主布局：左右结构[cite: 3]
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        # ================= 1. 左侧区域：图片交互区 + 底部按钮[cite: 3] =================
        leftLayout = QVBoxLayout()
        
        # 定义图片中各硬点区域的位置和名称
        rect_list = []
        hp_name_list = []
        
        rect = QRect(42, 35, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hpl_uc_top")
        
        rect = QRect(42, 82, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hpl_lc_top")

        # 创建图片显示控件[cite: 3]
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


        # ================= 2. 右侧区域：标签页控件 =================
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
            BRAKE_DESIGN_VARIABLES,
            self.simTab,
        )
        simLayout.addWidget(self.simVariableTable)
        self.V_initial_Edit = self.simVariableTable.editor("MLG_Vx")
        self.LMLG_M_Edit = self.simVariableTable.editor("MLG_Tb")

        simButtonLayout = QHBoxLayout()
        simButtonLayout.addStretch()
        self.simOkButton = QPushButton("设置全部设计变量")
        simButtonLayout.addWidget(self.simOkButton)
        simLayout.addLayout(simButtonLayout)

        self.tabs.addTab(self.simTab, "设计变量")

        # ----------------获取工程模板中的设计变量[cite: 3]----------------
        for _meaning, variable_name in BRAKE_DESIGN_VARIABLES:
            var_list = _get_brake_design_variable(
                *_brake_design_variable_names(variable_name)
            )
            if var_list:
                self.simVariableTable.editor(variable_name).setText(
                    "{:.12g}".format(var_list[0])
                )

        print("开始定义按钮的槽函数")
        self.okPushButton.clicked.connect(self.okClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        print("槽函数")
        # 自定义槽函数[cite: 3]
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
        if node is None :    #---------------选择为空、场景切换中或节点已失效
            self.strSelGeoFullName = ""
            self.selGeo.setText("")
            self.doubleLength.setText("")
            self.doubleRadius.setText("")
            self.dimensionOkButton.setEnabled(False)
        else :
            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":    #----------------表示茉莉平台选择集选中了几何体
                # --- 选中几何体时自动跳转到结构参数标签页 ---
                self.tabs.setCurrentIndex(0)

                if self.strSelGeoFullName != node_name :    #-----------表示之前选中的与当前选中的几何体不一样
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

            self.Parameterize = BrakeFactory.BrakeAdjustFactory(self.strSelFullName)

            if hp_name == "hps_lta_uta_atch" or \
                hp_name == "hps_lta_lc_atch" or \
                hp_name == "hps_uta_uc_atch" :
                self.xMarker.setEnabled(True)
                self.yMarker.setEnabled(False)
                self.zMarker.setEnabled(True)
            elif hp_name == "hpl_uc_top" or \
                hp_name == "hpl_uc_bot" :
                self.xMarker.setEnabled(False)
                self.yMarker.setEnabled(False)
                self.zMarker.setEnabled(True)
            elif hp_name == "hps_db_sf_atch" or \
                hp_name == "hps_db_uc_atch" :
                self.xMarker.setEnabled(True)
                self.yMarker.setEnabled(False)
                self.zMarker.setEnabled(True)
            elif hp_name == "hpr_wheel_center" or \
                hp_name == "hpl_wheel_center" :
                self.xMarker.setEnabled(False)
                self.yMarker.setEnabled(True)
                self.zMarker.setEnabled(False)
            elif hp_name == "hpl_lc_top" or \
                hp_name == "hpl_lc_bot" :
                self.xMarker.setEnabled(False)
                self.yMarker.setEnabled(False)
                self.zMarker.setEnabled(True)
            else :
                self.xMarker.setEnabled(False)
                self.yMarker.setEnabled(False)
                self.zMarker.setEnabled(False)

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
            os.path.join(AutoGenerater_dir, "model_template_2_brake.py"),
            "GCMB",
            globals(),
        )

    #---------------------ADM主体 + 硬点CMD + 公式补丁导入
    def modelImport(self) :
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_2_brake"),
            "template_2_brake",
        )

    def openSplineImportDialog(self):
        SplineImportDialog.show_spline_import_dialog(self)

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)

    #---------------硬点点击设置按钮的槽函数
    def okMarkClickButton(self):
        strCoord = self.xMarker.text()
        if not strCoord :
            msgBox = QMessageBox(self)
            msgBox.setText("硬点的X坐标输入为空")
            msgBox.exec_()
            return
        xCoord = float(strCoord)

        strCoord = self.yMarker.text()
        if not strCoord :
            msgBox = QMessageBox(self)
            msgBox.setText("硬点的Y坐标输入为空")
            msgBox.exec_()
            return
        yCoord = float(strCoord)

        strCoord = self.zMarker.text()
        if not strCoord :
            msgBox = QMessageBox(self)
            msgBox.setText("硬点的Z坐标输入为空")
            msgBox.exec_()
            return
        zCoord = float(strCoord)

        ascene = SelectionMonitor.get_active_scene()
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if ascene is None or node is None:
            return
        if  node :
            if SelectionMonitor.get_node_type(node) == "Fmbs::Point" :
                if self.Parameterize :
                    node.location = Jusme.Vector(xCoord, yCoord, zCoord)
                    self.Parameterize.Adjust()
                    ascene.recompute()
                else :
                    msgBox = QMessageBox(self)
                    msgBox.setText("该硬点在刹车模板中不支持调整")
                    msgBox.exec_()
                    self.xMarker.setText("")
                    self.yMarker.setText("")
                    self.zMarker.setText("")
        pass

    #---------------圆柱体几何参数设置按钮槽函数
    def okDimClickButton(self):
        strRadius = self.doubleRadius.text()
        print(strRadius)
        if not strRadius :
            msgBox = QMessageBox(self)
            msgBox.setText("圆柱体的半径尺寸输入为空")
            msgBox.exec_()
            return
        
        doubleRadius = float(strRadius)
        ascene = SelectionMonitor.get_active_scene()
        node = SelectionMonitor.get_active_node(self.strSelGeoFullName)
        if ascene is None or node is None:
            return
        if node :
            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":
                node.radius = doubleRadius
                ascene.recompute()
        pass

    #--------------仿真参数设置按钮槽函数
    def okSimClickButton(self):
        if not self.simVariableTable.validate_values(self):
            return
        missing_variables = []
        for _meaning, variable_name in BRAKE_DESIGN_VARIABLES:
            editor = self.simVariableTable.editor(variable_name)
            if not _set_brake_design_variable(
                float(editor.text()),
                *_brake_design_variable_names(variable_name)
            ):
                missing_variables.append(variable_name)

        if missing_variables:
            QMessageBox.warning(
                self,
                "设计变量设置完成",
                "以下设计变量在当前模型中不存在，其他变量已继续设置：\n{}".format(
                    "、".join(missing_variables)
                ),
            )
        pass

    #----------------------退出按钮点击事件
    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()


def show_brake_dialog(parent=None):
    dialog = BrakeDialog(parent)
    dialog.setWindowTitle("刹车仿真对话框")
    dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    dialog.show()
    return dialog


if __name__ == '__main__':
    _brake_dialog = show_brake_dialog()
