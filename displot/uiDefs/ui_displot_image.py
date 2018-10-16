# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './displot_image.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageTabPrototype(object):
    def setupUi(self, ImageTabPrototype):
        ImageTabPrototype.setObjectName("ImageTabPrototype")
        ImageTabPrototype.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageTabPrototype.sizePolicy().hasHeightForWidth())
        ImageTabPrototype.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(ImageTabPrototype)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(ImageTabPrototype)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.imageView = QtWidgets.QGraphicsView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageView.sizePolicy().hasHeightForWidth())
        self.imageView.setSizePolicy(sizePolicy)
        self.imageView.setObjectName("imageView")
        self.sidebar = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setObjectName("sidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebarLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.quickScanButton = QtWidgets.QPushButton(self.sidebar)
        self.quickScanButton.setCheckable(False)
        self.quickScanButton.setChecked(False)
        self.quickScanButton.setObjectName("quickScanButton")
        self.sidebarLayout.addWidget(self.quickScanButton)
        self.toolBox = QtWidgets.QToolBox(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.labelledItems = QtWidgets.QWidget()
        self.labelledItems.setGeometry(QtCore.QRect(0, 0, 270, 330))
        self.labelledItems.setObjectName("labelledItems")
        self.toolBoxLayout = QtWidgets.QHBoxLayout(self.labelledItems)
        self.toolBoxLayout.setContentsMargins(0, 0, 0, 3)
        self.toolBoxLayout.setObjectName("toolBoxLayout")
        self.listItems = QtWidgets.QListView(self.labelledItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.listItems.sizePolicy().hasHeightForWidth())
        self.listItems.setSizePolicy(sizePolicy)
        self.listItems.setObjectName("listItems")
        self.toolBoxLayout.addWidget(self.listItems)
        self.toolBox.addItem(self.labelledItems, "")
        self.sidebarLayout.addWidget(self.toolBox)
        self.dislocationTools = QtWidgets.QWidget(self.sidebar)
        self.dislocationTools.setObjectName("dislocationTools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dislocationTools)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddDisl = QtWidgets.QPushButton(self.dislocationTools)
        self.btnAddDisl.setObjectName("btnAddDisl")
        self.horizontalLayout_2.addWidget(self.btnAddDisl)
        self.btnRemDisl = QtWidgets.QPushButton(self.dislocationTools)
        self.btnRemDisl.setObjectName("btnRemDisl")
        self.horizontalLayout_2.addWidget(self.btnRemDisl)
        self.btnFindDisl = QtWidgets.QPushButton(self.dislocationTools)
        self.btnFindDisl.setObjectName("btnFindDisl")
        self.horizontalLayout_2.addWidget(self.btnFindDisl)
        self.sidebarLayout.addWidget(self.dislocationTools)
        self.label_minimap = QtWidgets.QLabel(self.sidebar)
        self.label_minimap.setObjectName("label_minimap")
        self.sidebarLayout.addWidget(self.label_minimap)
        self.minimap = QtWidgets.QGraphicsView(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.minimap.sizePolicy().hasHeightForWidth())
        self.minimap.setSizePolicy(sizePolicy)
        self.minimap.setBaseSize(QtCore.QSize(200, 200))
        self.minimap.setObjectName("minimap")
        self.sidebarLayout.addWidget(self.minimap)
        self.viewTools = QtWidgets.QWidget(self.sidebar)
        self.viewTools.setObjectName("viewTools")
        self.viewToolsLayout = QtWidgets.QFormLayout(self.viewTools)
        self.viewToolsLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.viewToolsLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.viewToolsLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.viewToolsLayout.setObjectName("viewToolsLayout")
        self.label_zoom = QtWidgets.QLabel(self.viewTools)
        self.label_zoom.setOpenExternalLinks(False)
        self.label_zoom.setObjectName("label_zoom")
        self.viewToolsLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_zoom)
        self.zoomDial = QtWidgets.QSpinBox(self.viewTools)
        self.zoomDial.setMinimum(10)
        self.zoomDial.setMaximum(400)
        self.zoomDial.setProperty("value", 100)
        self.zoomDial.setObjectName("zoomDial")
        self.viewToolsLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zoomDial)
        self.sidebarLayout.addWidget(self.viewTools)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(ImageTabPrototype)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageTabPrototype)

    def retranslateUi(self, ImageTabPrototype):
        _translate = QtCore.QCoreApplication.translate
        ImageTabPrototype.setWindowTitle(_translate("ImageTabPrototype", "Form"))
        self.quickScanButton.setText(_translate("ImageTabPrototype", "Quick Scan"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.labelledItems), _translate("ImageTabPrototype", "Labelled items"))
        self.btnAddDisl.setText(_translate("ImageTabPrototype", "Add"))
        self.btnRemDisl.setText(_translate("ImageTabPrototype", "Rem"))
        self.btnFindDisl.setText(_translate("ImageTabPrototype", "Find"))
        self.label_minimap.setText(_translate("ImageTabPrototype", "Minimap:"))
        self.label_zoom.setText(_translate("ImageTabPrototype", "Zoom:"))
        self.zoomDial.setSuffix(_translate("ImageTabPrototype", "%"))
