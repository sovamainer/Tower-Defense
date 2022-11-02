import sqlite3
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QLabel
from корзина import Tziv


def choose_your_personaluty():
    global ex
    if ex == 'log':
        ex = Login()
        ex.show()
    if ex == 'form1':
        ex_w = FirstForm()
        ex_w.show()


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


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.form3 = Tziv()
        self.setWindowTitle('Товары')

    def init_ui(self):
        super().__init__()
        uic.loadUi('Проект.ui', self)
        self.loaddata()
        self.tableWidget_4.setColumnWidth(0, 250)
        self.tableWidget_4.setColumnWidth(3, 250)
        self.tableWidget_4.setColumnWidth(1, 250)
        self.tableWidget_4.setColumnWidth(2, 234)
        self.tableWidget_3.setColumnWidth(0, 250)
        self.tableWidget_3.setColumnWidth(3, 250)
        self.tableWidget_3.setColumnWidth(1, 250)
        self.tableWidget_3.setColumnWidth(2, 234)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(3, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 234)
        self.pushButton_p = QPushButton(self)
        self.pushButton_p.resize(120, 23)
        self.pushButton_p.move(850, 20)
        self.pushButton_p.setText('Выйти из аккаунта')
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_p.clicked.connect(self.quit)

    def loaddata(self):
        con = sqlite3.connect('Chain_stores.db')
        cur = con.cursor()
        query = "SELECT * FROM products"
        tablerow = 0
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(len(cur.execute(query).fetchall()))
        self.tableWidget_4.setHorizontalHeaderLabels(['ID', 'Товар', 'Цена', 'Оценка'])
        for row in cur.execute(query):
            self.tableWidget_4.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_4.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_4.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget_4.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1
        tablerow1 = 0
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(len(cur.execute(query).fetchall()))
        self.tableWidget_3.setHorizontalHeaderLabels(['ID', 'Товар', 'Цена', 'Оценка'])
        for row in cur.execute(query):
            self.tableWidget_3.setItem(tablerow1, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_3.setItem(tablerow1, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_3.setItem(tablerow1, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget_3.setItem(tablerow1, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow1 += 1
        tablerow2 = 0
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(cur.execute(query).fetchall()))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Товар', 'Цена', 'Оценка'])
        for row in cur.execute(query):
            self.tableWidget.setItem(tablerow2, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow2, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow2, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow2, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow2 += 1

    def run(self):
        self.form3.show()

    def quit(self):
        global ex
        ex = 'log'
        choose_your_personaluty()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = 'log'
    choose_your_personaluty()
    sys.exit(app.exec())
