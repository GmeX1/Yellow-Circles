import sys
from ui_file import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Жёлтые круги')

        self.btn.clicked.connect(self.flag_switch)
        self.flag = False

    def flag_switch(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.generate(qp)
            qp.end()
        self.flag = False

    def generate(self, qp):
        for i in range(randint(1, 10)):
            size = randint(5, 100)
            pos_x = randint(0, self.width())
            pos_y = randint(0, self.height())
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(pos_x, pos_y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
