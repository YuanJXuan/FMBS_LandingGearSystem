from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap, QMouseEvent, QPainter


INTERACTIVE_IMAGE_WIDTH = 765
INTERACTIVE_IMAGE_HEIGHT = 560


def apply_standard_dialog(dialog, width=1400, height=720):
    """Apply layout sizing while preserving the host application's theme."""
    try:
        dialog.setMinimumSize(1250, 660)
        dialog.resize(width, height)
        root_layout = dialog.layout()
        if root_layout is not None:
            root_layout.setContentsMargins(18, 18, 18, 18)
            root_layout.setSpacing(18)
    except Exception as error:
        print("界面布局初始化失败，已使用宿主默认布局：{}".format(error))
        dialog.resize(width, height)


class mouseProcessView(QGraphicsView) :
    mySignal = Signal(str)
    def __init__(self, image_path, rect_list, hp_name_list,
                 display_width=None, display_height=None):
        scene = QGraphicsScene()
        super().__init__(scene)
        self.scene = scene

        source_pixmap = QPixmap(image_path)
        self.source_size = source_pixmap.size()
        width = display_width or self.source_size.width()
        height = display_height or self.source_size.height()
        self.display_width = int(width)
        self.display_height = int(height)
        self.pixmap = source_pixmap.scaled(
            self.display_width,
            self.display_height,
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation,
        )
        self.scene.addPixmap(self.pixmap)
        self.scene.setSceneRect(0, 0, self.display_width, self.display_height)
        
        #--------------设定鼠标移动跟踪行为，否则鼠标移动消息只有在左键按下的时候才会被接受
        self.setMouseTracking(True)

        self.rect_list = rect_list
        self.hp_name_list = hp_name_list
        

        self.setRenderHint(QPainter.Antialiasing)
        self.setWindowTitle("Image Display")
        self.setFixedSize(self.display_width, self.display_height)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) 
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.NoFrame)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        

        #------------------------定义鼠标在移动中处于矩形列表的索引
        self.index = -1

        #------------------------定义鼠标当前位置是否在某个举行区域内
        self.bInRect = False

   
    def mousePressEvent(self, event: QMouseEvent) :
        if event.button() == Qt.LeftButton:
            if self.index >= 0 :       #-----------------表示鼠标当前位置处于某个矩形区域
                #-------------发送自定义信号到主窗口的槽函数
                self.mySignal.emit(self.hp_name_list[self.index])
            else :
                self.mySignal.emit("")
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) :
        point = self.mapToScene(event.pos())
        source_width = max(1, self.source_size.width())
        source_height = max(1, self.source_size.height())
        source_point_x = point.x() * source_width / self.display_width
        source_point_y = point.y() * source_height / self.display_height
        self.bInRect = False
        inRect = 0
        for ele in self.rect_list :
            if ele.contains(int(source_point_x), int(source_point_y)) :
                self.bInRect = True
                self.index = inRect
                break
            inRect += 1

        if self.bInRect :
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        else :
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self.index = -1

        super().mouseMoveEvent(event) 
        
