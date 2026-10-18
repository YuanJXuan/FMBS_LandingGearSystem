# -*- coding: utf-8 -*-
"""Regression checks for the generic launcher on a shared Python process."""

import ast
import unittest
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
ENTRYPOINT = TEMPLATE_DIR / "GeneralWindow.py"
SHARE_DIR = TEMPLATE_DIR / "Share"


def _assigned_literal(tree, name):
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return ast.literal_eval(node.value)
    raise AssertionError("未找到入口配置：{}".format(name))


def _local_dependencies(module_name, local_modules):
    tree = ast.parse((SHARE_DIR / (module_name + ".py")).read_text(encoding="utf-8-sig"))
    dependencies = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            dependencies.update(
                alias.name.split(".", 1)[0]
                for alias in node.names
                if alias.name.split(".", 1)[0] in local_modules
            )
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            root_name = node.module.split(".", 1)[0]
            if root_name in local_modules:
                dependencies.add(root_name)
    return dependencies


class CaseEntrypointIsolationTests(unittest.TestCase):
    def test_every_reachable_share_module_is_isolated(self):
        source = ENTRYPOINT.read_text(encoding="utf-8-sig")
        tree = ast.parse(source)
        isolated_modules = set(_assigned_literal(tree, "_CASE_MODULE_NAMES"))
        local_modules = {path.stem for path in SHARE_DIR.glob("*.py")}

        reachable = set()
        pending = ["CaseLauncher"]
        while pending:
            module_name = pending.pop()
            if module_name in reachable:
                continue
            reachable.add(module_name)
            pending.extend(
                _local_dependencies(module_name, local_modules) - reachable
            )

        self.assertEqual(set(), reachable - isolated_modules)
        self.assertNotIn("sys.path.append", source)
        self.assertNotIn('"case_1"', source)
        self.assertIn("execution_globals=globals()", source)

    def test_removed_legacy_dependency_chain_is_not_reintroduced(self):
        for module_name in ("Common", "TireParameter", "ModelScriptRunner"):
            self.assertFalse((SHARE_DIR / (module_name + ".py")).exists())


if __name__ == "__main__":
    unittest.main()
