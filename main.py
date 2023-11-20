import sys
import random as rr
from PyQt5 import uic

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.a)
        self.flag = False
        self.qp = QPainter()

    def a(self):
        self.x = rr.randint(80, 400)
        self.y = rr.randint(80, 300)
        self.drawf()

    def draw(self):
        n = rr.randint(0, 80)
        x1 = self.x - (n // 2)
        y1 = self.y - (n // 2)
        self.qp.setBrush(QColor('yellow'))
        self.qp.drawEllipse(x1, y1, n, n)

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.draw()
            # Завершаем рисование
            self.qp.end()

    def drawf(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
