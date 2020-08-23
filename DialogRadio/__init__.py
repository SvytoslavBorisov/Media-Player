import sys
from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel, QApplication, QMainWindow, QHeaderView, QFileDialog, QAbstractItemView, QWidget
from radioAdd import Ui_Dialog
from PyQt5.QtCore import Qt


class DialogRadio(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        try:
            self.setupUi(self)
            self.setWindowTitle("Введите радиостанцию")
            self.pbOk.clicked.connect(self.getData)
            self.pbCancel.clicked.connect(self.cancel)
            self.data = []
            self.dx = 0
            self.dy = 0
        except Exception as e:
            print(e)

    def getData(self):
        try:
            self.data = []
            self.data.append(self.leTitle.text())
            self.data.append(self.leUrl.text())
            self.close()
            self.dx = 0
            self.dy = 0
        except Exception as e:
            print(e)

    def cancel(self):
        self.data = []
        self.close()
