# -*- coding: utf-8 -*-
"""Editable Marker-coordinate table driven by the information workbook."""

import math

from PySide2.QtCore import Signal
from PySide2.QtGui import QDoubleValidator, QStandardItem, QStandardItemModel
from PySide2.QtWidgets import (
    QAbstractItemView,
    QLineEdit,
    QMessageBox,
    QTreeView,
)

import ResponsiveTableColumns


class MarkerConfigurationTable(QTreeView):
    applyRequested = Signal()

    def __init__(self, parent=None):
        super(MarkerConfigurationTable, self).__init__(parent)
        self.markerModel = QStandardItemModel(self)
        self.markerModel.setHorizontalHeaderLabels(
            ["结构参数", "Marker名称", "X（世界）", "Y（世界）", "Z（世界）"]
        )
        self.setModel(self.markerModel)
        self.setRootIsDecorated(False)
        self.setAlternatingRowColors(True)
        self.setUniformRowHeights(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._editors = {}

        ResponsiveTableColumns.install(
            self,
            self.header(),
            (240, 500, 130, 130, 130),
            (150, 260, 90, 90, 90),
        )

    @staticmethod
    def _path_aliases(path):
        normalized = str(path or "").strip().lower().lstrip(".")
        aliases = {normalized} if normalized else set()
        parts = normalized.split(".")
        if str(path or "").strip().startswith(".") and len(parts) > 2:
            aliases.add(".".join(parts[1:]))
        return aliases

    def _entry_for_path(self, entries, path):
        wanted = self._path_aliases(path)
        for entry in entries or []:
            if wanted.intersection(self._path_aliases(entry.get("target"))):
                return entry
        return None

    @staticmethod
    def _sync_editor_text(editors, text):
        for editor in editors:
            if editor.text() != text:
                editor.setText(text)

    def set_entries(self, entries, coincident_groups=None):
        for axis_editors in self._editors.values():
            for editor in axis_editors.values():
                editor.deleteLater()
        self._editors = {}
        self.markerModel.removeRows(0, self.markerModel.rowCount())

        root = self.markerModel.invisibleRootItem()
        for row_number, entry in enumerate(entries or []):
            label_item = QStandardItem(entry["label"])
            target_item = QStandardItem(entry["target"])
            label_item.setEditable(False)
            target_item.setEditable(False)
            root.appendRow([label_item, target_item])

            axis_editors = {}
            for column, axis, value in zip(
                (2, 3, 4),
                ("x", "y", "z"),
                entry["coordinates"],
            ):
                editor = QLineEdit(self)
                validator = QDoubleValidator(-1.0e12, 1.0e12, 12, editor)
                validator.setNotation(QDoubleValidator.StandardNotation)
                editor.setValidator(validator)
                editor.setText("{:.12g}".format(value))
                editor.returnPressed.connect(self.applyRequested.emit)
                self.setIndexWidget(
                    self.markerModel.index(row_number, column), editor
                )
                axis_editors[axis] = editor
            self._editors[entry["id"]] = axis_editors

        for group in coincident_groups or []:
            group_entries = []
            for path in group:
                entry = self._entry_for_path(entries, path)
                if entry is not None and entry not in group_entries:
                    group_entries.append(entry)
            if len(group_entries) < 2:
                continue
            for axis in ("x", "y", "z"):
                editors = [
                    self._editors[entry["id"]][axis]
                    for entry in group_entries
                    if entry["id"] in self._editors
                ]
                for editor in editors:
                    peers = [candidate for candidate in editors if candidate is not editor]
                    editor.textEdited.connect(
                        lambda text, linked_editors=peers: self._sync_editor_text(
                            linked_editors, text
                        )
                    )

    def coordinate_values(self, entries, parent=None):
        values = {}
        errors = []
        first_invalid = None
        for entry in entries or []:
            axis_editors = self._editors.get(entry["id"], {})
            coordinates = []
            for axis in ("x", "y", "z"):
                editor = axis_editors.get(axis)
                if editor is None:
                    errors.append("{} 缺少{}输入框".format(entry["label"], axis.upper()))
                    continue
                editor.setStyleSheet("")
                try:
                    value = float(editor.text().strip())
                    if not math.isfinite(value):
                        raise ValueError("not finite")
                    coordinates.append(value)
                except (TypeError, ValueError):
                    editor.setStyleSheet("border: 1px solid #d9534f;")
                    errors.append("{} 的{}坐标无效".format(entry["label"], axis.upper()))
                    if first_invalid is None:
                        first_invalid = editor
            if len(coordinates) == 3:
                values[entry["id"]] = tuple(coordinates)

        if errors:
            if first_invalid is not None:
                first_invalid.setFocus()
            QMessageBox.warning(
                parent or self,
                "结构参数输入错误",
                "\n".join(errors),
            )
            return None
        return values
