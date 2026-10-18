# -*- coding: utf-8 -*-
"""工程模板的 ADM + 硬点 CMD + Python 补丁导入流程。"""

import importlib.util
import os
import re
import tempfile
import traceback

HPS_SOURCE_ALLOWED_COMMANDS = (
    "defaults units",
    "defaults attributes",
    "defaults model",
    "defaults coordinate_system",
    "model create",
    "model attributes",
    "model display",
    "view erase",
    "part attributes",
    "point create",
    "point attributes",
    "variable create",
)

HPS_OVERLAY_COMMANDS = (
    "defaults units",
    "point create",
    "point attributes",
    "variable create",
)


def _cmd_blocks(cmd_text):
    """按 Adams 的 ``!`` 分隔符拆分命令块。"""
    blocks = []
    block = []
    for raw_line in cmd_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("!"):
            if block:
                blocks.append(block)
                block = []
            continue
        block.append(raw_line.rstrip())
    if block:
        blocks.append(block)
    return blocks


def _validate_hps_source_file(cmd_path, expected_model_name):
    """Ensure the HPS source contains no physical model creation commands."""
    with open(cmd_path, "r", encoding="utf-8-sig", errors="ignore") as cmd_file:
        cmd_text = cmd_file.read()

    blocks = _cmd_blocks(cmd_text)
    commands = [
        " ".join(block[0].strip().rstrip("&").strip().lower().split())
        for block in blocks
    ]
    unsupported = sorted(
        set(command for command in commands if command not in HPS_SOURCE_ALLOWED_COMMANDS)
    )
    if unsupported:
        raise RuntimeError(
            "硬点 CMD 包含不允许的实体建模命令：{}".format(
                "、".join(unsupported)
            )
        )

    create_blocks = [
        "\n".join(block)
        for block, command in zip(blocks, commands)
        if command == "model create"
    ]
    if len(create_blocks) != 1:
        raise RuntimeError("硬点 CMD 必须且只能包含一条 model create")
    model_match = re.search(
        r"(?im)^\s*model_name\s*=\s*\.?([A-Za-z_][A-Za-z0-9_]*)",
        create_blocks[0],
    )
    actual_name = model_match.group(1) if model_match else ""
    if actual_name != expected_model_name:
        raise RuntimeError(
            "硬点 CMD 模型名不匹配：期望 {}，实际 {}".format(
                expected_model_name,
                actual_name or "<未识别>",
            )
        )

    expected_root = "." + expected_model_name
    foreign_roots = sorted(
        set(
            match.group(1)
            for match in re.finditer(
                r"(?<![A-Za-z0-9_])(\.[A-Za-z_][A-Za-z0-9_]*)\.",
                cmd_text,
            )
            if match.group(1).lower() != expected_root.lower()
        )
    )
    if foreign_roots:
        raise RuntimeError(
            "硬点 CMD 包含其他模型根路径：{}".format(
                "、".join(foreign_roots)
            )
        )


def build_hps_import_text(cmd_text, source_model_name, target_model_name):
    """Build a name-rewritten hardpoint/design-variable overlay for an ADM scene."""
    source_root = ".{}".format(source_model_name)
    target_root = ".{}".format(target_model_name)
    selected = []
    has_point = False
    for block in _cmd_blocks(cmd_text):
        command = " ".join(
            block[0].strip().rstrip("&").strip().lower().split()
        )
        if command not in HPS_OVERLAY_COMMANDS:
            continue
        if command == "point create":
            has_point = True
        selected.append("\n".join(block).replace(source_root, target_root))

    if not has_point:
        raise RuntimeError("硬点 CMD 中没有可导入的 Point")
    return "!\n" + "\n!\n".join(selected) + "\n!\n"


