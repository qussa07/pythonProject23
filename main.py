import sys
import random as rr
from PyQt5 import uic

from ui import Ui_Form
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Suprematism(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.a)
        self.flag = False
        self.qp = QPainter()

    def a(self):
        self.x = rr.randint(80, 400)
        self.y = rr.randint(80, 300)
        self.drawf()

    def create_color(self):
        self.r = rr.randint(0, 255)
        self.g = rr.randint(0, 255)
        self.b = rr.randint(0, 255)

    def draw(self):
        n = rr.randint(0, 80)
        x1 = self.x - (n // 2)
        y1 = self.y - (n // 2)
        self.create_color()
        self.qp.setBrush(QColor(self.r, self.g, self.b))
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
