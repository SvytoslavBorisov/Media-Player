# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 631)
        MainWindow.setStyleSheet("background-color: gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.hsMusic = QtWidgets.QSlider(self.centralwidget)
        self.hsMusic.setStyleSheet("QSlider {\n"
"border: 0px;\n"
"background: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"/*border-radius: 4px;*/\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,  stop: 0 #66e, stop: 1 #FC0B0B);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #FC0B0B, stop: 1 #F5ED14);\n"
"border: 1px solid #777;\n"
"height: 14px;\n"
"/*border-radius: 4px;*/\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: black;\n"
"/*background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,  stop: 0 #000, stop: 1 #FC0B0B);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #892919, stop: 1 #000);*/\n"
"border: 1px solid #777;\n"
"height: 14px;\n"
"/*border-radius: 4px;*/\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"/*background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"*/\n"
"background: none;\n"
"width: 12px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.hsMusic.setOrientation(QtCore.Qt.Horizontal)
        self.hsMusic.setObjectName("hsMusic")
        self.verticalLayout.addWidget(self.hsMusic)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbStop = QtWidgets.QPushButton(self.centralwidget)
        self.pbStop.setMinimumSize(QtCore.QSize(50, 50))
        self.pbStop.setMaximumSize(QtCore.QSize(50, 50))
        self.pbStop.setStyleSheet("\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/stop.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/stop.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/stop-orange.png);\n"
"}")
        self.pbStop.setText("")
        self.pbStop.setObjectName("pbStop")
        self.horizontalLayout.addWidget(self.pbStop)
        self.pbPlay = QtWidgets.QPushButton(self.centralwidget)
        self.pbPlay.setMinimumSize(QtCore.QSize(50, 50))
        self.pbPlay.setMaximumSize(QtCore.QSize(50, 50))
        self.pbPlay.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/play.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/play.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/play-orange.png);\n"
"}")
        self.pbPlay.setText("")
        self.pbPlay.setObjectName("pbPlay")
        self.horizontalLayout.addWidget(self.pbPlay)
        self.pbPause = QtWidgets.QPushButton(self.centralwidget)
        self.pbPause.setMinimumSize(QtCore.QSize(50, 50))
        self.pbPause.setMaximumSize(QtCore.QSize(50, 50))
        self.pbPause.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/pause.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/pause.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/pause-orange.png);\n"
"}")
        self.pbPause.setText("")
        self.pbPause.setObjectName("pbPause")
        self.horizontalLayout.addWidget(self.pbPause)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbVolume = QtWidgets.QPushButton(self.centralwidget)
        self.pbVolume.setMinimumSize(QtCore.QSize(50, 50))
        self.pbVolume.setMaximumSize(QtCore.QSize(50, 50))
        self.pbVolume.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/volume.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/volume.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/volume-orange.png);\n"
"}")
        self.pbVolume.setText("")
        self.pbVolume.setObjectName("pbVolume")
        self.horizontalLayout.addWidget(self.pbVolume)
        self.hsVolume = QtWidgets.QSlider(self.centralwidget)
        self.hsVolume.setMinimumSize(QtCore.QSize(50, 50))
        self.hsVolume.setStyleSheet("QSlider {\n"
"border: 0px;\n"
"background: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 3px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,  stop: 0 #66e, stop: 1 #FC0B0B);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #FC0B0B, stop: 1 #F5ED14);\n"
"border: 1px solid #777;\n"
"height: 14px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,  stop: 0 #000, stop: 1 #FC0B0B);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #892919, stop: 1 #000);\n"
"\n"
"border: 1px solid #777;\n"
"height: 14px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 12px;\n"
"margin-top: -6px;\n"
"margin-bottom: -6px;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.hsVolume.setOrientation(QtCore.Qt.Horizontal)
        self.hsVolume.setObjectName("hsVolume")
        self.horizontalLayout.addWidget(self.hsVolume)
        self.pbExit = QtWidgets.QPushButton(self.centralwidget)
        self.pbExit.setMinimumSize(QtCore.QSize(50, 50))
        self.pbExit.setMaximumSize(QtCore.QSize(50, 50))
        self.pbExit.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/play.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/play.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/play-orange.png);\n"
"}")
        self.pbExit.setText("")
        self.pbExit.setObjectName("pbExit")
        self.horizontalLayout.addWidget(self.pbExit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
