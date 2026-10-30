# -*- coding: utf-8 -*-
"""Safely monitor the host selection from the Qt main thread."""

from PySide2.QtCore import QObject, QTimer, Signal, Slot

import Jusme
import JusmeGui


def get_active_scene():
    """Return the active scene, or ``None`` while the host is switching scenes."""
    try:
        return Jusme.ActiveUSScene
    except Exception:
        return None


def get_active_node(node_name):
    """Resolve a node without leaking scene-switch errors into UI callbacks."""
    if not node_name:
        return None

    scene = get_active_scene()
    if scene is None:
        return None

    try:
        return scene.getObject(node_name)
    except Exception:
        return None


def get_node_type(node):
    """Return the host node type while tolerating stale proxy wrappers."""
    try:
        return node.Proxy.Type
    except Exception:
        return ""


class SelectionMonitor(QObject):
    """Poll ``JusmeGui.Selection`` with a main-thread ``QTimer``."""

    selectionChanged = Signal(str)

    def __init__(self, parent=None, interval_ms=500):
        super().__init__(parent)
        self._last_error = ""
        self._timer = QTimer(self)
        self._timer.setInterval(interval_ms)
        self._timer.timeout.connect(self._poll_selection)

    def start(self):
        if not self._timer.isActive():
            self._timer.start()
        self._poll_selection()

    def stop(self):
        self._timer.stop()

    def is_active(self):
        return self._timer.isActive()

    @Slot()
    def _poll_selection(self):
        node_name = ""
        try:
            selection = JusmeGui.Selection.getSelection()
            if selection is not None and len(selection) == 1:
                node_name = getattr(selection[0], "Name", "") or ""
            self._last_error = ""
        except Exception as exc:
            error_text = "{}: {}".format(type(exc).__name__, exc)
            if error_text != self._last_error:
                print("选择集监听暂时不可用：{}".format(error_text))
                self._last_error = error_text

        self.selectionChanged.emit(node_name)
