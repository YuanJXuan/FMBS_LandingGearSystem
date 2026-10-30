# -*- coding: utf-8 -*-

import ast
import os
import sys
import unittest
from pathlib import Path
from unittest import mock


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
SHARE_DIR = TEMPLATE_DIR / "Share"
sys.path.insert(0, str(SHARE_DIR))

import CaseConfiguration


EXPECTED_CASES = {
    "template_nlg_drop": "前起落震",
    "template_nlg_retract": "前起收放",
    "template_nlg_turn": "前起转弯",
    "template_mlg_drop": "主起落震",
    "template_mlg_brake": "主起刹车",
    "template_full_drop": "全机落震",
    "template_full_brake": "全机刹车",
}


class FixedCaseLauncherTests(unittest.TestCase):
    def test_all_fixed_cases_resolve_their_packaged_adm(self):
        self.assertEqual(EXPECTED_CASES, CaseConfiguration.CASE_DEFINITIONS)
        settings_keys = set()
        for case_name, title in EXPECTED_CASES.items():
            config = CaseConfiguration.build_fixed_model_config(
                str(TEMPLATE_DIR), case_name
            )
            self.assertEqual(title, config["window_title"])
            self.assertEqual(case_name, config["model_folder"])
            self.assertEqual(
                TEMPLATE_DIR / "Model" / case_name / (case_name + ".adm"),
                Path(config["default_adm_path"]),
            )
            settings_keys.add(config["settings_key"])
        self.assertEqual(len(EXPECTED_CASES), len(settings_keys))

    def test_generic_configuration_remains_unbound(self):
        config = CaseConfiguration.build_generic_config(str(TEMPLATE_DIR))
        self.assertNotIn("default_adm_path", config)
        self.assertEqual("通用界面", config["window_title"])
        self.assertEqual(
            TEMPLATE_DIR / "Model",
            Path(config["model_dir"]),
        )

    def test_toolbar_entry_script_and_icon_exist_for_every_case(self):
        toolbar_entries = {}
        for line in (TEMPLATE_DIR / "toolbarconfig.txt").read_text(
            encoding="utf-8-sig"
        ).splitlines():
            if "," in line:
                key, label = line.split(",", 1)
                toolbar_entries[key.strip()] = label.strip()

        for case_name, title in EXPECTED_CASES.items():
            self.assertEqual(title, toolbar_entries.get(case_name))
            entry_path = TEMPLATE_DIR / (case_name + ".py")
            icon_path = TEMPLATE_DIR / (case_name + ".png")
            self.assertTrue(entry_path.is_file())
            self.assertTrue(icon_path.is_file())

            tree = ast.parse(entry_path.read_text(encoding="utf-8-sig"))
            calls = [
                node
                for node in ast.walk(tree)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "show_template_dialog"
            ]
            self.assertEqual(1, len(calls))
            self.assertEqual(case_name, ast.literal_eval(calls[0].args[0]))

    def test_model_import_uses_optional_fixed_adm_path(self):
        source = (SHARE_DIR / "DedicatedCaseDialog.py").read_text(
            encoding="utf-8-sig"
        )
        self.assertIn('self.config.get("default_adm_path")', source)
        self.assertIn("adm_path=default_adm_path or None", source)

    def test_fixed_launchers_load_general_window_by_absolute_path(self):
        for case_name in EXPECTED_CASES:
            entry_path = TEMPLATE_DIR / (case_name + ".py")
            source = entry_path.read_text(encoding="utf-8-sig")
            opened_cases = []

            def fake_show_template_dialog(model_folder):
                opened_cases.append(model_folder)
                return object()

            with mock.patch(
                "runpy.run_path",
                return_value={"show_template_dialog": fake_show_template_dialog},
            ) as run_path:
                namespace = {
                    "__file__": str(entry_path),
                    "__name__": "_toolbar_entry_test",
                }
                exec(compile(source, str(entry_path), "exec"), namespace)

            loaded_path = os.path.normcase(
                os.path.abspath(run_path.call_args.args[0])
            )
            expected_path = os.path.normcase(
                os.path.abspath(str(TEMPLATE_DIR / "GeneralWindow.py"))
            )
            self.assertEqual(loaded_path, expected_path)
            self.assertEqual(
                run_path.call_args.kwargs.get("run_name"),
                "_template_2_general_window",
            )
            self.assertEqual(opened_cases, [case_name])
            self.assertNotIn("from GeneralWindow import", source)


if __name__ == "__main__":
    unittest.main()
