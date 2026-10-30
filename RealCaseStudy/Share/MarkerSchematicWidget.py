# -*- coding: utf-8 -*-
"""PNG schematic view shared by the sidebar and the enlarged window."""

from PySide2.QtCore import QPointF, QRectF, QSize, Qt, Signal
from PySide2.QtGui import QColor, QFont, QPainter, QPen, QPixmap
from PySide2.QtWidgets import (
    QApplication, QDialog, QHBoxLayout, QLabel, QMenu, QPushButton,
    QSizePolicy, QToolTip, QVBoxLayout, QWidget,
)

import MarkerSchematic


class MarkerSchematicView(QWidget):
    markerRequested = Signal(str)

    def __init__(self, parent=None):
        super(MarkerSchematicView, self).__init__(parent)
        self.pixmap = QPixmap()
        self.markers = []
        self.selected = ""
        self.locked = False
        self.setMinimumSize(220, 180)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMouseTracking(True)

    def sizeHint(self):
        return QSize(360, 300)

    def image_rect(self):
        return MarkerSchematic.fit_rect(
            (self.pixmap.width(), self.pixmap.height()),
            (self.width(), self.height()),
        )

    def set_state(self, pixmap, markers, selected, locked):
        self.pixmap = pixmap
        self.markers = markers
        self.selected = selected
        self.locked = locked
        self.unsetCursor()
        QToolTip.hideText()
        self.update()

    def _selectable(self, marker):
        return marker["available"] and (not self.locked or marker["number"] == self.selected)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        if self.pixmap.isNull():
            return
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        rect = self.image_rect()
        painter.drawPixmap(QRectF(*rect), self.pixmap, QRectF(self.pixmap.rect()))
        scale = rect[2] / self.pixmap.width()
        # Keep badges proportional so close callouts do not collide in the sidebar.
        # The independent screen-space hit radius remains at least twelve pixels.
        badge_radius = max(5.0, 23 * scale)
        font = QFont(self.font())
        font.setPixelSize(max(6, int(21 * scale)))
        font.setBold(True)
        painter.setFont(font)
        for marker in self.markers:
            selected = marker["number"] == self.selected
            color = QColor("#929ba5" if not self._selectable(marker)
                           else "#b36a00" if selected else "#1a61cb")
            dot = QPointF(*MarkerSchematic.screen_position(marker["point_normalized"], rect))
            badge = QPointF(*MarkerSchematic.screen_position(marker["badge_normalized"], rect))
            painter.setPen(QPen(Qt.white, 2))
            painter.setBrush(color)
            radius = max(4.5, 8 * scale)
            painter.drawEllipse(dot, radius, radius)
            if selected:
                painter.setPen(QPen(color, 2))
                painter.setBrush(Qt.NoBrush)
                painter.drawEllipse(dot, radius + 4, radius + 4)
            painter.setPen(QPen(color, 2))
            painter.setBrush(QColor("#fff0d4") if selected else QColor("white"))
            painter.drawEllipse(badge, badge_radius, badge_radius)
            painter.drawText(
                QRectF(badge.x() - badge_radius, badge.y() - badge_radius,
                       2 * badge_radius, 2 * badge_radius),
                Qt.AlignCenter, marker["number"],
            )

    def _hits(self, event):
        rect = self.image_rect()
        # The enlarged view also makes the whole visible numbered badge clickable.
        radius = max(12, 25 * rect[2] / max(1, self.pixmap.width()))
        return MarkerSchematic.hit_candidates(
            (event.pos().x(), event.pos().y()), self.markers, rect, radius,
        )

    def mouseMoveEvent(self, event):
        hits = self._hits(event)
        if not hits:
            self.unsetCursor()
            QToolTip.hideText()
            return
        self.setCursor(Qt.PointingHandCursor if any(self._selectable(m) for m in hits)
                       else Qt.ArrowCursor)
        lines = []
        for marker in hits:
            reason = marker["reason"]
            if marker["available"] and not self._selectable(marker):
                reason = "当前调整方式已锁定主控Marker"
            lines.append("{} · {}\n{}{}".format(
                marker["number"], marker.get("label", ""), marker["target"],
                "\n" + reason if reason else "",
            ))
        QToolTip.showText(event.globalPos(), "\n\n".join(lines), self)

    def leaveEvent(self, event):
        self.unsetCursor()
        QToolTip.hideText()
        super(MarkerSchematicView, self).leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return super(MarkerSchematicView, self).mousePressEvent(event)
        # Compute from the press itself: a click must not depend on a previous hover.
        hits = self._hits(event)
        if len(hits) == 1:
            if self._selectable(hits[0]):
                self.markerRequested.emit(hits[0]["number"])
        elif hits:
            menu = QMenu(self)
            actions = {}
            for marker in hits:
                action = menu.addAction("{} · {}".format(marker["number"], marker["label"]))
                action.setEnabled(self._selectable(marker))
                actions[action] = marker["number"]
            action = menu.exec_(event.globalPos())
            if action in actions:
                self.markerRequested.emit(actions[action])
            menu.deleteLater()


