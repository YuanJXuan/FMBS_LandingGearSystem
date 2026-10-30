# -*- coding: utf-8 -*-
"""Pure configuration for generic and fixed-model Template_2 launchers."""

from __future__ import print_function

import os


CASE_DEFINITIONS = {
    "template_nlg_drop": "前起落震",
    "template_nlg_retract": "前起收放",
    "template_nlg_turn": "前起转弯",
    "template_mlg_drop": "主起落震",
    "template_mlg_brake": "主起刹车",
    "template_full_drop": "全机落震",
    "template_full_brake": "全机刹车",
}


def build_generic_config(script_dir):
    """Build the unbound launcher configuration used by GeneralWindow."""
    script_dir = os.path.abspath(str(script_dir or ""))
    return {
        "model_dir": os.path.join(script_dir, "Model"),
        "model_full_dir": os.path.join(script_dir, "Model_Full"),
        "settings_key": "Template_2_GeneralWindow",
        "window_title": "通用界面",
    }


def build_fixed_model_config(script_dir, model_folder, window_title=""):
    """Build one shared-UI launcher bound to a registered ADM model."""
    script_dir = os.path.abspath(str(script_dir or ""))
    model_folder = str(model_folder or "").strip()
    if model_folder not in CASE_DEFINITIONS:
        raise ValueError("未注册的专用模型：{}".format(model_folder))

    model_root = os.path.abspath(os.path.join(script_dir, "Model"))
    model_dir = os.path.abspath(os.path.join(model_root, model_folder))
    if not os.path.isdir(model_dir):
        raise ValueError("找不到专用界面的模型目录：{}".format(model_dir))

    preferred_adm = os.path.join(model_dir, model_folder + ".adm")
    if os.path.isfile(preferred_adm):
        default_adm_path = preferred_adm
    else:
        adm_files = sorted(
            os.path.join(model_dir, name)
            for name in os.listdir(model_dir)
            if name.lower().endswith(".adm")
            and os.path.isfile(os.path.join(model_dir, name))
        )
        if len(adm_files) != 1:
            raise ValueError(
                "模型目录必须包含同名ADM或唯一的ADM文件：{}".format(model_dir)
            )
        default_adm_path = adm_files[0]

    return {
        "model_dir": model_dir,
        "model_full_dir": os.path.join(script_dir, "Model_Full"),
        "default_adm_path": default_adm_path,
        "settings_key": "Template_2_{}".format(model_folder),
        "window_title": str(
            window_title or CASE_DEFINITIONS[model_folder]
        ),
        "model_folder": model_folder,
    }
