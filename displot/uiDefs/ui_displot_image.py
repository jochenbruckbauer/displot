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
        self.toolBox = QtWidgets.QToolBox(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.imageTools = QtWidgets.QWidget()
        self.imageTools.setGeometry(QtCore.QRect(0, 0, 282, 291))
        self.imageTools.setObjectName("imageTools")
        self.imageToolsLayout_2 = QtWidgets.QVBoxLayout(self.imageTools)
        self.imageToolsLayout_2.setContentsMargins(3, 3, 3, 3)
        self.imageToolsLayout_2.setObjectName("imageToolsLayout_2")
        self.button_Scan = QtWidgets.QPushButton(self.imageTools)
        self.button_Scan.setFlat(False)
        self.button_Scan.setObjectName("button_Scan")
        self.imageToolsLayout_2.addWidget(self.button_Scan)
        self.imageToolsScroll = QtWidgets.QScrollArea(self.imageTools)
        self.imageToolsScroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageToolsScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageToolsScroll.setLineWidth(1)
        self.imageToolsScroll.setMidLineWidth(0)
        self.imageToolsScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imageToolsScroll.setWidgetResizable(True)
        self.imageToolsScroll.setObjectName("imageToolsScroll")
        self.imageToolsScrollArea = QtWidgets.QWidget()
        self.imageToolsScrollArea.setGeometry(QtCore.QRect(0, 0, 260, 471))
        self.imageToolsScrollArea.setObjectName("imageToolsScrollArea")
        self.imageToolsLayout = QtWidgets.QVBoxLayout(self.imageToolsScrollArea)
        self.imageToolsLayout.setContentsMargins(3, 3, 3, 3)
        self.imageToolsLayout.setObjectName("imageToolsLayout")
        self.label_step1 = QtWidgets.QLabel(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_step1.sizePolicy().hasHeightForWidth())
        self.label_step1.setSizePolicy(sizePolicy)
        self.label_step1.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_step1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_step1.setObjectName("label_step1")
        self.imageToolsLayout.addWidget(self.label_step1)
        self.layout_step1 = QtWidgets.QWidget(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout_step1.sizePolicy().hasHeightForWidth())
        self.layout_step1.setSizePolicy(sizePolicy)
        self.layout_step1.setObjectName("layout_step1")
        self.gridLayout = QtWidgets.QGridLayout(self.layout_step1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_GaussianSigma = QtWidgets.QLabel(self.layout_step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_GaussianSigma.sizePolicy().hasHeightForWidth())
        self.label_GaussianSigma.setSizePolicy(sizePolicy)
        self.label_GaussianSigma.setWordWrap(True)
        self.label_GaussianSigma.setObjectName("label_GaussianSigma")
        self.gridLayout.addWidget(self.label_GaussianSigma, 0, 0, 1, 1)
        self.value_GaussianSigma = QtWidgets.QDoubleSpinBox(self.layout_step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_GaussianSigma.sizePolicy().hasHeightForWidth())
        self.value_GaussianSigma.setSizePolicy(sizePolicy)
        self.value_GaussianSigma.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_GaussianSigma.setFrame(True)
        self.value_GaussianSigma.setMaximum(10.0)
        self.value_GaussianSigma.setSingleStep(0.01)
        self.value_GaussianSigma.setProperty("value", 1.6)
        self.value_GaussianSigma.setObjectName("value_GaussianSigma")
        self.gridLayout.addWidget(self.value_GaussianSigma, 0, 1, 1, 1)
        self.imageToolsLayout.addWidget(self.layout_step1, 0, QtCore.Qt.AlignTop)
        self.label_step2 = QtWidgets.QLabel(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_step2.sizePolicy().hasHeightForWidth())
        self.label_step2.setSizePolicy(sizePolicy)
        self.label_step2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_step2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_step2.setObjectName("label_step2")
        self.imageToolsLayout.addWidget(self.label_step2)
        self.layout_step2 = QtWidgets.QWidget(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout_step2.sizePolicy().hasHeightForWidth())
        self.layout_step2.setSizePolicy(sizePolicy)
        self.layout_step2.setObjectName("layout_step2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layout_step2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.value_DiscardMargins = QtWidgets.QSpinBox(self.layout_step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_DiscardMargins.sizePolicy().hasHeightForWidth())
        self.value_DiscardMargins.setSizePolicy(sizePolicy)
        self.value_DiscardMargins.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_DiscardMargins.setMaximum(1000)
        self.value_DiscardMargins.setProperty("value", 5)
        self.value_DiscardMargins.setObjectName("value_DiscardMargins")
        self.gridLayout_2.addWidget(self.value_DiscardMargins, 2, 2, 1, 1)
        self.label_DiscardMargins = QtWidgets.QLabel(self.layout_step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DiscardMargins.sizePolicy().hasHeightForWidth())
        self.label_DiscardMargins.setSizePolicy(sizePolicy)
        self.label_DiscardMargins.setWordWrap(True)
        self.label_DiscardMargins.setObjectName("label_DiscardMargins")
        self.gridLayout_2.addWidget(self.label_DiscardMargins, 2, 0, 1, 2)
        self.value_DiscardLabels = QtWidgets.QSpinBox(self.layout_step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_DiscardLabels.sizePolicy().hasHeightForWidth())
        self.value_DiscardLabels.setSizePolicy(sizePolicy)
        self.value_DiscardLabels.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_DiscardLabels.setMaximum(1000)
        self.value_DiscardLabels.setProperty("value", 8)
        self.value_DiscardLabels.setObjectName("value_DiscardLabels")
        self.gridLayout_2.addWidget(self.value_DiscardLabels, 0, 2, 1, 1)
        self.label_DiscardLabels = QtWidgets.QLabel(self.layout_step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DiscardLabels.sizePolicy().hasHeightForWidth())
        self.label_DiscardLabels.setSizePolicy(sizePolicy)
        self.label_DiscardLabels.setWordWrap(True)
        self.label_DiscardLabels.setObjectName("label_DiscardLabels")
        self.gridLayout_2.addWidget(self.label_DiscardLabels, 0, 0, 1, 2)
        self.imageToolsLayout.addWidget(self.layout_step2, 0, QtCore.Qt.AlignTop)
        self.label_step3 = QtWidgets.QLabel(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_step3.sizePolicy().hasHeightForWidth())
        self.label_step3.setSizePolicy(sizePolicy)
        self.label_step3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_step3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_step3.setObjectName("label_step3")
        self.imageToolsLayout.addWidget(self.label_step3)
        self.layout_step3 = QtWidgets.QWidget(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout_step3.sizePolicy().hasHeightForWidth())
        self.layout_step3.setSizePolicy(sizePolicy)
        self.layout_step3.setObjectName("layout_step3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layout_step3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_CorrelationTolerance = QtWidgets.QLabel(self.layout_step3)
        self.label_CorrelationTolerance.setToolTip("")
        self.label_CorrelationTolerance.setWordWrap(True)
        self.label_CorrelationTolerance.setObjectName("label_CorrelationTolerance")
        self.gridLayout_3.addWidget(self.label_CorrelationTolerance, 4, 0, 1, 3)
        self.label_DissimilarityTarget = QtWidgets.QLabel(self.layout_step3)
        self.label_DissimilarityTarget.setWordWrap(True)
        self.label_DissimilarityTarget.setObjectName("label_DissimilarityTarget")
        self.gridLayout_3.addWidget(self.label_DissimilarityTarget, 5, 0, 1, 3)
        self.label_DissimilarityTolerance = QtWidgets.QLabel(self.layout_step3)
        self.label_DissimilarityTolerance.setWordWrap(True)
        self.label_DissimilarityTolerance.setObjectName("label_DissimilarityTolerance")
        self.gridLayout_3.addWidget(self.label_DissimilarityTolerance, 6, 0, 1, 3)
        self.label_CorrelationTarget = QtWidgets.QLabel(self.layout_step3)
        self.label_CorrelationTarget.setWordWrap(True)
        self.label_CorrelationTarget.setObjectName("label_CorrelationTarget")
        self.gridLayout_3.addWidget(self.label_CorrelationTarget, 2, 0, 1, 3)
        self.value_DissimilarityTolerance = QtWidgets.QDoubleSpinBox(self.layout_step3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_DissimilarityTolerance.sizePolicy().hasHeightForWidth())
        self.value_DissimilarityTolerance.setSizePolicy(sizePolicy)
        self.value_DissimilarityTolerance.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_DissimilarityTolerance.setToolTip("")
        self.value_DissimilarityTolerance.setMaximum(100.0)
        self.value_DissimilarityTolerance.setSingleStep(0.01)
        self.value_DissimilarityTolerance.setProperty("value", 2.5)
        self.value_DissimilarityTolerance.setObjectName("value_DissimilarityTolerance")
        self.gridLayout_3.addWidget(self.value_DissimilarityTolerance, 6, 5, 1, 1)
        self.value_DissimilarityTarget = QtWidgets.QDoubleSpinBox(self.layout_step3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_DissimilarityTarget.sizePolicy().hasHeightForWidth())
        self.value_DissimilarityTarget.setSizePolicy(sizePolicy)
        self.value_DissimilarityTarget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_DissimilarityTarget.setWrapping(False)
        self.value_DissimilarityTarget.setFrame(True)
        self.value_DissimilarityTarget.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.value_DissimilarityTarget.setMinimum(-100.0)
        self.value_DissimilarityTarget.setMaximum(100.0)
        self.value_DissimilarityTarget.setSingleStep(0.01)
        self.value_DissimilarityTarget.setProperty("value", 18.0)
        self.value_DissimilarityTarget.setObjectName("value_DissimilarityTarget")
        self.gridLayout_3.addWidget(self.value_DissimilarityTarget, 5, 5, 1, 1)
        self.value_CorrelationTolerance = QtWidgets.QDoubleSpinBox(self.layout_step3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_CorrelationTolerance.sizePolicy().hasHeightForWidth())
        self.value_CorrelationTolerance.setSizePolicy(sizePolicy)
        self.value_CorrelationTolerance.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_CorrelationTolerance.setMaximum(100.0)
        self.value_CorrelationTolerance.setProperty("value", 0.2)
        self.value_CorrelationTolerance.setObjectName("value_CorrelationTolerance")
        self.gridLayout_3.addWidget(self.value_CorrelationTolerance, 4, 5, 1, 1)
        self.value_CorrelationTarget = QtWidgets.QDoubleSpinBox(self.layout_step3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_CorrelationTarget.sizePolicy().hasHeightForWidth())
        self.value_CorrelationTarget.setSizePolicy(sizePolicy)
        self.value_CorrelationTarget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_CorrelationTarget.setMinimum(-100.0)
        self.value_CorrelationTarget.setMaximum(100.0)
        self.value_CorrelationTarget.setSingleStep(0.01)
        self.value_CorrelationTarget.setProperty("value", 0.4)
        self.value_CorrelationTarget.setObjectName("value_CorrelationTarget")
        self.gridLayout_3.addWidget(self.value_CorrelationTarget, 2, 5, 1, 1)
        self.label_PatchSize = QtWidgets.QLabel(self.layout_step3)
        self.label_PatchSize.setWordWrap(True)
        self.label_PatchSize.setObjectName("label_PatchSize")
        self.gridLayout_3.addWidget(self.label_PatchSize, 0, 0, 1, 1)
        self.value_PatchSize = QtWidgets.QSpinBox(self.layout_step3)
        self.value_PatchSize.setMinimum(5)
        self.value_PatchSize.setMaximum(1000)
        self.value_PatchSize.setProperty("value", 25)
        self.value_PatchSize.setObjectName("value_PatchSize")
        self.gridLayout_3.addWidget(self.value_PatchSize, 0, 5, 1, 1)
        self.label_AnglesCompared = QtWidgets.QLabel(self.layout_step3)
        self.label_AnglesCompared.setWordWrap(True)
        self.label_AnglesCompared.setObjectName("label_AnglesCompared")
        self.gridLayout_3.addWidget(self.label_AnglesCompared, 1, 0, 1, 1)
        self.value_AnglesCompared = QtWidgets.QSpinBox(self.layout_step3)
        self.value_AnglesCompared.setFocusPolicy(QtCore.Qt.TabFocus)
        self.value_AnglesCompared.setMinimum(1)
        self.value_AnglesCompared.setMaximum(12)
        self.value_AnglesCompared.setProperty("value", 2)
        self.value_AnglesCompared.setObjectName("value_AnglesCompared")
        self.gridLayout_3.addWidget(self.value_AnglesCompared, 1, 5, 1, 1)
        self.imageToolsLayout.addWidget(self.layout_step3, 0, QtCore.Qt.AlignTop)
        self.imageToolsScroll.setWidget(self.imageToolsScrollArea)
        self.imageToolsLayout_2.addWidget(self.imageToolsScroll)
        self.toolBox.addItem(self.imageTools, "")
        self.labelledItems = QtWidgets.QWidget()
        self.labelledItems.setGeometry(QtCore.QRect(0, 0, 282, 291))
        self.labelledItems.setObjectName("labelledItems")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.labelledItems)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fragmentList = ImageTabList(self.labelledItems)
        self.fragmentList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fragmentList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.fragmentList.setAutoScroll(True)
        self.fragmentList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.fragmentList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fragmentList.setObjectName("fragmentList")
        self.fragmentList.setColumnCount(0)
        self.fragmentList.setRowCount(0)
        self.fragmentList.horizontalHeader().setCascadingSectionResizes(True)
        self.fragmentList.horizontalHeader().setDefaultSectionSize(20)
        self.fragmentList.horizontalHeader().setSortIndicatorShown(True)
        self.fragmentList.horizontalHeader().setStretchLastSection(True)
        self.fragmentList.verticalHeader().setVisible(False)
        self.fragmentList.verticalHeader().setDefaultSectionSize(20)
        self.fragmentList.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_2.addWidget(self.fragmentList)
        self.dislocationTools = QtWidgets.QWidget(self.labelledItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dislocationTools.sizePolicy().hasHeightForWidth())
        self.dislocationTools.setSizePolicy(sizePolicy)
        self.dislocationTools.setObjectName("dislocationTools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dislocationTools)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnAddDisl = QtWidgets.QPushButton(self.dislocationTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddDisl.sizePolicy().hasHeightForWidth())
        self.btnAddDisl.setSizePolicy(sizePolicy)
        self.btnAddDisl.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnAddDisl.setObjectName("btnAddDisl")
        self.horizontalLayout_2.addWidget(self.btnAddDisl)
        self.btnRemDisl = QtWidgets.QPushButton(self.dislocationTools)
        self.btnRemDisl.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnRemDisl.setObjectName("btnRemDisl")
        self.horizontalLayout_2.addWidget(self.btnRemDisl)
        self.btnMovDisl = QtWidgets.QPushButton(self.dislocationTools)
        self.btnMovDisl.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnMovDisl.setObjectName("btnMovDisl")
        self.horizontalLayout_2.addWidget(self.btnMovDisl)
        self.verticalLayout_2.addWidget(self.dislocationTools)
        self.toolBox.addItem(self.labelledItems, "")
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
        self.horizontalLayout.setSpacing(1)
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
        self.imageCurX = QtWidgets.QLabel(self.imageInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCurX.sizePolicy().hasHeightForWidth())
        self.imageCurX.setSizePolicy(sizePolicy)
        self.imageCurX.setMinimumSize(QtCore.QSize(75, 0))
        self.imageCurX.setFrameShape(QtWidgets.QFrame.Box)
        self.imageCurX.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageCurX.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.imageCurX.setObjectName("imageCurX")
        self.horizontalLayout.addWidget(self.imageCurX)
        self.imageCurY = QtWidgets.QLabel(self.imageInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCurY.sizePolicy().hasHeightForWidth())
        self.imageCurY.setSizePolicy(sizePolicy)
        self.imageCurY.setMinimumSize(QtCore.QSize(75, 0))
        self.imageCurY.setFrameShape(QtWidgets.QFrame.Box)
        self.imageCurY.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageCurY.setObjectName("imageCurY")
        self.horizontalLayout.addWidget(self.imageCurY)
        self.verticalLayout.addWidget(self.imageInfo)
        self.label_GaussianSigma.setBuddy(self.value_GaussianSigma)
        self.label_DiscardMargins.setBuddy(self.value_DiscardMargins)
        self.label_DiscardLabels.setBuddy(self.value_DiscardLabels)
        self.label_CorrelationTolerance.setBuddy(self.value_CorrelationTolerance)
        self.label_DissimilarityTarget.setBuddy(self.value_DissimilarityTarget)
        self.label_DissimilarityTolerance.setBuddy(self.value_DissimilarityTolerance)
        self.label_CorrelationTarget.setBuddy(self.value_CorrelationTarget)
        self.label_PatchSize.setBuddy(self.value_PatchSize)
        self.label_AnglesCompared.setBuddy(self.value_AnglesCompared)

        self.retranslateUi(ImageTabPrototype)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ImageTabPrototype)

    def retranslateUi(self, ImageTabPrototype):
        _translate = QtCore.QCoreApplication.translate
        ImageTabPrototype.setWindowTitle(_translate("ImageTabPrototype", "Form"))
        self.button_Scan.setText(_translate("ImageTabPrototype", "Scan image"))
        self.label_step1.setText(_translate("ImageTabPrototype", "<html><head/><body><p><span style=\" font-weight:600;\">Step 1:</span> Edge detection</p></body></html>"))
        self.label_GaussianSigma.setText(_translate("ImageTabPrototype", "<html><head/><body><p>Gaussian sigma<br/><span style=\" font-style:italic;\">(increase for less edges)</span></p></body></html>"))
        self.label_step2.setText(_translate("ImageTabPrototype", "<html><head/><body><p><span style=\" font-weight:600;\">Step 2:</span> Discrimination</p></body></html>"))
        self.value_DiscardMargins.setSuffix(_translate("ImageTabPrototype", "px"))
        self.label_DiscardMargins.setText(_translate("ImageTabPrototype", "Discard fragments within image margin of:"))
        self.value_DiscardLabels.setSuffix(_translate("ImageTabPrototype", "px"))
        self.label_DiscardLabels.setText(_translate("ImageTabPrototype", "Discard fragments with pixel area less than:"))
        self.label_step3.setText(_translate("ImageTabPrototype", "<html><head/><body><p><span style=\" font-weight:600;\">Step 3:</span> Co-occurence matrix testing</p></body></html>"))
        self.label_CorrelationTolerance.setText(_translate("ImageTabPrototype", "Correlation tolerance"))
        self.label_DissimilarityTarget.setText(_translate("ImageTabPrototype", "Dissimilarity target"))
        self.label_DissimilarityTolerance.setText(_translate("ImageTabPrototype", "Dissimilarity tolerance"))
        self.label_CorrelationTarget.setText(_translate("ImageTabPrototype", "Correlation target"))
        self.label_PatchSize.setText(_translate("ImageTabPrototype", "Size of each compared patch"))
        self.value_PatchSize.setSuffix(_translate("ImageTabPrototype", "px"))
        self.label_AnglesCompared.setText(_translate("ImageTabPrototype", "<html><head/><body><p>Angles of comparison<br/><span style=\" font-style:italic;\">(fractions of π)</span></p></body></html>"))
        self.value_AnglesCompared.setToolTip(_translate("ImageTabPrototype", "<html><head/><body><p>The script will attempt to compare each candidate area from a number of angles.</p><p>This number dictates how many angles will be generated, i.e. how many slices Pi should be split up into.</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.imageTools), _translate("ImageTabPrototype", "Dislocation detection"))
        self.btnAddDisl.setText(_translate("ImageTabPrototype", "Add"))
        self.btnRemDisl.setText(_translate("ImageTabPrototype", "Rem"))
        self.btnMovDisl.setText(_translate("ImageTabPrototype", "Mov"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.labelledItems), _translate("ImageTabPrototype", "Labelled items"))
        self.label_minimap.setText(_translate("ImageTabPrototype", "Minimap:"))
        self.label_zoom.setText(_translate("ImageTabPrototype", "Zoom:"))
        self.zoomDial.setSuffix(_translate("ImageTabPrototype", "%"))
        self.imageInfoLabel.setText(_translate("ImageTabPrototype", "No image loaded"))
        self.imageCurX.setText(_translate("ImageTabPrototype", "x:0"))
        self.imageCurY.setText(_translate("ImageTabPrototype", "y:0"))

from ui_widgets import ImageTabList, MinimapView, WorkImageView
