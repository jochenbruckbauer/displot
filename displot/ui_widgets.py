# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class DisplotGraphicsView(QtWidgets.QGraphicsView):

    @property
    def imageTab(self):
        return self._imageTab

    @imageTab.setter
    def imageTab(self, obj):
        if not isinstance(obj, QtWidgets.QWidget):
            raise TypeError('Value needs to be an instance of QtWidgets.QWidget')
        self._imageTab = obj

    def drawOverlayRect(self, handle, x, y, w, h, scene_w=None, scene_h=None,
    pen=None):
        """Draws a rectangle with the specified properties onto the scene
        currently attached to the QGraphicsView.

        This function ensures that the drawn rectangle will never be out of
        existing bounds of the graphics scene, and therefore will never resize
        the graphics scene unnecessarily. The function instead draws the
        rectangle at the nearest valid coordinates.

        Args:
            handle (QGraphicsRectItem): The rectangle Qt handle. If set to None,
                the function will create and return a new Qt handle for the
                rectangle.
            x (int): X coordinate of the top-left origin of the rectangle.
            y (int): Y coordinate of the top-left origin of the rectangle.
            w (int): Desired width of the rectangle.
            h (int): Desired height of the rectangle.
            scene_w (int): Desired width of the scene. If set to None, the
                function will check the current scene size automatically.
            scene_h (int): Desired height of the scene. If set to None, the
                function will check the current scene size automatically.
            pen (QPen): The pen used to draw the rectangle.

        Returns:
            QGraphicsRectItem: The rectangle.
        """

        scene = self.scene()

        if scene_w == None:
            scene_w = scene.width()
        if scene_h == None:
            scene_h = scene.height()

        # check and set drawing bounds to avoid stretching the scene
        if (x + w) > scene_w:
            x = scene_w - w
        if (y + h) > scene_h:
            y = scene_h - h
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if w > scene_w:
            w = scene_w
        if h > scene_h:
            h = scene_h

        # this is to avoid annoying 1px stretches at the w/h boundary
        w -= 1
        h -= 1

        if handle == None:
            handle = scene.addRect(x, y, w, h, pen);
        else:
            handle.setRect(x, y, w, h)

        return handle


class WorkImageView(DisplotGraphicsView):
    """A QGraphicsView object responsible for the main image view of the program.

    Note that it is tightly coupled to its parent QWidget object for reasons
    of UI interaction, but the assignment of its parent object reference cannot
    happen in the layout definition portion of this program.

    Attributes:
        imageTab: an object reference to the tab containing the graphics view.
        zoomLevel: a float value indicating the current zoom level of the scene.
    """

    MODE_NORMAL = 0
    MODE_REGION_NEW = 1
    MODE_REGION_MOVE = 2

    clickedRegionNew = QtCore.pyqtSignal(int, int, name='clickedRegionNew')
    clickedRegionMove = QtCore.pyqtSignal(int, int, name='clickedRegionMove')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mouseMode = self.MODE_NORMAL
        self.mouseGraphicsItem = None
        self.zoomLevel = 1

        self._labelX = None
        self._labelY = None

        self._regionNewHandle = None
        self._regionMoveHandle = None
        self.regionNewPen = None
        self.regionMovePen = None

        self.setMouseTracking(True)

    def setMouseMode(self, mode):
        """Sets the mouse mode for the main graphics view.

        Depending on the mouse mode the cursor will behave differently when
        interacting with the WorkImageView. The act of setting the mouse mode
        will also clean up any entities remaining from the previous mouse mode.

        Args:
            mode (int): The mode setting. Supported modes can be seen in the
                constants list of this class.

        """
        if self._regionNewHandle != None:
            self.scene().removeItem(self._regionNewHandle)
            self._regionNewHandle = None

        if self._regionMoveHandle != None:
            self.scene().removeItem(self._regionMoveHandle)
            self._regionMoveHandle = None

        self.mouseMode = mode

    def mouseCoords(self, x, y):
        rect = self.getVisibleRect()
        return (int(rect.x()+x), int(rect.y()+y))

    def initEvents(self):
        """Initialises some UI events. Run this after the image has been loaded."""
        self._zoomDial = self.imageTab.findChild(QtWidgets.QSpinBox, "zoomDial")
        self._zoomDial.valueChanged.connect(self._zoomEv)
        self._labelX = self.imageTab.findChild(QtWidgets.QLabel, "imageCurX")
        self._labelY = self.imageTab.findChild(QtWidgets.QLabel, "imageCurY")

    def getVisibleRect(self):
        return self.mapToScene(self.viewport().geometry()).boundingRect()

    def zoom(self, scale):
        """Zooms the scene according to the passed scale multiplier (float)."""
        self.scale(1 / self.zoomLevel, 1 / self.zoomLevel)
        self.scale(scale, scale)
        self.zoomLevel = scale

    def _zoomEv(self):
        self.zoom(int(self._zoomDial.cleanText()) / 100)
        self.imageTab._minimapView.drawViewbox()

    def mousePressEvent(self, e):
        m_x, m_y = self.mouseCoords(e.x(), e.y())

        if self.mouseMode == self.MODE_REGION_NEW:
            self.clickedRegionNew.emit(m_x, m_y)
            self.setMouseMode(self.MODE_NORMAL)

        if self.mouseMode == self.MODE_REGION_MOVE:
            self.clickedRegionMove.emit(m_x, m_y)
            self.setMouseMode(self.MODE_NORMAL)

    def mouseMoveEvent(self, e):
        m_x, m_y = self.mouseCoords(e.x(), e.y())

        # show current mouse position relative to the scene
        self._labelX.setText('x:'+str(m_x))
        self._labelY.setText('y:'+str(m_y))

        psize = self.imageTab._lastPatchSize
        bg_pixmap = self.imageTab._imageScenePixmap
        if bg_pixmap == None:
            max_w = None
            max_h = None
        else:
            max_w = bg_pixmap.boundingRect().width()
            max_h = bg_pixmap.boundingRect().height()

        if self.mouseMode == self.MODE_REGION_NEW:
            self._regionNewHandle = self.drawOverlayRect(self._regionNewHandle,
                m_x, m_y, psize, psize, max_w, max_h, self.regionNewPen)

        if self.mouseMode == self.MODE_REGION_MOVE:
            self._regionMoveHandle = self.drawOverlayRect(self._regionMoveHandle,
                m_x, m_y, psize, psize, max_w, max_h, self.regionMovePen)

    def resizeEvent(self, e):
        if self.imageTab.opened == True:
            self.imageTab._minimapView.drawViewbox()

    def scrollContentsBy(self, dx, dy):
        super().scrollContentsBy(dx, dy)
        self.imageTab._minimapView.drawViewbox()


