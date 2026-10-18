# -*- coding: utf-8 -*-
"""Entry point for the model-independent ADM interface."""

import os
import sys
import traceback

script_dir = os.path.dirname(os.path.abspath(__file__))
share_dir = os.path.join(script_dir, "Share")


_CASE_MODULE_NAMES = (
    "CaseConfiguration",
    "CaseLauncher",
    "DedicatedCaseDialog",
    "DynamicModelParameters",
    "FullModelGenerateDialog",
    "FullModelGenerator",
    "InformationConfiguration",
    "MarkerConfigurationTable",
    "MarkerCoordinateSystem",
    "ModelImportRunner",
    "ModelMarkerParameters",
    "ModelPartDiscovery",
    "RoadPosition",
    "ResultCurveWidget",
    "ResultData",
    "ResponsiveTableColumns",
    "SelectionMonitor",
    "SplineDataIO",
    "SplineImportDialog",
    "StructuralParameterization",
    "TirePartParameters",
    "VariableExcelIO",
    "VariableInputTable",
)


def _load_case_launcher():
    """Load this template's modules without polluting Jasmine's module cache."""
    original_path = list(sys.path)
    previous_modules = {
        name: sys.modules[name]
        for name in _CASE_MODULE_NAMES
        if name in sys.modules
    }
    for name in _CASE_MODULE_NAMES:
        sys.modules.pop(name, None)
    sys.path.insert(0, share_dir)
    try:
        launcher = __import__("CaseLauncher", fromlist=["show_case_dialog"])
        return launcher.show_case_dialog
    finally:
        sys.path[:] = original_path
        for name in _CASE_MODULE_NAMES:
            sys.modules.pop(name, None)
        sys.modules.update(previous_modules)


try:
    show_case_dialog = _load_case_launcher()
except Exception:
    print("[通用界面启动失败]\n{}".format(traceback.format_exc()))
    raise


def show_template_dialog(
    model_folder=None,
    window_title="",
    execution_globals=None,
    parent=None,
):
    """Open the shared UI in generic or fixed-model mode."""
    return show_case_dialog(
        script_dir,
        model_folder=model_folder,
        window_title=window_title,
        execution_globals=execution_globals,
        parent=parent,
    )


if __name__ == "__main__":
    _general_dialog = show_template_dialog(
        execution_globals=globals(),
    )
