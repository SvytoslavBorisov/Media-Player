# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 586)
        MainWindow.setStyleSheet("QScrollBar:vertical { \n"
"                   background: black; \n"
"                    border-radius: 4px; \n"
"                    margin: 0px;}\n"
"QScrollBar::handle:vertical { \n"
"                    background-color: rgb(222, 142, 55); \n"
"                    border-radius: 4px; \n"
"                    min-height: 20px; \n"
"                    margin: 0px 2px 0px 2px;}\n"
"QScrollBar::add-line:vertical { \n"
"                    background: black; \n"
"                    height: 0px; \n"
"                    border-radius: 4px; \n"
"                    subcontrol-position: right; \n"
"                    subcontrol-origin: margin;}\n"
"QScrollBar::sub-line:vertical { \n"
"                    background: black;\n"
"                    height: 0px; \n"
"                    border-radius: 4px; \n"
"                    subcontrol-position: left; \n"
"                    subcontrol-origin: margin;}\n"
"QScrollBar::add-page:vertical { \n"
"                    background: black; \n"
"                    height: 0px; \n"
"                    border-radius: 4px; \n"
"                    subcontrol-position: left; \n"
"                    subcontrol-origin: margin;}\n"
"QScrollBar::sub-page:vertical { \n"
"                    background: black; \n"
"                    height: 0px; \n"
"                    border-radius: 4px; \n"
"                    subcontrol-position: left; \n"
"                    subcontrol-origin: margin;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(5, 0, 0, 5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(41, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    padding : 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(229, 229, 229);\n"
"}\n"
"")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    padding : 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid gray;\n"
"    background-color: rgb(232, 17, 35);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 1px solid black;\n"
"    background-color: rgb(232, 17, 35);\n"
"}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, 5, -1)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.framePlayer = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePlayer.sizePolicy().hasHeightForWidth())
        self.framePlayer.setSizePolicy(sizePolicy)
        self.framePlayer.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:reflect, x1:0.528, y1:0.971591, x2:0.528955, y2:0.506, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.framePlayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePlayer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePlayer.setObjectName("framePlayer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.framePlayer)
        self.verticalLayout_3.setContentsMargins(9, 9, -1, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameTitle = QtWidgets.QFrame(self.framePlayer)
        self.frameTitle.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:reflect, x1:0.54, y1:0.471591, x2:0.54, y2:1, stop:0 rgba(222, 142, 55, 255), stop:1 rgba(230, 200, 100, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.frameTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTitle.setObjectName("frameTitle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameTitle)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bRadioState = QtWidgets.QPushButton(self.frameTitle)
        self.bRadioState.setMinimumSize(QtCore.QSize(73, 30))
        self.bRadioState.setMaximumSize(QtCore.QSize(73, 16777215))
        self.bRadioState.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    border: 1px solid gray;    \n"
"    image: url(:/img/Images/radio_notactive.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/radio_notactive.png);\n"
"}\n"
"QPushButton:checked{\n"
"    border-radius: 15px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/radio_active.png);\n"
"}")
        self.bRadioState.setText("")
        self.bRadioState.setCheckable(True)
        self.bRadioState.setChecked(True)
        self.bRadioState.setObjectName("bRadioState")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.bRadioState)
        self.verticalLayout.addWidget(self.bRadioState)
        self.bAudioState = QtWidgets.QPushButton(self.frameTitle)
        self.bAudioState.setMinimumSize(QtCore.QSize(73, 30))
        self.bAudioState.setMaximumSize(QtCore.QSize(73, 16777215))
        self.bAudioState.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    border: 1px solid gray;    \n"
"    image: url(:/img/Images/audio_notactive.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/audio_notactive.png);\n"
"}\n"
"QPushButton:checked{\n"
"    border-radius: 15px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/audio_active.png);\n"
"}")
        self.bAudioState.setText("")
        self.bAudioState.setCheckable(True)
        self.bAudioState.setObjectName("bAudioState")
        self.buttonGroup_2.addButton(self.bAudioState)
        self.verticalLayout.addWidget(self.bAudioState)
        self.bVideoState = QtWidgets.QPushButton(self.frameTitle)
        self.bVideoState.setMinimumSize(QtCore.QSize(73, 30))
        self.bVideoState.setMaximumSize(QtCore.QSize(73, 16777215))
        self.bVideoState.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    border: 1px solid gray;    \n"
"    image: url(:/img/Images/video_notactive.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/video_notactive.png);\n"
"}\n"
"QPushButton:checked{\n"
"    border-radius: 15px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/video_active.png);\n"
"}")
        self.bVideoState.setText("")
        self.bVideoState.setCheckable(True)
        self.bVideoState.setObjectName("bVideoState")
        self.buttonGroup_2.addButton(self.bVideoState)
        self.verticalLayout.addWidget(self.bVideoState)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lArtist = QtWidgets.QLabel(self.frameTitle)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lArtist.setFont(font)
        self.lArtist.setStyleSheet("border: 0px;\n"
"background-color: none;")
        self.lArtist.setAlignment(QtCore.Qt.AlignCenter)
        self.lArtist.setObjectName("lArtist")
        self.verticalLayout_2.addWidget(self.lArtist)
        self.lTitle = QtWidgets.QLabel(self.frameTitle)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lTitle.setFont(font)
        self.lTitle.setStyleSheet("border: 0px;\n"
"background-color: none;")
        self.lTitle.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lTitle.setObjectName("lTitle")
        self.verticalLayout_2.addWidget(self.lTitle)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.frameTitle)
        self.hsMusicSlider = QtWidgets.QSlider(self.framePlayer)
        self.hsMusicSlider.setStyleSheet("QSlider {\n"
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
        self.hsMusicSlider.setProperty("value", 50)
        self.hsMusicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hsMusicSlider.setObjectName("hsMusicSlider")
        self.verticalLayout_3.addWidget(self.hsMusicSlider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbPrevious = QtWidgets.QPushButton(self.framePlayer)
        self.pbPrevious.setMinimumSize(QtCore.QSize(28, 28))
        self.pbPrevious.setMaximumSize(QtCore.QSize(28, 28))
        self.pbPrevious.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/skip-previous.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/skip-previous.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/skip-previous-orange.png);\n"
"}")
        self.pbPrevious.setText("")
        self.pbPrevious.setCheckable(False)
        self.pbPrevious.setObjectName("pbPrevious")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pbPrevious)
        self.horizontalLayout.addWidget(self.pbPrevious)
        self.pbInBegin = QtWidgets.QPushButton(self.framePlayer)
        self.pbInBegin.setMinimumSize(QtCore.QSize(28, 28))
        self.pbInBegin.setMaximumSize(QtCore.QSize(28, 28))
        self.pbInBegin.setStyleSheet("QPushButton{\n"
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
        self.pbInBegin.setText("")
        self.pbInBegin.setCheckable(True)
        self.pbInBegin.setChecked(True)
        self.pbInBegin.setObjectName("pbInBegin")
        self.buttonGroup.addButton(self.pbInBegin)
        self.horizontalLayout.addWidget(self.pbInBegin)
        self.pbPlay = QtWidgets.QPushButton(self.framePlayer)
        self.pbPlay.setMinimumSize(QtCore.QSize(28, 28))
        self.pbPlay.setMaximumSize(QtCore.QSize(28, 28))
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
        self.pbPlay.setCheckable(True)
        self.pbPlay.setChecked(False)
        self.pbPlay.setFlat(False)
        self.pbPlay.setObjectName("pbPlay")
        self.buttonGroup.addButton(self.pbPlay)
        self.horizontalLayout.addWidget(self.pbPlay)
        self.pbStop = QtWidgets.QPushButton(self.framePlayer)
        self.pbStop.setMinimumSize(QtCore.QSize(28, 28))
        self.pbStop.setMaximumSize(QtCore.QSize(28, 28))
        self.pbStop.setStyleSheet("QPushButton{\n"
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
        self.pbStop.setText("")
        self.pbStop.setCheckable(True)
        self.pbStop.setObjectName("pbStop")
        self.buttonGroup.addButton(self.pbStop)
        self.horizontalLayout.addWidget(self.pbStop)
        self.pbNext = QtWidgets.QPushButton(self.framePlayer)
        self.pbNext.setMinimumSize(QtCore.QSize(28, 28))
        self.pbNext.setMaximumSize(QtCore.QSize(28, 28))
        self.pbNext.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/skip-next.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/skip-next.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/skip-next-orange.png);\n"
"}")
        self.pbNext.setText("")
        self.pbNext.setCheckable(False)
        self.pbNext.setObjectName("pbNext")
        self.buttonGroup.addButton(self.pbNext)
        self.horizontalLayout.addWidget(self.pbNext)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pbVolume = QtWidgets.QPushButton(self.framePlayer)
        self.pbVolume.setMinimumSize(QtCore.QSize(28, 28))
        self.pbVolume.setMaximumSize(QtCore.QSize(28, 28))
        self.pbVolume.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
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
        self.pbVolume.setCheckable(True)
        self.pbVolume.setChecked(True)
        self.pbVolume.setObjectName("pbVolume")
        self.horizontalLayout.addWidget(self.pbVolume)
        self.hsVolumeSlider = QtWidgets.QSlider(self.framePlayer)
        self.hsVolumeSlider.setStyleSheet("QSlider {\n"
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
        self.hsVolumeSlider.setProperty("value", 50)
        self.hsVolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hsVolumeSlider.setObjectName("hsVolumeSlider")
        self.horizontalLayout.addWidget(self.hsVolumeSlider)
        self.pbOpenWindow = QtWidgets.QPushButton(self.framePlayer)
        self.pbOpenWindow.setMinimumSize(QtCore.QSize(28, 28))
        self.pbOpenWindow.setMaximumSize(QtCore.QSize(28, 28))
        self.pbOpenWindow.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/bup.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/bup.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/bdown.png);\n"
