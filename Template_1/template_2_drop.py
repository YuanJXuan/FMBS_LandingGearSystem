# 引入窗体
from PySide2.QtGui import QBrush,QColor,QDoubleValidator
from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import *


import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
Share_dir = os.path.join(script_dir, "Share")
Drop_dir = os.path.join(script_dir, "Drop")
AutoGenerater_dir = os.path.join(script_dir, "AutoGenerater")
Model_dir = os.path.join(script_dir, "Model")
Image_dir = os.path.join(script_dir, "Image")

sys.path.append(Share_dir)
sys.path.append(Drop_dir)
sys.path.append(AutoGenerater_dir)

image_path = os.path.join(Image_dir, "Drop.jpg")

import Jusme
import Common
import DropAdmParameterization
import DropRoadPosition
import ModelImportRunner
import ModelScriptRunner
import math

import MouseEventGraphicsView
import SelectionMonitor
import SplineImportDialog
import VariableInputTable


DROP_SIMULATION_VARIABLES = [
    ("油液密度(kg/m³)", "NLG_rho_Oil"),
    ("主油腔压油面积(㎡)", "NLG_A_MAIN_OIL"),
    ("主油孔正行程(㎡)", "NLG_A_MAIN_POS"),
    ("低压腔压气面积(㎡)", "NLG_A_LOW"),
    ("高压腔压气面积(㎡)", "NLG_A_HIGH"),
    ("大气压强(Mpa)", "Patm"),
    ("回油孔反行程(㎡)", "NLG_A_RET_NEG"),
    ("回油孔正行程(㎡)", "NLG_A_RET_POS"),
    ("主油孔反行程(㎡)", "NLG_A_MAIN_NEG"),
    ("回油腔压油面积(㎡)", "NLG_A_RET_OIL"),
    ("低压腔初始充气压力(Mpa)", "NLG_P_LOW", True),
    ("高压腔初始充气压力(Mpa)", "NLG_P_HIGH"),
    ("低压腔初始充气容积(m³)", "NLG_V_LOW", True),
    ("高压腔初始充气容积(m³)", "NLG_V_HIGH"),
    ("气体多变指数(/)", "NLG_n_Poly", True),
    ("主油孔缩流系数(/)", "NLG_MAIN_Cd", True),
    ("回油孔缩流系数(/)", "NLG_RET_Cd"),
    ("前起轮胎质量(kg)", "NLG_m"),
    ("前起绕xy轴转动惯量(kg·m²)", "NLG_Ixx_Iyy"),
    ("前起绕z轴转动惯量(kg·m²)", "NLG_Izz"),
]

DROP_ROAD_LOCATION_PARAMETERS = [
    ("路面位置X(mm)", "lumian_road_part.location.x"),
    ("路面位置Y(mm)", "lumian_road_part.location.y"),
    ("路面位置Z(mm)", "lumian_road_part.location.z"),
]