def _load_patch_module(patch_path, template_name):
    module_name = "{}_adm_patch".format(template_name)
    spec = importlib.util.spec_from_file_location(module_name, patch_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("无法加载模型补丁：{}".format(patch_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _validate_template_files(template_dir, template_name=None):
    template_dir = os.path.abspath(template_dir)
    template_name = template_name or os.path.basename(template_dir.rstrip("\\/"))
    paths = {
        "adm": os.path.join(template_dir, "{}.adm".format(template_name)),
        "hps": os.path.join(template_dir, "{}_hps.cmd".format(template_name)),
        "patch": os.path.join(template_dir, "{}_patch.py".format(template_name)),
    }
    missing = [path for path in paths.values() if not os.path.isfile(path)]
    if missing:
        raise RuntimeError("模型导入文件不完整：\n{}".format("\n".join(missing)))
    _validate_hps_source_file(paths["hps"], template_name)
    return paths


def _adm_part_probes(adm_path, limit=3):
    """Read a few named physical parts used to verify that ADM really merged."""
    with open(adm_path, "r", encoding="utf-8-sig", errors="ignore") as adm_file:
        adm_text = adm_file.read()
    names = re.findall(
        r"(?im)^!\s*adams_view_name='([^']+)'\s*\r?\nPART/\d+",
        adm_text,
    )
    unique_names = []
    for name in names:
        name = name.strip().lstrip(".")
        if (
            name
            and name.lower() != "ground"
            and not name.lower().startswith("_cv")
            and name not in unique_names
        ):
            unique_names.append(name)
        if len(unique_names) >= limit:
            break
    if not unique_names:
        raise RuntimeError("ADM 中没有可用于完整性校验的命名零件")
    return unique_names


def import_adm_cmd_model(template_dir, expected_model_name=None):
    """导入 ADM 唯一场景，再叠加硬点 CMD 和公式补丁。"""
    import Jusme
    from Fmbs.File.sceneio.scene_cmd_io import SceneCMDIO
    from Fmbs.File.sceneio.scene_adm_io import SceneADMIO

    expected_model_name = expected_model_name or os.path.basename(
        os.path.abspath(template_dir).rstrip("\\/")
    )
    paths = _validate_template_files(template_dir, expected_model_name)

    # SceneADMIO always creates a new scene in the current platform version;
    # it cannot import into a scene previously created by CMD.  Import it first
    # to avoid the duplicate ``template_x`` + ``Unknown1`` model pair.
    adm_io_tool = SceneADMIO()
    adm_io_tool.import_adm(paths["adm"])

    scene = Jusme.ActiveUSScene
    if scene is None:
        raise RuntimeError("ADM 导入完成后没有活动模型")
    scene_name = str(getattr(scene, "Name", "") or "").strip()
    if not scene_name:
        raise RuntimeError("ADM 导入后场景名为空")
    model_name = scene_name
    model_root = "." + model_name
    if scene.getObject(model_root + ".ground") is None:
        raise RuntimeError("ADM 导入后找不到模型 ground：{}".format(model_root))
    missing_adm_parts = [
        name
        for name in _adm_part_probes(paths["adm"])
        if scene.getObject(model_root + "." + name) is None
    ]
    if missing_adm_parts:
        raise RuntimeError(
            "ADM 主体未完整导入到模型 {}，缺少零件：{}".format(
                expected_model_name,
                "、".join(missing_adm_parts),
            )
        )

    with open(paths["hps"], "r", encoding="utf-8-sig", errors="ignore") as cmd_file:
        hps_text = build_hps_import_text(
            cmd_file.read(),
            expected_model_name,
            model_name,
        )

    temp_cmd_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix="_hps_import.cmd",
            encoding="utf-8",
            delete=False,
        ) as temp_cmd:
            temp_cmd.write(hps_text)
            temp_cmd_path = temp_cmd.name
        cmd_io_tool = SceneCMDIO()
        cmd_io_tool.import_cmd(cmd_fp=temp_cmd_path, ref_adm_fn="", py_fn="")
    finally:
        if temp_cmd_path and os.path.isfile(temp_cmd_path):
            try:
                os.remove(temp_cmd_path)
            except OSError:
                pass

    overlay_scene = Jusme.ActiveUSScene
    overlay_name = str(getattr(overlay_scene, "Name", "") or "").strip()
    if overlay_scene is None or overlay_name != model_name:
        raise RuntimeError("硬点 CMD 叠加时意外创建了新场景")

    patch_module = _load_patch_module(paths["patch"], expected_model_name)
    apply_patch = getattr(patch_module, "apply_patch", None)
    if not callable(apply_patch):
        raise RuntimeError("模型补丁缺少 apply_patch()：{}".format(paths["patch"]))

    patch_result = apply_patch(template_dir, model_name) or {}
    scene.recompute()
    return model_name, patch_result


def generate_imported_model_from_dialog(
    dialog,
    template_dir,
    expected_model_name=None,
):
    """工程模板页面共用的带确认、进度和消息提示的导入入口。"""
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QMessageBox

    import Jusme

    try:
        expected_model_name = expected_model_name or os.path.basename(
            os.path.abspath(template_dir).rstrip("\\/")
        )
        _validate_template_files(template_dir, expected_model_name)
    except Exception as exc:
        QMessageBox.critical(dialog, "模型导入失败", str(exc))
        return False

    answer = QMessageBox.question(
        dialog,
        "确认导入模型",
        "导入 ADM 模型将关闭当前模型，"
        "并清理同名的旧模型，是否继续？",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No,
    )
    if answer != QMessageBox.Yes:
        return False

    import_button = getattr(dialog, "modelImportButton", None)
    if import_button is not None:
        import_button.setEnabled(False)

    QApplication.setOverrideCursor(Qt.WaitCursor)
    QApplication.processEvents()

    try:
        active_scene = Jusme.ActiveUSScene
        active_name = ""
        if active_scene is not None:
            active_name = str(getattr(active_scene, "Name", "") or "")
            Jusme.closeUSScene(active_name)

        # Clean up a stale named shell left by the former CMD-first workflow.
        # This is scoped to the template currently being re-imported.
        if active_name != expected_model_name:
            try:
                old_template_scene = Jusme.getUSScene(expected_model_name)
            except Exception:
                old_template_scene = None
            if old_template_scene is not None:
                Jusme.closeUSScene(expected_model_name)

        model_name, patch_result = import_adm_cmd_model(
            template_dir,
            expected_model_name,
        )
    except Exception as exc:
        print(traceback.format_exc())
        QMessageBox.critical(
            dialog,
            "模型导入失败",
            "ADM/CMD 模型导入过程中发生错误：\n{}\n\n"
            "已保留当前导入状态，详细信息请查看软件控制台。".format(exc),
        )
        return False
    finally:
        QApplication.restoreOverrideCursor()
        if import_button is not None:
            import_button.setEnabled(True)

    warnings = patch_result.get("warnings", [])
    errors = patch_result.get("errors", [])
    updated = patch_result.get("updated", 0)
    if model_name == expected_model_name:
        model_description = "模型 {} 已导入".format(model_name)
    else:
        model_description = "模板 {} 已导入，ADM场景名为 {}".format(
            expected_model_name,
            model_name,
        )
    if warnings or errors:
        detail_lines = list(warnings)
        detail_lines.extend(
            "{step}: {error_type}: {error}".format(**error)
            for error in errors[:8]
        )
        if len(errors) > 8:
            detail_lines.append(
                "其余 {} 条补丁错误请查看软件控制台。".format(len(errors) - 8)
            )
        QMessageBox.warning(
            dialog,
            "模型导入完成",
            "{}，补丁更新 {} 项，记录错误 {} 条。\n{}".format(
                model_description,
                updated,
                len(errors),
                "\n".join(detail_lines),
            ),
        )
    else:
        QMessageBox.information(
            dialog,
            "模型导入",
            "{}，补丁更新 {} 项。".format(model_description, updated),
        )

    dialog.okClickButton()
    return True
