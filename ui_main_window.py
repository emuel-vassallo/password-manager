# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 530)
        MainWindow.setStyleSheet(u"#buttonTabAddNew, #buttonTabGenerate, #buttonTabPasswords, #buttonTabSecurity {\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#buttonPasswords, #buttonAddNew, #buttonGenerate, #buttonSecurity {\n"
"	text-align: left;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamilies([u"Roboto"])
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameSidebar = QFrame(self.frame)
        self.frameSidebar.setObjectName(u"frameSidebar")
        self.frameSidebar.setMinimumSize(QSize(160, 0))
        self.frameSidebar.setMaximumSize(QSize(160, 16777215))
        self.frameSidebar.setFont(font)
        self.frameSidebar.setFrameShape(QFrame.StyledPanel)
        self.frameSidebar.setFrameShadow(QFrame.Plain)
        self.frameSidebarButtons = QFrame(self.frameSidebar)
        self.frameSidebarButtons.setObjectName(u"frameSidebarButtons")
        self.frameSidebarButtons.setGeometry(QRect(0, 100, 160, 160))
        self.frameSidebarButtons.setMinimumSize(QSize(160, 160))
        self.frameSidebarButtons.setMaximumSize(QSize(160, 160))
        self.frameSidebarButtons.setFont(font)
        self.frameSidebarButtons.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frameSidebarButtons)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonTabPasswords = QPushButton(self.frameSidebarButtons)
        self.buttonTabPasswords.setObjectName(u"buttonTabPasswords")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonTabPasswords.sizePolicy().hasHeightForWidth())
        self.buttonTabPasswords.setSizePolicy(sizePolicy)
        self.buttonTabPasswords.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(9)
        self.buttonTabPasswords.setFont(font1)
        self.buttonTabPasswords.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonTabPasswords.setLayoutDirection(Qt.LeftToRight)
        self.buttonTabPasswords.setAutoFillBackground(False)
        self.buttonTabPasswords.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"icons/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTabPasswords.setIcon(icon)
        self.buttonTabPasswords.setIconSize(QSize(14, 14))
        self.buttonTabPasswords.setCheckable(False)
        self.buttonTabPasswords.setChecked(False)
        self.buttonTabPasswords.setAutoRepeat(False)
        self.buttonTabPasswords.setAutoExclusive(False)
        self.buttonTabPasswords.setFlat(False)

        self.verticalLayout.addWidget(self.buttonTabPasswords)

        self.buttonTabAddNew = QPushButton(self.frameSidebarButtons)
        self.buttonTabAddNew.setObjectName(u"buttonTabAddNew")
        sizePolicy.setHeightForWidth(self.buttonTabAddNew.sizePolicy().hasHeightForWidth())
        self.buttonTabAddNew.setSizePolicy(sizePolicy)
        self.buttonTabAddNew.setMinimumSize(QSize(0, 30))
        self.buttonTabAddNew.setFont(font1)
        self.buttonTabAddNew.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonTabAddNew.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTabAddNew.setIcon(icon1)
        self.buttonTabAddNew.setIconSize(QSize(14, 14))

        self.verticalLayout.addWidget(self.buttonTabAddNew)

        self.buttonTabGenerate = QPushButton(self.frameSidebarButtons)
        self.buttonTabGenerate.setObjectName(u"buttonTabGenerate")
        sizePolicy.setHeightForWidth(self.buttonTabGenerate.sizePolicy().hasHeightForWidth())
        self.buttonTabGenerate.setSizePolicy(sizePolicy)
        self.buttonTabGenerate.setMinimumSize(QSize(0, 30))
        self.buttonTabGenerate.setFont(font1)
        self.buttonTabGenerate.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonTabGenerate.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTabGenerate.setIcon(icon2)
        self.buttonTabGenerate.setIconSize(QSize(14, 14))

        self.verticalLayout.addWidget(self.buttonTabGenerate)

        self.buttonTabSecurity = QPushButton(self.frameSidebarButtons)
        self.buttonTabSecurity.setObjectName(u"buttonTabSecurity")
        sizePolicy.setHeightForWidth(self.buttonTabSecurity.sizePolicy().hasHeightForWidth())
        self.buttonTabSecurity.setSizePolicy(sizePolicy)
        self.buttonTabSecurity.setMinimumSize(QSize(0, 30))
        self.buttonTabSecurity.setFont(font1)
        self.buttonTabSecurity.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonTabSecurity.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"icons/security.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTabSecurity.setIcon(icon3)
        self.buttonTabSecurity.setIconSize(QSize(14, 14))

        self.verticalLayout.addWidget(self.buttonTabSecurity)

        self.label = QLabel(self.frameSidebar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 161, 17))
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(10)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.frameSidebar)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.widgetPasswords = QWidget()
        self.widgetPasswords.setObjectName(u"widgetPasswords")
        self.verticalLayout_3 = QVBoxLayout(self.widgetPasswords)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.framePasswordDashboard = QFrame(self.widgetPasswords)
        self.framePasswordDashboard.setObjectName(u"framePasswordDashboard")
        self.framePasswordDashboard.setFrameShape(QFrame.NoFrame)
        self.framePasswordDashboard.setFrameShadow(QFrame.Raised)
        self.labelHeading_5 = QLabel(self.framePasswordDashboard)
        self.labelHeading_5.setObjectName(u"labelHeading_5")
        self.labelHeading_5.setGeometry(QRect(110, 30, 310, 20))
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        self.labelHeading_5.setFont(font3)
        self.labelHeading_5.setAlignment(Qt.AlignCenter)
        self.editSearch = QLineEdit(self.framePasswordDashboard)
        self.editSearch.setObjectName(u"editSearch")
        self.editSearch.setGeometry(QRect(40, 90, 451, 25))
        self.editSearch.setMinimumSize(QSize(0, 25))
        self.editSearch.setMaximumSize(QSize(16777215, 25))
        self.editSearch.setFont(font)
        self.editSearch.setFrame(True)
        self.editSearch.setClearButtonEnabled(True)
        self.tablePasswords = QTableWidget(self.framePasswordDashboard)
        if (self.tablePasswords.columnCount() < 4):
            self.tablePasswords.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePasswords.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePasswords.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePasswords.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePasswords.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablePasswords.setObjectName(u"tablePasswords")
        self.tablePasswords.setGeometry(QRect(40, 140, 450, 241))
        font4 = QFont()
        font4.setPointSize(9)
        self.tablePasswords.setFont(font4)
        self.tablePasswords.setAutoScroll(False)
        self.tablePasswords.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePasswords.setTabKeyNavigation(True)
        self.tablePasswords.setProperty("showDropIndicator", True)
        self.tablePasswords.setAlternatingRowColors(False)
        self.tablePasswords.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablePasswords.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePasswords.horizontalHeader().setCascadingSectionResizes(True)
        self.tablePasswords.horizontalHeader().setProperty("showSortIndicator", True)
        self.tablePasswords.horizontalHeader().setStretchLastSection(True)
        self.tablePasswords.verticalHeader().setVisible(False)
        self.frame_4 = QFrame(self.framePasswordDashboard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 410, 451, 40))
        self.frame_4.setFont(font1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonDelete = QPushButton(self.frame_4)
        self.buttonDelete.setObjectName(u"buttonDelete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(25)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonDelete.sizePolicy().hasHeightForWidth())
        self.buttonDelete.setSizePolicy(sizePolicy1)
        self.buttonDelete.setMinimumSize(QSize(0, 27))
        self.buttonDelete.setFont(font1)
        self.buttonDelete.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDelete.setIcon(icon4)
        self.buttonDelete.setIconSize(QSize(13, 13))

        self.gridLayout.addWidget(self.buttonDelete, 0, 2, 1, 1)

        self.buttonCopyPwd = QPushButton(self.frame_4)
        self.buttonCopyPwd.setObjectName(u"buttonCopyPwd")
        sizePolicy1.setHeightForWidth(self.buttonCopyPwd.sizePolicy().hasHeightForWidth())
        self.buttonCopyPwd.setSizePolicy(sizePolicy1)
        self.buttonCopyPwd.setMinimumSize(QSize(0, 27))
        self.buttonCopyPwd.setFont(font1)
        self.buttonCopyPwd.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCopyPwd.setIcon(icon5)
        self.buttonCopyPwd.setIconSize(QSize(13, 13))

        self.gridLayout.addWidget(self.buttonCopyPwd, 0, 0, 1, 1)

        self.buttonEdit = QPushButton(self.frame_4)
        self.buttonEdit.setObjectName(u"buttonEdit")
        sizePolicy1.setHeightForWidth(self.buttonEdit.sizePolicy().hasHeightForWidth())
        self.buttonEdit.setSizePolicy(sizePolicy1)
        self.buttonEdit.setMinimumSize(QSize(0, 27))
        self.buttonEdit.setFont(font1)
        self.buttonEdit.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonEdit.setIcon(icon6)
        self.buttonEdit.setIconSize(QSize(13, 13))

        self.gridLayout.addWidget(self.buttonEdit, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.framePasswordDashboard)

        self.stackedWidget.addWidget(self.widgetPasswords)
        self.widgetAdd = QWidget()
        self.widgetAdd.setObjectName(u"widgetAdd")
        self.verticalLayout_4 = QVBoxLayout(self.widgetAdd)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frameAddPassword = QFrame(self.widgetAdd)
        self.frameAddPassword.setObjectName(u"frameAddPassword")
        self.frameAddPassword.setFont(font)
        self.frameAddPassword.setFrameShape(QFrame.NoFrame)
        self.frameAddPassword.setFrameShadow(QFrame.Raised)
        self.labelHeading = QLabel(self.frameAddPassword)
        self.labelHeading.setObjectName(u"labelHeading")
        self.labelHeading.setGeometry(QRect(110, 30, 310, 20))
        self.labelHeading.setFont(font3)
        self.labelHeading.setAlignment(Qt.AlignCenter)
        self.frameFormButtons = QFrame(self.frameAddPassword)
        self.frameFormButtons.setObjectName(u"frameFormButtons")
        self.frameFormButtons.setGeometry(QRect(40, 400, 260, 40))
        self.frameFormButtons.setFont(font)
        self.frameFormButtons.setFrameShape(QFrame.NoFrame)
        self.frameFormButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameFormButtons)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonAddPassword = QPushButton(self.frameFormButtons)
        self.buttonAddPassword.setObjectName(u"buttonAddPassword")
        self.buttonAddPassword.setMinimumSize(QSize(0, 27))
        self.buttonAddPassword.setFont(font4)
        self.buttonAddPassword.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonAddPassword)

        self.buttonClear = QPushButton(self.frameFormButtons)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setMinimumSize(QSize(0, 27))
        self.buttonClear.setFont(font4)
        self.buttonClear.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonClear)

        self.framePasswordEntries = QFrame(self.frameAddPassword)
        self.framePasswordEntries.setObjectName(u"framePasswordEntries")
        self.framePasswordEntries.setGeometry(QRect(40, 70, 450, 301))
        self.framePasswordEntries.setFrameShape(QFrame.NoFrame)
        self.framePasswordEntries.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.framePasswordEntries)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frameTitleEntry = QFrame(self.framePasswordEntries)
        self.frameTitleEntry.setObjectName(u"frameTitleEntry")
        self.frameTitleEntry.setFrameShape(QFrame.NoFrame)
        self.frameTitleEntry.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameTitleEntry)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.labelTitle = QLabel(self.frameTitleEntry)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setFont(font1)
        self.labelTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.labelTitle)

        self.editTitle = QLineEdit(self.frameTitleEntry)
        self.editTitle.setObjectName(u"editTitle")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(8)
        self.editTitle.setFont(font5)

        self.verticalLayout_6.addWidget(self.editTitle)


        self.verticalLayout_10.addWidget(self.frameTitleEntry)

        self.frameUrlEntry = QFrame(self.framePasswordEntries)
        self.frameUrlEntry.setObjectName(u"frameUrlEntry")
        self.frameUrlEntry.setFrameShape(QFrame.NoFrame)
        self.frameUrlEntry.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frameUrlEntry)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.labelUrl = QLabel(self.frameUrlEntry)
        self.labelUrl.setObjectName(u"labelUrl")
        self.labelUrl.setFont(font1)
        self.labelUrl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.labelUrl)

        self.editUrl = QLineEdit(self.frameUrlEntry)
        self.editUrl.setObjectName(u"editUrl")
        self.editUrl.setFont(font5)

        self.verticalLayout_7.addWidget(self.editUrl)


        self.verticalLayout_10.addWidget(self.frameUrlEntry)

        self.frameUsernameEntry = QFrame(self.framePasswordEntries)
        self.frameUsernameEntry.setObjectName(u"frameUsernameEntry")
        self.frameUsernameEntry.setFrameShape(QFrame.NoFrame)
        self.frameUsernameEntry.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameUsernameEntry)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, -1)
        self.labelUsername = QLabel(self.frameUsernameEntry)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setFont(font1)
        self.labelUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.labelUsername)

        self.editUsername = QLineEdit(self.frameUsernameEntry)
        self.editUsername.setObjectName(u"editUsername")
        self.editUsername.setFont(font5)

        self.verticalLayout_8.addWidget(self.editUsername)


        self.verticalLayout_10.addWidget(self.frameUsernameEntry)

        self.framePasswordEntry = QFrame(self.framePasswordEntries)
        self.framePasswordEntry.setObjectName(u"framePasswordEntry")
        self.framePasswordEntry.setFrameShape(QFrame.NoFrame)
        self.framePasswordEntry.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.framePasswordEntry)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.labelPassword = QLabel(self.framePasswordEntry)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setFont(font1)
        self.labelPassword.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.labelPassword)

        self.editPassword = QLineEdit(self.framePasswordEntry)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setMinimumSize(QSize(0, 25))
        self.editPassword.setFont(font5)
        self.editPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.editPassword)


        self.verticalLayout_10.addWidget(self.framePasswordEntry)


        self.verticalLayout_4.addWidget(self.frameAddPassword)

        self.stackedWidget.addWidget(self.widgetAdd)
        self.widgetGenerate = QWidget()
        self.widgetGenerate.setObjectName(u"widgetGenerate")
        self.horizontalLayout_6 = QHBoxLayout(self.widgetGenerate)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frameGenerate = QFrame(self.widgetGenerate)
        self.frameGenerate.setObjectName(u"frameGenerate")
        font6 = QFont()
        font6.setPointSize(10)
        self.frameGenerate.setFont(font6)
        self.frameGenerate.setFrameShape(QFrame.NoFrame)
        self.frameGenerate.setFrameShadow(QFrame.Raised)
        self.labelHeading_2 = QLabel(self.frameGenerate)
        self.labelHeading_2.setObjectName(u"labelHeading_2")
        self.labelHeading_2.setGeometry(QRect(110, 30, 310, 20))
        self.labelHeading_2.setFont(font3)
        self.labelHeading_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.frameGenerate)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 90, 450, 71))
        self.groupBox_2.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 25))
        self.spinBox.setFont(font1)
        self.spinBox.setWrapping(False)
        self.spinBox.setFrame(True)
        self.spinBox.setAccelerated(False)
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(50)
        self.spinBox.setValue(15)

        self.horizontalLayout_4.addWidget(self.spinBox)

        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(0, 20))
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setValue(15)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)

        self.horizontalLayout_4.addWidget(self.horizontalSlider)

        self.groupBox = QGroupBox(self.frameGenerate)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 180, 450, 142))
        self.groupBox.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBoxUpper = QCheckBox(self.groupBox)
        self.checkBoxUpper.setObjectName(u"checkBoxUpper")
        self.checkBoxUpper.setFont(font1)
        self.checkBoxUpper.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxUpper)

        self.checkBoxLower = QCheckBox(self.groupBox)
        self.checkBoxLower.setObjectName(u"checkBoxLower")
        self.checkBoxLower.setFont(font1)
        self.checkBoxLower.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxLower)

        self.checkBoxDigits = QCheckBox(self.groupBox)
        self.checkBoxDigits.setObjectName(u"checkBoxDigits")
        self.checkBoxDigits.setFont(font1)
        self.checkBoxDigits.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxDigits)

        self.checkBoxSymbols = QCheckBox(self.groupBox)
        self.checkBoxSymbols.setObjectName(u"checkBoxSymbols")
        self.checkBoxSymbols.setFont(font1)
        self.checkBoxSymbols.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBoxSymbols)

        self.groupBox_3 = QGroupBox(self.frameGenerate)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(40, 400, 450, 71))
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelGeneratedPwd = QLabel(self.groupBox_3)
        self.labelGeneratedPwd.setObjectName(u"labelGeneratedPwd")
        self.labelGeneratedPwd.setFont(font5)
        self.labelGeneratedPwd.setCursor(QCursor(Qt.IBeamCursor))
        self.labelGeneratedPwd.setFrameShape(QFrame.StyledPanel)
        self.labelGeneratedPwd.setFrameShadow(QFrame.Plain)
        self.labelGeneratedPwd.setWordWrap(False)
        self.labelGeneratedPwd.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.labelGeneratedPwd)

        self.buttonCopyRandomPwd = QPushButton(self.groupBox_3)
        self.buttonCopyRandomPwd.setObjectName(u"buttonCopyRandomPwd")
        self.buttonCopyRandomPwd.setMinimumSize(QSize(30, 0))
        self.buttonCopyRandomPwd.setMaximumSize(QSize(30, 30))
        self.buttonCopyRandomPwd.setFont(font)
        self.buttonCopyRandomPwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonCopyRandomPwd.setIcon(icon5)
        self.buttonCopyRandomPwd.setIconSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.buttonCopyRandomPwd)

        self.buttonGeneratePwd = QPushButton(self.frameGenerate)
        self.buttonGeneratePwd.setObjectName(u"buttonGeneratePwd")
        self.buttonGeneratePwd.setGeometry(QRect(40, 350, 450, 27))
        self.buttonGeneratePwd.setFont(font1)
        self.buttonGeneratePwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.labelCopiedToClip = QLabel(self.frameGenerate)
        self.labelCopiedToClip.setObjectName(u"labelCopiedToClip")
        self.labelCopiedToClip.setGeometry(QRect(40, 470, 116, 31))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(8)
        font7.setItalic(False)
        self.labelCopiedToClip.setFont(font7)

        self.horizontalLayout_6.addWidget(self.frameGenerate)

        self.stackedWidget.addWidget(self.widgetGenerate)
        self.widgetSecurity = QWidget()
        self.widgetSecurity.setObjectName(u"widgetSecurity")
        self.horizontalLayout_7 = QHBoxLayout(self.widgetSecurity)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frameSecurity = QFrame(self.widgetSecurity)
        self.frameSecurity.setObjectName(u"frameSecurity")
        self.frameSecurity.setFrameShape(QFrame.NoFrame)
        self.frameSecurity.setFrameShadow(QFrame.Raised)
        self.labelHeading_3 = QLabel(self.frameSecurity)
        self.labelHeading_3.setObjectName(u"labelHeading_3")
        self.labelHeading_3.setGeometry(QRect(110, 30, 310, 20))
        self.labelHeading_3.setFont(font3)
        self.labelHeading_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.frameSecurity)

        self.stackedWidget.addWidget(self.widgetSecurity)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.buttonTabPasswords.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.buttonTabPasswords.setText(QCoreApplication.translate("MainWindow", u"Passwords", None))
        self.buttonTabAddNew.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.buttonTabGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.buttonTabSecurity.setText(QCoreApplication.translate("MainWindow", u"Security Check", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.labelHeading_5.setText(QCoreApplication.translate("MainWindow", u"Password Dashboard", None))
        self.editSearch.setText("")
        self.editSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.tablePasswords.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.tablePasswords.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Url", None));
        ___qtablewidgetitem2 = self.tablePasswords.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem3 = self.tablePasswords.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.buttonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.buttonCopyPwd.setText(QCoreApplication.translate("MainWindow", u"Copy Password", None))
        self.buttonEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.labelHeading.setText(QCoreApplication.translate("MainWindow", u"Add a New Password", None))
        self.buttonAddPassword.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.buttonClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.labelUrl.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.labelUsername.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.labelHeading_2.setText(QCoreApplication.translate("MainWindow", u"Generate a Random Password", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Password Length:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Character Types:", None))
        self.checkBoxUpper.setText(QCoreApplication.translate("MainWindow", u"Uppercase (A-Z)", None))
        self.checkBoxLower.setText(QCoreApplication.translate("MainWindow", u"Lowercase (a-z)", None))
        self.checkBoxDigits.setText(QCoreApplication.translate("MainWindow", u"Digits (0-9)", None))
        self.checkBoxSymbols.setText(QCoreApplication.translate("MainWindow", u"Symbols (!$%@#)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Random Password:", None))
        self.labelGeneratedPwd.setText("")
        self.buttonCopyRandomPwd.setText("")
        self.buttonGeneratePwd.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.labelCopiedToClip.setText("")
        self.labelHeading_3.setText(QCoreApplication.translate("MainWindow", u"Security Check", None))
    # retranslateUi

