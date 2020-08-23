from PyQt5 import QtMultimedia, QtWidgets, QtCore
from PyQt5.Qt import QBrush, QAbstractTableModel, QSize, QFont, QColor, QPixmap, QSizePolicy, QIcon, QImage, \
    QAbstractListModel, QMimeData, Qt, QStyledItemDelegate, QPushButton, QSlider, QApplication, QStyle, QStyleOptionButton
import datetime


class ModelForPlaylist(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self, None)
        self.playlist = data
        self.activeInd = -1
        self.mode = 'Audio'
        self.changed = set()
        self.horizontalHeaderOfTable = ['', '', '']

    def rowCount(self, parent=None, *args, **kwargs):
        try:
            return len(self.playlist)
        except Exception as e:
            print('Ошибка модели:', e)

    def columnCount(self, parent=None, *args, **kwargs):
        try:
            if self.mode == 'Audio':
                return len(self.horizontalHeaderOfTable)
            elif self.mode == 'Radio' or self.mode == 'Video':
                return len(self.horizontalHeaderOfTable) - 1
        except Exception as e:
            print('Ошибка модели:', e)

    def addMusic(self, data):
        self.beginResetModel()
        self.playlist.append(data)
        self.endResetModel()

    def delMusic(self, ind):
        self.beginResetModel()
        self.playlist.pop(ind)
        self.endResetModel()

    def newData(self, data):
        try:
            self.beginResetModel()
            self.playlist = data
            self.endResetModel()
        except Exception as e:
            print('Ошибка модели:', e)

    def active(self, ind):
        self.beginResetModel()
        self.activeInd = ind
        self.endResetModel()

    def change(self, data):
        self.beginResetModel()
        self.changed = data
        self.endResetModel()

    def data(self, index, role=None):
        try:
            row = index.row()
            column = index.column()
            if self.mode == 'Audio':
                if role == Qt.DisplayRole:
                    if column == 0:
                        return str(row + 1)
                    elif column == 1:
                        return self.playlist[row][0].split('/')[-1].split('.')[0]
                    elif column == 2:
                        return str(datetime.timedelta(minutes=int(self.playlist[row][1])))[:-3]
                elif role == Qt.TextAlignmentRole:
                    if column == 1:
                        return Qt.AlignVCenter | Qt.AlignLeft
                    elif column == 0:
                        return Qt.AlignVCenter | Qt.AlignCenter
                elif role == Qt.TextColorRole:
                    if row == self.activeInd:
                        return QBrush(QColor(222, 142, 55))
                    if row in self.changed:
                        return QBrush(QColor(222, 142, 55))
                    else:
                        return QBrush(QColor(255, 255, 255))
                elif role == Qt.BackgroundColorRole:
                    if row in self.changed:
                        return QBrush(QColor(200, 220, 200))
                elif role == Qt.FontRole:
                    f = QFont()
                    f.setPointSize(11)
                    f.setWeight(QFont.Bold)
                    return f
            elif self.mode == 'Radio' or self.mode == 'Video':
                if role == Qt.DisplayRole:
                    if column == 0:
                        return str(row + 1)
                    elif column == 1:
                        return self.playlist[row][0]['name']
                elif role == Qt.TextAlignmentRole:
                    if column == 1:
                        return Qt.AlignVCenter | Qt.AlignLeft
                    elif column == 0:
                        return Qt.AlignVCenter | Qt.AlignCenter
                elif role == Qt.TextColorRole:
                    if row == self.activeInd:
                        return QBrush(QColor(222, 142, 55))
                    else:
                        return QBrush(QColor(255, 255, 255))
                elif role == Qt.FontRole:
                    f = QFont()
                    f.setPointSize(11)
                    f.setWeight(QFont.Bold)
                    return f
        except Exception as e:
            print('Ошибка модели:', e)

    def headerData(self, p_int, Qt_Orientation, role=None):
        try:
            if role == Qt.DisplayRole:
                if Qt_Orientation == Qt.Horizontal:
                    return self.horizontalHeaderOfTable[p_int]
            return None
        except Exception as e:
            print('Ошибка модели:', e)

    def flags(self, index):
        try:
            if index.column() == 3:
                return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        except Exception as e:
            print('Ошибка модели:', e)

    '''def insertRows(self, position, rows):
        try:
            print(9)
            self.beginResetModel()
            self.beginInsertRows(self.createIndex(0, 0), position, position + rows - 1)

            for row in range(rows):
                self.playlist.insert(position, self.playlist[position])

            self.endInsertRows()
            self.endResetModel()
        except Exception as e:
            print(e)

    def removeRows(self, position, rows,):
        try:
            print(10)
            self.beginResetModel()
            self.beginInsertRows(self.createIndex(0, 0), position, position + rows - 1)

            for row in range(rows):
                self.playlist.removeAt(position)
            self.endRemoveRows()
            self.endResetModel()
        except Exception as e:
            print(e)

    def supportedDropActions(self):
        try:
            return Qt.MoveAction | Qt.CopyAction
        except Exception as e:
            print(e)

    def dropMimeData(self, *data, action, row, column, parent):
         try:
             print(1)
             if action == Qt.IgnoreAction:
                 return True
             if column > 2:
                 return False
             if row != -1:
                 beginRow = row
             elif parent.isValid():
                 beginRow = parent.row()
             else:
                 beginRow = self.rowCount(self.createIndex(0, 0))
             return beginRow
         except Exception as e:
             print(e)'''


class PlaylistDelegate(QStyledItemDelegate):

    def createEditor(self, parent, QStyleOptionViewItem, QModelIndex):
        editor = QPushButton(parent)

        editor.setText('sd')

        print(1)
        editor.clicked.connect(self.asd)
        return editor

    def asd(self):
        print('Нажал')

    def updateEditorGeometry(self, editor, option, index):
        buttonStyle = QStyleOptionButton()
        button_rect = QApplication.style().subElementRect(QStyle.SE_PushButtonContents, buttonStyle)
        buttonStyle.rect = option.rect
        editor.setGeometry(buttonStyle.rect)

    def paint(self, painter, option, index):
        try:
            print(12)
            buttonStyle = QStyleOptionButton()
            button_rect = QApplication.style().subElementRect(QStyle.SE_PushButtonContents, buttonStyle)
            buttonStyle.rect = option.rect
            #buttonStyle.state = QStyle.State_Enabled | QStyle.State_On

            QApplication.style().drawControl(QStyle.CE_PushButton, buttonStyle, painter)
        except Exception as e:
            print(e)
