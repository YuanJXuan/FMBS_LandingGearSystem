# -*- coding: utf-8 -*-
"""Small dependency-free Qt widget for overlaid simulation result curves."""

from __future__ import print_function

import math

from PySide2.QtCore import QPointF, QRectF, Qt
from PySide2.QtGui import QColor, QPainter, QPainterPath, QPen
from PySide2.QtWidgets import QWidget


def _number_text(value):
    return "{:.6g}".format(value)


def _screen_point(point, rect, bounds):
    left, top, width, height = rect
    x_min, x_max, y_min, y_max = bounds
    return (
        left + (point[0] - x_min) * width / (x_max - x_min),
        top + height - (point[1] - y_min) * height / (y_max - y_min),
    )


def _nearest_hover_sample(curves, rendered, position, rect, bounds, radius=10.0):
    """Hit-test visible lines, then snap to an original simulation sample.

    ``rendered`` contains (original index, screen x, screen y) per vertex.
    Only refine the hit segment's original samples; mouse movement need not
    project the entire result again. Sparse curves can be hit between samples.
    """
    mouse_x, mouse_y = position
    left, top, width, height = rect
    if not (left <= mouse_x <= left + width and top <= mouse_y <= top + height):
        return None
    best_distance = radius * radius
    hit = None
    for curve_index, vertices in enumerate(rendered):
        previous = None
        for vertex in vertices:
            start = previous if previous is not None else vertex
            dx, dy = vertex[1] - start[1], vertex[2] - start[2]
            length_squared = dx * dx + dy * dy
            fraction = 0.0
            if length_squared:
                fraction = max(0.0, min(1.0, (
                    (mouse_x - start[1]) * dx + (mouse_y - start[2]) * dy
                ) / length_squared))
            distance = (
                (mouse_x - start[1] - fraction * dx) ** 2
                + (mouse_y - start[2] - fraction * dy) ** 2
            )
            if distance < best_distance:
                best_distance = distance
                hit = (curve_index, start[0], vertex[0])
            previous = vertex
    if hit is None:
        return None
    curve_index, first_index, last_index = hit
    points = curves[curve_index]["points"]
    sample_index = min(
        range(first_index, last_index + 1),
        key=lambda index: sum(
            (pixel - mouse) ** 2
            for pixel, mouse in zip(_screen_point(points[index], rect, bounds), position)
        ),
    )
    return curve_index, sample_index


