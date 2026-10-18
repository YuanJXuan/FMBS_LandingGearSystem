# -*- coding: utf-8 -*-
"""Reusable three-column variable editor used by template dialogs."""

import math

from PySide2.QtCore import Signal
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtWidgets import (
    QAbstractItemView,
    QLineEdit,
    QMessageBox,
    QTreeView,
)

import ResponsiveTableColumns


class VariableInputTable(QTreeView):
    """Display variable meaning, internal name and editable value in one table.

    ``rows`` contains ``(meaning, variable_name)`` or optional
    ``(meaning, variable_name, read_only, numeric_only, editor_key)`` tuples.
    ``editor_key`` lets a configuration table display the real model path
    while still assigning a unique editor to repeated or aliased rows.
    """

    applyRequested = Signal()

    def __init__(self, rows, parent=None):
        super(VariableInputTable, self).__init__(parent)

        self.variableModel = QStandardItemModel(self)
        self.variableModel.setHorizontalHeaderLabels(
            ["变量含义", "变量名称", "函数/取值"]
        )
        self.setModel(self.variableModel)
        self.setRootIsDecorated(False)
        self.setAlternatingRowColors(True)
        self.setUniformRowHeights(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self._editors = {}
        self._numeric_only = {}
        self.set_rows(rows)

        ResponsiveTableColumns.install(
            self,
            self.header(),
            (280, 420, 520),
            (180, 260, 240),
        )

    def set_rows(self, rows):
        """Replace the displayed rows while preserving the table widget."""
        for editor in self._editors.values():
            editor.deleteLater()
        self._editors = {}
        self._numeric_only = {}
        self.variableModel.removeRows(0, self.variableModel.rowCount())

        root = self.variableModel.invisibleRootItem()
        for row_number, row in enumerate(rows):
            meaning, variable_name = row[0], row[1]
            read_only = bool(row[2]) if len(row) > 2 else False
            numeric_only = bool(row[3]) if len(row) > 3 else True
            editor_key = row[4] if len(row) > 4 else variable_name

            meaning_item = QStandardItem(meaning)
            name_item = QStandardItem(variable_name)
            meaning_item.setEditable(False)
            name_item.setEditable(False)
            root.appendRow([meaning_item, name_item])

            editor = QLineEdit(self)
            editor.setText("0.0")
            editor.setReadOnly(read_only)
            if not read_only:
                editor.returnPressed.connect(self.applyRequested.emit)
            self.setIndexWidget(self.variableModel.index(row_number, 2), editor)
            self._editors[editor_key] = editor
            self._numeric_only[editor_key] = numeric_only

    def editor(self, variable_name):
        """Return the value editor associated with ``variable_name``."""
        return self._editors.get(variable_name)

    def editors(self):
        """Return a shallow copy of the variable-to-editor mapping."""
        return dict(self._editors)

    def validate_values(self, parent=None):
        """Validate all displayed values and report invalid rows to the user."""
        invalid_names = []
        first_invalid = None
        for variable_name, editor in self._editors.items():
            editor.setStyleSheet("")
            if editor.isReadOnly() or not self._numeric_only.get(variable_name, True):
                continue
            try:
                value = float(editor.text().strip())
                if not math.isfinite(value):
                    raise ValueError("value is not finite")
            except (TypeError, ValueError):
                invalid_names.append(variable_name)
                editor.setStyleSheet("border: 1px solid #d9534f;")
                if first_invalid is None:
                    first_invalid = editor

        if not invalid_names:
            return True

        if first_invalid is not None:
            first_invalid.setFocus()
        QMessageBox.warning(
            parent or self,
            "参数输入错误",
            "以下变量的取值不是有效数字：\n{}".format(
                "、".join(invalid_names)
            ),
        )
        return False
