# -*- coding: utf-8 -*-
"""Shared interface for every dedicated engineering template case."""

from __future__ import print_function

import os

from PySide2.QtCore import QSettings, QSize, Qt
from PySide2.QtGui import QDoubleValidator, QIcon
from PySide2.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

import DynamicModelParameters
import FullModelGenerateDialog
import InformationConfiguration
import MarkerConfigurationTable
import ModelImportRunner
import ModelMarkerParameters
import RoadPosition
import ResultCurveWidget
import ResultData
import SelectionMonitor
import SplineImportDialog
import StructuralParameterization
import TirePartParameters
import VariableExcelIO
import VariableInputTable


ROAD_LOCATION_ROWS = (
    ("路面位置X(mm)", "road.location.x"),
    ("路面位置Y(mm)", "road.location.y"),
    ("路面位置Z(mm)", "road.location.z"),
)

PARAMETER_GROUP_DEFINITIONS = (
    (
        "buffer_parameters",
        "缓冲器参数信息",
        "设置缓冲器参数",
        True,
    ),
    (
        "other_parameters",
        "其他参数信息",
        "设置其他参数",
        True,
    ),
    (
        "structure_property_parameters",
        "结构参数信息",
        "设置结构参数信息",
        False,
    ),
)

PARAMETER_GROUP_LABELS = {
    key: tab_title
    for key, tab_title, _apply_text, _allow_excel in PARAMETER_GROUP_DEFINITIONS
}

# Labels are presentation metadata only.  Variable discovery and write-back
# always follow the active model, so model revisions do not require UI changes.
COMMON_VARIABLE_LABELS = {
    "NLG_rho_Oil": "油液密度(kg/m³)",
    "NLG_A_MAIN_OIL": "主油腔压油面积(㎡)",
    "NLG_A_MAIN_POS": "主油孔正行程(㎡)",
    "NLG_A_LOW": "低压腔压气面积(㎡)",
    "NLG_A_HIGH": "高压腔压气面积(㎡)",
    "Patm": "大气压强(Mpa)",
    "NLG_A_RET_NEG": "回油孔反行程(㎡)",
    "NLG_A_RET_POS": "回油孔正行程(㎡)",
    "NLG_A_MAIN_NEG": "主油孔反行程(㎡)",
    "NLG_A_RET_OIL": "回油腔压油面积(㎡)",
    "NLG_P_LOW": "低压腔初始充气压力(Mpa)",
    "NLG_P_HIGH": "高压腔初始充气压力(Mpa)",
    "NLG_V_LOW": "低压腔初始充气容积(m³)",
    "NLG_V_HIGH": "高压腔初始充气容积(m³)",
    "NLG_n_Poly": "气体多变指数(/)",
    "NLG_MAIN_Cd": "主油孔缩流系数(/)",
    "NLG_RET_Cd": "回油孔缩流系数(/)",
    "NLG_m": "前起轮胎质量(kg)",
    "NLG_Ixx_Iyy": "前起绕xy轴转动惯量(kg·m²)",
    "NLG_Izz": "前起绕z轴转动惯量(kg·m²)",
    "stiffness_oil": "油液刚度",
    "stiffness_stop": "限制力刚度",
    "stiffness_air": "空气弹簧力刚度",
    "damping_oil": "油液阻尼",
    "damping_stop": "限制力阻尼",
    "damping_air": "空气弹簧力阻尼",
    "damping_coefficient": "减摆阻尼系数",
    "initial_vel": "初始速度",
    "vel": "运动速度",
    "T_1": "转弯开始时间(s)",
    "T_2": "转弯结束时间(s)",
    "angle": "转弯角度(deg)",
    "NLG_DRAG_COEFF": "前起阻力系数(/)",
    "NLG_DRAG_CORFF": "前起阻力系数(/)",
    "NLG_PROJ_AREA": "前起投影面积(㎡)",
    "AIR_DENSITY": "空气密度(kg/m³)",
    "AIR_VELOCITY": "气流速度(m/s)",
    "NLG_ACTUATOR_STROKE": "前起作动筒行程(mm)",
    "NLG_RETRACT_TIME": "前起收起时间(s)",
    "NLG_UP_HOLD_TIME": "前起上位保持时间(s)",
    "NLG_EXTEND_TIME": "前起放下时间(s)",
    "MLG_n_Poly": "气体多变指数",
    "MLG_rho_Oil": "油液密度",
    "MLG_A_LOW": "低压腔有效面积",
    "MLG_V_LOW": "低压腔初始体积",
    "MLG_P_LOW": "低压腔初始压力",
    "MLG_A_MAIN_OIL": "主腔油液面积",
    "MLG_A_RET_OIL": "回油腔油液面积",
    "MLG_A_MAIN_POS": "主腔正向节流面积",
    "MLG_A_MAIN_NEG": "主腔负向节流面积",
    "MLG_A_RET_POS": "回油腔正向节流面积",
    "MLG_A_RET_NEG": "回油腔负向节流面积",
    "MLG_RET_Cd": "回油腔流量系数",
    "MLG_MAIN_Cd": "主腔流量系数",
    "MLG_Tb": "刹车力矩",
    "MLG_S0": "缓冲器初始长度",
    "MLG_Vx": "初始前进速度",
    "MLG_m": "轮胎质量",
    "MLG_Ixx_Iyy": "轮胎横向转动惯量",
    "MLG_lzz": "轮胎纵向转动惯量",
}


