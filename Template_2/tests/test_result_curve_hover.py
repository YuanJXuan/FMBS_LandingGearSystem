# -*- coding: utf-8 -*-
"""Numerical hover/coordinate checks; these do not require a Qt installation."""

import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


def load_widget_module():
    # Isolate only the Qt import surface. Hit-testing and curve preparation
    # are exercised as production code, without pretending to render a GUI.
    modules = {name: types.ModuleType(name) for name in (
        "PySide2", "PySide2.QtCore", "PySide2.QtGui", "PySide2.QtWidgets"
    )}
    for name in ("QPointF", "QRectF", "Qt"):
        setattr(modules["PySide2.QtCore"], name, object)
    for name in ("QColor", "QPainter", "QPainterPath", "QPen"):
        setattr(modules["PySide2.QtGui"], name, object)

    class WidgetStub:
        def __init__(self, parent=None):
            self.size = (800, 400)

        def setMinimumHeight(self, height):
            pass

        def setMouseTracking(self, enabled):
            self.mouse_tracking = enabled

        def update(self):
            pass

        def width(self):
            return self.size[0]

        def height(self):
            return self.size[1]

        def resizeEvent(self, event):
            pass

        def leaveEvent(self, event):
            pass

    modules["PySide2.QtWidgets"].QWidget = WidgetStub
    path = Path(__file__).resolve().parents[1] / "Share" / "ResultCurveWidget.py"
    spec = importlib.util.spec_from_file_location("_hover_widget_under_test", str(path))
    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, modules):
        spec.loader.exec_module(module)
    return module


widget_module = load_widget_module()


class ResultCurveHoverTests(unittest.TestCase):
    def setUp(self):
        self.rect = (20, 30, 200, 100)
        self.bounds = (0, 10, 0, 10)

    def pick(self, series, position, indices=None):
        curves = [{"points": points} for points in series]
        rendered = []
        for points in series:
            rendered.append([
                (index,) + widget_module._screen_point(points[index], self.rect, self.bounds)
                for index in (indices if indices is not None else range(len(points)))
            ])
        return widget_module._nearest_hover_sample(
            curves, rendered, position, self.rect, self.bounds
        )

    def test_screen_coordinates_use_current_axes_and_inverted_y(self):
        self.assertEqual(widget_module._screen_point((0, 10), self.rect, self.bounds), (20, 30))
        self.assertEqual(widget_module._screen_point((10, 0), self.rect, self.bounds), (220, 130))

    def test_closest_of_two_curves_is_selected_in_screen_space(self):
        self.assertEqual(self.pick(
            [[(0, 2), (5, 2), (10, 2)], [(0, 8), (5, 8), (10, 8)]],
            (121, 53),
        ), (1, 1))

    def test_sparse_line_is_hittable_between_samples_and_returns_real_sample(self):
        self.assertEqual(self.pick([[(0, 5), (10, 5)]], (180, 80)), (0, 1))

    def test_drawn_segment_refines_to_original_unsampled_point(self):
        self.assertEqual(self.pick(
            [[(0, 5), (2, 5), (4, 5), (6, 5), (8, 5), (10, 5)]],
            (139, 81), indices=[0, 5],
        ), (0, 3))

    def test_empty_space_and_area_outside_plot_do_not_show_coordinates(self):
        self.assertIsNone(self.pick([[(0, 5), (10, 5)]], (120, 30)))
        self.assertIsNone(self.pick([[(0, 5), (10, 5)]], (15, 80)))
        self.assertIsNone(self.pick([], (120, 80)))

    def test_single_sample_and_duplicate_time_are_supported(self):
        self.assertEqual(self.pick([[(5, 5)]], (121, 81)), (0, 0))
        self.assertEqual(self.pick([[(5, 2), (5, 8)]], (121, 55)), (0, 1))

    def test_constant_curve_resizes_without_stale_geometry_or_hover(self):
        widget = widget_module.ResultCurveWidget()
        widget.set_curve([5], [10], "constant", "s", "N")
        self.assertTrue(widget.mouse_tracking)
        old_rect, _, old_vertices = widget._plot_geometry()
        self.assertEqual(widget_module._nearest_hover_sample(
            widget._curves, old_vertices, old_vertices[0][0][1:], old_rect, widget._bounds
        ), (0, 0))
        widget._hover_sample = (0, 0)
        widget.size = (1200, 600)
        widget.resizeEvent(None)
        new_rect, _, new_vertices = widget._plot_geometry()
        self.assertIsNone(widget._hover_sample)
        self.assertNotEqual(old_rect, new_rect)
        self.assertNotEqual(old_vertices, new_vertices)

    def test_work_diagram_keeps_custom_axis_labels_and_units(self):
        widget = widget_module.ResultCurveWidget()
        widget.set_curves(
            [
                {
                    "label": "缓冲器功量图",
                    "title": "缓冲器功量图",
                    "x_label": "缓冲器位移",
                    "y_label": "轮胎垂向载荷",
                    "x_unit": "mm",
                    "y_unit": "N",
                    "x": [0, 10],
                    "y": [0, 100],
                }
            ]
        )

        self.assertEqual(widget._curves[0]["x_label"], "缓冲器位移")
        self.assertEqual(widget._curves[0]["y_label"], "轮胎垂向载荷")
        self.assertEqual(widget._curves[0]["x_unit"], "mm")
        self.assertEqual(widget._curves[0]["y_unit"], "N")

    def test_reselect_reload_clear_and_mouse_leave_remove_old_hover(self):
        widget = widget_module.ResultCurveWidget()
        for action in (
            lambda: widget.set_curve([0, 1], [3, 4]),
            widget.clear_curve,
            lambda: widget.leaveEvent(None),
        ):
            widget._hover_sample = (0, 0)
            widget._hover_position = (10, 20)
            action()
            self.assertIsNone(widget._hover_sample)
            self.assertIsNone(widget._hover_position)


if __name__ == "__main__":
    unittest.main()
