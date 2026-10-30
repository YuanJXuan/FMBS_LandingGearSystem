# -*- coding: utf-8 -*-
"""Fixed-model entry point for the full landing-gear drop case."""

import os
import runpy


_script_dir = os.path.dirname(os.path.abspath(__file__))
_general_window_path = os.path.join(_script_dir, "GeneralWindow.py")
show_template_dialog = runpy.run_path(
    _general_window_path,
    run_name="_template_2_general_window",
)["show_template_dialog"]


_case_dialog = show_template_dialog("template_full_drop")
