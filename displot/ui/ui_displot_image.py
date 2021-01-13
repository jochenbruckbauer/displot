# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './displot_image.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
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
        self.imageView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.imageView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.imageView.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.imageView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.imageView.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
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
        self.sidebarLayout.setContentsMargins(3, 0, 0, 0)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.toolBox = QtWidgets.QTabWidget(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setTabPosition(QtWidgets.QTabWidget.West)
        self.toolBox.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.toolBox.setUsesScrollButtons(True)
        self.toolBox.setTabBarAutoHide(False)
        self.toolBox.setObjectName("toolBox")
        self.imageTools = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageTools.sizePolicy().hasHeightForWidth())
        self.imageTools.setSizePolicy(sizePolicy)
        self.imageTools.setObjectName("imageTools")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.imageTools)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_Scan = QtWidgets.QPushButton(self.imageTools)
        self.button_Scan.setFlat(False)
        self.button_Scan.setObjectName("button_Scan")
        self.verticalLayout_2.addWidget(self.button_Scan)
        self.imageToolsScroll = QtWidgets.QScrollArea(self.imageTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageToolsScroll.sizePolicy().hasHeightForWidth())
        self.imageToolsScroll.setSizePolicy(sizePolicy)
        self.imageToolsScroll.setFrameShape(QtWidgets.QFrame.Box)
        self.imageToolsScroll.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageToolsScroll.setLineWidth(1)
        self.imageToolsScroll.setMidLineWidth(0)
        self.imageToolsScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imageToolsScroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.imageToolsScroll.setWidgetResizable(True)
        self.imageToolsScroll.setObjectName("imageToolsScroll")
        self.imageToolsScrollArea = QtWidgets.QWidget()
        self.imageToolsScrollArea.setGeometry(QtCore.QRect(0, 0, 241, 524))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageToolsScrollArea.sizePolicy().hasHeightForWidth())
        self.imageToolsScrollArea.setSizePolicy(sizePolicy)
        self.imageToolsScrollArea.setObjectName("imageToolsScrollArea")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.imageToolsScrollArea)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.DislocationPredictionLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DislocationPredictionLabel.sizePolicy().hasHeightForWidth())
        self.DislocationPredictionLabel.setSizePolicy(sizePolicy)
        self.DislocationPredictionLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.DislocationPredictionLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DislocationPredictionLabel.setObjectName("DislocationPredictionLabel")
        self.verticalLayout_4.addWidget(self.DislocationPredictionLabel)
        self.MLModelLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.MLModelLabel.setObjectName("MLModelLabel")
        self.verticalLayout_4.addWidget(self.MLModelLabel)
        self.value_MLModel = QtWidgets.QComboBox(self.imageToolsScrollArea)
        self.value_MLModel.setCurrentText("")
        self.value_MLModel.setObjectName("value_MLModel")
        self.verticalLayout_4.addWidget(self.value_MLModel)
        self.line_MLModel = QtWidgets.QFrame(self.imageToolsScrollArea)
        self.line_MLModel.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_MLModel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_MLModel.setObjectName("line_MLModel")
        self.verticalLayout_4.addWidget(self.line_MLModel)
        self.step1Layout = QtWidgets.QFormLayout()
        self.step1Layout.setObjectName("step1Layout")
        self.strideHorizontalLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.strideHorizontalLabel.setObjectName("strideHorizontalLabel")
        self.step1Layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.strideHorizontalLabel)
        self.strideHorizontalSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.strideHorizontalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.strideHorizontalSpinBox.setMaximum(2048)
        self.strideHorizontalSpinBox.setProperty("value", 256)
        self.strideHorizontalSpinBox.setObjectName("strideHorizontalSpinBox")
        self.step1Layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.strideHorizontalSpinBox)
        self.strideVerticalLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.strideVerticalLabel.setObjectName("strideVerticalLabel")
        self.step1Layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.strideVerticalLabel)
        self.strideVerticalSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.strideVerticalSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.strideVerticalSpinBox.setMaximum(2048)
        self.strideVerticalSpinBox.setProperty("value", 256)
        self.strideVerticalSpinBox.setObjectName("strideVerticalSpinBox")
        self.step1Layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.strideVerticalSpinBox)
        self.verticalLayout_4.addLayout(self.step1Layout)
        self.BlobDetectionLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BlobDetectionLabel.sizePolicy().hasHeightForWidth())
        self.BlobDetectionLabel.setSizePolicy(sizePolicy)
        self.BlobDetectionLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.BlobDetectionLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BlobDetectionLabel.setObjectName("BlobDetectionLabel")
        self.verticalLayout_4.addWidget(self.BlobDetectionLabel)
        self.step2Layout = QtWidgets.QFormLayout()
        self.step2Layout.setObjectName("step2Layout")
        self.minBlobRadiusLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.minBlobRadiusLabel.setObjectName("minBlobRadiusLabel")
        self.step2Layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minBlobRadiusLabel)
        self.minBlobRadiusSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.minBlobRadiusSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minBlobRadiusSpinBox.setMaximum(1000)
        self.minBlobRadiusSpinBox.setProperty("value", 5)
        self.minBlobRadiusSpinBox.setObjectName("minBlobRadiusSpinBox")
        self.step2Layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minBlobRadiusSpinBox)
        self.maxBlobRadiusLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.maxBlobRadiusLabel.setObjectName("maxBlobRadiusLabel")
        self.step2Layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxBlobRadiusLabel)
        self.maxBlobRadiusSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.maxBlobRadiusSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxBlobRadiusSpinBox.setMaximum(1000)
        self.maxBlobRadiusSpinBox.setProperty("value", 14)
        self.maxBlobRadiusSpinBox.setObjectName("maxBlobRadiusSpinBox")
        self.step2Layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxBlobRadiusSpinBox)
        self.minSigmaLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.minSigmaLabel.setObjectName("minSigmaLabel")
        self.step2Layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.minSigmaLabel)
        self.minSigmaSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.minSigmaSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minSigmaSpinBox.setMaximum(1000)
        self.minSigmaSpinBox.setProperty("value", 3)
        self.minSigmaSpinBox.setObjectName("minSigmaSpinBox")
        self.step2Layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.minSigmaSpinBox)
        self.maxSigmaLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.maxSigmaLabel.setObjectName("maxSigmaLabel")
        self.step2Layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.maxSigmaLabel)
        self.maxSigmaSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.maxSigmaSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxSigmaSpinBox.setMaximum(1000)
        self.maxSigmaSpinBox.setProperty("value", 15)
        self.maxSigmaSpinBox.setObjectName("maxSigmaSpinBox")
        self.step2Layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.maxSigmaSpinBox)
        self.numSigmaLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.numSigmaLabel.setObjectName("numSigmaLabel")
        self.step2Layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.numSigmaLabel)
        self.numSigmaSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.numSigmaSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numSigmaSpinBox.setMaximum(1000)
        self.numSigmaSpinBox.setProperty("value", 15)
        self.numSigmaSpinBox.setObjectName("numSigmaSpinBox")
        self.step2Layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.numSigmaSpinBox)
        self.sigmaThresholdLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.sigmaThresholdLabel.setObjectName("sigmaThresholdLabel")
        self.step2Layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sigmaThresholdLabel)
        self.sigmaThresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.imageToolsScrollArea)
        self.sigmaThresholdDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sigmaThresholdDoubleSpinBox.setDecimals(3)
        self.sigmaThresholdDoubleSpinBox.setMaximum(1.0)
        self.sigmaThresholdDoubleSpinBox.setSingleStep(0.01)
        self.sigmaThresholdDoubleSpinBox.setProperty("value", 0.1)
        self.sigmaThresholdDoubleSpinBox.setObjectName("sigmaThresholdDoubleSpinBox")
        self.step2Layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sigmaThresholdDoubleSpinBox)
        self.verticalLayout_4.addLayout(self.step2Layout)
        self.DiscriminationLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiscriminationLabel.sizePolicy().hasHeightForWidth())
        self.DiscriminationLabel.setSizePolicy(sizePolicy)
        self.DiscriminationLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.DiscriminationLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DiscriminationLabel.setObjectName("DiscriminationLabel")
        self.verticalLayout_4.addWidget(self.DiscriminationLabel)
        self.step3Layout = QtWidgets.QFormLayout()
        self.step3Layout.setObjectName("step3Layout")
        self.marginToleranceLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.marginToleranceLabel.setObjectName("marginToleranceLabel")
        self.step3Layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.marginToleranceLabel)
        self.marginToleranceSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.marginToleranceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.marginToleranceSpinBox.setMaximum(1000)
        self.marginToleranceSpinBox.setProperty("value", 3)
        self.marginToleranceSpinBox.setObjectName("marginToleranceSpinBox")
        self.step3Layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.marginToleranceSpinBox)
        self.overlapToleranceLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.overlapToleranceLabel.setObjectName("overlapToleranceLabel")
        self.step3Layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.overlapToleranceLabel)
        self.overlapToleranceSpinBox = QtWidgets.QSpinBox(self.imageToolsScrollArea)
        self.overlapToleranceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overlapToleranceSpinBox.setMaximum(1000)
        self.overlapToleranceSpinBox.setProperty("value", 2)
        self.overlapToleranceSpinBox.setObjectName("overlapToleranceSpinBox")
        self.step3Layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.overlapToleranceSpinBox)
        self.predictionThresholdLabel = QtWidgets.QLabel(self.imageToolsScrollArea)
        self.predictionThresholdLabel.setObjectName("predictionThresholdLabel")
        self.step3Layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.predictionThresholdLabel)
        self.predictionThresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.imageToolsScrollArea)
        self.predictionThresholdDoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.predictionThresholdDoubleSpinBox.setDecimals(2)
        self.predictionThresholdDoubleSpinBox.setMaximum(1.0)
        self.predictionThresholdDoubleSpinBox.setSingleStep(0.01)
        self.predictionThresholdDoubleSpinBox.setProperty("value", 0.33)
        self.predictionThresholdDoubleSpinBox.setObjectName("predictionThresholdDoubleSpinBox")
        self.step3Layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.predictionThresholdDoubleSpinBox)
        self.verticalLayout_4.addLayout(self.step3Layout)
        self.imageToolsScroll.setWidget(self.imageToolsScrollArea)
        self.verticalLayout_2.addWidget(self.imageToolsScroll)
        self.toolBox.addTab(self.imageTools, "")
        self.labelledItems = QtWidgets.QWidget()
        self.labelledItems.setObjectName("labelledItems")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.labelledItems)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.featureList = ImageTabTable(self.labelledItems)
        self.featureList.setFrameShape(QtWidgets.QFrame.Box)
        self.featureList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.featureList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.featureList.setAutoScroll(True)
        self.featureList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.featureList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.featureList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.featureList.setObjectName("featureList")
        self.featureList.horizontalHeader().setMinimumSectionSize(24)
        self.featureList.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.featureList)
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
        self.button_AutoCenterFrags = QtWidgets.QPushButton(self.dislocationTools)
        self.button_AutoCenterFrags.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/feathericons/3rdparty/feather/icons/map-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_AutoCenterFrags.setIcon(icon)
        self.button_AutoCenterFrags.setCheckable(True)
        self.button_AutoCenterFrags.setChecked(True)
        self.button_AutoCenterFrags.setObjectName("button_AutoCenterFrags")
        self.horizontalLayout_2.addWidget(self.button_AutoCenterFrags)
        self.button_SelectAllFrags = QtWidgets.QPushButton(self.dislocationTools)
        self.button_SelectAllFrags.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/feathericons/3rdparty/feather/icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_SelectAllFrags.setIcon(icon1)
        self.button_SelectAllFrags.setCheckable(False)
        self.button_SelectAllFrags.setChecked(False)
        self.button_SelectAllFrags.setObjectName("button_SelectAllFrags")
        self.horizontalLayout_2.addWidget(self.button_SelectAllFrags)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_AddFrag = QtWidgets.QPushButton(self.dislocationTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_AddFrag.sizePolicy().hasHeightForWidth())
        self.button_AddFrag.setSizePolicy(sizePolicy)
        self.button_AddFrag.setMaximumSize(QtCore.QSize(50, 16777215))
        self.button_AddFrag.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/feathericons/3rdparty/feather/icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_AddFrag.setIcon(icon2)
        self.button_AddFrag.setObjectName("button_AddFrag")
        self.horizontalLayout_2.addWidget(self.button_AddFrag)
        self.button_RemFrag = QtWidgets.QPushButton(self.dislocationTools)
        self.button_RemFrag.setMaximumSize(QtCore.QSize(50, 16777215))
        self.button_RemFrag.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/feathericons/3rdparty/feather/icons/minus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_RemFrag.setIcon(icon3)
        self.button_RemFrag.setObjectName("button_RemFrag")
        self.horizontalLayout_2.addWidget(self.button_RemFrag)
        self.button_MovFrag = QtWidgets.QPushButton(self.dislocationTools)
        self.button_MovFrag.setMaximumSize(QtCore.QSize(50, 16777215))
        self.button_MovFrag.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/feathericons/3rdparty/feather/icons/move.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_MovFrag.setIcon(icon4)
        self.button_MovFrag.setObjectName("button_MovFrag")
        self.horizontalLayout_2.addWidget(self.button_MovFrag)
        self.verticalLayout_3.addWidget(self.dislocationTools)
        self.toolBox.addTab(self.labelledItems, "")
        self.sidebarLayout.addWidget(self.toolBox)
        self.minimap = MinimapView(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.minimap.sizePolicy().hasHeightForWidth())
        self.minimap.setSizePolicy(sizePolicy)
        self.minimap.setMinimumSize(QtCore.QSize(297, 200))
        self.minimap.setMaximumSize(QtCore.QSize(297, 200))
        self.minimap.setBaseSize(QtCore.QSize(0, 0))
        self.minimap.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.minimap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minimap.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minimap.setObjectName("minimap")
        self.sidebarLayout.addWidget(self.minimap)
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
        self.imageInfoPBarFrame = QtWidgets.QFrame(self.imageInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageInfoPBarFrame.sizePolicy().hasHeightForWidth())
        self.imageInfoPBarFrame.setSizePolicy(sizePolicy)
        self.imageInfoPBarFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.imageInfoPBarFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageInfoPBarFrame.setObjectName("imageInfoPBarFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.imageInfoPBarFrame)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imageInfoPBar = QtWidgets.QProgressBar(self.imageInfoPBarFrame)
        self.imageInfoPBar.setMaximumSize(QtCore.QSize(150, 1000))
        self.imageInfoPBar.setProperty("value", 0)
        self.imageInfoPBar.setTextVisible(True)
        self.imageInfoPBar.setInvertedAppearance(False)
        self.imageInfoPBar.setObjectName("imageInfoPBar")
        self.horizontalLayout_4.addWidget(self.imageInfoPBar)
        self.horizontalLayout.addWidget(self.imageInfoPBarFrame)
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
        self.imageCurX.setMinimumSize(QtCore.QSize(60, 0))
        self.imageCurX.setFrameShape(QtWidgets.QFrame.Box)
        self.imageCurX.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageCurX.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.imageCurX.setObjectName("imageCurX")
        self.horizontalLayout.addWidget(self.imageCurX)
        self.imageCurY = QtWidgets.QLabel(self.imageInfo)
        self.imageCurY.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCurY.sizePolicy().hasHeightForWidth())
        self.imageCurY.setSizePolicy(sizePolicy)
        self.imageCurY.setMinimumSize(QtCore.QSize(60, 0))
        self.imageCurY.setFrameShape(QtWidgets.QFrame.Box)
        self.imageCurY.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageCurY.setObjectName("imageCurY")
        self.horizontalLayout.addWidget(self.imageCurY)
        self.imageZoom = QtWidgets.QFrame(self.imageInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageZoom.sizePolicy().hasHeightForWidth())
        self.imageZoom.setSizePolicy(sizePolicy)
        self.imageZoom.setMinimumSize(QtCore.QSize(100, 0))
        self.imageZoom.setMaximumSize(QtCore.QSize(120, 16777215))
        self.imageZoom.setFrameShape(QtWidgets.QFrame.Box)
        self.imageZoom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageZoom.setObjectName("imageZoom")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.imageZoom)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_zoom = QtWidgets.QLabel(self.imageZoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_zoom.sizePolicy().hasHeightForWidth())
        self.label_zoom.setSizePolicy(sizePolicy)
        self.label_zoom.setMinimumSize(QtCore.QSize(100, 0))
        self.label_zoom.setOpenExternalLinks(False)
        self.label_zoom.setObjectName("label_zoom")
        self.horizontalLayout_3.addWidget(self.label_zoom)
        self.zoomDial = QtWidgets.QSpinBox(self.imageZoom)
        self.zoomDial.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.zoomDial.setFont(font)
        self.zoomDial.setMinimum(10)
        self.zoomDial.setMaximum(400)
        self.zoomDial.setProperty("value", 100)
        self.zoomDial.setObjectName("zoomDial")
        self.horizontalLayout_3.addWidget(self.zoomDial)
        self.horizontalLayout.addWidget(self.imageZoom)
        self.verticalLayout.addWidget(self.imageInfo)
        self.MLModelLabel.setBuddy(self.value_MLModel)
        self.strideHorizontalLabel.setBuddy(self.strideHorizontalSpinBox)
        self.strideVerticalLabel.setBuddy(self.strideVerticalSpinBox)
        self.minBlobRadiusLabel.setBuddy(self.minBlobRadiusSpinBox)
        self.maxBlobRadiusLabel.setBuddy(self.maxBlobRadiusSpinBox)
        self.minSigmaLabel.setBuddy(self.minSigmaSpinBox)
        self.numSigmaLabel.setBuddy(self.numSigmaSpinBox)
        self.sigmaThresholdLabel.setBuddy(self.sigmaThresholdDoubleSpinBox)
        self.marginToleranceLabel.setBuddy(self.marginToleranceSpinBox)
        self.overlapToleranceLabel.setBuddy(self.overlapToleranceSpinBox)
        self.predictionThresholdLabel.setBuddy(self.predictionThresholdDoubleSpinBox)

        self.retranslateUi(ImageTabPrototype)
        self.toolBox.setCurrentIndex(0)
        #QtCore.QMetaObject.connectSlotsByName(ImageTabPrototype)

    def retranslateUi(self, ImageTabPrototype):
        _translate = QtCore.QCoreApplication.translate
        ImageTabPrototype.setWindowTitle(_translate("ImageTabPrototype", "Form"))
        self.button_Scan.setText(_translate("ImageTabPrototype", "Start prediction"))
        self.DislocationPredictionLabel.setText(_translate("ImageTabPrototype", "<html><head/><body><p><span style=\" font-weight:600;\">Settings:</span> Dislocation Prediction</p></body></html>"))
        self.MLModelLabel.setText(_translate("ImageTabPrototype", "Prediction model:"))
        self.strideHorizontalLabel.setText(_translate("ImageTabPrototype", "Stride (horizontal)"))
        self.strideHorizontalSpinBox.setSuffix(_translate("ImageTabPrototype", "px"))
        self.strideVerticalLabel.setText(_translate("ImageTabPrototype", "Stride (vertical)"))
        self.strideVerticalSpinBox.setSuffix(_translate("ImageTabPrototype", "px"))
        self.BlobDetectionLabel.setText(_translate("ImageTabPrototype", "<html><head/><body><p><span style=\" font-weight:600;\">Settings:</span> Blob Detection</p></body></html>"))
        self.minBlobRadiusLabel.setToolTip(_translate("ImageTabPrototype", "Minimum blob radius in pixels."))
        self.minBlobRadiusLabel.setText(_translate("ImageTabPrototype", "Minimum blob radius"))
        self.minBlobRadiusSpinBox.setSuffix(_translate("ImageTabPrototype", "px"))
        self.maxBlobRadiusLabel.setToolTip(_translate("ImageTabPrototype", "Maximum blob radius in pixels."))
        self.maxBlobRadiusLabel.setText(_translate("ImageTabPrototype", "Maximum blob radius"))
        self.maxBlobRadiusSpinBox.setSuffix(_translate("ImageTabPrototype", "px"))
        self.minSigmaLabel.setText(_translate("ImageTabPrototype", "Min. sigma"))
        self.maxSigmaLabel.setText(_translate("ImageTabPrototype", "Max. sigma"))
        self.numSigmaLabel.setText(_translate("ImageTabPrototype", "Num. sigma"))
        self.sigmaThresholdLabel.setText(_translate("ImageTabPrototype", "Threshold"))
        self.DiscriminationLabel.setText(_translate("ImageTabPrototype", "<html><head/><body><p><span style=\" font-weight:600;\">Settings:</span> Discrimination</p></body></html>"))
        self.marginToleranceLabel.setToolTip(_translate("ImageTabPrototype", "Prune features within this many pixels of the image border."))
        self.marginToleranceLabel.setText(_translate("ImageTabPrototype", "Margin tolerance"))
        self.marginToleranceSpinBox.setSuffix(_translate("ImageTabPrototype", "px"))
        self.overlapToleranceLabel.setToolTip(_translate("ImageTabPrototype", "Allow this many pixels of blob overlap."))
        self.overlapToleranceLabel.setText(_translate("ImageTabPrototype", "Overlap tolerance"))
        self.overlapToleranceSpinBox.setSuffix(_translate("ImageTabPrototype", "px"))
        self.predictionThresholdLabel.setToolTip(_translate("ImageTabPrototype", "Prune features with prediction confidence under this threshold."))
        self.predictionThresholdLabel.setText(_translate("ImageTabPrototype", "Prediction threshold"))
        self.toolBox.setTabText(self.toolBox.indexOf(self.imageTools), _translate("ImageTabPrototype", "TD Position"))
        self.button_AutoCenterFrags.setToolTip(_translate("ImageTabPrototype", "Toggle this button to control whether the view will\n"
"automatically center on fragments selected on the list."))
        self.button_SelectAllFrags.setToolTip(_translate("ImageTabPrototype", "Toggle selected and unselected features."))
        self.button_AddFrag.setToolTip(_translate("ImageTabPrototype", "Add new fragment to image."))
        self.button_RemFrag.setToolTip(_translate("ImageTabPrototype", "Remove selected fragments from image.\n"
"Selection is controlled using the checkboxes in the table above."))
        self.button_MovFrag.setToolTip(_translate("ImageTabPrototype", "Move selected fragment.\n"
"Selection is controlled by highlighting a row in the table above."))
        self.toolBox.setTabText(self.toolBox.indexOf(self.labelledItems), _translate("ImageTabPrototype", "Features"))
        self.imageInfoLabel.setText(_translate("ImageTabPrototype", "No image loaded"))
        self.imageCurX.setText(_translate("ImageTabPrototype", "x:0"))
        self.imageCurY.setText(_translate("ImageTabPrototype", "y:0"))
        self.label_zoom.setText(_translate("ImageTabPrototype", "Zoom:"))
        self.zoomDial.setSuffix(_translate("ImageTabPrototype", "%"))
from displot.ui._imagetab_table import ImageTabTable
from displot.ui._imageview import MinimapView, WorkImageView
from . import feathericons_rc