class MarkerSchematicPanel(QWidget):
    markerRequested = Signal(str)

    def __init__(self, parent=None):
        super(MarkerSchematicPanel, self).__init__(parent)
        self.setMinimumWidth(240)
        self._large_dialog = None
        self._large_view = None
        self._large_status = None
        self._image_key = None
        self._model_title = "结构示意图"
        self._scope_note = ""
        self.pixmap = QPixmap()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        header = QHBoxLayout()
        self.titleLabel = QLabel(self._model_title, self)
        header.addWidget(self.titleLabel, 1)
        self.enlargeButton = QPushButton("放大查看", self)
        self.enlargeButton.setAutoDefault(False)
        self.enlargeButton.clicked.connect(self.open_enlarged)
        header.addWidget(self.enlargeButton)
        layout.addLayout(header)
        self.view = MarkerSchematicView(self)
        self.view.markerRequested.connect(self.markerRequested.emit)
        layout.addWidget(self.view, 1)
        self.status = QLabel("点击图中的点或编号选择Marker", self)
        self.status.setWordWrap(True)
        self.status.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        self.status.setStyleSheet("color: #666666;")
        layout.addWidget(self.status)

    def load(self, data):
        import os
        key = (data["image_path"], os.path.getmtime(data["image_path"]))
        if key != self._image_key:
            pixmap = QPixmap(data["image_path"])
            if pixmap.isNull() or [pixmap.width(), pixmap.height()] != data["image_size"]:
                raise ValueError("示意图无法读取或图片尺寸与点位配置不一致")
            self.pixmap = pixmap
            self._image_key = key
        self._model_title = data["title"]
        self._scope_note = data.get("scope_note", "")
        self.titleLabel.setText(self._model_title + "示意图")
        if self._large_dialog is not None:
            self._large_dialog.setWindowTitle(self._model_title + " · 示意图选点")

    def set_markers(self, markers, selected="", locked=False):
        self.view.set_state(self.pixmap, markers, selected, locked)
        active = next((m for m in markers if m["number"] == selected), None)
        text = "已选：{} · {}".format(active["number"], active["label"]) if active else "点击图中的点或编号选择Marker"
        if self._scope_note:
            text += "\n" + self._scope_note
        if locked:
            text += "\n当前调整方式已锁定主控Marker；切换为按信息配置表联动可自由选点。"
        elif active and not active["available"]:
            text += "\n" + active["reason"]
        self.status.setText(text)
        if self._large_view is not None:
            self._large_view.set_state(self.pixmap, markers, selected, locked)
            self._large_status.setText(text)

    def clear(self):
        self.close_enlarged()
        self._scope_note = ""
        self.pixmap = QPixmap()
        self._image_key = None
        self._model_title = "结构示意图"
        self.titleLabel.setText(self._model_title)
        self.set_markers([])

    def close_enlarged(self):
        if self._large_dialog is not None:
            self._large_dialog.close()

    def open_enlarged(self):
        if self.pixmap.isNull():
            return
        if self._large_dialog is None:
            dialog = QDialog(self)
            dialog.setFont(self.font())
            dialog.setWindowTitle(self._model_title + " · 示意图选点")
            dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
            layout = QVBoxLayout(dialog)
            self._large_view = MarkerSchematicView(dialog)
            self._large_view.markerRequested.connect(self.markerRequested.emit)
            layout.addWidget(self._large_view, 1)
            self._large_status = QLabel(dialog)
            self._large_status.setFont(self.status.font())
            self._large_status.setWordWrap(True)
            layout.addWidget(self._large_status)
            screen = QApplication.primaryScreen()
            if screen is not None:
                area = screen.availableGeometry()
                dialog.resize(min(1100, int(area.width() * 0.9)),
                              min(870, int(area.height() * 0.9)))
            else:
                dialog.resize(1000, 780)
            self._large_dialog = dialog
        self.set_markers(self.view.markers, self.view.selected, self.view.locked)
        self._large_dialog.show()
        self._large_dialog.raise_()
        self._large_dialog.activateWindow()
