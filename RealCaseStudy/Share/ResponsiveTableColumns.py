# -*- coding: utf-8 -*-
"""Keep editable table columns fitted while preserving manual resizing."""

from __future__ import print_function

from PySide2.QtCore import QEvent, QObject, QTimer
from PySide2.QtWidgets import QHeaderView


class ResponsiveTableColumns(QObject):
    """Scale columns with the table and couple manual separator drags."""

    def __init__(self, view, header, preferred_widths, minimum_widths=None):
        super(ResponsiveTableColumns, self).__init__(view)
        self.view = view
        self.header = header
        self.preferred_widths = [max(1, int(value)) for value in preferred_widths]
        if minimum_widths is None:
            minimum_widths = [60] * len(self.preferred_widths)
        self.minimum_widths = [max(1, int(value)) for value in minimum_widths]
        if len(self.minimum_widths) != len(self.preferred_widths):
            raise ValueError("列最小宽度数量必须与列数一致")
        self._updating = False
        self._last_viewport_width = 0

        self.header.setStretchLastSection(False)
        self.header.setMinimumSectionSize(min(self.minimum_widths))
        for column, width in enumerate(self.preferred_widths):
            self.header.setSectionResizeMode(column, QHeaderView.Interactive)
            self.view.setColumnWidth(column, width)

        self.header.sectionResized.connect(self._section_resized)
        self.view.viewport().installEventFilter(self)
        QTimer.singleShot(0, self.fit_to_viewport)

    def eventFilter(self, watched, event):
        if watched is self.view.viewport() and event.type() == QEvent.Resize:
            QTimer.singleShot(0, self.fit_to_viewport)
        return super(ResponsiveTableColumns, self).eventFilter(watched, event)

    def _column_widths(self):
        return [
            max(1, int(self.header.sectionSize(column)))
            for column in range(len(self.preferred_widths))
        ]

    @staticmethod
    def _scaled_widths(weights, minimums, target):
        minimum_total = sum(minimums)
        if target <= minimum_total:
            return list(minimums)

        weights = [max(1.0, float(value)) for value in weights]
        remaining = target - minimum_total
        weight_total = sum(weights)
        raw = [remaining * value / weight_total for value in weights]
        additions = [int(value) for value in raw]
        widths = [width + addition for width, addition in zip(minimums, additions)]
        leftover = target - sum(widths)
        order = sorted(
            range(len(raw)),
            key=lambda index: raw[index] - additions[index],
            reverse=True,
        )
        for index in order[:leftover]:
            widths[index] += 1
        return widths

    def _apply_widths(self, widths):
        self._updating = True
        try:
            for column, width in enumerate(widths):
                self.header.resizeSection(
                    column,
                    max(self.minimum_widths[column], int(width)),
                )
        finally:
            self._updating = False

    def fit_to_viewport(self):
        if self._updating:
            return
        viewport_width = max(0, int(self.view.viewport().width()) - 1)
        if viewport_width <= 0 or viewport_width == self._last_viewport_width:
            return
        current = self._column_widths()
        weights = current if sum(current) > 0 else self.preferred_widths
        target = max(viewport_width, sum(self.minimum_widths))
        self._apply_widths(
            self._scaled_widths(weights, self.minimum_widths, target)
        )
        self._last_viewport_width = viewport_width

    def _section_resized(self, logical_index, old_size, new_size):
        if self._updating or old_size == new_size:
            return
        count = len(self.preferred_widths)
        if logical_index < 0 or logical_index >= count:
            return

        viewport_width = max(0, int(self.view.viewport().width()) - 1)
        target = max(viewport_width, sum(self.minimum_widths))
        widths = self._column_widths()
        difference = target - sum(widths)
        if difference == 0:
            return

        if logical_index < count - 1:
            candidates = list(range(logical_index + 1, count))
        else:
            candidates = list(range(logical_index - 1, -1, -1))

        remaining = difference
        if remaining > 0:
            widths[candidates[0]] += remaining
            remaining = 0
        else:
            for column in candidates:
                capacity = widths[column] - self.minimum_widths[column]
                change = min(capacity, -remaining)
                widths[column] -= change
                remaining += change
                if remaining == 0:
                    break

        if remaining != 0:
            widths[logical_index] = max(
                self.minimum_widths[logical_index],
                widths[logical_index] + remaining,
            )
        self._apply_widths(widths)


def install(view, header, preferred_widths, minimum_widths=None):
    """Install and retain a responsive column controller on ``view``."""
    controller = ResponsiveTableColumns(
        view,
        header,
        preferred_widths,
        minimum_widths,
    )
    view._responsive_column_controller = controller
    return controller