"}")
        self.pbOpenWindow.setText("")
        self.pbOpenWindow.setCheckable(True)
        self.pbOpenWindow.setChecked(False)
        self.pbOpenWindow.setObjectName("pbOpenWindow")
        self.horizontalLayout.addWidget(self.pbOpenWindow)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.framePlayer)
        self.framePlaylist = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePlaylist.sizePolicy().hasHeightForWidth())
        self.framePlaylist.setSizePolicy(sizePolicy)
        self.framePlaylist.setStyleSheet("QFrame#framePlaylist{\n"
"background-color: qlineargradient(spread:reflect, x1:0.528, y1:0.971591, x2:0.528955, y2:0.506, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"}")
        self.framePlaylist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePlaylist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePlaylist.setObjectName("framePlaylist")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.framePlaylist)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tvPlaylist = QtWidgets.QTableView(self.framePlaylist)
        self.tvPlaylist.setMouseTracking(False)
        self.tvPlaylist.setAutoFillBackground(False)
        self.tvPlaylist.setStyleSheet("QTableView {\n"
"     background-color: rgb(0, 0, 0);\n"
"     border-radius: 5px;}\n"
"QTableView::item:selected:active {\n"
"     background: rgb(191, 255, 191);\n"
"     border: 0px solid transparent;\n"
"      selection-color: rgb(222, 142, 55);}\n"
"QTableView::item:selected:!active {\n"
"     background: rgb(191, 255, 191);\n"
"     border: 0px solid transparent;\n"
"     selection-color: rgb(222, 142, 55);}")
        self.tvPlaylist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tvPlaylist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tvPlaylist.setObjectName("tvPlaylist")
        self.tvPlaylist.horizontalHeader().setVisible(False)
        self.tvPlaylist.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tvPlaylist)
        self.line_2 = QtWidgets.QFrame(self.framePlaylist)
        self.line_2.setStyleSheet("background-color: none;")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbAddMusic = QtWidgets.QPushButton(self.framePlaylist)
        self.pbAddMusic.setMinimumSize(QtCore.QSize(30, 30))
        self.pbAddMusic.setMaximumSize(QtCore.QSize(30, 30))
        self.pbAddMusic.setAutoFillBackground(False)
        self.pbAddMusic.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/plus-orange.png);\n"
