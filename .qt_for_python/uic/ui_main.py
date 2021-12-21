# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(866, 377)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 300))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"background:rgb(91,90,90);")
        MainWindow.setIconSize(QSize(24, 24))
        self.actionZalohuj = QAction(MainWindow)
        self.actionZalohuj.setObjectName(u"actionZalohuj")
        self.actionZaloguj = QAction(MainWindow)
        self.actionZaloguj.setObjectName(u"actionZaloguj")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.actionZaloguj.setFont(font)
        self.actionWyloguj = QAction(MainWindow)
        self.actionWyloguj.setObjectName(u"actionWyloguj")
        self.actionWyloguj.setFont(font)
        self.actionOtworzbazedanych = QAction(MainWindow)
        self.actionOtworzbazedanych.setObjectName(u"actionOtworzbazedanych")
        self.actionOtworzbazedanych.setFont(font)
        self.actionEdytujbazedanych = QAction(MainWindow)
        self.actionEdytujbazedanych.setObjectName(u"actionEdytujbazedanych")
        self.actionEdytujbazedanych.setFont(font)
        self.actionUstawienia_globalne = QAction(MainWindow)
        self.actionUstawienia_globalne.setObjectName(u"actionUstawienia_globalne")
        self.actionUstawienia_globalne.setFont(font)
        self.actionBacktomain = QAction(MainWindow)
        self.actionBacktomain.setObjectName(u"actionBacktomain")
        self.actionBacktomain.setFont(font)
        self.actionConnectDatabase = QAction(MainWindow)
        self.actionConnectDatabase.setObjectName(u"actionConnectDatabase")
        self.actionConnectDatabase.setFont(font)
        self.actionDisconnectDatabase = QAction(MainWindow)
        self.actionDisconnectDatabase.setObjectName(u"actionDisconnectDatabase")
        self.actionDisconnectDatabase.setFont(font)
        self.actionUstawienia_globalne_2 = QAction(MainWindow)
        self.actionUstawienia_globalne_2.setObjectName(u"actionUstawienia_globalne_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout_3 = QVBoxLayout(self.page_main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.page_main)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_27 = QLabel(self.page_main)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_27)

        self.label_28 = QLabel(self.page_main)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_28)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.page_main)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.page_main)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)

        self.lineEdit_6 = QLineEdit(self.page_main)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(18)
        self.lineEdit_6.setFont(font3)
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lineEdit_6)

        self.label_11 = QLabel(self.page_main)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.lineEdit_7 = QLineEdit(self.page_main)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(16)
        self.lineEdit_7.setFont(font4)
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.verticalLayout_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.page_main)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.page_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page_main)
        self.page_database_login = QWidget()
        self.page_database_login.setObjectName(u"page_database_login")
        self.horizontalLayout_2 = QHBoxLayout(self.page_database_login)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.page_database_login)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(36)
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.page_database_login)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.page_database_login)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_3 = QLineEdit(self.page_database_login)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setFont(font5)

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.page_database_login)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setFont(font5)

        self.verticalLayout_9.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.page_database_login)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setFont(font5)
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.lineEdit_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.bn_databaselogin = QPushButton(self.page_database_login)
        self.bn_databaselogin.setObjectName(u"bn_databaselogin")
        self.bn_databaselogin.setFont(font1)
        self.bn_databaselogin.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")

        self.verticalLayout_7.addWidget(self.bn_databaselogin)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.page_database_login)
        self.page_database = QWidget()
        self.page_database.setObjectName(u"page_database")
        self.horizontalLayout_13 = QHBoxLayout(self.page_database)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBox_2 = QComboBox(self.page_database)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)
        self.comboBox_2.setFont(font1)

        self.horizontalLayout_15.addWidget(self.comboBox_2)

        self.bn_databaseSet = QPushButton(self.page_database)
        self.bn_databaseSet.setObjectName(u"bn_databaseSet")
        sizePolicy.setHeightForWidth(self.bn_databaseSet.sizePolicy().hasHeightForWidth())
        self.bn_databaseSet.setSizePolicy(sizePolicy)
        self.bn_databaseSet.setFont(font1)
        self.bn_databaseSet.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")

        self.horizontalLayout_15.addWidget(self.bn_databaseSet)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.comboBox = QComboBox(self.page_database)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setFont(font4)

        self.verticalLayout_12.addWidget(self.comboBox)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.bn_databaseInfo = QPushButton(self.page_database)
        self.bn_databaseInfo.setObjectName(u"bn_databaseInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bn_databaseInfo.sizePolicy().hasHeightForWidth())
        self.bn_databaseInfo.setSizePolicy(sizePolicy3)
        self.bn_databaseInfo.setFont(font1)
        self.bn_databaseInfo.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(150,60,180);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(180,70,210);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(150,60,180);\n"
"}")

        self.horizontalLayout_12.addWidget(self.bn_databaseInfo)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.stackedWidget_2 = QStackedWidget(self.page_database)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy4)
        self.page_database_view = QWidget()
        self.page_database_view.setObjectName(u"page_database_view")
        self.verticalLayout_15 = QVBoxLayout(self.page_database_view)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea = QScrollArea(self.page_database_view)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 358, 504))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_15)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_16)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_17)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font6)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_18)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setOpenExternalLinks(True)

        self.verticalLayout_18.addWidget(self.label_19)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font6)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_21)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_22)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_23)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_24)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_25)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.stackedWidget_2.addWidget(self.page_database_view)
        self.page_database_edit = QWidget()
        self.page_database_edit.setObjectName(u"page_database_edit")
        self.verticalLayout_17 = QVBoxLayout(self.page_database_edit)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.bn_databaseDel = QPushButton(self.page_database_edit)
        self.bn_databaseDel.setObjectName(u"bn_databaseDel")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(26)
        self.bn_databaseDel.setFont(font7)
        self.bn_databaseDel.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(200,66,66);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(230,80,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(190,60,60);\n"
"}")

        self.verticalLayout_16.addWidget(self.bn_databaseDel)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.stackedWidget_2.addWidget(self.page_database_edit)

        self.horizontalLayout_14.addWidget(self.stackedWidget_2)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.page_database)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_6 = QHBoxLayout(self.page_login)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.page_login)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_login)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.page_login)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setFont(font5)
        self.lineEdit.setMaxLength(20)

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.page_login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.lineEdit_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.bn_login = QPushButton(self.page_login)
        self.bn_login.setObjectName(u"bn_login")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(22)
        self.bn_login.setFont(font8)
        self.bn_login.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")
        self.bn_login.setFlat(True)

        self.verticalLayout_6.addWidget(self.bn_login)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_login)
        self.page_profil = QWidget()
        self.page_profil.setObjectName(u"page_profil")
        self.verticalLayout_13 = QVBoxLayout(self.page_profil)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_26 = QLabel(self.page_profil)
        self.label_26.setObjectName(u"label_26")
        sizePolicy4.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy4)
        self.label_26.setMaximumSize(QSize(16777215, 50))
        self.label_26.setFont(font1)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_26)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.widget_2 = QWidget(self.page_profil)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.widget_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.stackedWidget.addWidget(self.page_profil)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_9 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.bn_settings_set = QPushButton(self.page_settings)
        self.bn_settings_set.setObjectName(u"bn_settings_set")
        self.bn_settings_set.setFont(font1)
        self.bn_settings_set.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")
        self.bn_settings_set.setFlat(True)

        self.verticalLayout_20.addWidget(self.bn_settings_set)

        self.comboBox_3 = QComboBox(self.page_settings)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(0, 0))
        self.comboBox_3.setFont(font4)

        self.verticalLayout_20.addWidget(self.comboBox_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_20)

        self.comboBox_4 = QComboBox(self.page_settings)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy3.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy3)
        self.comboBox_4.setFont(font4)

        self.horizontalLayout_10.addWidget(self.comboBox_4)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_10)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)

        self.label_29 = QLabel(self.page_settings)
        self.label_29.setObjectName(u"label_29")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy5)
        self.label_29.setFont(font1)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_29)

        self.lineEdit_8 = QLineEdit(self.page_settings)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font1)
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_8)

        self.label_30 = QLabel(self.page_settings)
        self.label_30.setObjectName(u"label_30")
        sizePolicy5.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy5)
        self.label_30.setFont(font1)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_30)

        self.lineEdit_9 = QLineEdit(self.page_settings)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font1)
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_9)

        self.label_31 = QLabel(self.page_settings)
        self.label_31.setObjectName(u"label_31")
        sizePolicy5.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy5)
        self.label_31.setFont(font1)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_31)

        self.lineEdit_10 = QLineEdit(self.page_settings)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font1)
        self.lineEdit_10.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lineEdit_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_2)


        self.horizontalLayout_16.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_11 = QLineEdit(self.page_settings)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_11.setFont(font4)
        self.lineEdit_11.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")
        self.lineEdit_11.setMaxLength(1)
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit_11)

        self.bn_settings_add = QPushButton(self.page_settings)
        self.bn_settings_add.setObjectName(u"bn_settings_add")
        self.bn_settings_add.setFont(font1)
        self.bn_settings_add.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")
        self.bn_settings_add.setFlat(True)

        self.horizontalLayout_11.addWidget(self.bn_settings_add)


        self.verticalLayout_22.addLayout(self.horizontalLayout_11)

        self.bn_settings_dell = QPushButton(self.page_settings)
        self.bn_settings_dell.setObjectName(u"bn_settings_dell")
        self.bn_settings_dell.setFont(font1)
        self.bn_settings_dell.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(200,66,66);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(230,80,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(190,60,60);\n"
"}")
        self.bn_settings_dell.setFlat(True)

        self.verticalLayout_22.addWidget(self.bn_settings_dell)

        self.bn_settings_save = QPushButton(self.page_settings)
        self.bn_settings_save.setObjectName(u"bn_settings_save")
        self.bn_settings_save.setFont(font1)
        self.bn_settings_save.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,120,150);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(50,130,170);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,120,150);\n"
