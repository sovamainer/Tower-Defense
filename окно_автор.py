import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from товары import FirstForm


class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('форма1.ui', self)
        self.spis = []
        self.loaddata1()
        self.form2 = FirstForm()
        self.pushButton_2.clicked.connect(self.run)
        self.p = QLabel(self)
        self.p.move(120, 265)
        self.p.resize(150, 30)
        self.setWindowTitle('Авторизация')

    def loaddata1(self):
        self.con1 = sqlite3.connect('Chain_stores.db')
        self.cur1 = self.con1.cursor()
        self.query1 = "SELECT * FROM logs"
        for row in self.cur1.execute(self.query1):
            self.spis.append((str(row[0]), row[1], str(row[2])))

    def run(self):
        a = self.lineEdit.text(), self.lineEdit_2.text()
        for elem in self.spis:
            if a[0] == elem[1] and a[1] == elem[2]:
                self.form2.show()
                self.hide()
                break
            else:
                self.p.setText('Пользователь не обнаружен')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())
