# -*- coding: utf-8 -*-
"""模型脚本的公共执行入口。

模型生成脚本按顶层语句逐条执行。某条语句发生运行时错误时，记录错误并
继续执行后续语句，以便尽量保持与软件控制台逐段执行时一致的行为。
"""

import ast
import os
import traceback


def execute_model_script(model_script, execution_globals):
    """逐条执行模型脚本，返回顶层语句数量和执行错误列表。"""
    with open(model_script, "r", encoding="utf-8-sig") as script_file:
        source_code = script_file.read()

    script_tree = ast.parse(source_code, filename=model_script)
    execute_errors = []

    # 使用调用页面的全局环境，尽量贴近软件控制台的执行方式。
    sentinel = object()
    old_name = execution_globals.get("__name__", sentinel)
    old_file = execution_globals.get("__file__", sentinel)
    execution_globals["__name__"] = "__main__"
    execution_globals["__file__"] = model_script

    try:
        for statement in script_tree.body:
            statement_module = ast.Module(body=[statement], type_ignores=[])
            ast.fix_missing_locations(statement_module)

            try:
                statement_code = compile(statement_module, model_script, "exec")
                exec(statement_code, execution_globals, execution_globals)
            except Exception as exc:
                line_number = getattr(statement, "lineno", 0)
                end_line_number = getattr(statement, "end_lineno", line_number)
                error_info = {
                    "line": line_number,
                    "end_line": end_line_number,
                    "statement": type(statement).__name__,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
                execute_errors.append(error_info)

                print(
                    "[模型脚本错误] 第{}-{}行 {}: {}: {}".format(
                        line_number,
                        end_line_number,
                        error_info["statement"],
                        error_info["error_type"],
                        error_info["error"],
                    )
                )
                print(traceback.format_exc())
    finally:
        if old_name is sentinel:
            execution_globals.pop("__name__", None)
        else:
            execution_globals["__name__"] = old_name

        if old_file is sentinel:
            execution_globals.pop("__file__", None)
        else:
            execution_globals["__file__"] = old_file

    return len(script_tree.body), execute_errors


def generate_model_from_dialog(
    dialog,
    model_script,
    scene_name,
    execution_globals,
):
    """执行页面共用的模型生成流程，成功后关闭参数对话框。"""
    # 延迟导入平台和界面模块，使 execute_model_script 可以独立测试。
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QMessageBox

    import Common
    import Jusme

    if not os.path.isfile(model_script):
        QMessageBox.critical(
            dialog,
            "模型生成失败",
            "找不到模型脚本：\n{}".format(model_script),
        )
        return False

    answer = QMessageBox.question(
        dialog,
        "确认生成模型",
        "生成模型将关闭当前模型，是否继续？",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No,
    )
    if answer != QMessageBox.Yes:
        return False

    generate_button = getattr(dialog, "modelGenerateButton", None)
    if generate_button is not None:
        generate_button.setEnabled(False)

    QApplication.setOverrideCursor(Qt.WaitCursor)
    QApplication.processEvents()

    generate_success = False
    statement_count = 0
    execute_errors = []

    try:
        model_name = Common.getModelName()
        if model_name:
            Jusme.closeUSScene(model_name)
        Jusme.newUSScene(scene_name)

        statement_count, execute_errors = execute_model_script(
            model_script,
            execution_globals,
        )

        active_scene = Jusme.ActiveUSScene
        if active_scene:
            try:
                active_scene.recompute()
            except Exception as exc:
                execute_errors.append(
                    {
                        "line": 0,
                        "end_line": 0,
                        "statement": "recompute",
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                    }
                )
                print("[模型刷新错误] {}: {}".format(type(exc).__name__, exc))
                print(traceback.format_exc())

        generate_success = True
        print(
            "模型脚本执行完成：{}，顶层语句{}条，错误{}条".format(
                model_script,
                statement_count,
                len(execute_errors),
            )
        )
    except Exception as exc:
        print(traceback.format_exc())
        QMessageBox.critical(
            dialog,
            "模型生成失败",
            "执行模型脚本时发生错误：\n{}".format(exc),
        )
    finally:
        QApplication.restoreOverrideCursor()
        if generate_button is not None:
            generate_button.setEnabled(True)

    if not generate_success:
        return False

    if execute_errors:
        QMessageBox.warning(
            dialog,
            "模型生成完成",
            "模型脚本已执行完成。\n"
            "共执行{}条顶层语句，其中{}条报错；后续语句已继续执行。\n"
            "详细错误请查看软件控制台。".format(
                statement_count,
                len(execute_errors),
            ),
        )
    else:
        QMessageBox.information(dialog, "模型生成", "模型生成完成。")

    dialog.okClickButton()
    return True