class ResultCurveWidget(QWidget):
    COLORS = (
        "#1565c0",
        "#d32f2f",
        "#2e7d32",
        "#7b1fa2",
        "#ef6c00",
        "#00838f",
        "#5d4037",
        "#455a64",
    )

    def __init__(self, parent=None):
        super(ResultCurveWidget, self).__init__(parent)
        self._curves = []
        self._message = "请加载仿真结果"
        self._bounds = None
        self._plot_cache = None
        self._hover_sample = None
        self._hover_position = None
        self.setMinimumHeight(360)
        self.setMouseTracking(True)

    def _clear_hover(self):
        self._hover_sample = None
        self._hover_position = None

    def clear_curve(self, message="请加载仿真结果"):
        self._curves = []
        self._bounds = None
        self._plot_cache = None
        self._clear_hover()
        self._message = str(message or "")
        self.update()

    def set_curve(self, x_values, y_values, title="", x_unit="", y_unit=""):
        self.set_curves(
            [
                {
                    "x": x_values,
                    "y": y_values,
                    "label": title,
                    "x_unit": x_unit,
                    "y_unit": y_unit,
                }
            ]
        )

    def set_curves(self, curves):
        prepared = []
        for curve in curves or []:
            points = []
            for x_value, y_value in zip(
                curve.get("x") or [],
                curve.get("y") or [],
            ):
                try:
                    x_number = float(x_value)
                    y_number = float(y_value)
                except (TypeError, ValueError):
                    continue
                if math.isfinite(x_number) and math.isfinite(y_number):
                    points.append((x_number, y_number))
            if not points:
                continue
            prepared.append(
                {
                    "label": str(curve.get("label") or curve.get("target") or "曲线"),
                    "title": str(curve.get("title") or curve.get("label") or ""),
                    "x_label": str(curve.get("x_label") or "时间"),
                    "y_label": str(curve.get("y_label") or "数值"),
                    "x_unit": str(curve.get("x_unit") or ""),
                    "y_unit": str(curve.get("y_unit") or ""),
                    "points": points,
                    "color": self.COLORS[len(prepared) % len(self.COLORS)],
                }
            )
        self._curves = prepared
        self._plot_cache = None
        self._clear_hover()
        self._bounds = None
        if prepared:
            x_min = min(point[0] for curve in prepared for point in curve["points"])
            x_max = max(point[0] for curve in prepared for point in curve["points"])
            y_min = min(point[1] for curve in prepared for point in curve["points"])
            y_max = max(point[1] for curve in prepared for point in curve["points"])
            if x_min == x_max:
                x_min -= 0.5
                x_max += 0.5
            if y_min == y_max:
                margin = max(abs(y_min) * 0.05, 0.5)
                y_min -= margin
                y_max += margin
            self._bounds = x_min, x_max, y_min, y_max
        self._message = "所选曲线中没有可显示的数值" if not prepared else ""
        self.update()

    def _plot_geometry(self):
        if self._plot_cache is None:
            legend_width = 0
            if len(self._curves) > 1:
                legend_width = min(220, max(140, int(self.width() * 0.24)))
            rect = (72, 44, max(20, self.width() - 96 - legend_width),
                    max(20, self.height() - 94))
            rendered = []
            max_points = max(200, int(rect[2] * 2))
            for curve in self._curves:
                points = curve["points"]
                step = max(1, int(math.ceil(len(points) / float(max_points))))
                indices = list(range(0, len(points), step))
                if indices[-1] != len(points) - 1:
                    indices.append(len(points) - 1)
                vertices = []
                for index in indices:
                    px, py = _screen_point(points[index], rect, self._bounds)
                    vertices.append((index, px, py))
                rendered.append(vertices)
            self._plot_cache = (rect, legend_width, rendered)
        return self._plot_cache

    def mouseMoveEvent(self, event):
        if not self._curves:
            return
        rect, _legend_width, rendered = self._plot_geometry()
        position = (event.pos().x(), event.pos().y())
        hit = _nearest_hover_sample(
            self._curves, rendered, position, rect, self._bounds
        )
        had_hover = self._hover_sample is not None
        self._hover_sample = hit
        self._hover_position = position if hit is not None else None
        if hit is not None or had_hover:
            self.update()

    def leaveEvent(self, event):
        self._clear_hover()
        self.update()
        super(ResultCurveWidget, self).leaveEvent(event)

    def resizeEvent(self, event):
        self._plot_cache = None
        self._clear_hover()
        super(ResultCurveWidget, self).resizeEvent(event)

    def _paint_hover(self, painter, rect):
        if self._hover_sample is None:
            return
        curve_index, sample_index = self._hover_sample
        curve = self._curves[curve_index]
        point = curve["points"][sample_index]
        px, py = _screen_point(point, rect, self._bounds)
        painter.save()
        painter.setClipRect(QRectF(*rect))
        painter.setPen(QPen(QColor(curve["color"]), 1, Qt.DashLine))
        painter.drawLine(QPointF(px, rect[1]), QPointF(px, rect[1] + rect[3]))
        painter.drawLine(QPointF(rect[0], py), QPointF(rect[0] + rect[2], py))
        painter.setPen(QPen(QColor(curve["color"]), 2))
        painter.setBrush(QColor("#ffffff"))
        painter.drawEllipse(QPointF(px, py), 4.5, 4.5)
        painter.restore()

        lines = [curve["label"] + "（采样点）"]
        for axis, value, unit in zip(
            (curve["x_label"], curve["y_label"]),
            point,
            (curve["x_unit"], curve["y_unit"]),
        ):
            lines.append("{} = {:.10g}{}".format(axis, value, " " + unit if unit else ""))
        metrics = painter.fontMetrics()
        line_height = metrics.height() + 4
        text_width = min(
            max(metrics.boundingRect(line).width() for line in lines),
            max(20, self.width() - 40),
        )
        box_width, box_height = text_width + 20, line_height * len(lines) + 14
        mouse_x, mouse_y = self._hover_position
        box_x, box_y = mouse_x + 16, mouse_y + 16
        if box_x + box_width > self.width() - 6:
            box_x = mouse_x - box_width - 16
        if box_y + box_height > self.height() - 6:
            box_y = mouse_y - box_height - 16
        box_x = max(6, min(box_x, self.width() - box_width - 6))
        box_y = max(6, min(box_y, self.height() - box_height - 6))
        painter.save()
        painter.setPen(QPen(QColor(curve["color"]), 1))
        painter.setBrush(QColor("#fffef6"))
        painter.drawRoundedRect(QRectF(box_x, box_y, box_width, box_height), 4, 4)
        painter.setPen(QColor("#202124"))
        for index, line in enumerate(lines):
            painter.drawText(
                QRectF(box_x + 10, box_y + 7 + index * line_height, text_width, line_height),
                Qt.AlignLeft | Qt.AlignVCenter,
                metrics.elidedText(line, Qt.ElideRight, int(text_width)),
            )
        painter.restore()

    def paintEvent(self, _event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillRect(self.rect(), QColor("#ffffff"))
        painter.setPen(QPen(QColor("#d5d9de"), 1))
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))

        if not self._curves:
            painter.setPen(QColor("#666666"))
            painter.drawText(self.rect(), Qt.AlignCenter, self._message)
            return

        title_height = 32
        rect, legend_width, rendered = self._plot_geometry()
        chart = QRectF(*rect)
        x_min, x_max, y_min, y_max = self._bounds

        painter.setPen(QColor("#202124"))
        title = (
            self._curves[0]["title"] or self._curves[0]["label"]
            if len(self._curves) == 1
            else "后处理曲线对比"
        )
        painter.drawText(
            QRectF(8, 4, self.width() - 16, title_height),
            Qt.AlignCenter,
            title,
        )

        for index in range(6):
            ratio = index / 5.0
            x_pixel = chart.left() + chart.width() * ratio
            y_pixel = chart.bottom() - chart.height() * ratio
            painter.setPen(QPen(QColor("#eceff1"), 1))
            painter.drawLine(QPointF(x_pixel, chart.top()), QPointF(x_pixel, chart.bottom()))
            painter.drawLine(QPointF(chart.left(), y_pixel), QPointF(chart.right(), y_pixel))
            painter.setPen(QColor("#5f6368"))
            x_label = _number_text(x_min + (x_max - x_min) * ratio)
            y_label = _number_text(y_min + (y_max - y_min) * ratio)
            painter.drawText(QRectF(x_pixel - 40, chart.bottom() + 4, 80, 20), Qt.AlignHCenter | Qt.AlignTop, x_label)
            painter.drawText(QRectF(2, y_pixel - 10, 64, 20), Qt.AlignRight | Qt.AlignVCenter, y_label)

        painter.setPen(QPen(QColor("#455a64"), 1))
        painter.drawRect(chart)
        x_units = {curve["x_unit"] for curve in self._curves if curve["x_unit"]}
        y_units = {curve["y_unit"] for curve in self._curves if curve["y_unit"]}
        x_labels = {curve["x_label"] for curve in self._curves if curve["x_label"]}
        y_labels = {curve["y_label"] for curve in self._curves if curve["y_label"]}
        x_unit = next(iter(x_units)) if len(x_units) == 1 else ""
        y_unit = next(iter(y_units)) if len(y_units) == 1 else ""
        x_label = next(iter(x_labels)) if len(x_labels) == 1 else "X"
        y_label = next(iter(y_labels)) if len(y_labels) == 1 else "数值"
        x_caption = x_label + (" ({})".format(x_unit) if x_unit else "")
        y_caption = y_label + (" ({})".format(y_unit) if y_unit else "")
        painter.drawText(QRectF(chart.left(), chart.bottom() + 25, chart.width(), 20), Qt.AlignCenter, x_caption)
        painter.drawText(QRectF(4, title_height, 64, 20), Qt.AlignLeft | Qt.AlignVCenter, y_caption)

        for curve, vertices in zip(self._curves, rendered):
            path = QPainterPath()
            for index, (_sample_index, x_pixel, y_pixel) in enumerate(vertices):
                if index == 0:
                    path.moveTo(x_pixel, y_pixel)
                else:
                    path.lineTo(x_pixel, y_pixel)
            painter.setPen(QPen(QColor(curve["color"]), 1.6))
            painter.drawPath(path)
            if len(vertices) == 1:
                painter.drawEllipse(QPointF(vertices[0][1], vertices[0][2]), 2.5, 2.5)

        if legend_width:
            legend_left = chart.right() + 18
            legend_top = chart.top() + 4
            for index, curve in enumerate(self._curves):
                row_top = legend_top + index * 24
                painter.setPen(QPen(QColor(curve["color"]), 2.2))
                painter.drawLine(
                    QPointF(legend_left, row_top + 8),
                    QPointF(legend_left + 24, row_top + 8),
                )
                label = curve["label"]
                if curve["y_unit"]:
                    label += " [{}]".format(curve["y_unit"])
                painter.setPen(QColor("#202124"))
                painter.drawText(
                    QRectF(legend_left + 30, row_top - 2, legend_width - 36, 22),
                    Qt.AlignLeft | Qt.AlignVCenter,
                    label,
                )
        self._paint_hover(painter, rect)
