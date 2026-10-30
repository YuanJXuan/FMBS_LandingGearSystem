# 引入窗体
from PySide2.QtGui import QBrush,QColor
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Motion_dir = os.path.join(script_dir, "Motion")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
sys.path.append(Share_dir)
sys.path.append(Motion_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import Common
import MotionFactory 
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable


# 构建插件对话框窗体
class MotionDialog(QDialog):
    
    def __init__(self, parent=None):
        super(MotionDialog, self).__init__(parent)
        print("开启Motion对话框构造函数")
        self.initUI()
        
    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        self.Parameterize = None
        self.strModelName = Common.getModelName()
        
        #--------------创建对话框主布局：左右结构
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        # ================= 1. 左侧区域：图片交互区 + 底部按钮 =================
        leftLayout = QVBoxLayout()
        
        # 定义图片中各硬点区域的位置和名称
        rect_list = []
        hp_name_list = []
        
        rect_list.append(QRect(42, 35, 78, 27)); hp_name_list.append("hps_uc_top")
        rect_list.append(QRect(42, 82, 78, 27)); hp_name_list.append("hps_lc_top")
        rect_list.append(QRect(5, 160, 78, 27)); hp_name_list.append("hsg_1")
        rect_list.append(QRect(5, 213, 78, 27)); hp_name_list.append("hsg_2")
        rect_list.append(QRect(5, 275, 78, 27)); hp_name_list.append("hps_uc_bot")
        rect_list.append(QRect(5, 322, 78, 27)); hp_name_list.append("hps_lc_bot")
        rect_list.append(QRect(98, 323, 110, 27)); hp_name_list.append("hpl_wheel_center")
        rect_list.append(QRect(267, 27, 110, 27)); hp_name_list.append("hps_db_sf_atch")
        rect_list.append(QRect(380, 190, 110, 27)); hp_name_list.append("hps_db_uc_atch")
        rect_list.append(QRect(380, 253, 110, 27)); hp_name_list.append("hps_lta_uta_atch")
        rect_list.append(QRect(380, 287, 110, 27)); hp_name_list.append("hps_uta_uc_atch")
        rect_list.append(QRect(380, 322, 110, 27)); hp_name_list.append("hps_lta_lc_atch")

        # 创建图片显示控件
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

        # 添加左侧布局到主布局 (占比可调)
        mainLayout.addLayout(leftLayout, 4)


        # ================= 2. 右侧区域：三个标签页 =================
        self.tabs = QTabWidget()
        mainLayout.addWidget(self.tabs, 5)

        # --- Tab 1: 结构参数 ---
        self.structTab = QWidget()
        structLayout = QFormLayout(self.structTab)
        
        self.hpName = QLineEdit(self)
        structLayout.addRow("硬点名称：", self.hpName)
        self.xMarker = QLineEdit(self); structLayout.addRow("X坐标：", self.xMarker)
        self.yMarker = QLineEdit(self); structLayout.addRow("Y坐标：", self.yMarker)
        self.zMarker = QLineEdit(self); structLayout.addRow("Z坐标：", self.zMarker)
        
        self.markOkButton = QPushButton("设置硬点坐标")
        self.markOkButton.setEnabled(False)
        structLayout.addRow("", self.markOkButton)

        # 间隔线或空行区分硬点和几何体
        structLayout.addRow(QLabel(""), QLabel(""))

        self.selGeo = QLineEdit(self)
        structLayout.addRow("几何体：", self.selGeo)
        self.doubleRadius = QLineEdit(self); structLayout.addRow("半径：", self.doubleRadius)
        self.doubleLength = QLineEdit(self); structLayout.addRow("长度：", self.doubleLength)
        self.doubleLength.setDisabled(True)
        
        self.dimensionOkButton = QPushButton("设置圆柱尺寸")
        self.dimensionOkButton.setEnabled(False)
        structLayout.addRow("", self.dimensionOkButton)

        self.tabs.addTab(self.structTab, "结构参数")


        # --- Tab 2: 仿真变量 ---
        self.simTab = QWidget()
        simLayout = QVBoxLayout(self.simTab)
        self.simVariableTable = VariableInputTable.VariableInputTable([
            ("前起阻力系数(/)", "NLG_DRAG_COEFF"),
            ("主起阻力系数(/)", "MLG_DRAG_COEFF"),
            ("前起投影面积(㎡)", "z"),
            ("主起投影面积(㎡)", "MLG_PROJ_AREA"),
            ("空气密度(kg/m³)", "AIR_DENSITY"),
            ("气流速度(m/s)", "AIR_VELOCITY"),
        ], self.simTab)
        simLayout.addWidget(self.simVariableTable)
        self.c0Edit = self.simVariableTable.editor("NLG_DRAG_COEFF")
        self.c0MLGEdit = self.simVariableTable.editor("MLG_DRAG_COEFF")
        self.paEdit = self.simVariableTable.editor("z")
        self.paMLGEdit = self.simVariableTable.editor("MLG_PROJ_AREA")
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
            ("主起作动筒行程(mm)", "MLG_ACTUATOR_STROKE"),
            ("主起收起时间(s)", "MLG_RETRACT_TIME"),
            ("主起上位保持时间(s)", "MLG_UP_HOLD_TIME"),
            ("主起放下时间(s)", "MLG_EXTEND_TIME"),
        ], self.travelTab)
        travelLayout.addWidget(self.travelVariableTable)
        self.NLG_ret_disp_edit = self.travelVariableTable.editor("NLG_ACTUATOR_STROKE")
        self.nlg_up_time_edit = self.travelVariableTable.editor("NLG_RETRACT_TIME")
        self.nlg_hold_time_edit = self.travelVariableTable.editor("NLG_UP_HOLD_TIME")
        self.nlg_down_time_edit = self.travelVariableTable.editor("NLG_EXTEND_TIME")
        self.MLG_ret_disp_edit = self.travelVariableTable.editor("MLG_ACTUATOR_STROKE")
        self.mlg_up_time_edit = self.travelVariableTable.editor("MLG_RETRACT_TIME")
        self.mlg_hold_time_edit = self.travelVariableTable.editor("MLG_UP_HOLD_TIME")
        self.mlg_down_time_edit = self.travelVariableTable.editor("MLG_EXTEND_TIME")

        # 确认设置按钮
        self.okParamTimeButton = QPushButton("设置行程参数", self)
        travelButtonLayout = QHBoxLayout()
        travelButtonLayout.addStretch()
        travelButtonLayout.addWidget(self.okParamTimeButton)
        travelLayout.addLayout(travelButtonLayout)

        self.tabs.addTab(self.travelTab, "行程参数")

        MouseEventGraphicsView.apply_standard_dialog(self)

        # ================= 数据读取与变量初始化 =================
        self.loadVariables()

        # ================= 绑定信号和槽 =================
        print("开始定义按钮的槽函数")
        self.okPushButton.clicked.connect(self.okClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.okParamTimeButton.clicked.connect(self.okParamTime)
        
        # 自定义槽函数
        self.view.mySignal.connect(self.mouseEventSlot)

        # 在 Qt 主线程中监听宿主选择集，避免跨线程访问场景对象。
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.selectionSlot)
        self.selectionMonitor.start()

    def loadVariables(self):
        # ----------------获取工程模板中的设计变量----------------
        print("开始----------读取设计变量C0")
        var_list = Common.getDesignVariable("NLG_DRAG_COEFF")
        if var_list :
            print("设计变量C0-------{}".format(var_list[0]))
            self.c0Edit.setText("{:.8f}".format(var_list[0]))

        print("开始----------读取设计变量C0_MLG")
        var_list = Common.getDesignVariable("MLG_DRAG_COEFF")
        if var_list :
            print("设计变量C0_MLG-------{}".format(var_list[0]))
            self.c0MLGEdit.setText("{:.8f}".format(var_list[0]))
      
        print("开始----------读取设计变量pa")
        var_list = Common.getDesignVariable("z")
        if var_list :
            print("设计变量pa-------{}".format(var_list[0]))
            self.paEdit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量pa_MLG")
        var_list = Common.getDesignVariable("MLG_PROJ_AREA")
        if var_list :
            print("设计变量pa_MLG-------{}".format(var_list[0]))
            self.paMLGEdit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量mi_du")
        var_list = Common.getDesignVariable("AIR_DENSITY")
        if var_list :
            print("设计变量mi_du-------{}".format(var_list[0]))
            self.mi_duEdit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量windV")
        var_list = Common.getDesignVariable("AIR_VELOCITY")
        if var_list :
            print("设计变量windV-------{}".format(var_list[0]))
            self.windVEdit.setText("{:.4f}".format(var_list[0]))

        # ---------------读取行程设计变量--------------------------
        print("开始----------读取设计变量NLG_ret_disp")
        var_list = Common.getDesignVariable("NLG_ACTUATOR_STROKE")
        if var_list :
            print("设计变量NLG_ret_disp-------{}".format(var_list[0]))
            self.NLG_ret_disp_edit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量nlg_up_time")
        var_list = Common.getDesignVariable("NLG_RETRACT_TIME")
        if var_list :
            print("设计变量nlg_up_time-------{}".format(var_list[0]))
            self.nlg_up_time_edit.setText("{:.4f}".format(var_list[0]))

        print("开始----------读取设计变量nlg_hold_time")
        var_list = Common.getDesignVariable("NLG_UP_HOLD_TIME")
        if var_list :
            print("设计变量nlg_hold_time-------{}".format(var_list[0]))
            self.nlg_hold_time_edit.setText("{:.4f}".format(var_list[0]))
       
        print("开始----------读取设计变量nlg_down_time")
        var_list = Common.getDesignVariable("NLG_EXTEND_TIME")
        if var_list :
            print("设计变量nlg_down_time-------{}".format(var_list[0]))
            self.nlg_down_time_edit.setText("{:.4f}".format(var_list[0]))
       
        print("开始----------读取设计变量MLG_ret_disp")
        var_list = Common.getDesignVariable("MLG_ACTUATOR_STROKE")
        if var_list :
            print("设计变量MLG_ret_disp-------{}".format(var_list[0]))
            self.MLG_ret_disp_edit.setText("{:.4f}".format(var_list[0]))
       
        print("开始----------读取设计变量mlg_up_time")
        var_list = Common.getDesignVariable("MLG_RETRACT_TIME")
        if var_list :
            print("设计变量mlg_up_time-------{}".format(var_list[0]))
            self.mlg_up_time_edit.setText("{:.4f}".format(var_list[0]))
       
        print("开始----------读取设计变量mlg_hold_time")
        var_list = Common.getDesignVariable("MLG_UP_HOLD_TIME")
        if var_list :
            print("设计变量mlg_hold_time-------{}".format(var_list[0]))
            self.mlg_hold_time_edit.setText("{:.4f}".format(var_list[0]))
        
        print("开始----------读取设计变量mlg_down_time")
        var_list = Common.getDesignVariable("MLG_EXTEND_TIME")
        if var_list :
            print("设计变量mlg_down_time-------{}".format(var_list[0]))
            self.mlg_down_time_edit.setText("{:.4f}".format(var_list[0]))


    #------------------------自定义监听茉莉平台鼠标消息槽函数
    def selectionSlot(self, node_name) :
        node = SelectionMonitor.get_active_node(node_name)
        if node is None :    #---------------选择为空、场景切换中或节点已失效
            self.strSelGeoFullName = ""
            #------------清空几何体输入的数据
            self.selGeo.setText("")
            self.doubleLength.setText("")
            self.doubleRadius.setText("")
            self.dimensionOkButton.setEnabled(False)
        else :
            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":    #----------------表示茉莉平台选择集选中了几何体
                
                # --- 新增：强制跳转到“结构参数”标签页（索引为0） ---
                self.tabs.setCurrentIndex(0)
                
                if self.strSelGeoFullName != node_name :    #-----------表示之前选中的与当前选中的几何体不一样
                    self.strSelGeoFullName = node_name
                    #--------------更新几何体名称对话框
                    strSelGeoName = Common.splitStringLast(self.strSelGeoFullName)
                    self.selGeo.setText(strSelGeoName)
                    #---------------更新对话框控件的圆柱体坐标数据
                    self.doubleLength.setText("{:.4f}".format(node.length))
                    self.doubleRadius.setText("{:.4f}".format(node.radius))
                    #-------------设定各对话框控件可用与不可用的属性
                    self.dimensionOkButton.setEnabled(True)
            else :
                #------------清空几何体输入的数据
                self.selGeo.setText("")
                self.doubleLength.setText("")
                self.doubleRadius.setText("")
                self.dimensionOkButton.setEnabled(False)
        pass

    #---------------------自定义鼠标按下消息槽函数
    def mouseEventSlot(self, hp_name) :
        # --- 新增：强制跳转到“结构参数”标签页（索引为0） ---
        self.tabs.setCurrentIndex(0)

        self.strSelFullName = ".{}.ground.{}".format(self.strModelName, hp_name)
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if node :
            #---------------设置硬点名称
            self.hpName.setText(hp_name)
            #---------------更新对话框控件的硬点的坐标数据
            self.xMarker.setText("{:.4f}".format(node.location.x))
            self.yMarker.setText("{:.4f}".format(node.location.y))
            self.zMarker.setText("{:.4f}".format(node.location.z))

            #--------------------------创建硬点参数化的类对象
            self.Parameterize = MotionFactory.MotionAdjustFactory(self.strSelFullName)

            #-------------设定各对话框控件可用与不可用的属性
            if hp_name == "hps_lta_uta_atch" or \
                hp_name == "hps_lta_lc_atch" or \
                hp_name == "hps_uta_uc_atch" :
                self.xMarker.setEnabled(True)
                self.yMarker.setEnabled(False)
                self.zMarker.setEnabled(True)
            elif hp_name == "hps_uc_top" or \
                hp_name == "hps_uc_bot" :
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
            elif hp_name == "hps_lc_top" or \
                hp_name == "hps_lc_bot" :
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
            #----------------清空硬点参数化对象
            self.Parameterize = None
        pass

    #---------------------定义文件浏览槽函数
    def modelGenerate(self) :
        ModelScriptRunner.generate_model_from_dialog(
            self,
            os.path.join(AutoGenerater_dir, "model_template_6_motion.py"),
            "gcmb6_motion",
            globals(),
        )

    #---------------------ADM主体 + 硬点CMD + 公式补丁导入
    def modelImport(self) :
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_6_motion"),
            "template_6_motion",
        )

    def openSplineImportDialog(self):
        SplineImportDialog.show_spline_import_dialog(self)

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
                #------------进行硬点的联动调整
                if self.Parameterize :
                    #-------------更改硬点的位置
                    node.location = Jusme.Vector(xCoord, yCoord, zCoord)
                    self.Parameterize.Adjust()
                    ascene.recompute()
                else :
                    msgBox = QMessageBox(self)
                    msgBox.setText("该硬点在落震模板中不支持调整")
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
        Common.setDesignVariable("NLG_DRAG_COEFF",float(self.c0Edit.text()))
        Common.setDesignVariable("MLG_DRAG_COEFF",float(self.c0MLGEdit.text()))
        Common.setDesignVariable("z",float(self.paEdit.text()))
        Common.setDesignVariable("MLG_PROJ_AREA",float(self.paMLGEdit.text()))
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
        Common.setDesignVariable("MLG_ACTUATOR_STROKE",float(self.MLG_ret_disp_edit.text()))
        Common.setDesignVariable("MLG_RETRACT_TIME",float(self.mlg_up_time_edit.text()))
        Common.setDesignVariable("MLG_UP_HOLD_TIME",float(self.mlg_hold_time_edit.text()))
        Common.setDesignVariable("MLG_EXTEND_TIME",float(self.mlg_down_time_edit.text()))
        pass

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)

    #----------------------退出按钮点击事件
    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()


def show_motion_dialog(parent=None):
    dialog = MotionDialog(parent)
    dialog.setWindowTitle("载荷分析(位移驱动)对话框")
    dialog.show()
    return dialog


if __name__ == '__main__':
    _motion_dialog = show_motion_dialog()

    
