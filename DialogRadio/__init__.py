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

    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton | e.buttons():
                self.setGeometry(self.pos().x() + (e.x() - self.dx), self.pos().y() + (e.y() - self.dy), self.width(), self.height())
        except Exception as e:
            print(e)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and (-3 < e.x() < 13 or -3 < e.y() < 13 or self.width() - 13 < e.x() < self.width() + 3 or self.height() - 13 < e.y() < self.height() + 3):
            self.dx = e.x()
            self.dy = e.y()
            self.setCursor(Qt.OpenHandCursor)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.setCursor(Qt.ArrowCursor)