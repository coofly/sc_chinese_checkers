from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView

class NoScrollGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def wheelEvent(self, event):
        # 禁用滚轮事件
        event.ignore()

class MainWindow:
    def __init__(self):
        # 加载UI文件
        ui_file = QFile("app/ui/main.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(ui_file)
        ui_file.close()
        
        # 替换 graphicsView
        self.ui.graphicsView = NoScrollGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView.setGeometry(0, 0, 1000, 1000)
        
        # 信号槽绑定
        self.ui.pushButton_startGame.clicked.connect(self.start_game)
        
        # 绘制游戏背景
        self.draw_background()

    def draw_background(self):
        scene = QGraphicsScene()
        pixmap = QPixmap("app/ui/res/background.png")
        scaled_pixmap = pixmap.scaled(self.ui.graphicsView.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        item = QGraphicsPixmapItem(scaled_pixmap)
        item.setTransformationMode(Qt.SmoothTransformation)  # 启用抗锯齿
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)

    def start_game(self):
        print("游戏开始！")