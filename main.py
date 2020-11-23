import sys

from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import choice

SIZE = [i for i in range(250)]
COLOR = [i for i in range(250)]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        size = choice(SIZE)
        rgb = (choice(COLOR), choice(COLOR), choice(COLOR))
        qp.setBrush(QColor(*rgb))
        qp.drawEllipse(250, 250, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