"    background-color: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/plus-orange.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/plus.png)\n"
"}\n"
"\n"
"")
        self.pbAddMusic.setText("")
        self.pbAddMusic.setObjectName("pbAddMusic")
        self.horizontalLayout_4.addWidget(self.pbAddMusic)
        self.pbDelMusic = QtWidgets.QPushButton(self.framePlaylist)
        self.pbDelMusic.setMinimumSize(QtCore.QSize(30, 30))
        self.pbDelMusic.setMaximumSize(QtCore.QSize(30, 30))
        self.pbDelMusic.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/minus-orange.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/minus-orange.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/minus.png)\n"
"}")
        self.pbDelMusic.setText("")
        self.pbDelMusic.setObjectName("pbDelMusic")
        self.horizontalLayout_4.addWidget(self.pbDelMusic)
        self.pbPlaylists = QtWidgets.QPushButton(self.framePlaylist)
        self.pbPlaylists.setMinimumSize(QtCore.QSize(30, 30))
        self.pbPlaylists.setMaximumSize(QtCore.QSize(30, 30))
        self.pbPlaylists.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pbPlaylists.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/playlist-orange.png);\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/playlist-orange.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/playlist.png)\n"
"}\n"
"\n"
"")
        self.pbPlaylists.setText("")
        self.pbPlaylists.setObjectName("pbPlaylists")
        self.horizontalLayout_4.addWidget(self.pbPlaylists)
        self.pbSort = QtWidgets.QPushButton(self.framePlaylist)
        self.pbSort.setMinimumSize(QtCore.QSize(30, 30))
        self.pbSort.setMaximumSize(QtCore.QSize(30, 30))
        self.pbSort.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/sort-orange.png);\n"