class DedicatedCaseDialog(QDialog):
    """One ADM-driven interface reusable by copied dedicated cases."""

    def __init__(self, config, parent=None):
        super(DedicatedCaseDialog, self).__init__(parent)
        self.config = dict(config)
        self.strSelFullName = ""
        self.strSelGeoFullName = ""
        self.markerItems = []
        self.contextSettings = QSettings(
            "Jusme",
            self.config.get("settings_key") or "Template_2_GeneralWindow",
        )
        self.currentAdmPath = ""
        self.currentModelDir = os.path.abspath(
            self.config.get("model_dir") or os.getcwd()
        )
        self.currentStructureParameterFile = ""
        self._restoreSavedModelContext()
        self.informationConfiguration = InformationConfiguration.empty_configuration(
            self.currentModelDir
        )
        self.structureParameterItems = []
        self.structureParameterErrors = []
        self.markerLinkageDefinitions = []
        self.structureParameterDefinitions = []
        self._loadModelConfigurationData()
        self.parameterTables = {}
        self.parameterStatuses = {}
        self.parameterExcelButtons = {}
        self.parameterRefreshButtons = {}
        self.parameterApplyButtons = {}
        self.dynamicParameterGroups = {
            key: [] for key in InformationConfiguration.PARAMETER_SECTION_KEYS
        }
        self.parameterGroupsFromConfiguration = {
            key: False for key in InformationConfiguration.PARAMETER_SECTION_KEYS
        }
        # Aggregate alias retained for compatibility with existing helpers.
        self.dynamicSimulationVariables = []
        self.dynamicTireVariables = []
        self.dynamicTirePartParameters = []
        self.simulationParametersFromConfiguration = False
        self.postprocessingEntriesById = {}
        self.postprocessingCurves = {}
        self.postprocessingWorkDiagrams = {}
        self.postprocessingLoadErrors = []
        saved_result_directory = str(
            self.contextSettings.value("postprocessing/result_directory", "") or ""
        )
        self.defaultPostprocessingResultDirectory = (
            ResultData.default_result_directory(__file__)
        )
        self.postprocessingResultDirectory = (
            self.defaultPostprocessingResultDirectory
            or saved_result_directory
        )
        self._build_ui()

    def _build_ui(self):
        main_layout = QVBoxLayout(self)

        self.modelImportButton = QPushButton("模型导入（ADM）", self)
        self.fullModelButton = QPushButton("生成完整模型", self)
        self.splineImportButton = QPushButton("修改样条曲线", self)
        self.configuredSplineButton = QPushButton("应用配置样条曲线", self)
        self.okPushButton = QPushButton("退出", self)
        button_layout = QHBoxLayout()
        button_layout.setSpacing(16)
        for button in (
            self.fullModelButton,
            self.modelImportButton,
            self.splineImportButton,
            self.configuredSplineButton,
        ):
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            button.setMinimumSize(178, 40)
            button.setStyleSheet(
                "QPushButton { color: #173f69; background: white; "
                "border: 1px solid #7899ba; border-radius: 7px; "
                "padding: 6px 14px; } "
                "QPushButton:hover { background: #edf5fc; }"
            )
        self.okPushButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.okPushButton.setMinimumSize(140, 40)
        self.okPushButton.setStyleSheet(
            "QPushButton { color: white; background: #1a61cb; "
            "border: 1px solid #1a61cb; border-radius: 7px; "
            "padding: 6px 14px; } "
            "QPushButton:hover { background: #1455b8; }"
        )
        button_layout.addStretch()
        button_layout.addWidget(self.fullModelButton)
        button_layout.addWidget(self.modelImportButton)
        button_layout.addWidget(self.splineImportButton)
        button_layout.addWidget(self.configuredSplineButton)
        button_layout.addWidget(self.okPushButton)

        self.tabs = QTabWidget(self)
        main_layout.addWidget(self.tabs, 1)
        self._build_structure_tab()
        self._build_information_structure_tab()
        self._build_parameter_tabs()
        self._build_tire_road_tab()
        self._build_postprocessing_tab()
        self._apply_button_icons()

        divider = QWidget(self)
        divider.setFixedHeight(1)
        divider.setStyleSheet("background-color: #d8e2ee;")
        main_layout.addWidget(divider)
        main_layout.addLayout(button_layout)

        self.okPushButton.clicked.connect(self.okClickButton)
        self.fullModelButton.clicked.connect(self.openFullModelGenerator)
        self.modelImportButton.clicked.connect(self.modelImport)
        self.splineImportButton.clicked.connect(self.openSplineImportDialog)
        self.configuredSplineButton.clicked.connect(self.applyConfiguredSplines)
        self.structureParameterSelector.currentIndexChanged.connect(
            self.structureParameterSelectorChanged
        )
        self.hpSelector.currentIndexChanged.connect(self.markerSelectorChanged)
        self.markerRefreshButton.clicked.connect(self.refreshMarkerList)
        self.markOkButton.clicked.connect(self.okMarkClickButton)
        self.dimensionOkButton.clicked.connect(self.okDimClickButton)
        self.infoMarkerRefreshButton.clicked.connect(
            self.reloadInformationConfiguration
        )
        self.infoMarkerApplyButton.clicked.connect(self.applyConfiguredMarkers)
        self.infoMarkerTable.applyRequested.connect(self.applyConfiguredMarkers)
        for group_key, _title, _apply_text, allow_excel in (
            PARAMETER_GROUP_DEFINITIONS
        ):
            self.parameterRefreshButtons[group_key].clicked.connect(
                self.reloadInformationConfiguration
            )
            self.parameterApplyButtons[group_key].clicked.connect(
                lambda _checked=False, key=group_key: self.applyParameterGroup(key)
            )
            self.parameterTables[group_key].applyRequested.connect(
                lambda key=group_key: self.applyParameterGroup(key)
            )
            if allow_excel:
                self.parameterExcelButtons[group_key].clicked.connect(
                    lambda _checked=False, key=group_key: self.importVariableExcel(
                        key
                    )
                )
        self.tireRoadRefreshButton.clicked.connect(self.refreshVariableTables)
        self.tireRoadOkButton.clicked.connect(self.okTireRoadClickButton)
        self.tireRoadVariableTable.applyRequested.connect(
            self.okTireRoadClickButton
        )
        self.postprocessingBrowseButton.clicked.connect(
            self.selectPostprocessingResultDirectory
        )
        self.postprocessingReloadButton.clicked.connect(
            self.loadPostprocessingResults
        )
        self.postprocessingModeSelector.currentIndexChanged.connect(
            self.postprocessingDisplayModeChanged
        )
        self.postprocessingDiagramSelector.currentIndexChanged.connect(
            self.showSelectedPostprocessingCurves
        )
        self.postprocessingCurveList.itemChanged.connect(
            self.showSelectedPostprocessingCurves
        )
        for editor in (self.xMarker, self.yMarker, self.zMarker):
            editor.returnPressed.connect(self.okMarkClickButton)
        for editor in (self.doubleLength, self.doubleRadius):
            editor.returnPressed.connect(self.okDimClickButton)
        # QDialog otherwise treats the first auto-default button as the Return
        # target.  That used to run modelImportButton after a parameter editor
        # had already handled Return, opening an unrelated ADM file dialog.
        for button in self.findChildren(QPushButton):
            button.setAutoDefault(False)
            button.setDefault(False)

        self._apply_standard_dialog()
        self.selectionMonitor = SelectionMonitor.SelectionMonitor(self)
        self.selectionMonitor.selectionChanged.connect(self.selectionSlot)
        self.selectionMonitor.start()
        self.refreshInformationMarkerTable()
        self.refreshMarkerList()
        self.refreshVariableTables()
        self.refreshPostprocessingConfiguration()

    def _apply_standard_dialog(self, width=1400, height=720):
        """Apply the common size without retaining the retired image widget."""
        try:
            self.setMinimumSize(1250, 660)
            self.resize(width, height)
            root_layout = self.layout()
            if root_layout is not None:
                root_layout.setContentsMargins(18, 18, 18, 18)
                root_layout.setSpacing(18)
        except Exception as exc:
            print("界面布局初始化失败，已使用宿主默认布局：{}".format(exc))
            self.resize(width, height)

    def _apply_button_icons(self):
        """Keep action icons consistent across the tabs and bottom toolbar."""
        icon_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "resources", "icons",
        )
        buttons = [
            (self.fullModelButton, "model_generate.png"),
            (self.modelImportButton, "model_import.png"),
            (self.splineImportButton, "spline_edit.png"),
            (self.configuredSplineButton, "spline_apply.png"),
            (self.markerRefreshButton, "refresh.png"),
            (self.markOkButton, "settings.png"),
            (self.dimensionOkButton, "settings.png"),
            (self.infoMarkerRefreshButton, "refresh.png"),
            (self.infoMarkerApplyButton, "settings.png"),
            (self.tireRoadRefreshButton, "refresh.png"),
            (self.tireRoadOkButton, "settings.png"),
            (self.postprocessingBrowseButton, "folder.png"),
            (self.postprocessingReloadButton, "results.png"),
        ]
        for group, icon_name in (
            (self.parameterExcelButtons, "excel_edit.png"),
            (self.parameterRefreshButtons, "refresh.png"),
            (self.parameterApplyButtons, "settings.png"),
        ):
            buttons.extend((button, icon_name) for button in group.values())
        icons = {}
        for button, icon_name in buttons:
            if icon_name not in icons:
                icons[icon_name] = QIcon(os.path.join(icon_dir, icon_name))
            button.setIcon(icons[icon_name])
            button.setIconSize(QSize(20, 20))
            button.setMinimumHeight(max(34, button.minimumHeight()))

    def _build_structure_tab(self):
        tab = QWidget(self)
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        panel_style = (
            "QFrame#structurePanel { border: 1px solid #aaaaaa; "
            "border-radius: 10px; }"
        )
        adjustment_panel = QFrame(tab)
        adjustment_panel.setObjectName("structurePanel")
        adjustment_panel.setStyleSheet(panel_style)
        adjustment_layout = QHBoxLayout(adjustment_panel)
        adjustment_layout.setContentsMargins(24, 16, 24, 16)
        adjustment_layout.setSpacing(18)
        adjustment_layout.addWidget(QLabel("调整方式：", adjustment_panel))
        self.structureParameterSelector = QComboBox(tab)
        self.structureParameterSelector.addItem("按信息配置表联动")
        adjustment_layout.addWidget(self.structureParameterSelector, 1)
        self.structureParameterInfo = QLabel(
            "可调Marker来自信息配置表，修改后自动执行配置的结构联动。",
            tab,
        )
        self.structureParameterInfo.setWordWrap(True)
        self.structureParameterInfo.setStyleSheet("color: #666666;")
        adjustment_layout.addWidget(self.structureParameterInfo, 2)
        layout.addWidget(adjustment_panel)

        panels = QHBoxLayout()
        panels.setSpacing(28)
        marker_panel = QFrame(tab)
        dimension_panel = QFrame(tab)
        for panel in (marker_panel, dimension_panel):
            panel.setObjectName("structurePanel")
            panel.setStyleSheet(panel_style)
            panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            panels.addWidget(panel, 1)
        layout.addLayout(panels, 1)

        marker_layout = QVBoxLayout(marker_panel)
        dimension_layout = QVBoxLayout(dimension_panel)
        marker_form = QFormLayout()
        dimension_form = QFormLayout()
        for panel_layout, form in (
            (marker_layout, marker_form),
            (dimension_layout, dimension_form),
        ):
            panel_layout.setContentsMargins(24, 22, 24, 20)
            panel_layout.setSpacing(14)
            form.setContentsMargins(0, 0, 0, 0)
            form.setHorizontalSpacing(18)
            form.setVerticalSpacing(14)
            form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
            form.setRowWrapPolicy(QFormLayout.DontWrapRows)
            panel_layout.addLayout(form)

        self.hpSelector = QComboBox(tab)
        self.hpSelector.addItem("请选择Marker")
        self.hpSelector.setMinimumContentsLength(12)
        self.hpSelector.setSizeAdjustPolicy(
            QComboBox.AdjustToMinimumContentsLengthWithIcon
        )
        self.markerRefreshButton = QPushButton("刷新Marker列表", tab)
        marker_selector_row = QWidget(tab)
        marker_selector_layout = QHBoxLayout(marker_selector_row)
        marker_selector_layout.setContentsMargins(0, 0, 0, 0)
        marker_selector_layout.addWidget(self.hpSelector, 1)
        marker_selector_layout.addWidget(self.markerRefreshButton)
        marker_form.addRow("可调Marker：", marker_selector_row)

        self.hpName = QLineEdit(tab)
        self.hpName.setReadOnly(True)
        marker_form.addRow("Marker路径：", self.hpName)
        self.xMarker = QLineEdit(tab)
        self.yMarker = QLineEdit(tab)
        self.zMarker = QLineEdit(tab)
        marker_form.addRow("X坐标：", self.xMarker)
        marker_form.addRow("Y坐标：", self.yMarker)
        marker_form.addRow("Z坐标：", self.zMarker)
        for editor in (self.xMarker, self.yMarker, self.zMarker):
            validator = QDoubleValidator(-1.0e9, 1.0e9, 12, editor)
            validator.setNotation(QDoubleValidator.StandardNotation)
            editor.setValidator(validator)
            editor.setEnabled(False)
        self.markOkButton = QPushButton("应用结构参数", tab)
        self.markOkButton.setEnabled(False)
        self.hpStatusLabel = QLabel("请从下拉框选择需要调整的Marker", tab)
        self.hpStatusLabel.setWordWrap(True)
        self.hpStatusLabel.setStyleSheet("color: #666666;")
        marker_layout.addWidget(self.hpStatusLabel)
        marker_layout.addStretch(1)
        marker_layout.addWidget(self.markOkButton, 0, Qt.AlignHCenter)

        self.selGeo = QLineEdit(tab)
        self.doubleRadius = QLineEdit(tab)
        self.doubleLength = QLineEdit(tab)
        for editor in (self.doubleRadius, self.doubleLength):
            validator = QDoubleValidator(1.0e-9, 1.0e9, 12, editor)
            validator.setNotation(QDoubleValidator.StandardNotation)
            editor.setValidator(validator)
        dimension_form.addRow("几何体：", self.selGeo)
        dimension_form.addRow("半径：", self.doubleRadius)
        dimension_form.addRow("长度：", self.doubleLength)
        self.dimensionOkButton = QPushButton("设置圆柱尺寸", tab)
        self.dimensionOkButton.setEnabled(False)
        dimension_layout.addStretch(1)
        dimension_layout.addWidget(self.dimensionOkButton, 0, Qt.AlignHCenter)
        for editor in (
            self.structureParameterSelector, self.hpSelector,
            self.markerRefreshButton, self.hpName,
            self.xMarker, self.yMarker, self.zMarker,
            self.selGeo, self.doubleRadius, self.doubleLength,
        ):
            editor.setMinimumHeight(30)
        for button in (self.markOkButton, self.dimensionOkButton):
            button.setMinimumSize(180, 34)
        self.tabs.addTab(tab, "结构参数")

    def _build_information_structure_tab(self):
        tab = QWidget(self)
        layout = QVBoxLayout(tab)
        self.infoMarkerTable = MarkerConfigurationTable.MarkerConfigurationTable(tab)
        layout.addWidget(self.infoMarkerTable, 1)
        self.infoMarkerStatus = QLabel("", tab)
        self.infoMarkerStatus.setWordWrap(True)
        footer = QHBoxLayout()
        footer.addWidget(self.infoMarkerStatus, 1)
        self.infoMarkerRefreshButton = QPushButton("重新读取配置表", tab)
        self.infoMarkerApplyButton = QPushButton("设置结构参数", tab)
        footer.addWidget(self.infoMarkerRefreshButton)
        footer.addWidget(self.infoMarkerApplyButton)
        layout.addLayout(footer)
        self.tabs.addTab(tab, "结构参数表")

    def _build_parameter_tabs(self):
        for group_key, tab_title, apply_text, allow_excel in (
            PARAMETER_GROUP_DEFINITIONS
        ):
            self._build_parameter_tab(
                group_key,
                tab_title,
                apply_text,
                allow_excel,
            )

    def _build_parameter_tab(
        self,
        group_key,
        tab_title,
        apply_text,
        allow_excel,
    ):
        tab = QWidget(self)
        layout = QVBoxLayout(tab)
        table = VariableInputTable.VariableInputTable([], tab)
        layout.addWidget(table)
        status = QLabel("", tab)
        status.setWordWrap(True)
        footer = QHBoxLayout()
        footer.addWidget(status, 1)
        if allow_excel:
            excel_button = QPushButton("Excel批量修改", tab)
            excel_button.setToolTip(
                "Excel A列填写变量名称/路径，B列填写新的 function；支持常值和公式文本"
            )
            footer.addWidget(excel_button)
            self.parameterExcelButtons[group_key] = excel_button
        refresh_button = QPushButton("重新读取配置表", tab)
        apply_button = QPushButton(apply_text, tab)
        footer.addWidget(refresh_button)
        footer.addWidget(apply_button)
        layout.addLayout(footer)
        self.tabs.addTab(tab, tab_title)
        self.parameterTables[group_key] = table
        self.parameterStatuses[group_key] = status
        self.parameterRefreshButtons[group_key] = refresh_button
        self.parameterApplyButtons[group_key] = apply_button

    def _build_tire_road_tab(self):
        tab = QWidget(self)
        layout = QVBoxLayout(tab)
        self.tireRoadVariableTable = VariableInputTable.VariableInputTable([], tab)
        layout.addWidget(self.tireRoadVariableTable)
        self.tireRoadStatus = QLabel("", tab)
        self.tireRoadStatus.setWordWrap(True)
        footer = QHBoxLayout()
        footer.addWidget(self.tireRoadStatus, 1)
        self.tireRoadRefreshButton = QPushButton("刷新参数列表", tab)
        self.tireRoadOkButton = QPushButton("设置轮胎与路面参数", tab)
        footer.addWidget(self.tireRoadRefreshButton)
        footer.addWidget(self.tireRoadOkButton)
        layout.addLayout(footer)
        self.tabs.addTab(tab, "轮胎与路面")

    def _build_postprocessing_tab(self):
        tab = QWidget(self)
        layout = QVBoxLayout(tab)

        result_row = QWidget(tab)
        result_layout = QHBoxLayout(result_row)
        result_layout.setContentsMargins(0, 0, 0, 0)
        self.postprocessingResultPath = QLineEdit(result_row)
        self.postprocessingResultPath.setReadOnly(True)
        self.postprocessingResultPath.setPlaceholderText(
            "请选择仿真生成的 object_data 目录或其上级目录"
        )
        self.postprocessingResultPath.setText(
            self.postprocessingResultDirectory
        )
        self.postprocessingBrowseButton = QPushButton("选择其他结果目录", result_row)
        result_layout.addWidget(self.postprocessingResultPath, 1)
        result_layout.addWidget(self.postprocessingBrowseButton)
        layout.addWidget(result_row)

        controls = QHBoxLayout()
        controls.addWidget(QLabel("显示方式：", tab))
        self.postprocessingModeSelector = QComboBox(tab)
        self.postprocessingModeSelector.addItem("时程曲线", "time_history")
        self.postprocessingModeSelector.addItem("功量图", "work_diagram")
        controls.addWidget(self.postprocessingModeSelector)
        controls.addWidget(QLabel("功量图：", tab))
        self.postprocessingDiagramSelector = QComboBox(tab)
        self.postprocessingDiagramSelector.setMinimumWidth(220)
        self.postprocessingDiagramSelector.setEnabled(False)
        controls.addWidget(self.postprocessingDiagramSelector)
        controls.addWidget(
            QLabel("鼠标靠近曲线可查看采样点坐标", tab)
        )
        controls.addStretch()
        layout.addLayout(controls)

        curve_area = QWidget(tab)
        curve_area_layout = QHBoxLayout(curve_area)
        curve_area_layout.setContentsMargins(0, 0, 0, 0)
        curve_area_layout.setSpacing(12)

        curve_list_panel = QWidget(curve_area)
        curve_list_layout = QVBoxLayout(curve_list_panel)
        curve_list_layout.setContentsMargins(0, 0, 0, 0)
        self.postprocessingCurveListLabel = QLabel(
            "后处理曲线（可多选）", curve_list_panel
        )
        curve_list_layout.addWidget(self.postprocessingCurveListLabel)
        self.postprocessingCurveList = QListWidget(curve_list_panel)
        self.postprocessingCurveList.setMinimumWidth(230)
        self.postprocessingCurveList.setMaximumWidth(360)
        curve_list_layout.addWidget(self.postprocessingCurveList, 1)
        curve_area_layout.addWidget(curve_list_panel)

        self.postprocessingCurveWidget = ResultCurveWidget.ResultCurveWidget(
            curve_area
        )
        curve_area_layout.addWidget(self.postprocessingCurveWidget, 1)
        layout.addWidget(curve_area, 1)
        self.postprocessingStatus = QLabel("", tab)
        self.postprocessingStatus.setWordWrap(True)
        footer = QHBoxLayout()
        footer.addWidget(self.postprocessingStatus, 1)
        self.postprocessingReloadButton = QPushButton("加载仿真结果", tab)
        footer.addWidget(self.postprocessingReloadButton)
        layout.addLayout(footer)
        self.tabs.addTab(tab, "后处理")

    def _loadInformationConfigurationData(self):
        case_model_dir = self.currentModelDir
        information_file = InformationConfiguration.find_information_workbook(
            case_model_dir
        )
        if not information_file:
            self.informationConfiguration = (
                InformationConfiguration.empty_configuration(case_model_dir)
            )
            self.informationConfiguration["warnings"].append(
                "当前ADM目录未找到信息配置表，已使用模型动态识别功能"
            )
            return
        try:
            self.informationConfiguration = (
                InformationConfiguration.load_information_configuration(
                    case_model_dir,
                    information_file,
                )
            )
        except InformationConfiguration.InformationConfigurationError as exc:
            self.informationConfiguration = (
                InformationConfiguration.empty_configuration(
                    case_model_dir,
                    str(exc),
                )
            )

    def _loadStructureParameterData(self):
        self.markerLinkageDefinitions = []
        self.structureParameterDefinitions = []
        self.structureParameterErrors = []
        if not self.currentStructureParameterFile:
            return
        try:
            self.markerLinkageDefinitions = (
                StructuralParameterization.load_parameter_file(
                    self.currentStructureParameterFile
                )
            )
            self.structureParameterDefinitions = [
                parameter
                for parameter in self.markerLinkageDefinitions
                if not parameter.get("table_only")
            ]
        except StructuralParameterization.ConfigurationError as exc:
            self.structureParameterErrors = [str(exc)]

    def _loadModelConfigurationData(self):
        self._loadInformationConfigurationData()
        self._loadStructureParameterData()

    def _restoreSavedModelContext(self):
        scene = SelectionMonitor.get_active_scene()
        active_model_name = (
            str(getattr(scene, "Name", "") or "").strip()
            if scene is not None
            else ""
        )
        active_signature = ModelImportRunner.scene_signature(scene)
        active_inventory = ModelImportRunner.scene_inventory(scene)
        context = ModelImportRunner.restore_model_context(
            self.contextSettings,
            active_model_name,
            active_signature,
            active_inventory,
        )
        if context is None:
            return False
        self.currentAdmPath = context["adm_path"]
        self.currentModelDir = context["model_dir"]
        self.currentStructureParameterFile = context[
            "structure_parameter_file"
        ]
        # Migrate legacy exact-signature settings to the tolerant inventory
        # format after the context has been restored successfully.
        ModelImportRunner.save_model_context(
            self.contextSettings,
            context["adm_path"],
            context.get("model_name") or active_model_name,
            active_signature,
            active_inventory,
            context.get("model_dir"),
        )
        return True

    def _activateImportedModelContext(self, imported):
        context = ModelImportRunner.build_model_context(
            imported["adm_path"],
            imported.get("resource_dir"),
        )
        self.currentAdmPath = context["adm_path"]
        self.currentModelDir = context["model_dir"]
        self.currentStructureParameterFile = context[
            "structure_parameter_file"
        ]
        ModelImportRunner.save_model_context(
            self.contextSettings,
            context["adm_path"],
            imported.get("model_name"),
            ModelImportRunner.scene_signature(
                SelectionMonitor.get_active_scene()
            ),
            ModelImportRunner.scene_inventory(
                SelectionMonitor.get_active_scene()
            ),
            context.get("model_dir"),
        )
        self._loadModelConfigurationData()

    def reloadInformationConfiguration(self, _checked=False, show_message=True):
        self._loadModelConfigurationData()
        self.refreshInformationMarkerTable()
        self.refreshMarkerList()
        self.refreshVariableTables()
        self.refreshPostprocessingConfiguration(clear_curve=True)
        if show_message:
            errors = self.informationConfiguration.get("errors", [])
            if errors:
                QMessageBox.warning(
                    self,
                    "信息配置表",
                    "配置表已读取，但存在以下问题：\n{}".format(
                        "\n".join(errors)
                    ),
                )
            else:
                QMessageBox.information(
                    self,
                    "信息配置表",
                    "已重新读取：\n{}".format(
                        self.informationConfiguration.get("file_path") or "未找到配置表"
                    ),
                )

    def refreshInformationMarkerTable(self):
        entries = self.informationConfiguration.get("markers", [])
        coincident_groups = []
        for parameter in self.markerLinkageDefinitions:
            for peer in parameter.get("coincident_with", []):
                coincident_groups.append((parameter["driver"], peer))
        self.infoMarkerTable.set_entries(entries, coincident_groups)
        errors = self.informationConfiguration.get("errors", [])
        warnings = self.informationConfiguration.get("warnings", [])
        scene = SelectionMonitor.get_active_scene()
        missing_markers = []
        if scene is not None:
            for entry in entries:
                path = StructuralParameterization.resolve_path(
                    scene, entry["target"]
                )
                try:
                    node = scene.getObject(path)
                except Exception:
                    node = None
                if node is None:
                    missing_markers.append(path)
        if errors:
            self.infoMarkerStatus.setText(
                "配置表存在 {} 个问题：{}".format(len(errors), errors[0])
            )
            self.infoMarkerStatus.setStyleSheet("color: #b00020;")
        elif missing_markers:
            self.infoMarkerStatus.setText(
                "配置表列出 {} 个Marker；当前模型找不到：{}".format(
                    len(entries), missing_markers[0]
                )
            )
            self.infoMarkerStatus.setStyleSheet("color: #b05a00;")
        elif warnings:
            self.infoMarkerStatus.setText(
                "配置表列出 {} 个Marker；配置警告：{}".format(
                    len(entries), warnings[0]
                )
            )
            self.infoMarkerStatus.setStyleSheet("color: #b05a00;")
        else:
            linkage_count = InformationConfiguration.count_marker_linkages(
                entries,
                self.markerLinkageDefinitions,
            )
            self.infoMarkerStatus.setText(
                "配置表列出 {} 个Marker，其中 {} 个配置了结构联动；"
                "输入为ADM世界坐标，写入时自动转换为所属零件局部坐标；"
                "后处理信息 {} 条，可在后处理页加载结果曲线。".format(
                    len(entries),
                    linkage_count,
                    len(self.informationConfiguration.get("postprocessing", [])),
                )
            )
            self.infoMarkerStatus.setStyleSheet("color: #666666;")
        self.infoMarkerApplyButton.setEnabled(bool(entries))
        self.configuredSplineButton.setEnabled(
            bool(self.informationConfiguration.get("splines", []))
        )

    def refreshPostprocessingConfiguration(self, clear_curve=False):
        entries = [
            entry
            for entry in self.informationConfiguration.get("postprocessing", [])
            if str(entry.get("target") or "").strip()
        ]
        had_items = self.postprocessingCurveList.count() > 0
        checked_ids = {
            self.postprocessingCurveList.item(index).data(Qt.UserRole)
            for index in range(self.postprocessingCurveList.count())
            if self.postprocessingCurveList.item(index).checkState() == Qt.Checked
        }
        self.postprocessingEntriesById = {
            entry.get("id") or entry["target"]: entry for entry in entries
        }
        self.postprocessingCurveList.blockSignals(True)
        self.postprocessingCurveList.clear()
        for index, (entry_id, entry) in enumerate(
            self.postprocessingEntriesById.items()
        ):
            y_unit = str(entry.get("y_unit") or "").strip()
            item_text = entry["label"]
            if y_unit:
                item_text += " [{}]".format(y_unit)
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, entry_id)
            item.setToolTip(entry["target"])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            should_check = entry_id in checked_ids or (
                not had_items and index == 0
            )
            item.setCheckState(Qt.Checked if should_check else Qt.Unchecked)
            self.postprocessingCurveList.addItem(item)
        self.postprocessingCurveList.blockSignals(False)

        diagrams = list(
            self.informationConfiguration.get("work_diagrams", [])
        )
        selected_diagram_id = self.postprocessingDiagramSelector.currentData()
        self.postprocessingDiagramSelector.blockSignals(True)
        self.postprocessingDiagramSelector.clear()
        for diagram in diagrams:
            self.postprocessingDiagramSelector.addItem(
                diagram["label"],
                diagram["id"],
            )
        if selected_diagram_id:
            selected_index = self.postprocessingDiagramSelector.findData(
                selected_diagram_id
            )
            if selected_index >= 0:
                self.postprocessingDiagramSelector.setCurrentIndex(
                    selected_index
                )
        self.postprocessingDiagramSelector.blockSignals(False)
        if not diagrams and self.postprocessingModeSelector.currentData() == "work_diagram":
            self.postprocessingModeSelector.setCurrentIndex(0)
        self.postprocessingDisplayModeChanged()

        enabled = bool(entries)
        self.postprocessingBrowseButton.setEnabled(enabled)
        self.postprocessingReloadButton.setEnabled(
            enabled and bool(self.postprocessingResultDirectory)
        )
        if clear_curve:
            self.postprocessingCurves = {}
            self.postprocessingWorkDiagrams = {}
            self.postprocessingLoadErrors = []
            self.postprocessingCurveWidget.clear_curve("请重新加载仿真结果")
        if not entries:
            self.postprocessingStatus.setText(
                "信息配置表中没有有效的后处理变量名"
            )
            self.postprocessingStatus.setStyleSheet("color: #b05a00;")
            self.postprocessingCurveWidget.clear_curve(
                "信息配置表中没有后处理变量"
            )
        elif self.postprocessingCurves:
            self.showSelectedPostprocessingCurves()
        else:
            if self.postprocessingResultDirectory:
                exists = os.path.isdir(self.postprocessingResultDirectory)
                self.postprocessingStatus.setText(
                    "信息配置表列出 {} 条后处理曲线、{} 张功量图；{}：{}".format(
                        len(entries),
                        len(diagrams),
                        "已自动定位结果目录" if exists else "默认结果目录尚未生成",
                        self.postprocessingResultDirectory,
                    )
                )
                self.postprocessingStatus.setStyleSheet(
                    "color: #666666;" if exists else "color: #b05a00;"
                )
            else:
                self.postprocessingStatus.setText(
                    "信息配置表列出 {} 条后处理曲线、{} 张功量图，请选择仿真结果目录。".format(
                        len(entries),
                        len(diagrams),
                    )
                )
                self.postprocessingStatus.setStyleSheet("color: #666666;")

    def selectPostprocessingResultDirectory(self):
        start_dir = self.postprocessingResultDirectory or self.currentModelDir
        selected = QFileDialog.getExistingDirectory(
            self,
            "选择仿真结果 object_data 目录或其上级目录",
            start_dir,
        )
        if not selected:
            return
        self.postprocessingResultDirectory = ResultData.normalize_result_directory(
            selected
        )
        self.postprocessingResultPath.setText(
            self.postprocessingResultDirectory
        )
        self.contextSettings.setValue(
            "postprocessing/result_directory",
            self.postprocessingResultDirectory,
        )
        self.postprocessingReloadButton.setEnabled(True)
        self.loadPostprocessingResults()

    def loadPostprocessingResults(self):
        entries = list(self.postprocessingEntriesById.values())
        if not entries:
            QMessageBox.warning(
                self,
                "后处理",
                "信息配置表中没有有效的后处理变量名",
            )
            return
        automatic_directory = ResultData.default_result_directory(__file__)
        if (
            automatic_directory
            and not os.path.isdir(self.postprocessingResultDirectory)
        ):
            self.defaultPostprocessingResultDirectory = automatic_directory
            self.postprocessingResultDirectory = automatic_directory
            self.postprocessingResultPath.setText(automatic_directory)
        if not self.postprocessingResultDirectory:
            self.selectPostprocessingResultDirectory()
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            loaded = ResultData.load_configured_results(
                self.postprocessingResultDirectory,
                entries,
            )
        except ResultData.ResultDataError as exc:
            self.postprocessingCurves = {}
            self.postprocessingWorkDiagrams = {}
            self.postprocessingLoadErrors = [str(exc)]
            self.postprocessingCurveWidget.clear_curve(str(exc))
            self.postprocessingStatus.setText(str(exc))
            self.postprocessingStatus.setStyleSheet("color: #b00020;")
            return
        except Exception as exc:
            message = "读取仿真结果时发生异常：{}: {}".format(
                type(exc).__name__, exc
            )
            self.postprocessingCurves = {}
            self.postprocessingWorkDiagrams = {}
            self.postprocessingLoadErrors = [message]
            self.postprocessingCurveWidget.clear_curve(message)
            self.postprocessingStatus.setText(message)
            self.postprocessingStatus.setStyleSheet("color: #b00020;")
            return
        finally:
            QApplication.restoreOverrideCursor()

        self.postprocessingResultDirectory = loaded["result_directory"]
        self.postprocessingResultPath.setText(
            self.postprocessingResultDirectory
        )
        self.postprocessingCurves = {
            curve["id"]: curve for curve in loaded["curves"]
        }
        work_result = ResultData.build_work_diagrams(
            loaded["curves"],
            self.informationConfiguration.get("work_diagrams", []),
        )
        self.postprocessingWorkDiagrams = {
            curve["id"]: curve for curve in work_result["curves"]
        }
        self.postprocessingLoadErrors = (
            list(loaded["errors"]) + list(work_result["errors"])
        )
        success_count = len(self.postprocessingCurves)
        diagram_count = len(self.postprocessingWorkDiagrams)
        error_count = len(self.postprocessingLoadErrors)
        if error_count:
            self.postprocessingStatus.setText(
                "已加载 {} 条曲线并生成 {} 张功量图，{} 项失败：{}".format(
                    success_count,
                    diagram_count,
                    error_count,
                    self.postprocessingLoadErrors[0],
                )
            )
            self.postprocessingStatus.setStyleSheet("color: #b05a00;")
        else:
            self.postprocessingStatus.setText(
                "已从 {} 加载 {} 条曲线，并生成 {} 张功量图。".format(
                    self.postprocessingResultDirectory,
                    success_count,
                    diagram_count,
                )
            )
            self.postprocessingStatus.setStyleSheet("color: #2e7d32;")
        self.showSelectedPostprocessingCurves()

    def postprocessingDisplayModeChanged(self, _index=-1):
        work_mode = (
            self.postprocessingModeSelector.currentData() == "work_diagram"
        )
        has_diagrams = self.postprocessingDiagramSelector.count() > 0
        self.postprocessingCurveList.setEnabled(not work_mode)
        self.postprocessingCurveListLabel.setEnabled(not work_mode)
        self.postprocessingDiagramSelector.setEnabled(
            work_mode and has_diagrams
        )
        self.showSelectedPostprocessingCurves()

    def showSelectedPostprocessingCurves(self, _item=None):
        if self.postprocessingModeSelector.currentData() == "work_diagram":
            diagram_id = self.postprocessingDiagramSelector.currentData()
            if not diagram_id:
                self.postprocessingCurveWidget.clear_curve(
                    "信息配置表中没有功量图配置"
                )
                return
            diagram = self.postprocessingWorkDiagrams.get(diagram_id)
            if diagram is None:
                self.postprocessingCurveWidget.clear_curve(
                    "请先加载仿真结果以生成功量图"
                )
                return
            self.postprocessingCurveWidget.set_curves([diagram])
            return
        selected_ids = []
        for index in range(self.postprocessingCurveList.count()):
            item = self.postprocessingCurveList.item(index)
            if item.checkState() == Qt.Checked:
                selected_ids.append(item.data(Qt.UserRole))
        if not selected_ids:
            self.postprocessingCurveWidget.clear_curve(
                "请在左侧勾选需要显示的曲线"
            )
            return
        curves = [
            self.postprocessingCurves[entry_id]
            for entry_id in selected_ids
            if entry_id in self.postprocessingCurves
        ]
        if not curves:
            self.postprocessingCurveWidget.clear_curve(
                "所选曲线尚未从仿真结果中加载"
            )
            return
        self.postprocessingCurveWidget.set_curves(curves)

    def applyConfiguredMarkers(self):
        entries = self.informationConfiguration.get("markers", [])
        coordinates = self.infoMarkerTable.coordinate_values(entries, self)
        if coordinates is None:
            return
        updated, errors = InformationConfiguration.apply_marker_values(
            SelectionMonitor.get_active_scene(),
            entries,
            coordinates,
            self.markerLinkageDefinitions,
        )
        self._show_apply_result(
            "结构参数设置",
            self.infoMarkerStatus,
            updated,
            errors,
        )
        if not errors:
            for entry in entries:
                entry["coordinates"] = tuple(coordinates[entry["id"]])
            self.refreshInformationMarkerTable()
            self.refreshMarkerList()

    def applyConfiguredSplines(self):
        configured = self.informationConfiguration.get("splines", [])
        if not configured:
            QMessageBox.warning(self, "配置样条曲线", "信息配置表中没有样条曲线信息")
            return
        answer = QMessageBox.question(
            self,
            "应用配置样条曲线",
            "将按照信息配置表覆盖 {} 条样条曲线，是否继续？".format(
                len(configured)
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer != QMessageBox.Yes:
            return
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            updated, errors = InformationConfiguration.apply_configured_splines(
                SelectionMonitor.get_active_scene(),
                self.informationConfiguration,
            )
        finally:
            QApplication.restoreOverrideCursor()
        if errors:
            QMessageBox.warning(
                self,
                "配置样条曲线",
                "未修改样条曲线：\n{}".format("\n".join(errors)),
            )
        else:
            QMessageBox.information(
                self,
                "配置样条曲线",
                "已按照配置表修改 {} 条样条曲线。".format(updated),
            )

    def refreshVariableTables(self):
        scene = SelectionMonitor.get_active_scene()
        variables = DynamicModelParameters.discover_model_variables(scene)
        ordinary_variables, self.dynamicTireVariables = (
            DynamicModelParameters.partition_variables(variables)
        )
        configured_groups = InformationConfiguration.simulation_parameter_groups(
            self.informationConfiguration
        )
        labels = dict(COMMON_VARIABLE_LABELS)
        labels.update(self.config.get("variable_labels", {}))
        self.parameterGroupsFromConfiguration = {
            key: bool(configured_groups.get(key))
            for key in InformationConfiguration.PARAMETER_SECTION_KEYS
        }
        self.simulationParametersFromConfiguration = any(
            self.parameterGroupsFromConfiguration.values()
        )
        if self.simulationParametersFromConfiguration:
            self.dynamicParameterGroups = {
                key: InformationConfiguration.resolve_simulation_parameters(
                    scene,
                    configured_groups.get(key, []),
                    variables,
                )
                for key in InformationConfiguration.PARAMETER_SECTION_KEYS
            }
        else:
            self.dynamicParameterGroups = {
                key: [] for key in InformationConfiguration.PARAMETER_SECTION_KEYS
            }
            self.dynamicParameterGroups["other_parameters"] = (
                InformationConfiguration.dynamic_simulation_parameters(
                    ordinary_variables,
                    labels,
                )
            )
        self.dynamicSimulationVariables = [
            item
            for key in InformationConfiguration.PARAMETER_SECTION_KEYS
            for item in self.dynamicParameterGroups.get(key, [])
        ]
        configured_node_ids = {
            id(item.get("node"))
            for item in self.dynamicSimulationVariables
            if item.get("node") is not None
        }
        self.dynamicTireVariables = [
            item for item in self.dynamicTireVariables
            if id(item.get("node")) not in configured_node_ids
        ]
        self.dynamicTirePartParameters = (
            TirePartParameters.discover_wheel_parameters(scene)
        )

        for group_key in InformationConfiguration.PARAMETER_SECTION_KEYS:
            table = self.parameterTables[group_key]
            parameters = self.dynamicParameterGroups.get(group_key, [])
            table.set_rows(
                InformationConfiguration.simulation_table_rows(parameters)
            )
            InformationConfiguration.populate_simulation_table(
                table,
                parameters,
            )

        tire_road_rows = DynamicModelParameters.table_rows(
            self.dynamicTireVariables, labels
        )
        tire_road_rows.extend(
            TirePartParameters.table_rows(self.dynamicTirePartParameters)
        )
        has_road = RoadPosition.is_available(scene)
        if has_road:
            tire_road_rows.extend(ROAD_LOCATION_ROWS)
        self.tireRoadVariableTable.set_rows(tire_road_rows)
        DynamicModelParameters.populate_table(
            self.tireRoadVariableTable, self.dynamicTireVariables
        )
        TirePartParameters.populate_table(
            self.tireRoadVariableTable, self.dynamicTirePartParameters
        )
        self.roadLocationEditors = tuple(
            self.tireRoadVariableTable.editor(row[1]) for row in ROAD_LOCATION_ROWS
        )
        if has_road:
            try:
                location = RoadPosition.get_location(scene)
                for editor, value in zip(self.roadLocationEditors, location):
                    editor.setText("{:.12g}".format(value))
            except Exception as exc:
                self.tireRoadStatus.setText("路面位置读取失败：{}".format(exc))

        for group_key in InformationConfiguration.PARAMETER_SECTION_KEYS:
            parameters = self.dynamicParameterGroups.get(group_key, [])
            status = self.parameterStatuses[group_key]
            group_label = PARAMETER_GROUP_LABELS[group_key]
            if scene is None:
                if self.parameterGroupsFromConfiguration.get(group_key):
                    status.setText(
                        "配置表列出 {} 个{}；当前没有活动模型".format(
                            len(parameters), group_label
                        )
                    )
                else:
                    status.setText("配置表中没有{}；当前没有活动模型".format(group_label))
                continue
            unresolved = [
                item for item in parameters if item.get("resolution_error")
            ]
            if self.parameterGroupsFromConfiguration.get(group_key):
                status.setText(
                    "配置表列出 {} 个{}，当前模型已匹配 {} 个、未匹配 {} 个".format(
                        len(parameters),
                        group_label,
                        len(parameters) - len(unresolved),
                        len(unresolved),
                    )
                )
            elif (
                not self.simulationParametersFromConfiguration
                and group_key == "other_parameters"
            ):
                status.setText(
                    "当前目录没有参数分组配置，已动态识别 {} 个状态变量".format(
                        len(parameters)
                    )
                )
            else:
                status.setText("配置表中没有{}".format(group_label))

        if scene is None:
            self.tireRoadStatus.setText("当前没有活动模型")
        else:
            self.tireRoadStatus.setText(
                "已读取 {} 个轮胎/路面变量、{} 个轮胎零件参数、{} 个路面位置参数".format(
                    len(self.dynamicTireVariables),
                    len(self.dynamicTirePartParameters),
                    3 if has_road else 0,
                )
            )

    def refreshMarkerList(self):
        scene = SelectionMonitor.get_active_scene()
        configured_entries = self.informationConfiguration.get("markers", [])
        self.markerItems = []
        missing_count = 0
        for entry in configured_entries:
            resolved_path, node = StructuralParameterization.resolve_object(
                scene,
                entry["target"],
            )
            if node is None:
                missing_count += 1
            self.markerItems.append(
                {
                    "name": entry["label"],
                    "display": entry["label"],
                    "path": resolved_path,
                    "node": node,
                    "configuration_entry": entry,
                }
            )
        selected_path = self.strSelFullName
        self.hpSelector.blockSignals(True)
        self.hpSelector.clear()
        self.hpSelector.addItem("请选择Marker")
        selected_index = 0
        for index, item in enumerate(self.markerItems, 1):
            self.hpSelector.addItem(item["display"])
            if item["path"] == selected_path:
                selected_index = index
        self.hpSelector.setCurrentIndex(selected_index)
        self.hpSelector.blockSignals(False)

        if scene is None:
            status = "当前没有活动模型"
        elif not configured_entries:
            status = "信息配置表中没有Marker配置"
        elif missing_count:
            status = "信息配置表列出 {} 个Marker，其中 {} 个在当前模型中未找到".format(
                len(configured_entries),
                missing_count,
            )
        else:
            status = "已读取信息配置表中的 {} 个Marker，请从下拉框选择".format(
                len(self.markerItems)
            )
        self.hpStatusLabel.setText(status)
        self.hpStatusLabel.setStyleSheet("color: #666666;")
        if selected_index:
            self.markerSelectorChanged(selected_index)
        else:
            self.strSelFullName = ""
            self.hpName.clear()
            self.xMarker.clear()
            self.yMarker.clear()
            self.zMarker.clear()
            for editor in (self.xMarker, self.yMarker, self.zMarker):
                editor.setEnabled(False)
            self.markOkButton.setEnabled(False)
        self.refreshStructureParameterList()

    def _selectedStructureParameter(self):
        index = self.structureParameterSelector.currentIndex()
        if index <= 0 or index > len(self.structureParameterItems):
            return None
        return self.structureParameterItems[index - 1]

    def refreshStructureParameterList(self):
        scene = SelectionMonitor.get_active_scene()
        current = self._selectedStructureParameter()
        current_id = current.get("id") if current else ""
        (
            self.structureParameterItems,
            unavailable,
        ) = StructuralParameterization.available_parameters(
            scene,
            self.structureParameterDefinitions,
        )

        self.structureParameterSelector.blockSignals(True)
        self.structureParameterSelector.clear()
        self.structureParameterSelector.addItem("按信息配置表联动")
        selected_index = 0
        for index, parameter in enumerate(self.structureParameterItems, 1):
            self.structureParameterSelector.addItem(parameter["label"])
            if parameter.get("id") == current_id:
                selected_index = index
        self.structureParameterSelector.setCurrentIndex(selected_index)
        self.structureParameterSelector.blockSignals(False)

        if self.structureParameterErrors:
            self.structureParameterInfo.setText(self.structureParameterErrors[0])
            self.structureParameterInfo.setStyleSheet("color: #b00020;")
        elif self.structureParameterDefinitions:
            self.structureParameterInfo.setText(
                "已加载 {} 个结构参数，当前模型可用 {} 个、不可用 {} 个。".format(
                    len(self.structureParameterDefinitions),
                    len(self.structureParameterItems),
                    len(unavailable),
                )
            )
            self.structureParameterInfo.setStyleSheet("color: #666666;")
        else:
            marker_count = len(self.informationConfiguration.get("markers", []))
            linkage_count = InformationConfiguration.count_marker_linkages(
                self.informationConfiguration.get("markers", []),
                self.markerLinkageDefinitions,
            )
            if marker_count:
                self.structureParameterInfo.setText(
                    "可调Marker与信息配置表一致，共 {} 个；其中 {} 个配置了结构联动。".format(
                        marker_count,
                        linkage_count,
                    )
                )
            else:
                self.structureParameterInfo.setText(
                    "信息配置表中没有Marker配置，当前没有可调Marker。"
                )
            self.structureParameterInfo.setStyleSheet("color: #666666;")
        self.structureParameterSelectorChanged(selected_index)

    def structureParameterSelectorChanged(self, index):
        parameter = self._selectedStructureParameter()
        if parameter is None:
            self.hpSelector.setEnabled(True)
            self.markOkButton.setText("应用结构参数")
            marker_index = self.hpSelector.currentIndex()
            if marker_index > 0:
                self.markerSelectorChanged(marker_index)
            return

        scene = SelectionMonitor.get_active_scene()
        target_path = StructuralParameterization.driver_path(scene, parameter)
        marker_index = 0
        for index, marker in enumerate(self.markerItems, 1):
            if marker["path"].lower() == target_path.lower():
                marker_index = index
                break
        if marker_index <= 0:
            self.hpSelector.setEnabled(False)
            self.markOkButton.setEnabled(False)
            self.structureParameterInfo.setText(
                "结构参数主控Marker未出现在可编辑列表：{}".format(target_path)
            )
            self.structureParameterInfo.setStyleSheet("color: #b00020;")
            return

        self.hpSelector.blockSignals(True)
        self.hpSelector.setCurrentIndex(marker_index)
        self.hpSelector.blockSignals(False)
        self.hpSelector.setEnabled(False)
        self.markerSelectorChanged(marker_index)
        self.markOkButton.setText("应用结构参数")
        description = parameter.get("description") or "按配置规则联动结构对象。"
        self.structureParameterInfo.setText(
            "{} 可修改方向：{}。".format(
                description,
                "、".join(axis.upper() for axis in parameter["axes"]),
            )
        )
        self.structureParameterInfo.setStyleSheet("color: #0b5c9e;")

    def markerSelectorChanged(self, index):
        if index <= 0 or index > len(self.markerItems):
            return
        self.tabs.setCurrentIndex(0)
        scene = SelectionMonitor.get_active_scene()
        marker = self.markerItems[index - 1]
        self.strSelFullName = marker["path"]
        try:
            node = scene.getObject(marker["path"]) if scene is not None else None
        except Exception:
            node = None
        if node is None:
            node = marker.get("node")
        available = node is not None

        if node is None:
            self.hpName.clear()
            self.xMarker.clear()
            self.yMarker.clear()
            self.zMarker.clear()
            status = "当前模型中未找到该Marker"
        else:
            self.hpName.setText(marker["path"])
            entry = marker.get("configuration_entry")
            if entry is not None:
                coordinates = entry["coordinates"]
            else:
                coordinates = (
                    node.location.x,
                    node.location.y,
                    node.location.z,
                )
            self.xMarker.setText("{:.12g}".format(coordinates[0]))
            self.yMarker.setText("{:.12g}".format(coordinates[1]))
            self.zMarker.setText("{:.12g}".format(coordinates[2]))
            status = "显示信息配置表中的世界坐标；提交后自动更新关联结构"

        parameter = self._selectedStructureParameter()
        editable_axes = set(parameter["axes"]) if parameter else set("xyz")
        self.xMarker.setEnabled(available and "x" in editable_axes)
        self.yMarker.setEnabled(available and "y" in editable_axes)
        self.zMarker.setEnabled(available and "z" in editable_axes)
        self.markOkButton.setEnabled(available)
        self.markOkButton.setText(
            "应用结构参数"
            if parameter or marker.get("configuration_entry") is not None
            else "设置Marker坐标"
        )
        if parameter and available:
            status = "已锁定非参数化方向；提交后按配置更新联动对象"
        self.hpStatusLabel.setText(status)
        self.hpStatusLabel.setStyleSheet(
            "color: #666666;" if available else "color: #b05a00;"
        )

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
        if self.strSelGeoFullName != node_name:
            self.strSelGeoFullName = node_name
            self.selGeo.setText(str(node_name).rsplit(".", 1)[-1])
            self.doubleLength.setText("{:.4f}".format(node.length))
            self.doubleRadius.setText("{:.4f}".format(node.radius))
            self.dimensionOkButton.setEnabled(True)

    def okMarkClickButton(self):
        texts = (self.xMarker.text(), self.yMarker.text(), self.zMarker.text())
        if not all(texts):
            QMessageBox.warning(self, "Marker调整", "Marker坐标输入为空")
            return
        scene = SelectionMonitor.get_active_scene()
        if scene is None:
            QMessageBox.warning(self, "Marker调整", "当前没有活动模型")
            return
        index = self.hpSelector.currentIndex()
        if index <= 0 or index > len(self.markerItems):
            QMessageBox.warning(self, "Marker调整", "请先选择一个Marker")
            return
        marker = self.markerItems[index - 1]
        coordinates = tuple(float(value) for value in texts)
        self.markOkButton.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            entry = marker.get("configuration_entry")
            if entry is not None:
                marker_batch, coordinate_values, synchronized_ids = (
                    InformationConfiguration.marker_coordinates_for_selection(
                        self.informationConfiguration.get("markers", []),
                        self.markerLinkageDefinitions,
                        entry["id"],
                        coordinates,
                    )
                )
                updated, errors = InformationConfiguration.apply_marker_values(
                    scene,
                    marker_batch,
                    coordinate_values,
                    self.markerLinkageDefinitions,
                )
                success = not errors
                if success:
                    for configured_entry in self.informationConfiguration.get(
                        "markers", []
                    ):
                        if configured_entry["id"] in coordinate_values:
                            configured_entry["coordinates"] = tuple(
                                coordinate_values[configured_entry["id"]]
                            )
                    message = "Marker结构参数调整完成，已更新 {} 个对象".format(
                        updated
                    )
                    if len(synchronized_ids) > 1:
                        message += "，并同步 {} 个重合Marker".format(
                            len(synchronized_ids)
                        )
                else:
                    message = "；".join(errors)
                    for error in errors:
                        print("[通用结构参数化错误] {}".format(error))
            else:
                parameter = self._selectedStructureParameter()
                if parameter is None:
                    success, message = ModelMarkerParameters.set_marker_location(
                        scene,
                        marker,
                        coordinates,
                    )
                else:
                    result = StructuralParameterization.apply_parameter(
                        scene,
                        parameter,
                        coordinates,
                    )
                    success, message = result.success, result.message
                    for error in result.errors:
                        print("[通用结构参数化错误] {}".format(error))
        except Exception as exc:
            success = False
            message = "Marker调整发生异常：{}: {}".format(
                type(exc).__name__,
                exc,
            )
        finally:
            QApplication.restoreOverrideCursor()

        if success and marker.get("configuration_entry") is not None:
            self.refreshInformationMarkerTable()
            self.refreshMarkerList()
        else:
            self.markerSelectorChanged(index)
        self.hpStatusLabel.setText(message)
        self.hpStatusLabel.setStyleSheet(
            "color: #0b7a2a;" if success else "color: #b00020;"
        )
        if not success:
            QMessageBox.warning(self, "Marker调整失败", message)
        else:
            QMessageBox.information(
                self,
                "Marker调整",
                "设置完成。\n{}".format(message),
            )

    def okDimClickButton(self):
        if not self.doubleRadius.text() or not self.doubleLength.text():
            QMessageBox.warning(self, "几何体调整", "圆柱体的半径或长度输入为空")
            return
        scene = SelectionMonitor.get_active_scene()
        node = SelectionMonitor.get_active_node(self.strSelGeoFullName)
        if scene is None or node is None:
            return
        if SelectionMonitor.get_node_type(node) == "Fmbs::ShapeCylinder":
            radius = float(self.doubleRadius.text())
            length = float(self.doubleLength.text())
            if radius <= 0.0 or length <= 0.0:
                QMessageBox.warning(
                    self, "几何体调整", "圆柱体的半径和长度必须大于0"
                )
                return
            old_radius = node.radius
            old_length = node.length
            try:
                node.radius = radius
                node.length = length
                scene.recompute()
            except Exception as exc:
                node.radius = old_radius
                node.length = old_length
                try:
                    scene.recompute()
                except Exception:
                    pass
                QMessageBox.warning(
                    self,
                    "几何体调整",
                    "圆柱体尺寸修改失败，已恢复原值：{}".format(exc),
                )
                return
            self.hpStatusLabel.setText(
                "圆柱尺寸已更新；下次设置结构参数时，cm将按当前长度重新居中"
            )
            self.hpStatusLabel.setStyleSheet("color: #0b7a2a;")
            QMessageBox.information(
                self,
                "几何体调整",
                "设置完成。\n圆柱体半径和长度已更新。",
            )

    def applyParameterGroup(self, group_key):
        table = self.parameterTables.get(group_key)
        status = self.parameterStatuses.get(group_key)
        parameters = self.dynamicParameterGroups.get(group_key, [])
        group_label = PARAMETER_GROUP_LABELS.get(group_key, "参数")
        if table is None or status is None:
            return
        if not table.validate_values(self):
            return
        updated, errors = InformationConfiguration.apply_simulation_table(
            SelectionMonitor.get_active_scene(),
            table,
            parameters,
        )
        self._show_apply_result(
            "{}设置".format(group_label), status, updated, errors
        )

    def okSimClickButton(self):
        """Compatibility entry point for callers of the retired single tab."""
        self.applyParameterGroup("other_parameters")

    def importVariableExcel(self, group_key="other_parameters"):
        scene = SelectionMonitor.get_active_scene()
        if scene is None:
            QMessageBox.warning(self, "Excel批量修改", "当前没有活动模型")
            return

        # Refresh before matching so the workbook is always checked against
        # the variables that are actually present in the current ADM model.
        self.refreshVariableTables()
        excel_state_variables = [
            item for item in self.dynamicParameterGroups.get(group_key, [])
            if item.get("value_property") == "function"
            and not item.get("resolution_error")
        ]
        if not excel_state_variables:
            QMessageBox.warning(
                self,
                "Excel批量修改",
                "当前{}列表中没有可批量修改的状态变量。".format(
                    PARAMETER_GROUP_LABELS.get(group_key, "参数")
                ),
            )
            return

        initial_dir = self.config.get("model_dir") or os.getcwd()
        file_path, _selected_filter = QFileDialog.getOpenFileName(
            self,
            "选择变量批量修改Excel",
            initial_dir,
            "Excel 工作簿 (*.xlsx)",
        )
        if not file_path:
            return

        try:
            sheet_name, workbook_updates = VariableExcelIO.read_variable_updates(
                file_path
            )
            matched_updates, match_errors = VariableExcelIO.match_variable_updates(
                excel_state_variables,
                workbook_updates,
            )
        except VariableExcelIO.VariableExcelError as exc:
            QMessageBox.warning(self, "Excel格式错误", str(exc))
            return

        if match_errors:
            QMessageBox.warning(
                self,
                "Excel变量校验失败",
                "未修改模型，请先修正以下问题：\n{}".format(
                    "\n".join(match_errors)
                ),
            )
            return

        answer = QMessageBox.question(
            self,
            "确认批量修改",
            "工作表“{}”中有 {} 个变量通过校验，是否写入当前模型？".format(
                sheet_name, len(matched_updates)
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )
        if answer != QMessageBox.Yes:
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            updated, errors = DynamicModelParameters.apply_function_updates(
                scene, matched_updates
            )
        finally:
            QApplication.restoreOverrideCursor()

        if errors:
            QMessageBox.warning(
                self,
                "Excel批量修改失败",
                "未完成批量修改：\n{}".format("\n".join(errors)),
            )
            return

        table = self.parameterTables[group_key]
        for item, function_text, _row_number in matched_updates:
            editor = table.editor(item.get("key", item["name"]))
            if editor is not None:
                editor.setText(str(function_text))
        self.parameterStatuses[group_key].setText(
            "已从 Excel 批量修改 {} 个状态变量".format(updated)
        )
        QMessageBox.information(
            self,
            "Excel批量修改",
            "已成功修改 {} 个状态变量。".format(updated),
        )

    def okTireRoadClickButton(self):
        if not self.tireRoadVariableTable.validate_values(self):
            return
        scene = SelectionMonitor.get_active_scene()
        updated, errors = DynamicModelParameters.apply_table_values(
            scene, self.tireRoadVariableTable, self.dynamicTireVariables
        )
        tire_updated, tire_errors = TirePartParameters.apply_table_values(
            scene,
            self.tireRoadVariableTable,
            self.dynamicTirePartParameters,
        )
        updated += tire_updated
        errors.extend(tire_errors)
        if all(editor is not None for editor in self.roadLocationEditors):
            try:
                RoadPosition.set_location(
                    scene,
                    tuple(float(editor.text()) for editor in self.roadLocationEditors),
                )
            except Exception as exc:
                errors.append("路面位置: {}".format(exc))
        self._show_apply_result(
            "轮胎与路面参数设置", self.tireRoadStatus, updated, errors
        )

    def _show_apply_result(self, title, status_label, updated, errors):
        if errors:
            QMessageBox.warning(
                self,
                title,
                "已修改 {} 个变量，以下项目失败：\n{}".format(
                    updated, "\n".join(errors)
                ),
            )
        else:
            status_label.setText("已修改 {} 个变量".format(updated))
            status_label.setStyleSheet("color: #0b7a2a;")
            QMessageBox.information(
                self,
                title,
                "设置完成，共修改 {} 个参数。".format(updated),
            )

    def modelImport(self):
        default_adm_path = str(
            self.config.get("default_adm_path") or ""
        ).strip()
        imported = ModelImportRunner.generate_imported_model_from_dialog(
            self,
            self.currentModelDir or self.config.get("model_dir"),
            adm_path=default_adm_path or None,
        )
        if imported:
            self._activateImportedModelContext(imported)
            self.refreshInformationMarkerTable()
            self.refreshMarkerList()
            self.refreshVariableTables()
            self.refreshPostprocessingConfiguration(clear_curve=True)

    def openFullModelGenerator(self):
        imported = FullModelGenerateDialog.show_full_model_generate_dialog(
            self.config.get("model_full_dir"),
            self,
        )
        if imported:
            self._activateImportedModelContext(imported)
            self.refreshInformationMarkerTable()
            self.refreshMarkerList()
            self.refreshVariableTables()
            self.refreshPostprocessingConfiguration(clear_curve=True)

    def openSplineImportDialog(self):
        SplineImportDialog.show_spline_import_dialog(self)

    def closeEvent(self, event):
        self.selectionMonitor.stop()
        super(DedicatedCaseDialog, self).closeEvent(event)

    def okClickButton(self):
        self.selectionMonitor.stop()
        self.accept()