class MinimapView(DisplotGraphicsView):
    """A QGraphicsView object responsible for displaying the loaded image minimap.

    Note that it is tightly coupled to its parent QWidget object for reasons
    of UI interaction, but the assignment of its parent object reference cannot
    happen in the layout definition portion of this program.

    Attributes:
        imageTab: an object reference to the tab containing the graphics view.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mmPen = QtGui.QPen(QtGui.QColor.fromRgb(0,255,0))
        self._mmBox = None

    def getMinimapRatio(self):
        """Returns a single float representing the ideal scaling ratio for the
        minimap pixmap with regards to the full sized image. Will always return
        the smallest ratio if aspect is not preserved.
        """
        imh = self.imageTab._qImage

        w_ratio = self.rect().width() / imh.width()
        h_ratio = self.rect().height() / imh.height()
        if w_ratio > h_ratio:
            return h_ratio
        else:
            return w_ratio

    def getImageRatio(self):
        """Returns a tuple containing the horizontal and vertical scaling ratios
        of the minimap scene view with regards to the full sized image.

        Generally both scaling ratios should be the same, but if aspect ratio
        was not preserved for some reason then they won't be.
        """
        return self.transform().m11(), self.transform().m22()

    def drawViewbox(self):
        """Draws the rectangle representing the current visible area on the
        minimap.
        """
        imv = self.imageTab._imageView
        viewport_box = imv.mapToScene(imv.viewport().rect()).boundingRect()
        bg_pixmap = self.imageTab._minimapScenePixmap.boundingRect()

        ratio = self.getMinimapRatio()
        max_w = bg_pixmap.width() * ratio
        max_h = bg_pixmap.height() * ratio
        box_w = viewport_box.width() * ratio
        box_h = viewport_box.height() * ratio
        box_x = viewport_box.x() * ratio
        box_y = viewport_box.y() * ratio

        self._mmBox = self.drawOverlayRect(self._mmBox,
            box_x, box_y, box_w, box_h, max_w, max_h, self._mmPen)

    def _drawViewboxEv(self, e):
        """Method to handle minimap mouse events before centering the viewport
        and passing the overlay draw calls.
        """
        imv = self.imageTab._imageView
        viewport_box = imv.mapToScene(imv.viewport().rect()).boundingRect()
        bg_pixmap = self.imageTab._imageScenePixmap.boundingRect()
        ratio = 1 / self.getMinimapRatio()

        #x = (e.x() * ratio) - (viewport_box.width() / 2)
        x = e.x() * ratio
        y = e.y() * ratio

        min_x = viewport_box.width() / 2
        min_y = viewport_box.height() / 2
        max_x = bg_pixmap.width() - min_x
        max_y = bg_pixmap.height() - min_y
        if x < min_x:
            x = min_x
        if x > max_x:
            x = max_x
        if y < min_y:
            y = min_y
        if y > max_y:
            y = max_y

        imv.centerOn(x, y)
        self.drawViewbox()

    def mousePressEvent(self, e):
        self._drawViewboxEv(e)

    def mouseMoveEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            self._drawViewboxEv(e)


class ImageTabList(QtWidgets.QTableView):
    """Custom TableView implementation for the dislocation list on each image tab.

    Attributes:
        model (:obj:`ImageTabListModel`): The data model contained within the
            ImageTabList table.

    """

    modelDataChanged = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._imageTab = None
        self.model = None

        self.setData([])

    @property
    def imageTab(self):
        return self._imageTab

    @imageTab.setter
    def imageTab(self, obj):
        if not isinstance(obj, QtWidgets.QWidget):
            raise TypeError('Value needs to be an instance of QtWidgets.QWidget')
        self._imageTab = obj

    def setData(self, data):
        """Constructs a model object and passes the argument data to it.

        Calling this method will automatically populate the table with the data
        list passed to it.

        Args:
            mode (list): A list of ImageTabRegion objects.

        """
        self.model = ImageTabListModel(data, self)
        self.model.dataChanged.connect(lambda: self.modelDataChanged.emit())
        self.setModel(self.model)
        self.resetView()
        self.setItemDelegateForColumn(2, ImageTabListFragColour(self))
        self.setItemDelegateForColumn(3, ImageTabListFragVisibility(self))
        self.setItemDelegateForColumn(4, ImageTabListCheckBox(self))

    def resetView(self):
        """Resets the table column width and adjusts header settings.

        """
        hheader = self.horizontalHeader()
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.resizeRowsToContents()

        self.setColumnWidth(0, 70)
        self.setColumnWidth(1, 70)
        self.setColumnWidth(2, 30)
        self.setColumnWidth(3, 30)
        self.setColumnWidth(4, 30)

    def selectedItems(self):
        ind = self.selectedIndexes()
        if len(ind) > 0:
            return self.model.getDataObject(ind[0].row())
        return None

    def selectionChanged(self, selected, deselected):
        if not self._imageTab is None:
            self._imageTab._cntrFragBtn
            self._imageTab.unhighlightAllFragments()
            sel = self.selectedItems()
            if not sel is None:
                if self._imageTab._cntrFragBtn.isChecked() == True:
                    sel.centerOn()
                sel.highlight()

        super().selectionChanged(selected, deselected)


class ImageTabListModel(QtCore.QAbstractTableModel):
    """Data model for the dislocation list.

    Used to prepare and display data within the QTableView it is attached to.
    Note that this class accepts a list of objects (ImageTabRegion like) as its
    data input. Note that even though lists and objects are mutable in Python,
    it's not guaranteed that data changes imposed on the model will be reflected
    on the data list originally passed to the model. Changes to individual objects
    generally will be, while additions of new objects will not without explicit
    handling.

    See http://doc.qt.io/qt-5/qabstractitemmodel.html for a detailed description
    of reimplemented functions.

    Attributes:
        modelData (list): The data model contained within the
            ImageTabList table.
        modelIndices (list): List of string values describing each individual row.
            At present it's just a integer based ID.

    """

    def __init__(self, input, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.modelData = input
        self.modelIndices = list(map(str, range(1, len(self.modelData) + 1)))
        self.headers = ['Pos:X', 'Pos:Y', 'c', 'v', 's']
        self._addQueue = []

    def getDataObject(self, row):
        if row >= len(self.modelData):
            return None
        return self.modelData[row]

    def getDataObjectRow(self, obj):
        try:
            return self.modelData.index(obj)
        except ValueError:
            return None

    def getCheckedDataObjects(self):
        ret = []
        for obj in self.modelData:
            if obj.isSelected == False:
                continue
            ret.append(obj)
        return ret

    def addDataObject(self, obj):
        self._addQueue.append(obj)

    def notifyDataChanged(self, row=None):
        self.dataChanged.emit(
            self.createIndex(row, 0),
            self.createIndex(row, 4),
            [QtCore.Qt.DisplayRole]
        )

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.modelData)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            return self.headers[section]
        elif orientation == QtCore.Qt.Vertical:
            return self.modelIndices[section]

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()

        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return QtCore.QVariant(self.modelData[index.row()].midpoint[0])
            if index.column() == 1:
                return QtCore.QVariant(self.modelData[index.row()].midpoint[1])
            if index.column() == 2:
                #value = self.modelData[index.row()]
                return QtCore.QVariant()
                #return QtCore.QVariant(self.modelData[index.row()].isHidden)

        if role == QtCore.Qt.DecorationRole:
            if index.column() == 3:
                if self.modelData[index.row()].isHidden == True:
                    return True
                else:
                    return False

        if role == QtCore.Qt.CheckStateRole:
            if index.column() == 4:
                if self.modelData[index.row()].isSelected == True:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked

        return QtCore.QVariant()

    def setData(self, index, value, role):
        if not index.isValid():
            return False

        if role == QtCore.Qt.EditRole:
            if index.column() < 2:
                try:
                    value = int(value)
                except ValueError:
                    return False

            if index.column() == 0:
                self.modelData[index.row()].moveMidpoint(x=value)
                self.modelData[index.row()].updateUi()
            if index.column() == 1:
                self.modelData[index.row()].moveMidpoint(y=value)
                self.modelData[index.row()].updateUi()

        if role == QtCore.Qt.DecorationRole and index.column() == 3:
            if value == True:
                self.modelData[index.row()].isHidden = True
            else:
                self.modelData[index.row()].isHidden = False

        if role == QtCore.Qt.CheckStateRole and index.column() == 4:
            if value == QtCore.Qt.Checked:
                self.modelData[index.row()].isSelected = True
            else:
                self.modelData[index.row()].isSelected = False

        self.dataChanged.emit(index, index, [role])
        return super().setData(index, value, role)

    def insertRows(self, row, count, parent=QtCore.QModelIndex()):
        if count != len(self._addQueue):
            return False

        row_last = row + count - 1
        row_nextindex = len(self.modelIndices) + 1

        self.beginInsertRows(parent, row, row_last)
        self.modelData[row:row] = self._addQueue
        self.modelIndices[row:row] = list(map(str, range(row_nextindex, row_nextindex + count)))
        self._addQueue = []
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        row_last = row + count

        self.beginRemoveRows(parent, row, row_last)
        del self.modelData[row:row_last]
        del self.modelIndices[row:row_last]
        self.endRemoveRows()
        return True

    def flags(self, index):
        if index.column() == 3:
            return QtCore.Qt.ItemIsEnabled
        if index.column() == 4:
            return QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsEditable | super().flags(index)


class ImageTabListFragColour(QtWidgets.QStyledItemDelegate):
    pass


class ImageTabListFragVisibility(QtWidgets.QItemDelegate):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(
            QtGui.QPixmap(":/feathericons/vendor/feather/icons/eye-off.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On
        )
        self.icon.addPixmap(
            QtGui.QPixmap(":/feathericons/vendor/feather/icons/eye.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        self.iconSize = 20

    def paint(self, painter, option, index):
        painter.save()

        if index.data(QtCore.Qt.DecorationRole) == True:
            state = QtGui.QIcon.On
        else:
            state = QtGui.QIcon.Off

        pixmap = self.icon.pixmap(self.iconSize, self.iconSize, QtGui.QIcon.Normal, state)
        xy = (option.rect.x() + (option.rect.width() / 2) - (self.iconSize / 2), option.rect.y())
        painter.drawPixmap(xy[0], xy[1], pixmap)
        super().drawFocus(painter, option, option.rect)

        painter.restore()
        super().paint(painter, option, index)

    def editorEvent(self, event, model, option, index):
        if index.data(QtCore.Qt.DecorationRole) == True:
            state = False
        else:
            state = True

        if event.type() == QtCore.QEvent.MouseButtonRelease:
            return model.setData(index, state, QtCore.Qt.DecorationRole)
        else:
            return False


class ImageTabListCheckBox(QtWidgets.QItemDelegate):

    def paint(self, painter, option, index):
        if index.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked

        super().drawCheck(painter, option, option.rect, state)
        super().drawFocus(painter, option, option.rect)
        super().paint(painter, option, index)

    def editorEvent(self, event, model, option, index):
        if index.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
            state = QtCore.Qt.Unchecked
        else:
            state = QtCore.Qt.Checked

        if event.type() == QtCore.QEvent.MouseButtonRelease:
            return model.setData(index, state, QtCore.Qt.CheckStateRole)
        else:
            return False