"    padding: 3px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/sort-orange.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/sort.png)\n"
"}")
        self.pbSort.setText("")
        self.pbSort.setObjectName("pbSort")
        self.horizontalLayout_4.addWidget(self.pbSort)
        self.leFind = QtWidgets.QLineEdit(self.framePlaylist)
        self.leFind.setMinimumSize(QtCore.QSize(200, 30))
        self.leFind.setStyleSheet("background-color: rgb(145, 145, 145);\n"
"border: 1px solid black;\n"
"border-radius:5px;")
        self.leFind.setPlaceholderText("")
        self.leFind.setObjectName("leFind")
        self.horizontalLayout_4.addWidget(self.leFind)
        self.pbFind = QtWidgets.QPushButton(self.framePlaylist)
        self.pbFind.setMinimumSize(QtCore.QSize(30, 30))
        self.pbFind.setMaximumSize(QtCore.QSize(30, 30))
        self.pbFind.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/search-orange.png);\n"
"    padding: 3px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"\n"
"    image: url(:/img/Images/search-orange.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/search.png)\n"
"}")
        self.pbFind.setText("")
        self.pbFind.setObjectName("pbFind")
        self.horizontalLayout_4.addWidget(self.pbFind)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pbSettings = QtWidgets.QPushButton(self.framePlaylist)
        self.pbSettings.setMinimumSize(QtCore.QSize(30, 30))
        self.pbSettings.setMaximumSize(QtCore.QSize(30, 30))
        self.pbSettings.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    image: url(:/img/Images/setup-orange.png);\n"
"    padding: 3px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    image: url(:/img/Images/setup-orange.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    border: 1px solid black;\n"
"    image: url(:/img/Images/setup.png);\n"
"}")
        self.pbSettings.setText("")
        self.pbSettings.setObjectName("pbSettings")
        self.horizontalLayout_4.addWidget(self.pbSettings)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.framePlaylist)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MediaPlayer"))
        self.pushButton_2.setText(_translate("MainWindow", "   -   "))
        self.pushButton.setText(_translate("MainWindow", "   X   "))
        self.lArtist.setText(_translate("MainWindow", "Песня - Исполнитель"))
        self.lTitle.setText(_translate("MainWindow", "НАЗВАНИЕ АЛЬБОМА"))
