# 引入窗体
from PySide2.QtGui import QBrush,QColor
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Force_dir = os.path.join(script_dir, "Force")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
sys.path.append(Share_dir)
sys.path.append(Force_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import Common
import ForceFactory 
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable

# 构建插件对话框窗体
class ForceDialog(QDialog):
    
    def __init__(self, parent=None):
        super(ForceDialog, self).__init__(parent)
        print("开启Force对话框构造函数")
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

        self.view = MouseEventGraphicsView.mouseProcessView(
            image_path, rect_list, hp_name_list,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_WIDTH,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_HEIGHT
        )
        leftLayout.addWidget(self.view, 0, Qt.AlignTop | Qt.AlignHCenter)

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

        # 调整比例：左侧占3，右侧占7
        mainLayout.addLayout(leftLayout, 3)

        # ================= 2. 右侧区域：三个标签页 =================
        self.tabs = QTabWidget()
        mainLayout.addWidget(self.tabs, 7)

        # --- Tab 1: 结构参数 ---
        self.structTab = QWidget()
        sub2FormLayout = QFormLayout(self.structTab)
        self.hpName = QLineEdit(self); sub2FormLayout.addRow("硬点名称：", self.hpName)
        self.xMarker = QLineEdit(self); sub2FormLayout.addRow("X坐标：", self.xMarker)
        self.yMarker = QLineEdit(self); sub2FormLayout.addRow("Y坐标：", self.yMarker)
        self.zMarker = QLineEdit(self); sub2FormLayout.addRow("Z坐标：", self.zMarker)
        self.markOkButton = QPushButton("设置硬点坐标"); sub2FormLayout.addRow("", self.markOkButton)
        self.markOkButton.setEnabled(False)
        sub2FormLayout.addRow(QLabel(""), QLabel(""))
        self.selGeo = QLineEdit(self); sub2FormLayout.addRow("几何体：", self.selGeo)
        self.doubleRadius = QLineEdit(self); sub2FormLayout.addRow("半径：", self.doubleRadius)
        self.doubleLength = QLineEdit(self); sub2FormLayout.addRow("长度：", self.doubleLength)
        self.doubleLength.setDisabled(True)
        self.dimensionOkButton = QPushButton("设置圆柱尺寸"); sub2FormLayout.addRow("", self.dimensionOkButton)
        self.dimensionOkButton.setEnabled(False)
        self.tabs.addTab(self.structTab, "结构参数")

        # --- Tab 2: 仿真变量 ---
        self.simTab = QWidget()
        simLayout = QVBoxLayout(self.simTab)
        self.simVariableTable = VariableInputTable.VariableInputTable([
            ("前起阻力系数(/)", "NLG_DRAG_COEFF"),
            ("主起阻力系数(/)", "MLG_DRAG_COEFF"),
            ("前起投影面积(㎡)", "NLG_PROJ_AREA"),
            ("主起(单侧)投影面积(㎡)", "MLG_PROJ_AREA"),
            ("空气密度(kg/m³)", "AIR_DENSITY"),
            ("气流速度(m/s)", "AIR_VELOCITY"),
        ], self.simTab)
        simLayout.addWidget(self.simVariableTable)
        self.c0Edit = self.simVariableTable.editor("NLG_DRAG_COEFF")
        self.c0MLGEdit = self.simVariableTable.editor("MLG_DRAG_COEFF")
        self.paEdit = self.simVariableTable.editor("NLG_PROJ_AREA")
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
        travelTabLayout = QVBoxLayout(self.travelTab)
        self.travelVariableTable = VariableInputTable.VariableInputTable([
            ("前起收起载荷(N)", "NLG_RETRACT_FORCE"),
            ("前起收起载荷持续时间(s)", "NLG_RETRACT_HOLD_TIME"),
            ("前起放下载荷(N)", "NLG_EXTEND_FORCE"),
            ("前起放下载荷持续时间(s)", "NLG_EXTEND_HOLD_TIME"),
            ("前起锁弹簧刚度(N/mm)", "NLG_LOCK_SPRING_K"),
            ("前起锁弹簧阻尼(N·s/mm)", "NLG_LOCK_SPRING_C"),
            ("前起解锁时刻(s)", "NLG_LOCK_UNLOCK_TIME"),
            ("前起解锁载荷(N)", "NLG_UNLOCK_FORCE"),
            ("主起收起载荷(N)", "MLG_RETRACT_FORCE"),
            ("主起收起载荷持续时间(s)", "MLG_RETRACT_HOLD_TIME"),
            ("主起放下载荷(N)", "MLG_EXTEND_FORCE"),
            ("主起放下载荷持续时间(s)", "MLG_EXTEND_HOLD_TIME"),
            ("主起锁弹簧刚度(N/mm)", "MLG_LOCK_SPRING_K"),
            ("主起锁弹簧阻尼(N·s/mm)", "MLG_LOCK_SPRING_C"),
            ("主起解锁时刻(s)", "MLG_LOCK_UNLOCK_TIME"),
            ("主起解锁载荷(N)", "MLG_UNLOCK_FORCE"),
        ], self.travelTab)
        travelTabLayout.addWidget(self.travelVariableTable)

        self.nlg_zdtup_F_edit = self.travelVariableTable.editor("NLG_RETRACT_FORCE")
        self.nlg_zdtup_t2_edit = self.travelVariableTable.editor("NLG_RETRACT_HOLD_TIME")
        self.nlg_zdtdown_F_edit = self.travelVariableTable.editor("NLG_EXTEND_FORCE")
        self.nlg_zdtdown_t2_edit = self.travelVariableTable.editor("NLG_EXTEND_HOLD_TIME")
        self.nlg_suo_K_edit = self.travelVariableTable.editor("NLG_LOCK_SPRING_K")
        self.nlg_suo_C_edit = self.travelVariableTable.editor("NLG_LOCK_SPRING_C")
        self.nlg_suo_jiesuo_shike_edit = self.travelVariableTable.editor("NLG_LOCK_UNLOCK_TIME")
        self.nlg_suo_jiesuo_F_edit = self.travelVariableTable.editor("NLG_UNLOCK_FORCE")
        self.mlg_zdtup_F_edit = self.travelVariableTable.editor("MLG_RETRACT_FORCE")
        self.mlg_zdtup_t2_edit = self.travelVariableTable.editor("MLG_RETRACT_HOLD_TIME")
        self.mlg_zdtdown_F_edit = self.travelVariableTable.editor("MLG_EXTEND_FORCE")
        self.mlg_zdtdown_t2_edit = self.travelVariableTable.editor("MLG_EXTEND_HOLD_TIME")
        self.mlg_suo_K_edit = self.travelVariableTable.editor("MLG_LOCK_SPRING_K")
        self.mlg_suo_C_edit = self.travelVariableTable.editor("MLG_LOCK_SPRING_C")
        self.mlg_suo_jiesuo_shike_edit = self.travelVariableTable.editor("MLG_LOCK_UNLOCK_TIME")
        self.mlg_suo_jiesuo_F_edit = self.travelVariableTable.editor("MLG_UNLOCK_FORCE")

        self.okParamTimeButton = QPushButton("设置行程参数")
        travelButtonLayout = QHBoxLayout()
        travelButtonLayout.addStretch()
        travelButtonLayout.addWidget(self.okParamTimeButton)
        travelTabLayout.addLayout(travelButtonLayout)
        self.tabs.addTab(self.travelTab, "行程参数")
        
        MouseEventGraphicsView.apply_standard_dialog(self)
        #----------------获取工程模板中的设计变量

        print("开始----------读取设计变量C0")
        var_list = Common.getDesignVariable("NLG_DRAG_COEFF")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量C0-------{}".format(design_var))
            self.c0Edit.setText("{:.8f}".format(design_var))

        print("开始----------读取设计变量C0_MLG")
        var_list = Common.getDesignVariable("MLG_DRAG_COEFF")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量C0_MLG-------{}".format(design_var))
            self.c0MLGEdit.setText("{:.8f}".format(design_var))
      
        print("开始----------读取设计变量pa")
        var_list = Common.getDesignVariable("NLG_PROJ_AREA")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量pa-------{}".format(design_var))
            self.paEdit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量pa_MLG")
        var_list = Common.getDesignVariable("MLG_PROJ_AREA")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量pa_MLG-------{}".format(design_var))
            self.paMLGEdit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量mi_du")
        var_list = Common.getDesignVariable("AIR_DENSITY")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mi_du-------{}".format(design_var))
            self.mi_duEdit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量windV")
        design_var = 0
        var_list = Common.getDesignVariable("AIR_VELOCITY")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量windV-------{}".format(design_var))
            self.windVEdit.setText("{:.4f}".format(design_var))

        #---------------读取主起行程设计变量--------------------------
        
        print("开始----------读取设计变量mlg_zdtup_F")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_RETRACT_FORCE")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_zdtup_F-------{}".format(design_var))
            self.mlg_zdtup_F_edit.setText("{:.4f}".format(design_var))


        print("开始----------读取设计变量mlg_zdtup_t2")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_RETRACT_HOLD_TIME")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_zdtup_t2-------{}".format(design_var))
            self.mlg_zdtup_t2_edit.setText("{:.4f}".format(design_var))
       
       
       
        print("开始----------读取设计变量mlg_zdtdown_F")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_EXTEND_FORCE")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_zdtdown_F-------{}".format(design_var))
            self.mlg_zdtdown_F_edit.setText("{:.4f}".format(design_var))
       
        
        print("开始----------读取设计变量mlg_zdtdown_t2")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_EXTEND_HOLD_TIME")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_zdtdown_t2-------{}".format(design_var))
            self.mlg_zdtdown_t2_edit.setText("{:.4f}".format(design_var))


        print("开始----------读取设计变量mlg_suo_K")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_LOCK_SPRING_K")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_suo_K-------{}".format(design_var))
            self.mlg_suo_K_edit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量mlg_suo_C")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_LOCK_SPRING_C")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_suo_C-------{}".format(design_var))
            self.mlg_suo_C_edit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量mlg_suo_jiesuo_shike")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_LOCK_UNLOCK_TIME")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_suo_jiesuo_shike-------{}".format(design_var))
            self.mlg_suo_jiesuo_shike_edit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量mlg_suo_jiesuo_F")
        design_var = 0
        var_list = Common.getDesignVariable("MLG_UNLOCK_FORCE")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量mlg_suo_jiesuo_F-------{}".format(design_var))
            self.mlg_suo_jiesuo_F_edit.setText("{:.4f}".format(design_var))

        
        
        
        
        
        #---------------读取前起行程设计变量--------------------------
        
        print("开始----------读取设计变量nlg_zdtup_F")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_RETRACT_FORCE")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_zdtup_F-------{}".format(design_var))
            self.nlg_zdtup_F_edit.setText("{:.4f}".format(design_var))


        print("开始----------读取设计变量nlg_zdtup_t2")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_RETRACT_HOLD_TIME")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_zdtup_t2-------{}".format(design_var))
            self.nlg_zdtup_t2_edit.setText("{:.4f}".format(design_var))
       
       
       
        print("开始----------读取设计变量nlg_zdtdown_F")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_EXTEND_FORCE")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_zdtdown_F-------{}".format(design_var))
            self.nlg_zdtdown_F_edit.setText("{:.4f}".format(design_var))
       
        
        print("开始----------读取设计变量nlg_zdtdown_t2")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_EXTEND_HOLD_TIME")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_zdtdown_t2-------{}".format(design_var))
            self.nlg_zdtdown_t2_edit.setText("{:.4f}".format(design_var))


        print("开始----------读取设计变量nlg_suo_K")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_LOCK_SPRING_K")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_suo_K-------{}".format(design_var))
            self.nlg_suo_K_edit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量nlg_suo_C")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_LOCK_SPRING_C")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_suo_C-------{}".format(design_var))
            self.nlg_suo_C_edit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量nlg_suo_jiesuo_shike")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_LOCK_UNLOCK_TIME")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_suo_jiesuo_shike-------{}".format(design_var))
            self.nlg_suo_jiesuo_shike_edit.setText("{:.4f}".format(design_var))

        print("开始----------读取设计变量nlg_suo_jiesuo_F")
        design_var = 0
        var_list = Common.getDesignVariable("NLG_UNLOCK_FORCE")
        if var_list :
            design_var = var_list[0]
            print(design_var)
            print("设计变量nlg_suo_jiesuo_F-------{}".format(design_var))
            self.nlg_suo_jiesuo_F_edit.setText("{:.4f}".format(design_var))

     

        print("开始定义按钮的槽函数")
        self.okPushButton.clicked.connect(self.okClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.okParamTimeButton.clicked.connect(self.okParamTime)
        #------------------自定义槽函数
        self.view.mySignal.connect(self.mouseEventSlot)

        # 在 Qt 主线程中监听宿主选择集，避免跨线程访问场景对象。
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.selectionSlot)
        self.selectionMonitor.start()


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

            self.Parameterize = ForceFactory.ForceAdjustFactory(self.strSelFullName)

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
            os.path.join(AutoGenerater_dir, "model_template_6_force.py"),
            "gcmb6_force",
            globals(),
        )

    #---------------------ADM主体 + 硬点CMD + 公式补丁导入
    def modelImport(self) :
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_6_force"),
            "template_6_force",
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
        xCoord = float(strX)
        yCoord = float(strY)
        zCoord = float(strZ)

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
                    msgBox.setText("该硬点在落震模板中不支持调整")
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
        Common.setDesignVariable("NLG_DRAG_COEFF", float(self.c0Edit.text()))
        Common.setDesignVariable("MLG_DRAG_COEFF", float(self.c0MLGEdit.text()))
        Common.setDesignVariable("NLG_PROJ_AREA", float(self.paEdit.text()))
        Common.setDesignVariable("MLG_PROJ_AREA", float(self.paMLGEdit.text()))
        Common.setDesignVariable("AIR_DENSITY", float(self.mi_duEdit.text()))
        Common.setDesignVariable("AIR_VELOCITY", float(self.windVEdit.text()))
        pass

    #--------------行程参数设置槽函数
    def okParamTime(self):
        if not self.travelVariableTable.validate_values(self):
            return
        Common.setDesignVariable("NLG_RETRACT_FORCE", float(self.nlg_zdtup_F_edit.text()))
        Common.setDesignVariable("NLG_RETRACT_HOLD_TIME", float(self.nlg_zdtup_t2_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_FORCE", float(self.nlg_zdtdown_F_edit.text()))
        Common.setDesignVariable("NLG_EXTEND_HOLD_TIME", float(self.nlg_zdtdown_t2_edit.text()))
        Common.setDesignVariable("NLG_LOCK_SPRING_K", float(self.nlg_suo_K_edit.text()))
        Common.setDesignVariable("NLG_LOCK_SPRING_C", float(self.nlg_suo_C_edit.text()))
        Common.setDesignVariable("NLG_LOCK_UNLOCK_TIME", float(self.nlg_suo_jiesuo_shike_edit.text()))
        Common.setDesignVariable("NLG_UNLOCK_FORCE", float(self.nlg_suo_jiesuo_F_edit.text()))
        Common.setDesignVariable("MLG_RETRACT_FORCE", float(self.mlg_zdtup_F_edit.text()))
        Common.setDesignVariable("MLG_RETRACT_HOLD_TIME", float(self.mlg_zdtup_t2_edit.text()))
        Common.setDesignVariable("MLG_EXTEND_FORCE", float(self.mlg_zdtdown_F_edit.text()))
        Common.setDesignVariable("MLG_EXTEND_HOLD_TIME", float(self.mlg_zdtdown_t2_edit.text()))
        Common.setDesignVariable("MLG_LOCK_SPRING_K", float(self.mlg_suo_K_edit.text()))
        Common.setDesignVariable("MLG_LOCK_SPRING_C", float(self.mlg_suo_C_edit.text()))
        Common.setDesignVariable("MLG_LOCK_UNLOCK_TIME", float(self.mlg_suo_jiesuo_shike_edit.text()))
        Common.setDesignVariable("MLG_UNLOCK_FORCE", float(self.mlg_suo_jiesuo_F_edit.text()))
        pass

    #----------------------退出按钮点击事件
    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)


def show_force_dialog(parent=None):
    dialog = ForceDialog(parent)
    dialog.setWindowTitle("载荷分析(载荷驱动)对话框")
    dialog.show()
    return dialog


if __name__ == '__main__':
    _force_dialog = show_force_dialog()

    
