
# 引入窗体
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *

from PySide2.QtGui import QStandardItem, QStandardItemModel


import sys
import os
import traceback

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")
Assembly_dir = os.path.join(script_dir, "Assembly")
Assembly_model_dir = os.path.join(script_dir, "AssemblyModel")


n_tire_double_file = os.path.join(
    Assembly_model_dir, "Tire", "Brake", "BrakeN.tpa"
)
m_tire_single_flie = os.path.join(
    Assembly_model_dir, "Tire", "Brake", "BrakeM.tpa"
)

sys.path.append(Share_dir)
sys.path.append(Model_dir)
sys.path.append(Assembly_dir)
sys.path.append(Assembly_model_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

#-------------------------导入茉莉平台相关库
import Jusme
import Common
import DesignVariable
import ModelScriptRunner
import SelectionMonitor

import MouseEventGraphicsView
import DoubleClickedEdit

import AssemblyFactory

import AssemblyAdjustFactory





# 构建插件对话框窗体
class AssemblyDialog(QDialog):
    strModelName = ""    #------------定义工程模板的名称
    strSelHpFullName = ""  #------------定义选中硬点的名称
    strSelGeoFullName = ""  #------------定义鼠标击中的几何体整体名称
    nOperationCondition = 0 #------------定义工况的索引   0------刹车  1------落震  2--------转弯    3-------收放
    strnTireFilePath = n_tire_double_file    #------------定义自定义前轮胎文件路径
    strmTireFilePath = m_tire_single_flie    #------------定义自定义后轮胎文件路径

    mainGridLayout = None   #--------------定义主题布局控件
    landgearGroup = None    #--------------定义起落架构型Group控件
    landinggearSubFormLayout = None  #--------------定义起落架构型子布局控件
    operationConditionGroup = None   #-------------定义工况Group控件
    opreationConditionSubFormLayout = None   #--------------定义工况类型子布局控件
    nlgStructureComb = None   #-------------定义前起构型组合框
    mlgStructionComb = None   #-------------定义主起构型组合框
    nlgWheelComb = None   #-------定义前机轮构型组合框
    mlgWheelComb = None   #--------定义主机轮构型组合框
    nwheelEdit = None      #--------定义前机轮参数的文件
    mwheelEdit = None      #--------定义后几轮参数文件

    operationConditionButtonGroup = None   #--------------定义工况选择按钮组
    brakeRadioButton = None   #---------定义刹车单选框
    dropRadioButton = None  #---------定义落震单选框
    turnRadioButton = None  #---------定义转弯单选框
    retractionRadioButton = None #-------定义收放单选框

    assemblyGridLayout = None   #---------模型操作布局控件
    assemblyGroup = None        #---------模型操作组合框
    assembGenerateButton = None #---------模型生成按钮
    quitButton = None           #---------退出按钮



    #-------------------------------------------右侧标签部分控件定义
    infoTabWidget = None    #----------定义Tab控件
    imageSubTabWidget = None  #---------定义图片显示窗体
    paraSubTabWidget = None  #-------------定义参数化修改窗口
    designVariableSubWidget = None   #------------设计变量子窗口(通用)
    
    #-----------------------------图片交互拾取子窗口控件
    imageSubLayout = None  #---------图片子窗口布局控件
    imageGroup = None
    imageClickView = None  #----------定义图片显示控件

    #------------------------------参数化修改窗口子空间
    paraSubLayout = None   #----------参数化修改窗口布局控件
    hpGroup = None         #----------硬点参数Group
    hpSubFormLayout = None #----------硬点参数布局控件
    geoGroup = None        #----------几何体参数Group
    geoSubFormLayout = None #---------几何体参数布局控件

    hpNameEdit = None   #-------硬点名称控件
    hpXEdit = None      #-------硬点X坐标边界框
    hpYEdit = None      #-------硬点Y坐标边界框
    hpZEdit = None      #-------硬点Z坐标边界框
    hpSetButton = None  #-------硬点坐标设定按钮

    geoNameEdit = None  #--------几何体名称
    geoRadiusEdit = None #------几何体半径编辑框
    geoLenEdit = None #--------几何体长度编辑框
    geoSetButton = None  #-------几何尺寸设定按钮

    designVariableLayout = None    #----------设计变量设定页面总体布局控件
    designVariableGroup = None     #------------设计变量组合框
    designVariableVLayout = None   #------------设计变量页面子布局控件
    designVariableTreeView = None #--------存放设计变量的树视图控件
    designVariableModel = None    #--------存放设计变量model对象
    designVariableRoot = None
    designVariableSetButton = None   #---------设定设计变量参数按钮

    timer = None    #------------定义计时器

    # turnDesignVariable = None    #------------定义转弯设计参数类
    # dropDesignVariable = None    #------------定义落震设计参数类
    # brakeDesignVariable = None   #------------定义刹车设计参数类
    # retractDesignVariable = None #------------定义收放设计参数类
    variableObject = None


    AssemblyWriter = None  #-----------定义装配操作对象

    Parameterize = None
    

    #-------------------图片交互子窗口

    def __init__(self, parent=None):
        super(AssemblyDialog, self).__init__(parent)

        #----------------创建各类设计参数对象
        # self.brakeDesignVariable = DesignVariable.BrakeVariable("brake design variables", 0)
        # self.dropDesignVariable = DesignVariable.DropVariable("drop design variables", 1)
        # self.turnDesignVariable = DesignVariable.TurnVariable("turn design variables", 2)
        # self.retractDesignVariable = DesignVariable.RetractVariable("rectract design variables", 3)
        #self.variableObject = DesignVariable.CreateVariableObject(self.nOperationCondition)


        #------------创建设计变量对象
        self.createDesignVariableObject()

        #--------------读取模型中的设计变量
        self.readDesignVariables()
        #print("0000000000000")

        #-----------------初始化补充信息写入器
        if self.AssemblyWriter :
            del self.AssemblyWriter
        self.AssemblyWriter = AssemblyFactory.CreateAssembly(self.nOperationCondition, self.variableObject)

        
        self.initUI()

        #----------------应用统一窗口尺寸与视觉样式
        MouseEventGraphicsView.apply_standard_dialog(self)

    #---------------清除设计变量树控件中的子控件
    def clearDesignVariableSubUI(self) :
        if self.designVariableTreeView :
            self.designVariableRoot.removeRows(0, self.designVariableRoot.rowCount())

    #---------------读取模型中的设计变量
    def readDesignVariables(self) :
        DesignVariable.ReadModelDesignVariables(self.variableObject)
        pass

    #---------------根据仿真工况的选择刷新设计变量界面
    def refreshDesignVariableUI(self) :
        #-----------------清除树控件中的所有数据
        self.clearDesignVariableSubUI()
        

        var_index = 0
        if self.variableObject :
            for (chi, eng) in zip(self.variableObject.chinese_name_list, self.variableObject.english_name_list) :
                item1 = QStandardItem(chi)
                item2 = QStandardItem(eng)
                self.designVariableRoot.appendRow([item1, item2])
                index = self.designVariableModel.index(var_index, 2)
                edit = QLineEdit()
                val = self.variableObject.name_val_dic[eng]
                edit.setText("{:.4f}".format(val))

                self.designVariableTreeView.setIndexWidget(index, edit)
                var_index += 1

        # var_index = 0
        # if self.nOperationCondition == 0 :  #----------表示刹车工况
        #     for (chi, eng, val) in zip(self.brakeDesignVariable.chinese_name_list, self.brakeDesignVariable.english_name_list, self.brakeDesignVariable.value_list) :
        #         item1 = QStandardItem(chi)
        #         item2 = QStandardItem(eng)
        #         self.designVariableRoot.appendRow([item1, item2])
        #         index = self.designVariableModel.index(var_index, 2)
        #         edit = QLineEdit()
        #         self.designVariableTreeView.setIndexWidget(index, edit)
        #         var_index += 1
        #     pass
        # elif self.nOperationCondition == 1 :    #---------表示落震工况
        #     for (chi, eng, val) in zip(self.dropDesignVariable.chinese_name_list, self.dropDesignVariable.english_name_list, self.dropDesignVariable.value_list) :
        #         item1 = QStandardItem(chi)
        #         item2 = QStandardItem(eng)
        #         self.designVariableRoot.appendRow([item1, item2])
        #         index = self.designVariableModel.index(var_index, 2)
        #         edit = QLineEdit()
        #         self.designVariableTreeView.setIndexWidget(index, edit)
        #         var_index += 1
        #     pass
        # elif self.nOperationCondition == 2 :  #--------表示转弯工况
        #     for (chi, eng, val) in zip(self.turnDesignVariable.chinese_name_list, self.turnDesignVariable.english_name_list, self.turnDesignVariable.value_list) :
        #         item1 = QStandardItem(chi)
        #         item2 = QStandardItem(eng)
        #         self.designVariableRoot.appendRow([item1, item2])
        #         index = self.designVariableModel.index(var_index, 2)
        #         edit = QLineEdit()
        #         self.designVariableTreeView.setIndexWidget(index, edit)
        #         var_index += 1
        #     pass
        # elif self.nOperationCondition == 3 :
        #     for (chi, eng, val) in zip(self.retractDesignVariable.chinese_name_list, self.retractDesignVariable.english_name_list, self.retractDesignVariable.value_list) :
        #         item1 = QStandardItem(chi)
        #         item2 = QStandardItem(eng)
        #         self.designVariableRoot.appendRow([item1, item2])
        #         index = self.designVariableModel.index(var_index, 2)
        #         edit = QLineEdit()
        #         self.designVariableTreeView.setIndexWidget(index, edit)
        #         var_index += 1
        #     pass
        # else :
        #     pass

        pass

    def initUI(self):
        #------------初始化工程模板名称
        self.strModelName = Common.getModelName()

        #--------------创建对话框Grid根布局
        self.mainGridLayout = QGridLayout()
        self.setLayout(self.mainGridLayout)

        #----------创建起落架构型Group控件
        self.landgearGroup = QGroupBox("起落架构型", self)
        self.mainGridLayout.addWidget(self.landgearGroup, 0, 0, 1, 1)
        #self.assemblyGridLayout.setRowStretch(5, 2)

        #---------创建起落架构型子布局控件
        self.landinggearSubFormLayout = QFormLayout(self.landgearGroup)

        #----------工况Group控件
        self.operationConditionGroup = QGroupBox("工况类型", self)
        self.mainGridLayout.addWidget(self.operationConditionGroup, 1, 0, 1, 1)

        #----------装配操作区域布局控件
        self.assemblyGroup = QGroupBox("模型生成")
        self.mainGridLayout.addWidget(self.assemblyGroup, 2, 0, 1, 1)
        self.assemblyGridLayout = QGridLayout(self.assemblyGroup)
        self.assembGenerateButton = QPushButton("模型生成")
        self.quitButton = QPushButton("退出")
        #self.quitButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        #self.assembGenerateButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.assemblyGridLayout.addWidget(self.assembGenerateButton, 0, 0, 1, 1)
        self.assemblyGridLayout.addWidget(self.quitButton, 0, 1, 1, 1)


        #---------创建工况类型子布局控件
        self.opreationConditionSubFormLayout = QFormLayout(self.operationConditionGroup)

        #----------------------对起落架构型进行控件创建
        self.nlgStructureComb = QComboBox(self)
        self.landinggearSubFormLayout.addRow("前起构型", self.nlgStructureComb)

        self.mlgStructionComb = QComboBox(self)
        self.landinggearSubFormLayout.addRow("主起构型", self.mlgStructionComb)

        self.nlgWheelComb = QComboBox(self)
        self.landinggearSubFormLayout.addRow("前机轮", self.nlgWheelComb)

        self.mlgWheelComb = QComboBox(self)
        self.landinggearSubFormLayout.addRow("后机轮", self.mlgWheelComb)

        self.nwheelEdit = DoubleClickedEdit.DoubleClickedLineEdit(0)
        self.landinggearSubFormLayout.addRow("前轮文件", self.nwheelEdit)
        self.nwheelEdit.setText(self.strnTireFilePath)

        self.mwheelEdit = DoubleClickedEdit.DoubleClickedLineEdit(1)
        self.landinggearSubFormLayout.addRow("后轮文件", self.mwheelEdit)
        self.mwheelEdit.setText(self.strmTireFilePath)
        #self.wheelEdit.setReadOnly(True)


        #--------------------设定起落架构型各组合框填充数据
        self.nlgStructureComb.addItem("油气式缓冲支柱前起落架")
        self.mlgStructionComb.addItem("油气式缓冲支柱主起落架")
        self.nlgWheelComb.addItem("单轴单轮")
        self.nlgWheelComb.addItem("单轴双轮")
        self.nlgWheelComb.setCurrentIndex(1)

        self.mlgWheelComb.addItem("单轴单轮")
        self.mlgWheelComb.addItem("单轴双轮")
        self.mlgWheelComb.setCurrentIndex(0)

        


        #-----------------------创建各工况单选框按钮
        self.operationConditionButtonGroup = QButtonGroup()
        self.brakeRadioButton = QRadioButton("刹车仿真")
        self.dropRadioButton = QRadioButton("落震仿真")
        self.turnRadioButton = QRadioButton("转弯仿真")
        self.retractionRadioButton = QRadioButton("收放仿真")
        self.operationConditionButtonGroup.addButton(self.brakeRadioButton)
        self.operationConditionButtonGroup.addButton(self.dropRadioButton)
        self.operationConditionButtonGroup.addButton(self.turnRadioButton)
        self.operationConditionButtonGroup.addButton(self.retractionRadioButton)
        self.brakeRadioButton.setChecked(True)

        #---------------------添加工况子布局控件
        self.opreationConditionSubFormLayout.addRow("工况选择",  self.brakeRadioButton)
        self.opreationConditionSubFormLayout.addRow("",  self.dropRadioButton)
        self.opreationConditionSubFormLayout.addRow("",  self.turnRadioButton)
        self.opreationConditionSubFormLayout.addRow("",  self.retractionRadioButton)

        #--------------------创建tab控件
        self.infoTabWidget = QTabWidget()
        self.mainGridLayout.addWidget(self.infoTabWidget, 0, 1, 3, 1)

        #-------------------创建tab控件子窗口
        self.imageSubTabWidget = QWidget()
        self.infoTabWidget.addTab(self.imageSubTabWidget, "硬点拾取")

        self.paraSubTabWidget = QWidget()
        self.infoTabWidget.addTab(self.paraSubTabWidget, "参数化修改")

        self.designVariableSubWidget = QWidget()
        self.infoTabWidget.addTab(self.designVariableSubWidget, "设计变量输入")


        #--------------------------------------------------创建各子窗口的控件
        self.imageSubLayout = QGridLayout()
        self.imageSubTabWidget.setLayout(self.imageSubLayout)
        #----------定义图片显示控件
        #----------------------定义图片中各硬点区域的位置和名称
        rect_list = []
        hp_name_list = []
        rect = QRect(42, 35, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_uc_top")
        
        rect = QRect(42, 82, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_lc_top")

        rect = QRect(5, 160, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hsg_1")

        rect = QRect(5, 213, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hsg_2")

        rect = QRect(5, 275, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_uc_bot")

        rect = QRect(5, 322, 78, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_lc_bot")

        rect = QRect(98, 323, 110, 27)
        rect_list.append(rect)
        hp_name_list.append("hpl_wheel_center")

        rect = QRect(267, 27, 110, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_db_sf_atch")

        rect = QRect(380, 190, 110, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_db_uc_atch")

        rect = QRect(380, 253, 110, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_lta_uta_atch")

        rect = QRect(380, 287, 110, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_uta_uc_atch")

        rect = QRect(380, 322, 110, 27)
        rect_list.append(rect)
        hp_name_list.append("hps_lta_lc_atch")

        self.imageClickView = MouseEventGraphicsView.mouseProcessView(
            image_path, rect_list, hp_name_list,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_WIDTH,
            MouseEventGraphicsView.INTERACTIVE_IMAGE_HEIGHT
        )
        self.imageSubLayout.addWidget(
            self.imageClickView, 0, 0, 1, 1, Qt.AlignCenter
        )

        #------------------创建顶点输入标签页控件
        self.paraSubLayout = QGridLayout()
        self.paraSubTabWidget.setLayout(self.paraSubLayout)

        self.hpGroup = QGroupBox("硬点坐标设定")
        self.paraSubLayout.addWidget(self.hpGroup, 0, 0, 1, 1)

        self.geoGroup = QGroupBox("几何参数设定")
        self.paraSubLayout.addWidget(self.geoGroup, 0, 1, 1, 1)
        self.geoSubFormLayout = QFormLayout(self.geoGroup)
        self.hpSubFormLayout = QFormLayout(self.hpGroup)

        #----------------添加硬点信息子控件
        self.hpNameEdit = QLineEdit()
        self.hpNameEdit.setEnabled(False)
        self.hpSubFormLayout.addRow("名称", self.hpNameEdit)

        self.hpXEdit = QLineEdit()
        self.hpSubFormLayout.addRow("X坐标", self.hpXEdit)

        self.hpYEdit = QLineEdit()
        self.hpSubFormLayout.addRow("Y坐标", self.hpYEdit)

        self.hpZEdit = QLineEdit()
        self.hpSubFormLayout.addRow("Y坐标", self.hpZEdit)
        
        self.hpSetButton = QPushButton("设定")
        self.hpSetButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.hpSubFormLayout.addRow("", self.hpSetButton)
        self.hpSetButton.setEnabled(False)

        #----------------添加几何体信息子控件
        self.geoNameEdit = QLineEdit()
        self.geoSubFormLayout.addRow("几何体", self.geoNameEdit)
        self.geoNameEdit.setEnabled(False)

        self.geoRadiusEdit = QLineEdit()
        self.geoSubFormLayout.addRow("半径", self.geoRadiusEdit)

        self.geoLenEdit = QLineEdit()
        self.geoSubFormLayout.addRow("长度", self.geoLenEdit)
        self.geoLenEdit.setEnabled(False)

        self.geoSetButton = QPushButton("设定")
        self.geoSetButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.geoSubFormLayout.addRow("", self.geoSetButton)

        #---------------------------添加设计变量各子空间
        self.designVariableLayout = QVBoxLayout()
        self.designVariableSubWidget.setLayout(self.designVariableLayout)

        temp_widget = QWidget()
        self.designVariableLayout.addWidget(temp_widget)
        self.designVariableVLayout = QVBoxLayout()
        temp_widget.setLayout(self.designVariableVLayout)
        
        #------------------创建TreeView控件
        self.designVariableModel = QStandardItemModel()
        self.designVariableModel.setHorizontalHeaderLabels(["变量含义", "变量名称", "变量取值"])
        self.designVariableTreeView = QTreeView()
        self.designVariableTreeView.setModel(self.designVariableModel)
        self.designVariableRoot = self.designVariableModel.invisibleRootItem()

        self.designVariableVLayout.addWidget(self.designVariableTreeView)

        #---------------更新设计变量树控件
        self.refreshDesignVariableUI()

        self.designVariableSetButton = QPushButton("变量设定")
        self.designVariableSetButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.designVariableLayout.addWidget(self.designVariableSetButton, 0, Qt.AlignRight)

        #-----------在 Qt 主线程中监听宿主选择集
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.timerProcess)
        self.selectionMonitor.start()


        #-------------------定义各类槽函数
        self.imageClickView.mySignal.connect(self.imageHpClicked)
        self.nwheelEdit.mySignal.connect(self.wheelDoubleClicked)
        self.mwheelEdit.mySignal.connect(self.wheelDoubleClicked)

        self.brakeRadioButton.toggled.connect(self.brakeRadioClicked)
        self.dropRadioButton.toggled.connect(self.dropRadioClicked)
        self.turnRadioButton.toggled.connect(self.turnRadioClicked)
        self.retractionRadioButton.toggled.connect(self.retractionRadioClicked)

        #-----------定义退出按钮和模型生成按钮槽函数
        self.quitButton.clicked.connect(self.quitClickedEvent)
        self.assembGenerateButton.clicked.connect(self.assemblyClickedEvent)
        self.designVariableSetButton.clicked.connect(self.variablesSetEvent)
        self.geoSetButton.clicked.connect(self.dimensionClickedEvent)
        self.hpSetButton.clicked.connect(self.hpPositionClickedEvent)

    #-----------------------硬点位置调整槽函数
    def hpPositionClickedEvent(self) :
        if self.strSelHpFullName == "" :
            msgBox = QMessageBox(self)
            msgBox.setText("请选择某个可调整的硬点")
            msgBox.exec_()
            pass

        node = SelectionMonitor.get_active_node(self.strSelHpFullName)
        if node is None:
            return
        if  node :
            if self.Parameterize :
                #----------得到编辑框输入的坐标值
                x_pos = float(self.hpXEdit.text())
                y_pos = float(self.hpYEdit.text())
                z_pos = float(self.hpZEdit.text())

                #-------------更改硬点的位置
                node.location = Jusme.Vector(x_pos, y_pos, z_pos)
                self.Parameterize.Adjust()
            else :
                 msgBox = QMessageBox(self)
                 msgBox.setText("该硬点不支持参数化调整")
                 msgBox.exec_()

        pass




    def dimensionClickedEvent(self) :
        if self.strSelGeoFullName != "" :
            strRadius = self.geoRadiusEdit.text()
            dRadius = float(strRadius)
            node = SelectionMonitor.get_active_node(self.strSelGeoFullName)
            if node is None:
                return
            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":
                node.radius = dRadius
                msgBox = QMessageBox(self)
                msgBox.setText("几何尺寸已更新")
                msgBox.exec_()
        pass

    def variablesSetEvent(self) :
        nCount = self.designVariableModel.rowCount()
        
        for i in range(nCount) :
            #----------得到设计变量的名称
            item = self.designVariableModel.item(i, 1)
            var_name = item.text()
    
            #--------------得到第三列的编辑框控件
            index = self.designVariableModel.index(i, 2)

            #------------将窗体控件强制转换为文本框控件
            widget : QLineEdit = self.designVariableTreeView.indexWidget(index)
            #------------得到设计变量的数值
            strVal = widget.text()
            val = float(strVal)
            #print(var_name, val)

            #--------------修改模型的设计变量数据
            Common.setDesignVariable(var_name, val)

            #--------------更新设计变量成员的数据
            self.variableObject.name_val_dic[var_name] = val 

        msgBox = QMessageBox(self)
        msgBox.setText("设计变量更新已完成")
        msgBox.exec_()

        #print(self.variableObject.name_val_dic)
        pass


    def wheelDoubleClicked(self, type) :
        file_path_list = QFileDialog.getOpenFileName(None, "选择文件", "", "所有文件(*.tpa)")
        if file_path_list :
            if type == 0 :  #-------表示前轮控件发出的信号
                self.strnTireFilePath = file_path_list[0]
                self.nwheelEdit.setText(self.strnTireFilePath)
            elif type == 1 : #------表示后轮控件发出的信号
                self.strmTireFilePath = file_path_list[0]
                self.mwheelEdit.setText(self.strmTireFilePath)
            pass
        pass

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)

    #----------点击退出按钮槽函数
    def quitClickedEvent(self) :
        self.selectionMonitor.stop()
        self.accept()

    def getModelScriptFiles(self) :
        dragbrace_file_name = "nlg_dragbrace.py"
        if self.nOperationCondition == 3 :
            dragbrace_file_name = "nlg_dragbrace_retract.py"

        return [
            os.path.join(Assembly_model_dir, "subframe.py"),
            os.path.join(Assembly_model_dir, "nlg_absorber.py"),
            os.path.join(Assembly_model_dir, "nlg_rod_turn.py"),
            os.path.join(Assembly_model_dir, dragbrace_file_name),
            os.path.join(Assembly_model_dir, "mlg_absorber.py"),
        ]

    def executeModelScripts(self, model_script_files) :
        import Fmbs.import_all_node as model_node_factory

        original_make_node = model_node_factory.MakeSceneNodeByType
        created_nodes = {}
        statement_count = 0
        execute_errors = []

        def make_or_reuse_node(node_type, node_name, *args, **kwargs) :
            cached_node = created_nodes.get(node_name)
            if cached_node is not None :
                cached_type, node = cached_node
                if cached_type != node_type :
                    raise RuntimeError(
                        "模型节点{}被重复定义为{}和{}".format(
                            node_name, cached_type, node_type
                        )
                    )
                return node

            node = None
            scene = SelectionMonitor.get_active_scene()
            if scene is not None :
                try :
                    node = scene.getObject(node_name)
                except Exception :
                    node = None

            if node is None :
                node = original_make_node(node_type, node_name, *args, **kwargs)

            created_nodes[node_name] = (node_type, node)
            return node

        model_node_factory.MakeSceneNodeByType = make_or_reuse_node
        try :
            for model_script in model_script_files :
                try :
                    file_statement_count, file_errors = (
                        ModelScriptRunner.execute_model_script(
                            model_script,
                            {},
                        )
                    )
                    statement_count += file_statement_count
                    for error_info in file_errors :
                        error_info["file"] = os.path.basename(model_script)
                    execute_errors.extend(file_errors)

                    print(
                        "模型脚本执行完成：{}，顶层语句{}条，错误{}条".format(
                            model_script,
                            file_statement_count,
                            len(file_errors),
                        )
                    )
                except Exception as exc :
                    error_info = {
                        "file": os.path.basename(model_script),
                        "line": 0,
                        "end_line": 0,
                        "statement": "script",
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                    }
                    execute_errors.append(error_info)
                    print(
                        "[模型脚本错误] {} 无法继续解析或执行：{}: {}".format(
                            error_info["file"],
                            error_info["error_type"],
                            error_info["error"],
                        )
                    )
                    print(traceback.format_exc())
        finally :
            model_node_factory.MakeSceneNodeByType = original_make_node

        return statement_count, execute_errors

    def loadPythonModelFiles(self) :
        model_script_files = self.getModelScriptFiles()
        required_files = list(model_script_files)
        required_files.append(self.strnTireFilePath)
        missing_files = [
            file_path for file_path in required_files
            if not file_path or not os.path.isfile(file_path)
        ]
        if missing_files :
            QMessageBox.critical(
                self,
                "模型生成失败",
                "以下模型输入文件不存在：\n{}".format("\n".join(missing_files)),
            )
            return False

        answer = QMessageBox.question(
            self,
            "确认生成模型",
            "生成模型将关闭当前模型，是否继续？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes :
            return False

        monitor_was_active = self.selectionMonitor.is_active()
        self.selectionMonitor.stop()
        self.assembGenerateButton.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        QApplication.processEvents()

        generate_error = None
        model_statement_count = 0
        model_script_errors = []
        try :
            active_scene = SelectionMonitor.get_active_scene()
            if active_scene is not None :
                Jusme.closeUSScene(active_scene.Name)
            Jusme.newUSScene("Unknown")

            model_statement_count, model_script_errors = (
                self.executeModelScripts(model_script_files)
            )


            #--------------------------------------补充数模中的额外信息
            if self.AssemblyWriter :
                self.AssemblyWriter.InitDesignVariables()
                self.AssemblyWriter.InitElement()
                self.AssemblyWriter.InitMarker()
                self.AssemblyWriter.InitForce()
                self.AssemblyWriter.InitJoint()
                self.AssemblyWriter.InitMotion()
                self.AssemblyWriter.InitMeasure()

            Common.createTire(self.nOperationCondition, self.strnTireFilePath)
            Common.createTire(self.nOperationCondition, self.strmTireFilePath)

            active_scene = SelectionMonitor.get_active_scene()
            if active_scene is not None :
                active_scene.recompute()
        except Exception as exc :
            print(traceback.format_exc())
            generate_error = exc
        finally :
            QApplication.restoreOverrideCursor()
            self.assembGenerateButton.setEnabled(True)
            if monitor_was_active and self.isVisible() :
                self.selectionMonitor.start()

        if generate_error is not None :
            QMessageBox.critical(
                self,
                "模型生成失败",
                "生成过程中发生错误，当前场景可能不完整：\n{}".format(
                    generate_error
                ),
            )
            return False

        if model_script_errors :
            QMessageBox.warning(
                self,
                "模型生成完成",
                "模型脚本已执行完成。\n"
                "共执行{}条顶层语句，其中{}条报错；后续语句和其余部件脚本已继续执行。\n"
                "详细错误请查看软件控制台。".format(
                    model_statement_count,
                    len(model_script_errors),
                ),
            )
        else :
            QMessageBox.information(self, "模型生成", "模型生成完成。")
        return True

    #-----------模型自动生成按钮槽函数
    def assemblyClickedEvent(self) :
        self.loadPythonModelFiles()

    #------------生成设计变量对象
    def createDesignVariableObject(self) :
        if self.variableObject :
            del self.variableObject
        self.variableObject = DesignVariable.CreateVariableObject(self.nOperationCondition)
        pass


    def createAssemblyWriter(self) :
        if self.AssemblyWriter :
            del self.AssemblyWriter
        
        #--------------创建装配信息写入对象  
        self.AssemblyWriter = AssemblyFactory.CreateAssembly(self.nOperationCondition, self.variableObject)
        pass

    def RefreshTireFile(self) :
        if self.nOperationCondition == 0 :
            self.strnTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Brake", "BrakeN.tpa"
            )
            self.strmTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Brake", "BrakeM.tpa"
            )
        elif self.nOperationCondition == 1 :  #-----------表示落震
            self.strnTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Drop", "DropN.tpa"
            )
            self.strmTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Drop", "DropM.tpa"
            )
        elif self.nOperationCondition == 2 : #---------------表示转弯
            self.strnTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Turn", "TurnN.tpa"
            )
            self.strmTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Turn", "TurnM.tpa"
            )
        elif self.nOperationCondition == 3 :   #----------表示收放
            self.strnTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Retract", "RetractN.tpa"
            )
            self.strmTireFilePath = os.path.join(
                Assembly_model_dir, "Tire", "Retract", "RetractM.tpa"
            )
        else :
            self.strnTireFilePath = ""
            self.strmTireFilePath = ""

        self.nwheelEdit.setText(self.strnTireFilePath)
        self.mwheelEdit.setText(self.strmTireFilePath)

        pass

    #-----------刹车单选框点击槽函数
    def brakeRadioClicked(self) :
        self.nOperationCondition = 0

        #-----------创建新的设计变量对象
        self.createDesignVariableObject()

        #------------读取刹车工况的设计变量
        self.readDesignVariables()

        #--------------创建装配信息写入对象  
        self.createAssemblyWriter()
        
        self.refreshDesignVariableUI()

        self.RefreshTireFile()
        pass

    #----------落震单选框点击槽函数
    def dropRadioClicked(self) :
        self.nOperationCondition = 1

        #-----------创建新的设计变量对象
        self.createDesignVariableObject()

        #------------读取落震工况的设计变量
        self.readDesignVariables()

        #--------------创建装配信息写入对象  
        self.createAssemblyWriter()

        self.refreshDesignVariableUI()

        self.RefreshTireFile()
        pass

    #----------转弯单选框点击槽函数
    def turnRadioClicked(self) :
        self.nOperationCondition = 2

        #-----------创建新的设计变量对象
        self.createDesignVariableObject()

        #------------读取转弯工况的设计变量
        self.readDesignVariables()

        #--------------创建装配信息写入对象  
        self.createAssemblyWriter()

        self.refreshDesignVariableUI()

        self.RefreshTireFile()
        pass


    #---------收放单选框点击槽函数
    def retractionRadioClicked(self) :
        self.nOperationCondition = 3

        #-----------创建新的设计变量对象
        self.createDesignVariableObject()

        #------------读取转弯工况的设计变量
        self.readDesignVariables()

        #--------------创建装配信息写入对象  
        self.createAssemblyWriter()

        self.refreshDesignVariableUI()

        self.RefreshTireFile()
        pass

    #------------------计时器处理函数
    def timerProcess(self, strSelName) :
        if strSelName :
            node = SelectionMonitor.get_active_node(strSelName)
            if node is None:
                self.strSelGeoFullName = ""
                self.geoNameEdit.setText("")
                self.geoRadiusEdit.setText("")
                self.geoLenEdit.setText("")
                self.geoSetButton.setEnabled(False)
                return

            if self.strSelGeoFullName == strSelName :
                return

            self.strSelGeoFullName = strSelName

            if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":    #----------------表示茉莉平台选择集选中了几何体
                self.infoTabWidget.setCurrentIndex(1)

                #---------------更新参数化调整标签页的控件
                #---------得到整体名称中的几何体名称
                strLocalName = Common.splitStringLast(self.strSelGeoFullName)
                self.geoNameEdit.setText(strLocalName)

                self.geoRadiusEdit.setText("{:.4f}".format(node.radius))
                self.geoLenEdit.setText("{:.4f}".format(node.length))

                self.geoSetButton.setEnabled(True)
            else :
                self.strSelGeoFullName = ""
                self.geoNameEdit.setText("")
                self.geoRadiusEdit.setText("")
                self.geoLenEdit.setText("")
                self.geoSetButton.setEnabled(False)
            
        else :
            self.strSelGeoFullName = ""
            self.geoNameEdit.setText("")
            self.geoRadiusEdit.setText("")
            self.geoLenEdit.setText("")
            self.geoSetButton.setEnabled(False)
        pass

    #---------------------自定义硬点图片鼠标按下消息槽函数
    def imageHpClicked(self, hp_name) :
        self.strSelHpFullName = ".{}.ground.{}".format(self.strModelName, hp_name)
        node = SelectionMonitor.get_active_node(self.strSelHpFullName)
 
        if node :
            #----------------更新参数化标签页和的控件状态
            self.hpNameEdit.setText(hp_name)

            self.hpXEdit.setText("{:.4f}".format(node.location.x))
            self.hpYEdit.setText("{:.4f}".format(node.location.y))
            self.hpZEdit.setText("{:.4f}".format(node.location.z))
            self.hpSetButton.setEnabled(True)


            #------------------------------创建参数化对象
            #-----------清空原先的参数化对象
            if self.Parameterize :
                del self.Parameterize
                self.Parameterize = None

            #-----------------创建新的参数化对象
            self.Parameterize = AssemblyAdjustFactory.CreateAssemblyHpsAdjust(hp_name)
            

            #-------------------此处添加硬点坐标移动的编辑框使能和禁能
            if hp_name == "hps_lta_uta_atch" or \
                hp_name == "hps_lta_lc_atch" or \
                hp_name == "hps_uta_uc_atch" :
                self.hpXEdit.setEnabled(True)
                self.hpYEdit.setEnabled(False)
                self.hpZEdit.setEnabled(True)
            elif hp_name == "hps_uc_top" or \
                hp_name == "hps_uc_bot" :
                self.hpXEdit.setEnabled(False)
                self.hpYEdit.setEnabled(False)
                self.hpZEdit.setEnabled(True)
            elif hp_name == "hps_db_sf_atch" or \
                hp_name == "hps_db_uc_atch" :
                self.hpXEdit.setEnabled(True)
                self.hpYEdit.setEnabled(False)
                self.hpZEdit.setEnabled(True)
            elif hp_name == "hpr_wheel_center" or \
                hp_name == "hpl_wheel_center" :
                self.hpXEdit.setEnabled(False)
                self.hpYEdit.setEnabled(True)
                self.hpZEdit.setEnabled(False)
            elif hp_name == "hps_lc_top" or \
                hp_name == "hps_lc_bot" :
                self.hpXEdit.setEnabled(False)
                self.hpYEdit.setEnabled(False)
                self.hpZEdit.setEnabled(True)
            else :
                self.hpXEdit.setEnabled(False)
                self.hpYEdit.setEnabled(False)
                self.hpZEdit.setEnabled(False)

            #----------------切换到硬点输入标签页
            self.infoTabWidget.setCurrentIndex(1)

            pass
        else :
            #----------------更新参数化标签页和的控件状态
            self.hpNameEdit.setText("")

            self.hpXEdit.setText("")
            self.hpYEdit.setText("")
            self.hpZEdit.setText("")
            self.hpSetButton.setEnabled(False)
            pass
        pass



def show_assembly_dialog(parent=None):
    dialog = AssemblyDialog(parent)
    dialog.setWindowTitle("起落架自动装配对话框")
    dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    dialog.show()
    return dialog


if __name__ == '__main__':
    _assembly_dialog = show_assembly_dialog()
