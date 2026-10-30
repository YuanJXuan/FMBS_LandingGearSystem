# -*- coding: utf-8 -*-
"""Launcher for the model-independent ADM interface."""

from __future__ import print_function

import os

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon

from CaseConfiguration import build_fixed_model_config, build_generic_config
from DedicatedCaseDialog import DedicatedCaseDialog


class GeneralDialog(DedicatedCaseDialog):
    def __init__(
        self,
        script_dir,
        model_folder=None,
        window_title="",
        execution_globals=None,
        parent=None,
    ):
        if model_folder:
            config = build_fixed_model_config(
                script_dir,
                model_folder,
                window_title,
            )
        else:
            config = build_generic_config(script_dir)
        super(GeneralDialog, self).__init__(config, parent)


def show_case_dialog(
    script_dir,
    model_folder=None,
    window_title="",
    execution_globals=None,
    parent=None,
):
    dialog = GeneralDialog(
        script_dir,
        model_folder,
        window_title,
        execution_globals,
        parent,
    )
    dialog.setWindowTitle(
        dialog.config.get("window_title") or "通用界面"
    )
    dialog.setWindowIcon(
        QIcon(os.path.join(os.path.abspath(script_dir), "GeneralWindow.png"))
    )
    dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    dialog.show()
    return dialog