"}")

        self.verticalLayout_22.addWidget(self.bn_settings_save)

        self.bn_settings_delprofile = QPushButton(self.page_settings)
        self.bn_settings_delprofile.setObjectName(u"bn_settings_delprofile")
        self.bn_settings_delprofile.setFont(font1)
        self.bn_settings_delprofile.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(200,66,66);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(230,80,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(190,60,60);\n"
"}")

        self.verticalLayout_22.addWidget(self.bn_settings_delprofile)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_4)


        self.horizontalLayout_16.addLayout(self.verticalLayout_22)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 33))
        font9 = QFont()
        font9.setPointSize(16)
        self.menubar.setFont(font9)
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 lightgray, stop:1 darkgray);\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: rgb(120,120,120);\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: rgb(160,140,140);\n"
"}")
        self.menuBaza_danych = QMenu(self.menubar)
        self.menuBaza_danych.setObjectName(u"menuBaza_danych")
        self.menuUstawienia_sesji = QMenu(self.menubar)
        self.menuUstawienia_sesji.setObjectName(u"menuUstawienia_sesji")
        self.menuStronaglowna = QMenu(self.menubar)
        self.menuStronaglowna.setObjectName(u"menuStronaglowna")
        self.menuUstawienia = QMenu(self.menubar)
        self.menuUstawienia.setObjectName(u"menuUstawienia")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuStronaglowna.menuAction())
        self.menubar.addAction(self.menuUstawienia_sesji.menuAction())
        self.menubar.addAction(self.menuBaza_danych.menuAction())
        self.menubar.addAction(self.menuUstawienia.menuAction())
        self.menuBaza_danych.addAction(self.actionOtworzbazedanych)
        self.menuBaza_danych.addSeparator()
        self.menuBaza_danych.addAction(self.actionEdytujbazedanych)
        self.menuUstawienia_sesji.addAction(self.actionZaloguj)
        self.menuUstawienia_sesji.addAction(self.actionWyloguj)
        self.menuUstawienia_sesji.addSeparator()
        self.menuUstawienia_sesji.addSeparator()
        self.menuUstawienia_sesji.addAction(self.actionConnectDatabase)
        self.menuUstawienia_sesji.addAction(self.actionDisconnectDatabase)
        self.menuStronaglowna.addAction(self.actionBacktomain)
        self.menuUstawienia.addAction(self.actionUstawienia_globalne_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.actionZalohuj.setText(QCoreApplication.translate("MainWindow", u"Zalohuj", None))
        self.actionZaloguj.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.actionWyloguj.setText(QCoreApplication.translate("MainWindow", u"Wyloguj", None))
        self.actionOtworzbazedanych.setText(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz baz\u0119 danych", None))
        self.actionEdytujbazedanych.setText(QCoreApplication.translate("MainWindow", u"Edytuj baz\u0119 danych", None))
        self.actionUstawienia_globalne.setText(QCoreApplication.translate("MainWindow", u"Ustawienia globalne", None))
        self.actionBacktomain.setText(QCoreApplication.translate("MainWindow", u"Wr\u00f3\u0107 do strony g\u0142\u00f3wnej", None))
        self.actionConnectDatabase.setText(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105cz z baz\u0105 danych", None))
        self.actionDisconnectDatabase.setText(QCoreApplication.translate("MainWindow", u"Roz\u0142\u0105cz z baz\u0105 danych", None))
        self.actionUstawienia_globalne_2.setText(QCoreApplication.translate("MainWindow", u"Ustawienia globalne", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zalogowano jako:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"{name}", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Profil:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"{profil}", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nazwa cz\u0119\u015bci (wymagane)", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nazwa cz\u0119\u015bci (wymagane)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Komentarz (opcjonalny)", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Komentarz (opcjonalny)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Do cz\u0119\u015bci {button} przydzielono numer: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"{num}", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Adres hosta:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"U\u017cytkownik:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Has\u0142o:", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[127.0.0.1]", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[root]", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[password]", None))
        self.bn_databaselogin.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.bn_databaseSet.setText(QCoreApplication.translate("MainWindow", u" Ustaw ", None))
        self.bn_databaseInfo.setText(QCoreApplication.translate("MainWindow", u">\n"
">\n"
">", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Numer:", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Litera:", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Komentarz:", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Zakres dzia\u0142ania rodzica (litery):", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Sygnatura czasowa:", None))
        self.label_25.setText("")
        self.bn_databaseDel.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Kod/Has\u0142o:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[Imi\u0119 Nazwisko]", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[1234]", None))
        self.bn_login.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Wybierz profil", None))
        self.bn_settings_set.setText(QCoreApplication.translate("MainWindow", u"Ustaw", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Nazwa profilu", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Minimalny zakres numeracji", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Maksymalny zakres numeracji", None))
        self.bn_settings_add.setText(QCoreApplication.translate("MainWindow", u"Dodaj liter\u0119", None))
        self.bn_settings_dell.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 liter\u0119", None))
        self.bn_settings_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz profil", None))
        self.bn_settings_delprofile.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 profil", None))
        self.menuBaza_danych.setTitle(QCoreApplication.translate("MainWindow", u"Baza danych", None))
        self.menuUstawienia_sesji.setTitle(QCoreApplication.translate("MainWindow", u"Ustawienia sesji", None))
        self.menuStronaglowna.setTitle(QCoreApplication.translate("MainWindow", u"Strona g\u0142\u00f3wna", None))
        self.menuUstawienia.setTitle(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
    # retranslateUi

