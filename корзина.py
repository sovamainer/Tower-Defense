import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class Tziv(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('С формами.ui', self)
        self.setWindowTitle('Корзина')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tziv()
    ex.show()
    sys.exit(app.exec())