# 构建插件对话框窗体
class DropDialog(QDialog):
    
    def __init__(self, parent=None):
        super(DropDialog, self).__init__(parent)
        print("开启Drop对话框构造函数")
        self.initUI()

    def initUI(self):
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        active_scene = SelectionMonitor.get_active_scene()
        self.strModelName = getattr(active_scene, "Name", "") if active_scene else ""

        #--------------创建对话框主布局：左右结构[cite: 5]
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        # ================= 1. 左侧区域：图片交互区 + 底部按钮[cite: 5] =================
        leftLayout = QVBoxLayout()
        
        #----------------------定义图片中各硬点区域的位置和名称
        rect_list = []
        hp_name_list = []
        
        rect = QRect(42, 35, 78, 27); rect_list.append(rect); hp_name_list.append("hps_uc_top")
        rect = QRect(42, 82, 78, 27); rect_list.append(rect); hp_name_list.append("hps_lc_top")
        rect = QRect(5, 275, 78, 27); rect_list.append(rect); hp_name_list.append("hps_uc_bot")
        rect = QRect(5, 322, 78, 27); rect_list.append(rect); hp_name_list.append("hps_lc_bot")
        rect = QRect(98, 323, 110, 27); rect_list.append(rect); hp_name_list.append("hpl_wheel_center1")
        rect = QRect(267, 27, 110, 27); rect_list.append(rect); hp_name_list.append("hps_db_sf_atch")
        rect = QRect(380, 190, 110, 27); rect_list.append(rect); hp_name_list.append("hps_db_uc_atch")
        rect = QRect(380, 253, 110, 27); rect_list.append(rect); hp_name_list.append("hps_lta_uta_atch")
        rect = QRect(380, 287, 110, 27); rect_list.append(rect); hp_name_list.append("hps_uta_uc_atch")
        rect = QRect(380, 322, 110, 27); rect_list.append(rect); hp_name_list.append("hps_lta_lc_atch")

        # 创建图片显示控件[cite: 5]
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
        mainLayout.addWidget(self.tabs, 6)

        # --- Tab 1: 结构参数 ---
        self.structTab = QWidget()
        sub2FormLayout = QFormLayout(self.structTab)
        
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
        self.hpStatusLabel = QLabel("硬点参数化仅适用于template_2_drop的ADM导入模型")
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
        self.simVariableTable = VariableInputTable.VariableInputTable(
            DROP_SIMULATION_VARIABLES + DROP_ROAD_LOCATION_PARAMETERS,
            self.simTab,
        )
        simLayout.addWidget(self.simVariableTable)

        self.densityEdit = self.simVariableTable.editor("NLG_rho_Oil")
        self.oilAreaEdit = self.simVariableTable.editor("NLG_A_MAIN_OIL")
        self.oilHoleAreaEdit = self.simVariableTable.editor("NLG_A_MAIN_POS")
        self.airAreaEdit = self.simVariableTable.editor("NLG_A_LOW")
        self.patmEdit = self.simVariableTable.editor("Patm")
        self.NLG_Asdl_Edit = self.simVariableTable.editor("NLG_A_RET_NEG")
        self.NLG_Asd_Edit = self.simVariableTable.editor("NLG_A_RET_POS")
        self.NLG_Ahdl_Edit = self.simVariableTable.editor("NLG_A_MAIN_NEG")
        self.NLG_As_Edit = self.simVariableTable.editor("NLG_A_RET_OIL")
        self.Pa0Result = self.simVariableTable.editor("NLG_P_LOW")
        self.Va0Result = self.simVariableTable.editor("NLG_V_LOW")
        self.GammaResult = self.simVariableTable.editor("NLG_n_Poly")
        self.CdResult = self.simVariableTable.editor("NLG_MAIN_Cd")
        self.highPressureEdit = self.simVariableTable.editor("NLG_P_HIGH")
        self.highVolumeEdit = self.simVariableTable.editor("NLG_V_HIGH")
        self.highAreaEdit = self.simVariableTable.editor("NLG_A_HIGH")
        self.returnCdEdit = self.simVariableTable.editor("NLG_RET_Cd")
        self.tireMassEdit = self.simVariableTable.editor("NLG_m")
        self.tireIxxIyyEdit = self.simVariableTable.editor("NLG_Ixx_Iyy")
        self.tireIzzEdit = self.simVariableTable.editor("NLG_Izz")
        self.roadLocationXEdit = self.simVariableTable.editor(
            "lumian_road_part.location.x"
        )
        self.roadLocationYEdit = self.simVariableTable.editor(
            "lumian_road_part.location.y"
        )
        self.roadLocationZEdit = self.simVariableTable.editor(
            "lumian_road_part.location.z"
        )

        simButtonLayout = QHBoxLayout()
        simButtonLayout.addStretch()
        self.simOkButton = QPushButton("设置仿真参数")
        self.calibrationOkButton = QPushButton("启用参数校准")
        simButtonLayout.addWidget(self.simOkButton)
        simButtonLayout.addWidget(self.calibrationOkButton)
        simLayout.addLayout(simButtonLayout)

        self.tabs.addTab(self.simTab, "仿真变量")


        # --- Tab 3: 实验数据 (原自校准参数整合) ---
        self.expTab = QWidget()
        sub3FormLayout = QFormLayout(self.expTab)
        
        self.data_F0_Edit = QLineEdit(self); self.data_F0_Edit.setText("0.0")
        sub3FormLayout.addRow("静压曲线-初始点力值F0：", self.data_F0_Edit)

        self.data_Ff_Edit = QLineEdit(self); self.data_Ff_Edit.setText("0.0")
        sub3FormLayout.addRow("静压曲线-终点力值Ff：", self.data_Ff_Edit)

        self.data_Ffr_Edit = QLineEdit(self); self.data_Ffr_Edit.setText("0.0")
        sub3FormLayout.addRow("静压曲线-摩擦力值Ffr:", self.data_Ffr_Edit)

        self.data_F3_x_Edit = QLineEdit(self); self.data_F3_x_Edit.setText("0.0")
        sub3FormLayout.addRow("静压曲线-缓冲器最大位移F3_x:", self.data_F3_x_Edit)

        self.data_F5_x_Edit = QLineEdit(self); self.data_F5_x_Edit.setText("0.0")
        sub3FormLayout.addRow("缓冲器最大位移F5_x:", self.data_F5_x_Edit)

        self.data_F5_y_Edit = QLineEdit(self); self.data_F5_y_Edit.setText("0.0")
        sub3FormLayout.addRow("缓冲器最大位移处垂向载荷F5_y:", self.data_F5_y_Edit)

        self.data_F6_x_Edit = QLineEdit(self); self.data_F6_x_Edit.setText("0.0")
        sub3FormLayout.addRow("最大垂向载荷处缓冲器位移F6_x:", self.data_F6_x_Edit)

        self.data_F6_y_Edit = QLineEdit(self); self.data_F6_y_Edit.setText("0.0")
        sub3FormLayout.addRow("最大垂向载荷F6_y:", self.data_F6_y_Edit)

        self.data_s_Edit = QLineEdit(self); self.data_s_Edit.setText("0.0")
        sub3FormLayout.addRow("缓冲器速度:", self.data_s_Edit)

        self.paramCalibButton = QPushButton("执行参数自校准", self)
        sub3FormLayout.addRow("", self.paramCalibButton)

        self.tabs.addTab(self.expTab, "实验数据")


        # ================= 数据读取与变量初始化[cite: 5] =================
        if self.strModelName:
            for row in DROP_SIMULATION_VARIABLES:
                variable_name = row[1]
                var_list = Common.getDesignVariable(variable_name)
                if var_list:
                    precision = 8 if variable_name == "NLG_rho_Oil" else 4
                    self.simVariableTable.editor(variable_name).setText(
                        ("{:.%df}" % precision).format(var_list[0])
                    )
            try:
                road_location = DropRoadPosition.get_location(active_scene)
            except RuntimeError:
                road_location = None
            if road_location is not None:
                for row, value in zip(
                    DROP_ROAD_LOCATION_PARAMETERS,
                    road_location,
                ):
                    self.simVariableTable.editor(row[1]).setText(
                        "{:.4f}".format(value)
                    )


        # ================= 绑定信号和槽[cite: 5] =================
        self.okPushButton.clicked.connect(self.okClickButton)
        self.modelGenerateButton.clicked.connect(self.modelGenerate)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.simOkButton.clicked.connect(self.okSimClickButton)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.calibrationOkButton.clicked.connect(self.okCalibrationClickButton)
        self.paramCalibButton.clicked.connect(self.paramCalibration)

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

        ascene = SelectionMonitor.get_active_scene()
        self.strModelName = getattr(ascene, "Name", "") if ascene else ""
        compatibility_error = DropAdmParameterization.compatibility_error(ascene)
        hp_name = DropAdmParameterization.canonical_hardpoint_name(hp_name)
        self.strSelFullName = DropAdmParameterization.hardpoint_path(
            hp_name,
            ascene,
        )
        node = SelectionMonitor.get_active_node(self.strSelFullName)
        if node :
            self.hpName.setText(hp_name)
            self.xMarker.setText("{:.12g}".format(node.location.x))
            self.yMarker.setText("{:.12g}".format(node.location.y))
            self.zMarker.setText("{:.12g}".format(node.location.z))

            axes = DropAdmParameterization.get_rule(hp_name)
            is_drop_model = not compatibility_error
            self.xMarker.setEnabled(bool(is_drop_model and axes and "x" in axes))
            self.yMarker.setEnabled(bool(is_drop_model and axes and "y" in axes))
            self.zMarker.setEnabled(bool(is_drop_model and axes and "z" in axes))
            self.markOkButton.setEnabled(bool(is_drop_model and axes))

            if not is_drop_model:
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

    #---------------------定义模型生成槽函数
    def modelGenerate(self) :
        ModelScriptRunner.generate_model_from_dialog(
            self,
            os.path.join(AutoGenerater_dir, "model_template_2_drop.py"),
            "GCMB",
            globals(),
        )

    #---------------------ADM主体 + 硬点CMD + 公式补丁导入
    def modelImport(self) :
        ModelImportRunner.generate_imported_model_from_dialog(
            self,
            os.path.join(Model_dir, "template_2_drop"),
            "template_2_drop",
        )

    #---------------------从Excel替换模型中的Spline数据
    def openSplineImportDialog(self):
        SplineImportDialog.show_spline_import_dialog(self)

    #------------------------------------定义窗口关闭事件
    def closeEvent(self, event ):
        self.selectionMonitor.stop()
        super().closeEvent(event)

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
            result = DropAdmParameterization.adjust_hardpoint(
                self.strSelFullName,
                strX,
                strY,
                strZ,
                scene=ascene,
            )
        except Exception as exc:
            print("[Drop参数化异常] {}".format(exc))
            self.hpStatusLabel.setText("硬点调整发生未预期异常，模型未确认修改")
            self.hpStatusLabel.setStyleSheet("color: #b00020;")
            QMessageBox.critical(
                self,
                "硬点调整异常",
                "硬点参数化发生未预期异常：{}\n请重新导入模型后重试。".format(exc),
            )
        finally:
            QApplication.restoreOverrideCursor()

        axes = DropAdmParameterization.get_rule(self.strSelFullName)
        is_drop_model = DropAdmParameterization.is_compatible_scene(ascene)
        self.markOkButton.setEnabled(bool(is_drop_model and axes))
        if result is None:
            return

        if not result.success:
            self.hpStatusLabel.setText(result.message)
            self.hpStatusLabel.setStyleSheet("color: #b00020;")
            QMessageBox.warning(self, "硬点调整失败", result.message)
            for error in result.errors:
                print("[Drop参数化错误] {}".format(error))
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
        active_scene = SelectionMonitor.get_active_scene()
        road_coordinates = (
            float(self.roadLocationXEdit.text()),
            float(self.roadLocationYEdit.text()),
            float(self.roadLocationZEdit.text()),
        )
        if DropRoadPosition.find_road_part(active_scene) is None:
            QMessageBox.warning(
                self,
                "路面位置设置失败",
                "当前模型中未找到路面零件 lumian_road_part",
            )
            return
        if DropRoadPosition.find_ground_reference(active_scene) is None:
            QMessageBox.warning(
                self,
                "路面位置设置失败",
                "当前模型中未找到 ground.lumian_ref_1",
            )
            return
        if not all(math.isfinite(value) for value in road_coordinates):
            QMessageBox.warning(
                self,
                "路面位置设置失败",
                "路面位置必须是有限数值",
            )
            return
        for row in DROP_SIMULATION_VARIABLES:
            read_only = bool(row[2]) if len(row) > 2 else False
            if read_only:
                continue
            variable_name = row[1]
            Common.setDesignVariable(
                variable_name,
                float(self.simVariableTable.editor(variable_name).text()),
            )
        DropRoadPosition.set_location(active_scene, road_coordinates)
        pass

    #----------------------退出按钮点击事件
    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()

    #=================参数自校准逻辑函数====================
    def paramCalibration(self):
        if not self.simVariableTable.validate_values(self):
            return
        try:
            F0 = float(self.data_F0_Edit.text()) if self.data_F0_Edit.text() else 0.0
            Ff = float(self.data_Ff_Edit.text()) if self.data_Ff_Edit.text() else 0.0
            Ffr = float(self.data_Ffr_Edit.text()) if self.data_Ffr_Edit.text() else 0.0
            F3_x = float(self.data_F3_x_Edit.text()) if self.data_F3_x_Edit.text() else 0.0
            F5_x = float(self.data_F5_x_Edit.text()) if self.data_F5_x_Edit.text() else 0.0
            F5_y = float(self.data_F5_y_Edit.text()) if self.data_F5_y_Edit.text() else 0.0
            F6_x = float(self.data_F6_x_Edit.text()) if self.data_F6_x_Edit.text() else 0.0
            F6_y = float(self.data_F6_y_Edit.text()) if self.data_F6_y_Edit.text() else 0.0
            s = float(self.data_s_Edit.text()) if self.data_s_Edit.text() else 0.0

            NLG_A_LOW = float(self.airAreaEdit.text()) if self.airAreaEdit.text() else 0.0
            NLG_A_MAIN_OIL = float(self.oilAreaEdit.text()) if self.oilAreaEdit.text() else 0.0
            NLG_A_MAIN_POS = float(self.oilHoleAreaEdit.text()) if self.oilHoleAreaEdit.text() else 0.0
            Patm = float(self.patmEdit.text()) if self.patmEdit.text() else 0.0
            density = float(self.densityEdit.text()) if self.densityEdit.text() else 0.0
        except ValueError:
            self.Pa0Result.setText("无效输入")
            self.Va0Result.setText("无效输入")
            self.GammaResult.setText("无效输入")
            self.CdResult.setText("无效输入")
            return
         
        NLG_P_LOW = 0
        NLG_V_LOW = 0
        NLG_n_Poly = 0
        NLG_MAIN_Cd = 0
                          
        try:
            Fa5 = F5_y - Ffr
            NLG_P_LOW = F0 / NLG_A_LOW
            NLG_V_LOW = (((Ff / NLG_A_LOW) + Patm) * NLG_A_LOW * F3_x) / ((Ff / NLG_A_LOW) - NLG_P_LOW)
            NLG_n_Poly = math.log(((Fa5 / NLG_A_LOW) + Patm) / (NLG_P_LOW + Patm), NLG_V_LOW / (NLG_V_LOW - NLG_A_LOW * F5_x))
            Fa6 = NLG_A_LOW * ((NLG_P_LOW + Patm) * (math.pow((NLG_V_LOW / (NLG_V_LOW - NLG_A_LOW * F6_x)), NLG_n_Poly)) - Patm)
            Fh6 = F6_y - Fa6 - Ffr
            NLG_MAIN_Cd = math.sqrt((density * math.pow(NLG_A_MAIN_OIL, 3) * math.pow(s, 2)) / (2000 * Fh6 * math.pow(NLG_A_MAIN_POS, 2)))
            
            self.Pa0Result.setText(f"{NLG_P_LOW:.4f}")
            self.Va0Result.setText(f"{NLG_V_LOW:.4f}")
            self.GammaResult.setText(f"{NLG_n_Poly:.4f}")
            self.CdResult.setText(f"{NLG_MAIN_Cd:.4f}")

            Common.setDesignVariable("NLG_P_LOW", float(self.Pa0Result.text()))
            Common.setDesignVariable("NLG_V_LOW", float(self.Va0Result.text()))
            Common.setDesignVariable("NLG_n_Poly", float(self.GammaResult.text()))
            Common.setDesignVariable("NLG_MAIN_Cd", float(self.CdResult.text()))

        except (ValueError, ZeroDivisionError):
            self.Pa0Result.setText("无效输入")
            self.Va0Result.setText("无效输入")
            self.GammaResult.setText("无效输入")
            self.CdResult.setText("无效输入")
            return

    def okCalibrationClickButton(self):
        self.paramCalibration()


def show_drop_dialog(parent=None):
    dialog = DropDialog(parent)
    dialog.setWindowTitle("落震仿真对话框")
    dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    dialog.show()
    return dialog


if __name__ == '__main__':
    _drop_dialog = show_drop_dialog()

    
