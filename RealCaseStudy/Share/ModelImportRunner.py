# -*- coding: utf-8 -*-
"""User-selected ADM model import for the generic dedicated-case interface."""

from __future__ import print_function

import hashlib
import json
import os
import traceback


CONTEXT_ADM_PATH_KEY = "model_context/adm_path"
CONTEXT_MODEL_NAME_KEY = "model_context/model_name"
CONTEXT_SCENE_SIGNATURE_KEY = "model_context/scene_signature"
CONTEXT_SCENE_INVENTORY_KEY = "model_context/scene_inventory"
CONTEXT_RESOURCE_DIR_KEY = "model_context/resource_dir"


def _normalized_model_name(model_name):
    return str(model_name or "").strip().lstrip(".").lower()


def scene_inventory(scene):
    """Return model-tree identities without reading mutable property values."""
    if scene is None:
        return []
    objects = getattr(scene, "Objects", None)
    try:
        objects = list(objects or [])
    except Exception:
        objects = []
    if not objects:
        getter = getattr(scene, "getObjects", None)
        if callable(getter):
            try:
                objects = list(getter() or [])
            except Exception:
                objects = []

    entries = []
    for node in objects:
        name = str(getattr(node, "Name", "") or "").strip()
        if not name:
            continue
        try:
            node_type = str(getattr(node.Proxy, "Type", "") or "").strip()
        except Exception:
            node_type = str(getattr(node, "TypeId", "") or "").strip()
        entries.append("{}\t{}".format(name, node_type))
    return sorted(set(entries))


def scene_signature(scene):
    """Build a compact fingerprint from the current model-tree inventory."""
    entries = scene_inventory(scene)
    if not entries:
        return ""
    payload = "\n".join(entries).encode("utf-8", "replace")
    return hashlib.sha256(payload).hexdigest()


def _inventories_match(saved_inventory, active_inventory, threshold=0.8):
    """Allow runtime nodes while rejecting a genuinely different model tree."""
    saved = set(saved_inventory or [])
    active = set(active_inventory or [])
    if not saved or not active:
        return True
    overlap = len(saved.intersection(active)) / float(min(len(saved), len(active)))
    return overlap >= threshold


def clear_saved_model_context(settings):
    """Remove a stale ADM context from a QSettings-compatible store."""
    try:
        settings.remove(CONTEXT_ADM_PATH_KEY)
        settings.remove(CONTEXT_MODEL_NAME_KEY)
        settings.remove(CONTEXT_SCENE_SIGNATURE_KEY)
        settings.remove(CONTEXT_SCENE_INVENTORY_KEY)
        settings.remove(CONTEXT_RESOURCE_DIR_KEY)
        settings.sync()
    except Exception:
        return False
    return True


def save_model_context(
    settings,
    adm_path,
    model_name,
    signature="",
    inventory=None,
    resource_dir="",
):
    """Persist the last successfully imported ADM and its Jasmine scene name."""
    try:
        adm_path = _validate_adm_file(adm_path)
        model_name = str(model_name or "").strip().lstrip(".")
        if not model_name:
            return False
        settings.setValue(CONTEXT_ADM_PATH_KEY, adm_path)
        settings.setValue(CONTEXT_MODEL_NAME_KEY, model_name)
        settings.setValue(CONTEXT_SCENE_SIGNATURE_KEY, str(signature or ""))
        settings.setValue(
            CONTEXT_SCENE_INVENTORY_KEY,
            json.dumps(list(inventory or []), ensure_ascii=False),
        )
        settings.setValue(
            CONTEXT_RESOURCE_DIR_KEY,
            os.path.abspath(str(resource_dir or os.path.dirname(adm_path))),
        )
        settings.sync()
    except Exception:
        return False
    return True


def restore_model_context(
    settings,
    active_model_name,
    active_signature="",
    active_inventory=None,
):
    """Restore a saved context only when it belongs to the active scene."""
    active_key = _normalized_model_name(active_model_name)
    if not active_key:
        return None
    try:
        adm_path = str(settings.value(CONTEXT_ADM_PATH_KEY, "") or "").strip()
        saved_model_name = str(
            settings.value(CONTEXT_MODEL_NAME_KEY, "") or ""
        ).strip()
        saved_signature = str(
            settings.value(CONTEXT_SCENE_SIGNATURE_KEY, "") or ""
        ).strip()
        raw_inventory = str(
            settings.value(CONTEXT_SCENE_INVENTORY_KEY, "") or ""
        ).strip()
        resource_dir = str(
            settings.value(CONTEXT_RESOURCE_DIR_KEY, "") or ""
        ).strip()
        saved_inventory = json.loads(raw_inventory) if raw_inventory else []
        if not isinstance(saved_inventory, list):
            saved_inventory = []
    except Exception:
        return None
    if not adm_path or _normalized_model_name(saved_model_name) != active_key:
        return None
    active_signature = str(active_signature or "").strip()
    if saved_inventory and active_inventory:
        if not _inventories_match(saved_inventory, active_inventory):
            return None
    # Exact signatures from older versions are intentionally not a hard gate.
    # Jasmine may add result/runtime nodes to an otherwise unchanged scene.
    # The inventory comparison above handles new contexts and a legacy context
    # is migrated by the dialog immediately after a successful restore.
    try:
        context = build_model_context(adm_path, resource_dir or None)
    except Exception:
        clear_saved_model_context(settings)
        return None
    context["model_name"] = saved_model_name
    return context


