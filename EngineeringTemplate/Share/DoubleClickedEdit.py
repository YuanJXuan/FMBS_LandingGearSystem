from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import *

from PySide2.QtGui import  QMouseEvent

class DoubleClickedLineEdit(QLineEdit) :
    mySignal = Signal(int)
    nType = 0   #--------------用于区分是哪个控件发出来的
    def __init__(self, type, parent = None):
        super().__init__(parent)
        self.nType = type

    def mouseDoubleClickEvent(self, event : QMouseEvent):
        self.mySignal.emit(self.nType)
        return super().mouseDoubleClickEvent(event)
    pass