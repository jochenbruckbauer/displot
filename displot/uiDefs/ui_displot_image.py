# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './displot_image.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
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
        self.verticalLayout = QtWidgets.QVBoxLayout(ImageTabPrototype)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(ImageTabPrototype)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(1)
        self.splitter.setMidLineWidth(3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.imageView = WorkImageView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageView.sizePolicy().hasHeightForWidth())
        self.imageView.setSizePolicy(sizePolicy)
        self.imageView.setMinimumSize(QtCore.QSize(400, 400))
        self.imageView.setObjectName("imageView")
        self.sidebar = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QtCore.QSize(300, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(300, 16777215))
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
        self.labelledItems.setGeometry(QtCore.QRect(0, 0, 282, 227))
        self.labelledItems.setObjectName("labelledItems")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.labelledItems)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listItems = QtWidgets.QTableView(self.labelledItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.listItems.sizePolicy().hasHeightForWidth())
        self.listItems.setSizePolicy(sizePolicy)
        self.listItems.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listItems.setSortingEnabled(True)
        self.listItems.setObjectName("listItems")
        self.verticalLayout_2.addWidget(self.listItems)
        self.dislocationTools = QtWidgets.QWidget(self.labelledItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dislocationTools.sizePolicy().hasHeightForWidth())
        self.dislocationTools.setSizePolicy(sizePolicy)
        self.dislocationTools.setObjectName("dislocationTools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dislocationTools)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_2.addWidget(self.dislocationTools)
        self.toolBox.addItem(self.labelledItems, "")
        self.imageTools = QtWidgets.QWidget()
        self.imageTools.setGeometry(QtCore.QRect(0, 0, 282, 227))
        self.imageTools.setObjectName("imageTools")
        self.toolBox.addItem(self.imageTools, "")
        self.actions = QtWidgets.QWidget()
        self.actions.setGeometry(QtCore.QRect(0, 0, 282, 227))
        self.actions.setObjectName("actions")
        self.toolBox.addItem(self.actions, "")
        self.sidebarLayout.addWidget(self.toolBox)
        self.label_minimap = QtWidgets.QLabel(self.sidebar)
        self.label_minimap.setObjectName("label_minimap")
        self.sidebarLayout.addWidget(self.label_minimap)
        self.minimap = MinimapView(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.minimap.sizePolicy().hasHeightForWidth())
        self.minimap.setSizePolicy(sizePolicy)
        self.minimap.setMinimumSize(QtCore.QSize(150, 200))
        self.minimap.setMaximumSize(QtCore.QSize(300, 200))
        self.minimap.setBaseSize(QtCore.QSize(0, 0))
        self.minimap.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.minimap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minimap.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
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
        self.verticalLayout.addWidget(self.splitter)
        self.imageInfo = QtWidgets.QWidget(ImageTabPrototype)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageInfo.sizePolicy().hasHeightForWidth())
        self.imageInfo.setSizePolicy(sizePolicy)
        self.imageInfo.setObjectName("imageInfo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.imageInfo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageInfoLabel = QtWidgets.QLabel(self.imageInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageInfoLabel.sizePolicy().hasHeightForWidth())
        self.imageInfoLabel.setSizePolicy(sizePolicy)
        self.imageInfoLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.imageInfoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageInfoLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageInfoLabel.setObjectName("imageInfoLabel")
        self.horizontalLayout.addWidget(self.imageInfoLabel)
        self.verticalLayout.addWidget(self.imageInfo)

        self.retranslateUi(ImageTabPrototype)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageTabPrototype)

    def retranslateUi(self, ImageTabPrototype):
        _translate = QtCore.QCoreApplication.translate
        ImageTabPrototype.setWindowTitle(_translate("ImageTabPrototype", "Form"))
        self.quickScanButton.setText(_translate("ImageTabPrototype", "Quick Scan"))
        self.btnAddDisl.setText(_translate("ImageTabPrototype", "Add"))
        self.btnRemDisl.setText(_translate("ImageTabPrototype", "Rem"))
        self.btnFindDisl.setText(_translate("ImageTabPrototype", "Find"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.labelledItems), _translate("ImageTabPrototype", "Labelled items"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.imageTools), _translate("ImageTabPrototype", "Image tools"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.actions), _translate("ImageTabPrototype", "Actions"))
        self.label_minimap.setText(_translate("ImageTabPrototype", "Minimap:"))
        self.label_zoom.setText(_translate("ImageTabPrototype", "Zoom:"))
        self.zoomDial.setSuffix(_translate("ImageTabPrototype", "%"))
        self.imageInfoLabel.setText(_translate("ImageTabPrototype", "No image loaded"))

from ui_tabwidgets import MinimapView, WorkImageView