def find_structure_parameter_file(model_dir, adm_path=""):
    """Find an optional structure-parameter JSON beside an ADM model."""
    model_dir = os.path.abspath(str(model_dir or ""))
    adm_stem = os.path.splitext(os.path.basename(str(adm_path or "")))[0]
    file_names = []
    if adm_stem:
        file_names.extend(
            (
                adm_stem + "_structure_parameters.json",
                adm_stem + ".structure_parameters.json",
            )
        )
    file_names.append("structure_parameters.json")
    for folder in (model_dir, os.path.join(model_dir, "信息配置")):
        for file_name in file_names:
            candidate = os.path.join(folder, file_name)
            if os.path.isfile(candidate):
                return candidate
    # Generated ADM files may intentionally have a different stem while still
    # using the single structure definition shipped with their source package.
    fallback_files = []
    for folder in (model_dir, os.path.join(model_dir, "信息配置")):
        try:
            fallback_files.extend(
                os.path.join(folder, file_name)
                for file_name in os.listdir(folder)
                if file_name.lower().endswith("_structure_parameters.json")
                and os.path.isfile(os.path.join(folder, file_name))
            )
        except OSError:
            continue
    fallback_files = sorted(set(fallback_files))
    if len(fallback_files) == 1:
        return fallback_files[0]
    return ""


def build_model_context(adm_path, resource_dir=None):
    """Resolve every UI-side resource from the selected ADM directory."""
    adm_path = _validate_adm_file(adm_path)
    model_dir = os.path.abspath(str(resource_dir or os.path.dirname(adm_path)))
    if not os.path.isdir(model_dir):
        model_dir = os.path.dirname(adm_path)
    structure_file = find_structure_parameter_file(model_dir, adm_path)
    return {
        "adm_path": adm_path,
        "model_dir": model_dir,
        "structure_parameter_file": structure_file,
        "tire_files": _files_with_extensions(model_dir, (".tir",)),
        "road_files": _files_with_extensions(model_dir, (".rdf",)),
    }


def _files_with_extensions(model_dir, extensions):
    """List model-package resources without looking outside the ADM folder."""
    try:
        file_names = os.listdir(model_dir)
    except OSError:
        return []
    extensions = tuple(extension.lower() for extension in extensions)
    return sorted(
        os.path.join(model_dir, file_name)
        for file_name in file_names
        if os.path.isfile(os.path.join(model_dir, file_name))
        and os.path.splitext(file_name)[1].lower() in extensions
    )


def _validate_adm_file(adm_path):
    """Return a normalized ADM path or raise a user-facing error."""
    adm_path = os.path.abspath(str(adm_path or "").strip())
    if not adm_path or not os.path.isfile(adm_path):
        raise RuntimeError("未找到ADM模型文件：{}".format(adm_path or "<未选择>"))
    if os.path.splitext(adm_path)[1].lower() != ".adm":
        raise RuntimeError("请选择扩展名为 .adm 的模型文件")
    return adm_path


def import_adm_model(adm_path):
    """Import an arbitrary ADM file and return the active Jasmine scene name."""
    import Jusme
    from Fmbs.File.sceneio.scene_adm_io import SceneADMIO

    adm_path = _validate_adm_file(adm_path)
    adm_io_tool = SceneADMIO()
    adm_io_tool.import_adm(adm_path)

    scene = Jusme.ActiveUSScene
    if scene is None:
        raise RuntimeError("ADM导入完成后没有活动模型")
    model_name = str(getattr(scene, "Name", "") or "").strip()
    if not model_name:
        raise RuntimeError("ADM导入后场景名为空")

    model_root = "." + model_name.lstrip(".")
    try:
        ground = scene.getObject(model_root + ".ground")
    except Exception:
        ground = None
    if ground is None:
        raise RuntimeError("ADM导入后找不到模型ground：{}".format(model_root))

    recompute = getattr(scene, "recompute", None)
    if callable(recompute):
        recompute()
    return model_name


def generate_imported_model_from_dialog(dialog, initial_dir=None, adm_path=None):
    """Let the user choose any ADM file, then import it into Jasmine."""
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QFileDialog, QMessageBox

    import Jusme

    if not adm_path:
        selected_path, _selected_filter = QFileDialog.getOpenFileName(
            dialog,
            "选择ADM模型",
            os.path.abspath(initial_dir) if initial_dir else "",
            "Adams模型 (*.adm);;所有文件 (*)",
        )
        if not selected_path:
            return None
        adm_path = selected_path

    try:
        adm_path = _validate_adm_file(adm_path)
    except Exception as exc:
        QMessageBox.critical(dialog, "模型导入失败", str(exc))
        return None

    answer = QMessageBox.question(
        dialog,
        "确认导入模型",
        "将导入ADM文件：\n{}\n\n并关闭当前模型，是否继续？".format(
            adm_path
        ),
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No,
    )
    if answer != QMessageBox.Yes:
        return None

    import_button = getattr(dialog, "modelImportButton", None)
    if import_button is not None:
        import_button.setEnabled(False)

    QApplication.setOverrideCursor(Qt.WaitCursor)
    QApplication.processEvents()
    try:
        active_scene = Jusme.ActiveUSScene
        if active_scene is not None:
            active_name = str(getattr(active_scene, "Name", "") or "").strip()
            if active_name:
                Jusme.closeUSScene(active_name)
        model_name = import_adm_model(adm_path)
    except Exception as exc:
        print(traceback.format_exc())
        QMessageBox.critical(
            dialog,
            "模型导入失败",
            "ADM模型导入过程中发生错误：\n{}\n\n"
            "已保留当前导入状态，详细信息请查看软件控制台。".format(exc),
        )
        return None
    finally:
        QApplication.restoreOverrideCursor()
        if import_button is not None:
            import_button.setEnabled(True)

    QMessageBox.information(
        dialog,
        "模型导入",
        "ADM文件 {} 已导入，当前场景名为 {}。".format(
            os.path.basename(adm_path),
            model_name,
        ),
    )
    context = build_model_context(adm_path)
    context["model_name"] = model_name
    return context
