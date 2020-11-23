import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import choice

SIZE = [i for i in range(250)]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(250, 250, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
