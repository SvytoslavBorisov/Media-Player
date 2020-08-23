import sys
import os
from mutagen.mp3 import MP3
import json
from ctypes import *
import styles
import socket
from PyQt5.Qt import QIcon
from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel, QApplication, QMainWindow, QHeaderView, QFileDialog, \
    QAbstractItemView, QWidget, QErrorMessage, QMenu, QGridLayout, QSpacerItem, QGraphicsDropShadowEffect, QDialog
from PyQt5.QtCore import QUrl, QModelIndex, Qt, QEvent, QObject, pyqtSignal, QTimer, QEvent
from mainwindow3 import Ui_MainWindow
from DialogRadio import DialogRadio
from PyQt5 import QtMultimedia, QtMultimediaWidgets
from classModelPlaylist import ModelForPlaylist, PlaylistDelegate
import resource


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:

            # ---------------------------------------------------------------------------------------------------------------
            #                                        Загрузка стилей для MediaPlayer
            # ---------------------------------------------------------------------------------------------------------------

            self.setWindowFlags(Qt.FramelessWindowHint)
            #self.setAttribute(Qt.WA_TranslucentBackground)
            self.frameTitle.setMouseTracking(True)
            self.setMouseTracking(True)

            self.setWindowIcon(QIcon('Images/ico.png'))
            self.framePlayer.setStyleSheet(styles.framePlayer)
            self.frameTitle.setStyleSheet(styles.frameTitle)
            self.bRadioState.setStyleSheet(styles.bRadioState)
            self.bRadioState.setChecked(False)
            self.bAudioState.setStyleSheet(styles.bAudioState)
            self.bAudioState.setChecked(True)
            self.bVideoState.setStyleSheet(styles.bVideoState)
            self.bVideoState.setChecked(False)
            self.lArtist.setStyleSheet(styles.lArtist)
            self.lArtist.setText('')
            self.lTitle.setStyleSheet(styles.lTitle)
            self.lTitle.setText('')
            self.hsMusicSlider.setStyleSheet(styles.hsMusicSlider)
            self.pbPrevious.setStyleSheet(styles.pbPrevious)
            self.pbInBegin.setStyleSheet(styles.pbInBegin)
            self.pbInBegin.setChecked(False)
            self.pbPlay.setStyleSheet(styles.pbPlay)
            self.pbStop.setStyleSheet(styles.pbStop)
            self.pbNext.setStyleSheet(styles.pbNext)
            self.pbVolume.setStyleSheet(styles.pbVolume)
            self.playlistMenu = QMenu()
            self.playlistMenu.setStyleSheet(styles.playlistMenu)
            self.pbPlaylists.setMenu(self.playlistMenu)
            self.hsVolumeSlider.setStyleSheet(styles.hsVolumeSlider)
            self.tvPlaylist.setShowGrid(False)
            self.tvPlaylist.setSelectionMode(QAbstractItemView.SingleSelection)
            self.leFind.setPlaceholderText('Поиск')

            # ---------------------------------------------------------------------------------------------------------------
            #                                    Установка подсказок для кнопок
            # ---------------------------------------------------------------------------------------------------------------

            self.setWindowTitle('MediaPlayer')
            self.bRadioState.setToolTip('Перейти к плейлисту Радио')
            self.bAudioState.setToolTip('Перейти к плейлисту Аудио')
            self.bVideoState.setToolTip('Перейти к плейлисту Видео')
            self.pbPrevious.setToolTip('Предыдущая композиция')
            self.pbInBegin.setToolTip('Остановить воспроизведение')
            self.pbPlay.setToolTip('Воспроизвести')
            self.pbStop.setToolTip('Пауза')
            self.pbNext.setToolTip('Следующая композиция')
            self.pbVolume.setToolTip('Выкл/Вкл звук')
            self.hsVolumeSlider.setToolTip('Регулятор громкости')

            # ---------------------------------------------------------------------------------------------------------------

            self.playlist = []    # Список всех композиций
            self.indFind = set()  # Список индексов, подходящих под критери композиций
            self.indActivePlaylist = 0
            self.play = False     # Играет ли музыка
            self.pause = False    # Стоит ли на паузе
            self.full = False
            self.presss = False
            self.mode = 'Audio'   # Mode = 'Audio'

            # ---------------------------------------------------------------------------------------------------------------

            self.playlistMenu.addAction('Новый плейлист')
            self.playlistMenu.addSeparator()
            self.playlistMenu.addAction('Удалить плейлист')
            self.playlistMenu.addSeparator()

            resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))  # Загружаем плейлист
            for y in resp.items():
                self.playlist.append([])
                self.playlistMenu.addAction(y[0])
                for x in y[1]:
                    if os.path.exists(x[0]['url']):
                        self.playlist[self.indActivePlaylist].append([x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                self.indActivePlaylist += 1

            self.indActivePlaylist = 0

            # ---------------------------------------------------------------------------------------------------------------

            self.myMedia = QtMultimedia.QMediaPlayer(self)                  # Создаём активный плейлист
            self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)     # Создаём активный плейлист
            self.myMedia.setVolume(50)                                      # Стандартная громкость
            self.myMedia.setPlaylist(self.myPlaylist)                       # Добавляем плейлист в активные

            # ---------------------------------------------------------------------------------------------------------------

            temp = []
            for x in self.playlist[self.indActivePlaylist]:
                local = QUrl.fromLocalFile(x[0])                             # Переводим глобальный путь в локальный
                self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))  # Добавляем композицию в плейлист
                temp.append([x[0], x[1].length])                             # Сохраняем (Название и Длину) для таблицы

            # ---------------------------------------------------------------------------------------------------------------

            self.modelForPlayLists = ModelForPlaylist(temp)   # Модель для Таблицы Плейлистов
            self.tvPlaylist.setModel(self.modelForPlayLists)
            #self.deleg = PlaylistDelegate()
            #self.tvPlaylist.setItemDelegateForColumn(3, self.deleg)

            self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
            self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)        # Размер строк
            self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)                     # Размер строк

            '''self.tvPlaylist.setDragDropMode(QAbstractItemView.InternalMove)
            self.tvPlaylist.setDragEnabled(True)
            self.tvPlaylist.setAcceptDrops(True)
            self.tvPlaylist.setDropIndicatorShown(True)'''

            self.InBegin()  # Переводим трек в начало

            # ---------------------------------------------------------------------------------------------------------------
            #                                      Сигналы кнопок и других виджетов
            # ---------------------------------------------------------------------------------------------------------------

            self.pbStop.clicked.connect(self.stopMusic)                # Кнопка "Пауза"
            self.pbPlay.clicked.connect(self.playMusic)                # Кнопка "Воспроизвести"
            self.pbInBegin.clicked.connect(self.InBegin)               # Кнопка "Стоп"
            self.pbNext.clicked.connect(self.ToNext)                   # Кнопка "Следующий"
            self.pbPrevious.clicked.connect(self.ToPrevious)           # Кнопка "Предыдущий"
            self.pbDelMusic.clicked.connect(self.delFile)              # Кнопка "Удалить музыку"
            self.pbOpenWindow.clicked.connect(self.openWindow)         # Кнопка "Скрыть/Открыть окно"
            self.pbVolume.clicked.connect(self.offVol)                 # Кнопка "Выкл/Вкл звук"
            self.pbFind.clicked.connect(self.closeFind)                # Кнопка "Поиск"
            self.pbAddMusic.clicked.connect(self.newFile)              # Кнопка "Добавить музыку"
            self.pbSort.clicked.connect(self.sortPlaylist)             # Кнопка "Отсортировать"
            self.bRadioState.clicked.connect(self.setActiveRadio)      # Mode = "Radio"
            self.bAudioState.clicked.connect(self.setActiveAudio)      # Mode = "Audio"
            self.bVideoState.clicked.connect(self.setActiveVideo)      # Mode = "Video"

            self.leFind.textEdited.connect(self.findMusic)             # Изменение в LineEdit
            self.myMedia.positionChanged.connect(self.SetMusic)        # Изменение в позиции музыки

            self.hsVolumeSlider.sliderMoved.connect(self.SetVol)       # Регулятор громкости - Движение
            self.hsMusicSlider.sliderMoved.connect(self.SetMusicTime)  # Регулятор музыки - Движение
            self.hsMusicSlider.sliderPressed.connect(self.stopMusic)   # Регулятор музыки - Нажатие
            self.hsMusicSlider.sliderReleased.connect(self.playMusic)  # Регулятор музыки - Отпускание

            self.tvPlaylist.doubleClicked.connect(self.startMusic)     # Двойной клик по строке таблицы
            self.playlistMenu.triggered.connect(self.clickPlaylistMenu)
            self.pushButton.clicked.connect(self.ex)
            self.pushButton_2.clicked.connect(self.vis)
            self.tmrVideo = QTimer()
            self.tmrVideo.timeout.connect(self.onFull)
            self.tvPlaylist.setMouseTracking(True)
            self.tvPlaylist.installEventFilter(self)
            self.installEventFilter(self)
            self.framePlayer.setMaximumHeight(180)
            self.framePlayer.setFixedWidth(456)

            # ---------------------------------------------------------------------------------------------------------------
        except Exception as e:
            print('Ошибка ' + str(e))

    def eventFilter(self, obj, event):
        try:
            if event.type() == QEvent.MouseMove:
                if self.mode == 'Video' and self.full and not self.framePlaylist.isVisible():
                    self.offFull()
                    self.tmrVideo.setInterval(5000)
                    self.tmrVideo.start()
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Space:
                    if self.myMedia.state() != QtMultimedia.QMediaPlayer.PlayingState:
                        if len(self.playlist[self.indActivePlaylist]) > 0:
                            self.pbPlay.setChecked(True)
                            self.playMusic()
                    else:
                        self.stopMusic()
                        self.pbStop.setChecked(True)

            return False
        except Exception as e:
            print(e)

    def offFull(self):
        try:
            #self.vw.show()
            self.verticalLayout_2.addWidget(self.vw)
            self.frame.setVisible(True)
        except Exception as e:
            print(e)

    def onFull(self):
        try:
            self.gridLayout.addWidget(self.vw)
            self.vw.showFullScreen()
            self.frame.setVisible(False)
        except Exception as e:
            print(e)

    def ex(self):
        sys.exit()

    def vis(self):
        self.showMinimized()

    def fullScreen(self):
        try:
            if self.full and self.mode == 'Video':
                self.offFull()
                self.showNormal()
                if self.framePlaylist.isVisible():
                    self.setMinimumHeight(591)
                    self.setGeometry(self.pos().x(), self.pos().y(), 466, 591)
                    self.framePlayer.setMaximumHeight(180)
                else:
                    self.setMinimumHeight(225)
                    self.setGeometry(self.pos().x(), self.pos().y(), 466, 225)
                    self.framePlayer.setMaximumHeight(180)
                self.full = not self.full
                self.bAudioState.setVisible(True)
                self.bRadioState.setVisible(True)
                self.bVideoState.setVisible(True)
                self.tmrVideo.stop()
            elif self.mode == 'Video':
                self.framePlayer.setMaximumHeight(10000)
                self.full = not self.full
                self.bAudioState.setVisible(False)
                self.framePlaylist.setVisible(False)
                self.bRadioState.setVisible(False)
                self.bVideoState.setVisible(False)
                self.showFullScreen()
        except Exception as e:
            print('fullScreen: ' + str(e))

    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton | e.buttons() and self.presss and not self.full:
                self.setGeometry(self.pos().x() + (e.x() - self.dx), self.pos().y() + (e.y() - self.dy), self.width(), self.height())
        except Exception as e:
            print(e)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and (-3 < e.x() < 13 or -3 < e.y() < 30 or self.width() - 13 < e.x() < self.width() + 3 or self.height() - 13 < e.y() < self.height() + 3) and not self.full:
            self.dx = e.x()
            self.dy = e.y()
            self.presss = True
            self.setCursor(Qt.OpenHandCursor)
        else:
            self.presss = False

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton and self.presss and not self.full:
            self.setCursor(Qt.ArrowCursor)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        try:
            if 0 < args[0].pos().x() < self.frameTitle.width() and\
                    15 < args[0].pos().y() < self.frameTitle.height() + 15:
                self.fullScreen()
        except Exception as e:
            print('mouseDoubleClickEvent: ' + str(e))

    def setActiveVideo(self):
        try:
            if self.mode == 'Video':
                pass
            else:
                self.myMedia.stop()
                self.playlist = []  # Список всех композиций
                self.indFind = set()  # Список индексов, подходящих под критери композиций
                self.play = False  # Играет ли музыка
                self.pause = False  # Стоит ли на паузе
                self.indActivePlaylist = 0
                self.hsMusicSlider.setMinimum(0)
                self.hsMusicSlider.setSliderPosition(0)
                self.modelForPlayLists.activeInd = -1

                self.vw = QtMultimediaWidgets.QVideoWidget()
                self.verticalLayout_2.addWidget(self.vw)
                self.vw.setMouseTracking(True)
                self.vw.installEventFilter(self)
                self.mode = 'Video'
                self.modelForPlayLists.mode = 'Video'
                self.pbPlay.setChecked(True)
                self.bVideoState.setChecked(True)

                self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист

                self.myMedia.setVolume(50)

                resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))

                self.playlistMenu.clear()
                self.playlistMenu.addAction('Новый плейлист')
                self.playlistMenu.addSeparator()
                self.playlistMenu.addAction('Удалить плейлист')
                self.playlistMenu.addSeparator()

                for y in resp.items():
                    self.playlist.append([])
                    self.playlistMenu.addAction(y[0])
                    for x in y[1]:
                        if os.path.exists(x[0]['url']) or 'http' in x[0]['url']:
                            self.playlist[self.indActivePlaylist].append(x[0])  # Добавляем в плейлист Путь к файлу
                    self.indActivePlaylist += 1

                self.indActivePlaylist = 0

                temp = []
                for x in self.playlist[self.indActivePlaylist]:
                    temp.append([x])
                    self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))

                self.myMedia.setPlaylist(self.myPlaylist)
                self.myMedia.setVideoOutput(self.vw)
                self.lArtist.setVisible(False)
                self.lTitle.setVisible(False)
                self.framePlayer.setMinimumHeight(180)

                self.modelForPlayLists.newData(temp)
        except Exception as e:
            print('Ошибка ' + str(e))

    def clickPlaylistMenu(self, event):
        try:
            if self.mode == 'Audio':
                if event.text() == 'Новый плейлист':
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе
                    self.indActivePlaylist = 0
                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))  # Загружаем плейлист

                    resp['NewPlaylist ' + str(len(resp) + 1)] = []

                    self.playlistMenu.clear()
                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()
                    self.playlistMenu.addAction('Удалить плейлист')
                    self.playlistMenu.addSeparator()

                    for y in resp.items():
                        self.playlist.append([])
                        self.playlistMenu.addAction(y[0])
                        for x in y[1]:
                            if os.path.exists(x[0]['url']):
                                self.playlist[self.indActivePlaylist].append(
                                    [x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                        self.indActivePlaylist += 1

                    self.indActivePlaylist = -1

                    with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        local = QUrl.fromLocalFile(x[0])  # Переводим глобальный путь в локальный
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))  # Добавляем композицию в плейлист
                        temp.append([x[0], x[1].length])  # Сохраняем (Название и Длину) для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
                elif event.text() == 'Удалить плейлист' and len(self.playlist) > 1:
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе

                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))  # Загружаем плейлист

                    self.playlistMenu.clear()
                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()
                    self.playlistMenu.addAction('Удалить плейлист')
                    self.playlistMenu.addSeparator()

                    temp = int(self.indActivePlaylist)
                    self.indActivePlaylist = 0

                    for y in resp.items():
                        if self.indActivePlaylist != temp:
                            self.playlist.append([])
                            self.playlistMenu.addAction(y[0])
                            for x in y[1]:
                                if os.path.exists(x[0]['url']):
                                    self.playlist[self.indActivePlaylist].append(
                                        [x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                        else:
                            numer = y[0]
                        self.indActivePlaylist += 1

                    resp.pop(numer)
                    self.indActivePlaylist = 0

                    with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        local = QUrl.fromLocalFile(x[0])  # Переводим глобальный путь в локальный
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))  # Добавляем композицию в плейлист
                        temp.append([x[0], x[1].length])  # Сохраняем (Название и Длину) для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                        QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
                else:
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе
                    self.indActivePlaylist = 0
                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))  # Загружаем плейлист
                    tempInd = 0
                    for y in resp.items():
                        self.playlist.append([])
                        if event.text() == y[0]:
                            tempInd = self.indActivePlaylist
                        for x in y[1]:
                            if os.path.exists(x[0]['url']):
                                self.playlist[self.indActivePlaylist].append(
                                    [x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                        self.indActivePlaylist += 1

                    self.indActivePlaylist = tempInd

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        local = QUrl.fromLocalFile(x[0])  # Переводим глобальный путь в локальный
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))  # Добавляем композицию в плейлист
                        temp.append([x[0], x[1].length])  # Сохраняем (Название и Длину) для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
            elif self.mode == 'Radio':
                if event.text() == 'Новый плейлист':
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе
                    self.indActivePlaylist = 0
                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))  # Загружаем плейлист

                    resp['NewPlaylist ' + str(len(resp) + 1)] = []

                    self.playlistMenu.clear()
                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()
                    self.playlistMenu.addAction('Удалить плейлист')
                    self.playlistMenu.addSeparator()

                    for y in resp.items():
                        self.playlist.append([])
                        self.playlistMenu.addAction(y[0])
                        for x in y[1]:
                            self.playlist[self.indActivePlaylist].append(x[0])  # Добавляем в плейлист Путь к файлу,
                        self.indActivePlaylist += 1

                    self.indActivePlaylist = -1

                    with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))  # Добавляем композицию в плейлист
                        temp.append([x])  # Сохраняем Название для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
                elif event.text() == 'Удалить плейлист' and len(self.playlist) > 1:
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе

                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))  # Загружаем плейлист

                    self.playlistMenu.clear()
                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()
                    self.playlistMenu.addAction('Удалить плейлист')
                    self.playlistMenu.addSeparator()

                    temp = int(self.indActivePlaylist)
                    self.indActivePlaylist = 0

                    for y in resp.items():
                        if self.indActivePlaylist != temp:
                            self.playlist.append([])
                            self.playlistMenu.addAction(y[0])
                            for x in y[1]:
                                if os.path.exists(x[0]['url']):
                                    self.playlist[self.indActivePlaylist].append(
                                        [x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                        else:
                            numer = y[0]
                        self.indActivePlaylist += 1

                    resp.pop(numer)
                    self.indActivePlaylist = 0

                    with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        self.myPlaylist.addMedia(
                            QtMultimedia.QMediaContent(QUrl(x['url'])))  # Добавляем композицию в плейлист
                        temp.append([x])  # Сохраняем Название для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                        QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
                else:
                    self.pbPlay.setChecked(False)
                    self.myMedia.stop()
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.indActivePlaylist = 0
                    self.play = False  # Играет ли радио
                    self.pause = False  # Стоит ли на паузе
                    self.lTitle.setText('')
                    self.lArtist.setText('')
                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.hsMusicSlider.setMaximum(1)
                    self.modelForPlayLists.activeInd = -1

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))  # Загружаем плейлист
                    tempInd = 0
                    for y in resp.items():
                        self.playlist.append([])
                        if event.text() == y[0]:
                            tempInd = self.indActivePlaylist
                        for x in y[1]:
                            self.playlist[self.indActivePlaylist].append(x[0])  # Добавляем в плейлист Путь к файлу,
                        self.indActivePlaylist += 1

                    self.indActivePlaylist = tempInd

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        self.myPlaylist.addMedia(
                            QtMultimedia.QMediaContent(QUrl(x['url'])))  # Добавляем композицию в плейлист
                        temp.append([x])  # Сохраняем Название для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.modelForPlayLists.newData(temp)

                    self.InBegin()  # Переводим трек в начало
            elif self.mode == 'Video':
                if event.text() == 'Новый плейлист':
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе
                    self.indActivePlaylist = 0
                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))

                    self.playlistMenu.clear()

                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()

                    self.indActivePlaylist = 0

                    resp['NewPlaylist ' + str(len(resp) + 1)] = []

                    self.playlistMenu.clear()
                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()
                    self.playlistMenu.addAction('Удалить плейлист')
                    self.playlistMenu.addSeparator()

                    for y in resp.items():
                        self.playlist.append([])
                        self.playlistMenu.addAction(y[0])
                        for x in y[1]:
                            if os.path.exists(x[0]['url']):
                                self.playlist[self.indActivePlaylist].append(x[0])  # Добавляем в плейлист Путь к файлу
                        self.indActivePlaylist += 1

                    self.indActivePlaylist = -1

                    with open('VideoPlaylists/video.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        temp.append([x])
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))

                    self.myMedia.setVideoOutput(self.vw)
                    self.lArtist.setVisible(False)
                    self.lTitle.setVisible(False)

                    self.modelForPlayLists.newData(temp)

                    self.myPlaylist.setCurrentIndex(0)

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
                elif event.text() == 'Удалить плейлист' and len(self.playlist) > 1:
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе

                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    # ---------------------------------------------------------------------------------------------------------------

                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))  # Загружаем плейлист

                    self.playlistMenu.clear()
                    self.playlistMenu.addAction('Новый плейлист')
                    self.playlistMenu.addSeparator()
                    self.playlistMenu.addAction('Удалить плейлист')
                    self.playlistMenu.addSeparator()

                    temp = int(self.indActivePlaylist)
                    self.indActivePlaylist = 0

                    for y in resp.items():
                        if self.indActivePlaylist != temp:
                            self.playlist.append([])
                            self.playlistMenu.addAction(y[0])
                            for x in y[1]:
                                if os.path.exists(x[0]['url']):
                                    self.playlist[self.indActivePlaylist].append(
                                        [x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                        else:
                            numer = y[0]
                        self.indActivePlaylist += 1

                    resp.pop(numer)
                    self.indActivePlaylist = 0

                    with open('VideoPlaylists/video.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        self.myPlaylist.addMedia(
                            QtMultimedia.QMediaContent(QUrl(x['url'])))  # Добавляем композицию в плейлист
                        temp.append([x])  # Сохраняем Название для таблицы

                    # ---------------------------------------------------------------------------------------------------------------

                    self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                        QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало
                else:
                    self.myMedia.stop()
                    self.pbPlay.setChecked(False)
                    self.playlist = []  # Список всех композиций
                    self.indFind = set()  # Список индексов, подходящих под критери композиций
                    self.play = False  # Играет ли музыка
                    self.pause = False  # Стоит ли на паузе
                    self.indActivePlaylist = 0
                    self.hsMusicSlider.setMinimum(0)
                    self.hsMusicSlider.setSliderPosition(0)
                    self.modelForPlayLists.activeInd = -1
                    self.lTitle.setText('')
                    self.lArtist.setText('')

                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))

                    tempInd = 0

                    for y in resp.items():
                        self.playlist.append([])
                        if event.text() == y[0]:
                            tempInd = self.indActivePlaylist
                        for x in y[1]:
                            if os.path.exists(x[0]['url']):
                                self.playlist[self.indActivePlaylist].append(x[0])  # Добавляем в плейлист Путь к файлу
                        self.indActivePlaylist += 1

                    self.indActivePlaylist = tempInd

                    with open('VideoPlaylists/video.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    # ---------------------------------------------------------------------------------------------------------------

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                    self.myMedia.setVolume(50)  # Стандартная громкость
                    self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                    # ---------------------------------------------------------------------------------------------------------------

                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        temp.append([x])
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))

                    self.myMedia.setVideoOutput(self.vw)
                    self.lArtist.setVisible(False)
                    self.lTitle.setVisible(False)

                    self.modelForPlayLists.newData(temp)

                    self.myPlaylist.setCurrentIndex(0)

                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                        QHeaderView.ResizeToContents)  # Размер строк
                    self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                    self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                    self.InBegin()  # Переводим трек в начало

        except Exception as e:
            print(e)

    def delChange(self, ind):
        try:
            temp = set()
            temp.add(ind.row())
            self.tvPlaylist.setCurrentIndex(ind)
            self.modelForPlayLists.change(temp)
        except Exception as e:
            print(e)

    def keyPressEvent(self, event):
        try:
            if self.tvPlaylist.currentIndex().row() != -1 and event.key() == Qt.Key_Enter - 1:  # Если нажат Enter и
                self.startMusic(self.tvPlaylist.currentIndex())                                 # выбрана строка, то проиграть композицию
            if self.tvPlaylist.currentIndex().row() != -1:
                if self.mode == 'Audio':
                    if event.key() == Qt.Key_Control and self.tvPlaylist.currentIndex().row() != len(self.playlist[self.indActivePlaylist]) - 1:

                        tempInd = self.myPlaylist.currentIndex()

                        if self.tvPlaylist.currentIndex().row() == tempInd:
                            tempInd -= 1

                        resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))

                        self.playlist[self.indActivePlaylist] = self.playlist[self.indActivePlaylist][:self.tvPlaylist.currentIndex().row() - 1] + \
                                                                [self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row()]] + \
                                                                [self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row() - 1]] + \
                                                                self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row() + 1:]

                        resp[list(resp.keys())[self.indActivePlaylist]] = []
                        temp = []
                        for x in self.playlist[self.indActivePlaylist]:
                            temp.append([x[0], x[1].length])
                            resp[list(resp.keys())[self.indActivePlaylist]].append(
                                [{"name": x[0].split('/')[-1], 'url': x[0]}])

                        with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                            f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                        self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                        self.myMedia.setPlaylist(self.myPlaylist)

                        for x in self.playlist[self.indActivePlaylist]:
                            local = QUrl.fromLocalFile(x[0])
                            self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))

                        self.modelForPlayLists.newData(temp)

                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                            QHeaderView.ResizeToContents)  # Размер строк
                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                        self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк
                        if self.pbPlay.isChecked():
                            self.myPlaylist.setCurrentIndex(tempInd)
                            self.myMedia.play()
                    if event.key() == Qt.Key_Alt and self.tvPlaylist.currentIndex().row() != 0:

                        tempInd = self.myPlaylist.currentIndex()

                        if self.tvPlaylist.currentIndex().row() == tempInd:
                            tempInd += 1

                        resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))

                        self.playlist[self.indActivePlaylist] = self.playlist[self.indActivePlaylist][:self.tvPlaylist.currentIndex().row()] + \
                                                                [self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row() + 1]] + \
                                                                [self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row()]] + \
                                                                self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row() + 2:]

                        resp[list(resp.keys())[self.indActivePlaylist]] = []
                        temp = []
                        for x in self.playlist[self.indActivePlaylist]:
                            temp.append([x[0], x[1].length])
                            resp[list(resp.keys())[self.indActivePlaylist]].append(
                                [{"name": x[0].split('/')[-1], 'url': x[0]}])

                        with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                            f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                        self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                        self.myMedia.setPlaylist(self.myPlaylist)

                        for x in self.playlist[self.indActivePlaylist]:
                            local = QUrl.fromLocalFile(x[0])
                            self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))

                        self.modelForPlayLists.newData(temp)

                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                            QHeaderView.ResizeToContents)  # Размер строк
                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                        self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк
                        if self.pbPlay.isChecked():
                            self.myPlaylist.setCurrentIndex(tempInd)
                            self.myMedia.play()
                elif self.mode == 'Radio':
                    if event.key() == Qt.Key_Control and self.tvPlaylist.currentIndex().row() != len(self.playlist[self.indActivePlaylist]):

                        tempInd = self.myPlaylist.currentIndex()

                        if self.tvPlaylist.currentIndex().row() == tempInd:
                            tempInd -= 1

                        resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))

                        self.playlist[self.indActivePlaylist] = self.playlist[self.indActivePlaylist][
                                                                :self.tvPlaylist.currentIndex().row() - 1] + \
                                                                [self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row()]] + \
                                                                [self.playlist[self.indActivePlaylist][
                                                                     self.tvPlaylist.currentIndex().row() - 1]] + \
                                                                self.playlist[self.indActivePlaylist][ self.tvPlaylist.currentIndex().row() + 1:]

                        resp[list(resp.keys())[self.indActivePlaylist]] = []
                        temp = []
                        for x in self.playlist[self.indActivePlaylist]:
                            temp.append(x)
                            resp[list(resp.keys())[self.indActivePlaylist]].append(
                                [{"name": x['name'], 'url': x['url']}])

                        with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                            f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                        self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                        self.myMedia.setPlaylist(self.myPlaylist)

                        for x in self.playlist[self.indActivePlaylist]:
                            self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))

                        self.modelForPlayLists.newData(temp)

                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                            QHeaderView.ResizeToContents)  # Размер строк
                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                        self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк
                        self.myPlaylist.setCurrentIndex(tempInd)
                    if event.key() == Qt.Key_Alt and self.tvPlaylist.currentIndex().row() != 0:

                        tempInd = self.myPlaylist.currentIndex()

                        if self.tvPlaylist.currentIndex().row() == tempInd:
                            tempInd += 1

                        resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))

                        self.playlist[self.indActivePlaylist] = self.playlist[self.indActivePlaylist][:self.tvPlaylist.currentIndex().row()] + \
                                                                [self.playlist[self.indActivePlaylist][
                                                                     self.tvPlaylist.currentIndex().row() + 1]] + \
                                                                [self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row()]] + \
                                                                self.playlist[self.indActivePlaylist][self.tvPlaylist.currentIndex().row() + 2:]

                        resp[list(resp.keys())[self.indActivePlaylist]] = []
                        temp = []
                        for x in self.playlist[self.indActivePlaylist]:
                            temp.append(x)
                            resp[list(resp.keys())[self.indActivePlaylist]].append(
                                [{"name": x['name'], 'url': x['url']}])

                        with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                            f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                        self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                        self.myMedia.setPlaylist(self.myPlaylist)

                        for x in self.playlist[self.indActivePlaylist]:
                            self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))

                        self.modelForPlayLists.newData(temp)

                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(
                            QHeaderView.ResizeToContents)  # Размер строк
                        self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                        self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк
                        self.myPlaylist.setCurrentIndex(tempInd)
        except Exception as e:
            print('Ошибка keyPressEvent ' + str(e))

    def startMusic(self, ind):
        try:
            if len(self.playlist[self.indActivePlaylist]) > 0:
                if self.mode == 'Audio':
                    self.modelForPlayLists.change(set())
                    self.hsMusicSlider.setMinimum(0)
                    self.pbPlay.setChecked(True)
                    self.myPlaylist.setCurrentIndex(ind.row())
                    self.tvPlaylist.selectRow(ind.row())
                    self.modelForPlayLists.active(ind.row())
                    self.myMedia.play()
                    self.play = True
                elif self.mode == 'Radio':
                    self.modelForPlayLists.change(set())
                    self.hsMusicSlider.setMinimum(0)
                    self.pbPlay.setChecked(True)
                    self.myPlaylist.setCurrentIndex(ind.row())
                    self.tvPlaylist.selectRow(ind.row())
                    self.modelForPlayLists.active(ind.row())
                    try:
                        socket.gethostbyaddr('www.yandex.ru')
                        self.myMedia.play()
                        self.play = True
                        if self.modelForPlayLists.activeInd != -1:
                            self.lTitle.setText(
                                self.playlist[self.indActivePlaylist][self.myPlaylist.currentIndex()]['name'])
                        else:
                            self.lTitle.setText('')
                            self.lArtist.setText('')
                    except socket.gaierror:
                        errorMessage = QErrorMessage()
                        errorMessage.showMessage("Отсутствует подключение к интернету или некорректен радиопоток.")
                        errorMessage.exec()
                elif self.mode == 'Video':
                    self.modelForPlayLists.change(set())
                    self.hsMusicSlider.setMinimum(0)
                    self.pbPlay.setChecked(True)
                    self.myPlaylist.setCurrentIndex(ind.row())
                    self.tvPlaylist.selectRow(ind.row())
                    self.modelForPlayLists.active(ind.row())
                    self.myMedia.play()
                    self.play = True
        except Exception as e:
            print(e)

    def SetMusic(self):
        try:
            if len(self.playlist[self.indActivePlaylist]) > 0:
                if self.mode == 'Audio':
                    if self.pbPlay.isChecked():
                        self.hsMusicSlider.setSliderPosition(self.myMedia.position())
                    self.hsMusicSlider.setMaximum(self.myMedia.duration())
                    temp = self.myMedia.metaData(QtMultimedia.QMediaMetaData.Title)
                    if temp:
                        self.lTitle.setText(self.myMedia.metaData(QtMultimedia.QMediaMetaData.Title))
                    elif self.modelForPlayLists.activeInd != -1:
                        self.lTitle.setText(self.playlist[self.indActivePlaylist][self.myPlaylist.currentIndex()][0].split('/')[-1].split('.')[0])
                    else:
                        self.lTitle.setText('')
                    data = self.myMedia.metaData(QtMultimedia.QMediaMetaData.ContributingArtist)
                    if data:
                        self.lArtist.setText(data[0])
                    elif self.modelForPlayLists.activeInd != -1:
                        self.lArtist.setText('Неизвестно')
                    else:
                        self.lArtist.setText('')
                    if self.myMedia.position() == self.myMedia.duration():
                        if self.myPlaylist.currentIndex() == -1:
                            self.tvPlaylist.selectRow(0)
                            Index = self.modelForPlayLists.createIndex(0, 0)
                            self.startMusic(Index)
                        else:
                            self.tvPlaylist.selectRow(self.myPlaylist.currentIndex())
                            self.modelForPlayLists.active(self.myPlaylist.currentIndex())
                elif self.mode == 'Radio':
                    self.hsMusicSlider.setMaximum(1)
                elif self.mode == 'Video':
                    if self.pbPlay.isChecked():
                        self.hsMusicSlider.setSliderPosition(self.myMedia.position())
                    self.hsMusicSlider.setMaximum(self.myMedia.duration())
                    if self.myMedia.position() == self.myMedia.duration():
                        if self.myPlaylist.currentIndex() == -1:
                            self.tvPlaylist.selectRow(0)
                            Index = self.modelForPlayLists.createIndex(0, 0)
                            self.startMusic(Index)
                        else:
                            self.tvPlaylist.selectRow(self.myPlaylist.currentIndex())
                            self.modelForPlayLists.active(self.myPlaylist.currentIndex())
            else:
                self.lTitle.setText('')
                self.lArtist.setText('')
        except Exception as e:
            print(e)

    def SetMusicTime(self, x):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0 and self.pbPlay.isChecked():
                    self.myMedia.setPosition(x)
            elif self.mode == 'Radio':
                pass
            elif self.mode == 'Video':
                if len(self.playlist[self.indActivePlaylist]) > 0 and self.pbPlay.isChecked():
                    self.myMedia.setPosition(x)
        except Exception as e:
            print(e)

    def stopMusic(self):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.pause()
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.stop()
            else:
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.pause()
        except Exception as e:
            print(e)

    def playMusic(self):
        try:
            if self.mode == 'Audio':
                if self.pbPlay.isChecked() and len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setPosition(self.hsMusicSlider.sliderPosition())
                    self.myMedia.play()
                else:
                    self.pbPlay.setChecked(False)
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.play()
            elif self.mode == 'Video':
                if self.pbPlay.isChecked() and len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setPosition(self.hsMusicSlider.sliderPosition())
                    self.myMedia.play()
        except Exception as e:
            print(e)

    def InBegin(self):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setPosition(0)
                    self.myMedia.stop()
                    self.hsMusicSlider.setSliderPosition(0)
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.stop()
            elif self.mode == 'Video':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setPosition(0)
                    self.myMedia.stop()
                    self.hsMusicSlider.setSliderPosition(0)
        except Exception as e:
            print(e)

    def SetVol(self, x):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setVolume(x)
                    if x == 0:
                        self.pbVolume.setChecked(False)
                    else:
                        self.pbVolume.setChecked(True)
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setVolume(x)
                    if x == 0:
                        self.pbVolume.setChecked(False)
                    else:
                        self.pbVolume.setChecked(True)
            elif self.mode == 'Video':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    self.myMedia.setVolume(x)
                    if x == 0:
                        self.pbVolume.setChecked(False)
                    else:
                        self.pbVolume.setChecked(True)
        except Exception as e:
            print(e)

    def offVol(self):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myMedia.volume() == 0:
                        self.myMedia.setVolume(50)
                        self.hsVolumeSlider.setSliderPosition(50)
                    else:
                        self.myMedia.setVolume(0)
                        self.hsVolumeSlider.setSliderPosition(0)
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myMedia.volume() == 0:
                        self.myMedia.setVolume(50)
                        self.hsVolumeSlider.setSliderPosition(50)
                    else:
                        self.myMedia.setVolume(0)
                        self.hsVolumeSlider.setSliderPosition(0)
            elif self.mode == 'Video':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myMedia.volume() == 0:
                        self.myMedia.setVolume(50)
                        self.hsVolumeSlider.setSliderPosition(50)
                    else:
                        self.myMedia.setVolume(0)
                        self.hsVolumeSlider.setSliderPosition(0)
        except Exception as e:
            print(e)

    def ToNext(self):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myPlaylist.currentIndex() >= self.modelForPlayLists.rowCount() - 1:
                        Index = self.modelForPlayLists.createIndex(0, 0)
                    else:
                        Index = self.modelForPlayLists.createIndex(self.myPlaylist.currentIndex() + 1, 1)
                    self.tvPlaylist.setCurrentIndex(Index)
                    self.startMusic(Index)
                    self.myMedia.stop()
                    self.myMedia.play()
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myPlaylist.currentIndex() >= self.modelForPlayLists.rowCount() - 1:
                        Index = self.modelForPlayLists.createIndex(0, 0)
                    else:
                        Index = self.modelForPlayLists.createIndex(self.myPlaylist.currentIndex() + 1, 1)
                    self.tvPlaylist.setCurrentIndex(Index)
                    self.startMusic(Index)
                    self.myMedia.stop()
                    self.myMedia.play()
            elif self.mode == 'Video':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myPlaylist.currentIndex() >= self.modelForPlayLists.rowCount() - 1:
                        Index = self.modelForPlayLists.createIndex(0, 0)
                    else:
                        Index = self.modelForPlayLists.createIndex(self.myPlaylist.currentIndex() + 1, 1)
                    self.tvPlaylist.setCurrentIndex(Index)
                    self.startMusic(Index)
                    self.myMedia.stop()
                    self.myMedia.play()
        except Exception as e:
            print(e)

    def ToPrevious(self):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myPlaylist.currentIndex() - 1 < 0:
                        Index = self.modelForPlayLists.createIndex(self.modelForPlayLists.rowCount() - 1, 1)
                    else:
                        Index = self.modelForPlayLists.createIndex(self.myPlaylist.currentIndex() - 1, 1)
                    self.tvPlaylist.setCurrentIndex(Index)
                    self.startMusic(Index)
                    self.myMedia.stop()
                    self.myMedia.play()
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myPlaylist.currentIndex() - 1 < 0:
                        Index = self.modelForPlayLists.createIndex(self.modelForPlayLists.rowCount() - 1, 1)
                    else:
                        Index = self.modelForPlayLists.createIndex(self.myPlaylist.currentIndex() - 1, 1)
                    self.tvPlaylist.setCurrentIndex(Index)
                    self.startMusic(Index)
                    self.myMedia.stop()
                    self.myMedia.play()
            elif self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0:
                    if self.myPlaylist.currentIndex() - 1 < 0:
                        Index = self.modelForPlayLists.createIndex(self.modelForPlayLists.rowCount() - 1, 1)
                    else:
                        Index = self.modelForPlayLists.createIndex(self.myPlaylist.currentIndex() - 1, 1)
                    self.tvPlaylist.setCurrentIndex(Index)
                    self.startMusic(Index)
                    self.myMedia.stop()
                    self.myMedia.play()
        except Exception as e:
            print(e)

    def newFile(self):
        try:
            if self.mode == 'Audio':

                files = QFileDialog().getOpenFileNames(filter='*.mp3 *.waw *.flac *.ogg')

                if len(files[0]) != 0:
                    for st in files[0]:
                        resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))
                        resp[list(resp.keys())[self.indActivePlaylist]].append([{"name": st.split('/')[-1], 'url': st}])

                        with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                            f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                        resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))
                        self.playlist[self.indActivePlaylist].append(
                            [list(resp.values())[self.indActivePlaylist][-1][0]['url'],
                             MP3(list(resp.values())[self.indActivePlaylist][-1][0]['url']).info])
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile(st)))
                        self.modelForPlayLists.addMusic([st, MP3(st).info.length])

            elif self.mode == 'Radio':
                #st = [input('Введите название радиостанции: '), input('Введите радиопоток: ')]

                self.dlg = DialogRadio()
                self.dlg.setWindowFlags(Qt.FramelessWindowHint)
                self.dlg.exec()
                st = self.dlg.data

                if len(st) != 0 and st[0] != '' and st[1] != '':
                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))
                    resp[list(resp.keys())[self.indActivePlaylist]].append([{"name": st[0], 'url': st[1]}])

                    with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))
                    self.playlist[self.indActivePlaylist].append([list(resp.values())[self.indActivePlaylist][-1][0]])
                    self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(st[1])))

                    self.modelForPlayLists.addMusic(resp[list(resp.keys())[self.indActivePlaylist]][-1][0])
            elif self.mode == 'Video':
                st = QFileDialog.getOpenFileName(filter='*.avi *.wmv *.mpeg *.mkv')

                if st[0] != '' and st[1] != '':
                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))
                    resp[list(resp.keys())[self.indActivePlaylist]].append([{"name": st[0].split('/')[-1].split('.')[0], 'url': st[0]}])

                    with open('VideoPlaylists/video.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))
                    self.playlist[self.indActivePlaylist].append([list(resp.values())[self.indActivePlaylist][-1][0]])
                    self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(st[0])))

                    self.modelForPlayLists.addMusic(resp[list(resp.keys())[self.indActivePlaylist]][-1])

        except Exception as e:
            print(e)

    def delFile(self):
        try:
            if self.mode == 'Audio':
                if len(self.playlist[self.indActivePlaylist]) > 0 and self.tvPlaylist.currentIndex().row() != -1:
                    ind = self.tvPlaylist.currentIndex().row()
                    self.playlist[self.indActivePlaylist].pop(ind)
                    indTemp = self.myPlaylist.currentIndex()
                    self.myPlaylist.removeMedia(ind)
                    self.modelForPlayLists.delMusic(ind)

                    resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))
                    resp[list(resp.keys())[self.indActivePlaylist]].pop(ind)
                    with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    if ind == indTemp and self.myMedia.state() == QtMultimedia.QMediaPlayer.PlayingState:
                        if ind == 0:
                            Index = self.modelForPlayLists.createIndex(0, 0)
                            self.myPlaylist.setCurrentIndex(0)
                            self.startMusic(Index)
                        else:
                            Index = self.modelForPlayLists.createIndex(ind - 1, 0)
                            self.myPlaylist.setCurrentIndex(ind - 1)
                            self.startMusic(Index)
            elif self.mode == 'Radio':
                if len(self.playlist[self.indActivePlaylist]) > 0 and self.tvPlaylist.currentIndex().row() != -1:
                    ind = self.tvPlaylist.currentIndex().row()
                    indTemp = self.myPlaylist.currentIndex()
                    if ind == indTemp and self.myMedia.state() == QtMultimedia.QMediaPlayer.PlayingState:
                        self.myMedia.stop()
                    self.playlist[self.indActivePlaylist].pop(ind)
                    self.myPlaylist.removeMedia(ind)
                    self.modelForPlayLists.delMusic(ind)

                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))

                    resp[list(resp.keys())[self.indActivePlaylist]].pop(ind)

                    with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))
            elif self.mode == 'Video':
                if len(self.playlist[self.indActivePlaylist]) > 0 and self.tvPlaylist.currentIndex().row() != -1:
                    ind = self.tvPlaylist.currentIndex().row()
                    self.playlist[self.indActivePlaylist].pop(ind)
                    indTemp = self.myPlaylist.currentIndex()
                    self.myPlaylist.removeMedia(ind)
                    self.modelForPlayLists.delMusic(ind)

                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))

                    resp[list(resp.keys())[self.indActivePlaylist]].pop(ind)

                    with open('VideoPlaylists/video.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    if ind == indTemp and self.myMedia.state() == QtMultimedia.QMediaPlayer.PlayingState:
                        if ind == 0:
                            Index = self.modelForPlayLists.createIndex(0, 0)
                            self.myPlaylist.setCurrentIndex(0)
                            self.startMusic(Index)
                        else:
                            Index = self.modelForPlayLists.createIndex(ind - 1, 0)
                            self.myPlaylist.setCurrentIndex(ind - 1)
                            self.startMusic(Index)
        except Exception as e:
            print(e)

    def openWindow(self):
        try:
            if self.framePlaylist.isVisible() and not self.full:
                self.framePlaylist.setVisible(not self.framePlaylist.isVisible())
                self.setMinimumHeight(227)
                self.setGeometry(self.pos().x(), self.pos().y(), 466, 227)
            elif not self.full:
                self.framePlaylist.setVisible(not self.framePlaylist.isVisible())
                self.setMinimumHeight(591)
                self.setGeometry(self.pos().x(), self.pos().y(), 466, 591)
            else:
                self.framePlaylist.setVisible(not self.framePlaylist.isVisible())
                self.showFullScreen()
        except Exception as e:
            print(e)

    def sortPlaylist(self):
        try:
            if len(self.playlist[self.indActivePlaylist]) > 0:
                if self.mode == 'Audio':
                    self.playlist[self.indActivePlaylist] = sorted(self.playlist[self.indActivePlaylist], key=lambda x: x[0])
                    resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))

                    resp[list(resp.keys())[self.indActivePlaylist]] = []
                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        temp.append([x[0], x[1].length])
                        resp[list(resp.keys())[self.indActivePlaylist]].append([{"name": x[0].split('/')[-1], 'url': x[0]}])

                    with open('MusicPlaylists/playlist.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                    self.myMedia.setPlaylist(self.myPlaylist)

                    for x in self.playlist[self.indActivePlaylist]:
                        local = QUrl.fromLocalFile(x[0])
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))

                    self.modelForPlayLists.newData(temp)
                    self.play = False
                    self.myMedia.stop()
                elif self.mode == 'Radio':
                    self.myMedia.stop()
                    self.playlist[self.indActivePlaylist] = sorted(self.playlist[self.indActivePlaylist], key=lambda x: x['name'])
                    resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))

                    resp[list(resp.keys())[self.indActivePlaylist]] = []
                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        temp.append(x)
                        resp[list(resp.keys())[self.indActivePlaylist]].append([{"name": x['name'], 'url': x['url']}])

                    with open('RadioPlaylists/radio.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                    self.myMedia.setPlaylist(self.myPlaylist)

                    for x in self.playlist[self.indActivePlaylist]:
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))

                    self.modelForPlayLists.newData(temp)
                    self.play = False
                elif self.mode == 'Video':
                    self.playlist[self.indActivePlaylist] = sorted(self.playlist[self.indActivePlaylist],
                                                                   key=lambda x: x[0])
                    resp = json.load(open('VideoPlaylists/video.json', 'r', encoding='utf-8'))

                    resp[list(resp.keys())[self.indActivePlaylist]] = []
                    temp = []
                    for x in self.playlist[self.indActivePlaylist]:
                        temp.append([x[0], x[1].length])
                        resp[list(resp.keys())[self.indActivePlaylist]].append(
                            [{"name": x[0].split('/')[-1], 'url': x[0]}])

                    with open('VideoPlaylists/video.json', 'w', encoding='utf-8') as f:
                        f.write(str(json.dumps(resp, ensure_ascii=False, indent=4)))

                    self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)
                    self.myMedia.setPlaylist(self.myPlaylist)

                    for x in self.playlist[self.indActivePlaylist]:
                        local = QUrl.fromLocalFile(x[0])
                        self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))

                    self.modelForPlayLists.newData(temp)
                    self.play = False
                    self.myMedia.stop()

        except Exception as e:
            print(e)

    def findMusic(self):
        try:
            st = self.leFind.text()
            i = 0
            self.indFind = set()
            for x in self.playlist[self.indActivePlaylist]:
                if st in x[0].split('/')[-1]:
                    self.indFind.add(i)
                i += 1
            self.modelForPlayLists.change(self.indFind)
        except Exception as e:
            print(e)

    def closeFind(self):
        try:
            self.leFind.clear()
            self.indFind = set()
            self.modelForPlayLists.change(set())
        except Exception as e:
            print(e)

    def setActiveRadio(self):
        try:
            if self.mode == 'Radio':
                pass
            else:
                self.myMedia.stop()
                if self.mode == 'Video':
                    if self.full:
                        self.fullScreen()
                    self.vw.setVisible(False)
                self.mode = 'Radio'
                self.modelForPlayLists.mode = 'Radio'
                self.playlist = []    # Список всех композиций
                self.indFind = set()  # Список индексов, подходящих под критери композиций
                self.indActivePlaylist = 0
                self.play = False     # Играет ли радио
                self.pause = False    # Стоит ли на паузе
                self.lArtist.setVisible(True)
                self.lTitle.setVisible(True)
                self.bRadioState.setChecked(True)
                self.lTitle.setText('')
                self.lArtist.setText('')
                self.hsMusicSlider.setMinimum(0)
                self.hsMusicSlider.setSliderPosition(0)
                self.hsMusicSlider.setMaximum(1)
                self.modelForPlayLists.activeInd = -1

                # ---------------------------------------------------------------------------------------------------------------

                resp = json.load(open('RadioPlaylists/radio.json', 'r', encoding='utf-8'))  # Загружаем плейлист
                self.playlistMenu.clear()

                self.playlistMenu.addAction('Новый плейлист')
                self.playlistMenu.addSeparator()
                self.playlistMenu.addAction('Удалить плейлист')
                self.playlistMenu.addSeparator()

                for y in resp.items():
                    self.playlist.append([])
                    self.playlistMenu.addAction(y[0])
                    for x in y[1]:
                        self.playlist[self.indActivePlaylist].append(x[0])  # Добавляем в плейлист Путь к файлу,
                    self.indActivePlaylist += 1

                self.indActivePlaylist = 0

                # ---------------------------------------------------------------------------------------------------------------

                self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                self.myMedia.setVolume(50)                                   # Стандартная громкость
                self.myMedia.setPlaylist(self.myPlaylist)                    # Добавляем плейлист в активные

                # ---------------------------------------------------------------------------------------------------------------

                temp = []
                for x in self.playlist[self.indActivePlaylist]:
                    self.myPlaylist.addMedia(QtMultimedia.QMediaContent(QUrl(x['url'])))  # Добавляем композицию в плейлист
                    temp.append([x])                                                        # Сохраняем Название для таблицы

                # ---------------------------------------------------------------------------------------------------------------

                self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                self.modelForPlayLists.newData(temp)

                self.InBegin()  # Переводим трек в начало
        except Exception as e:
            print('Ошибка радио: ' + str(e))

    def setActiveAudio(self):
        try:
            if self.mode == 'Audio':
                pass
            else:
                self.myMedia.stop()
                if self.mode == 'Video':
                    if self.full:
                        self.fullScreen()
                    self.vw.setVisible(False)
                self.mode = 'Audio'
                self.modelForPlayLists.mode = 'Audio'
                self.playlist = []  # Список всех композиций
                self.indFind = set()  # Список индексов, подходящих под критери композиций
                self.indActivePlaylist = 0
                self.play = False  # Играет ли радио
                self.pause = False  # Стоит ли на паузе
                self.lArtist.setVisible(True)
                self.bAudioState.setChecked(True)
                self.lTitle.setVisible(True)
                self.lTitle.setText('')
                self.lArtist.setText('')
                self.hsMusicSlider.setMinimum(0)
                self.hsMusicSlider.setSliderPosition(0)
                self.hsMusicSlider.setMaximum(1)
                self.modelForPlayLists.activeInd = -1

                # ---------------------------------------------------------------------------------------------------------------

                resp = json.load(open('MusicPlaylists/playlist.json', 'r', encoding='utf-8'))  # Загружаем плейлист
                self.playlistMenu.clear()

                self.playlistMenu.addAction('Новый плейлист')
                self.playlistMenu.addSeparator()
                self.playlistMenu.addAction('Удалить плейлист')
                self.playlistMenu.addSeparator()

                for y in resp.items():
                    self.playlist.append([])
                    self.playlistMenu.addAction(y[0])
                    for x in y[1]:
                        if os.path.exists(x[0]['url']):
                            self.playlist[self.indActivePlaylist].append(
                                [x[0]['url'], MP3(x[0]['url']).info])  # Добавляем в плейлист Путь к файлу
                    self.indActivePlaylist += 1

                self.indActivePlaylist = 0

                # ---------------------------------------------------------------------------------------------------------------

                self.myPlaylist = QtMultimedia.QMediaPlaylist(self.myMedia)  # Создаём активный плейлист
                self.myMedia.setVolume(50)  # Стандартная громкость

                # ---------------------------------------------------------------------------------------------------------------

                temp = []

                for x in self.playlist[self.indActivePlaylist]:
                    local = QUrl.fromLocalFile(x[0])  # Переводим глобальный путь в локальный
                    self.myPlaylist.addMedia(QtMultimedia.QMediaContent(local))  # Добавляем композицию в плейлист
                    temp.append([x[0], x[1].length])  # Сохраняем (Название и Длину) для таблицы

                # ---------------------------------------------------------------------------------------------------------------

                self.modelForPlayLists.newData(temp)  # Модель для Таблицы Плейлистов

                self.tvPlaylist.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Размер строк
                self.tvPlaylist.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Размер строк
                self.tvPlaylist.setSelectionBehavior(QAbstractItemView.SelectRows)  # Размер строк

                self.myMedia.setPlaylist(self.myPlaylist)  # Добавляем плейлист в активные

                self.InBegin()  # Переводим трек в начало

        except Exception as e:
            print(e)


app = QApplication(sys.argv)
application = MyWindow()
application.show()
sys.exit(app.exec_())
