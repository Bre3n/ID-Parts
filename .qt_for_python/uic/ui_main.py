# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.actionUstawienia_globalne_2.setFont(font)
        self.actionversion = QAction(MainWindow)
        self.actionversion.setObjectName(u"actionversion")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.actionversion.setFont(font1)
        self.actionWybierz_profil = QAction(MainWindow)
        self.actionWybierz_profil.setObjectName(u"actionWybierz_profil")
        self.actionWybierz_profil.setFont(font)
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_29 = QLabel(self.page_main)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_29)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_27 = QLabel(self.page_main)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_27)

        self.label_28 = QLabel(self.page_main)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
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
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)

        self.lineEdit_6 = QLineEdit(self.page_main)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(18)
        self.lineEdit_6.setFont(font4)
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
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.lineEdit_7 = QLineEdit(self.page_main)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(16)
        self.lineEdit_7.setFont(font5)
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
        self.label.setEnabled(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_30 = QLabel(self.page_main)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"border:5px solid black;\n"
"border-bottom: 5px solid red;\n"
"border-top: 5px solid red;\n"
"")

        self.horizontalLayout.addWidget(self.label_30)

        self.label_31 = QLabel(self.page_main)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.horizontalLayout.addWidget(self.label_31)

        self.label_2 = QLabel(self.page_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border:5px solid black;\n"
"border-bottom: 5px solid red;\n"
"border-top: 5px solid red;\n"
"")

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
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(36)
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.page_database_login)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.page_database_login)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)
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
        self.lineEdit_3.setFont(font6)
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.page_database_login)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setFont(font6)
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_9.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.page_database_login)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setFont(font6)
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.lineEdit_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.label_40 = QLabel(self.page_database_login)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"Courier New"])
        self.label_40.setFont(font7)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_40)

        self.bn_databaselogin = QPushButton(self.page_database_login)
        self.bn_databaselogin.setObjectName(u"bn_databaselogin")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(22)
        self.bn_databaselogin.setFont(font8)
        self.bn_databaselogin.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #FF6F61;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #FF958A;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #FF6F61;\n"
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
        self.label_38 = QLabel(self.page_database)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_38)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_9)

        self.db_radiobox = QRadioButton(self.page_database)
        self.db_radiobox.setObjectName(u"db_radiobox")
        self.db_radiobox.setFont(font3)
        self.db_radiobox.setStyleSheet(u"QRadioButton {\n"
"    color:black;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")

        self.horizontalLayout_22.addWidget(self.db_radiobox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.bn_database_back = QPushButton(self.page_database)
        self.bn_database_back.setObjectName(u"bn_database_back")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bn_database_back.sizePolicy().hasHeightForWidth())
        self.bn_database_back.setSizePolicy(sizePolicy3)
        font9 = QFont()
        font9.setPointSize(18)
        self.bn_database_back.setFont(font9)
        self.bn_database_back.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(200,66,66);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(230,80,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(190,60,60);\n"
"}")
        self.bn_database_back.setIconSize(QSize(35, 35))

        self.horizontalLayout_16.addWidget(self.bn_database_back)

        self.lineEdit_13 = QLineEdit(self.page_database)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy4)
        self.lineEdit_13.setFont(font5)
        self.lineEdit_13.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.lineEdit_13)

        self.bn_database_search = QPushButton(self.page_database)
        self.bn_database_search.setObjectName(u"bn_database_search")
        sizePolicy3.setHeightForWidth(self.bn_database_search.sizePolicy().hasHeightForWidth())
        self.bn_database_search.setSizePolicy(sizePolicy3)
        self.bn_database_search.setFont(font5)
        self.bn_database_search.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")

        self.horizontalLayout_16.addWidget(self.bn_database_search)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBox_2 = QComboBox(self.page_database)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy4.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy4)
        self.comboBox_2.setFont(font2)

        self.horizontalLayout_15.addWidget(self.comboBox_2)

        self.bn_databaseSet = QPushButton(self.page_database)
        self.bn_databaseSet.setObjectName(u"bn_databaseSet")
        sizePolicy.setHeightForWidth(self.bn_databaseSet.sizePolicy().hasHeightForWidth())
        self.bn_databaseSet.setSizePolicy(sizePolicy)
        self.bn_databaseSet.setFont(font2)
        self.bn_databaseSet.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"border-radius:7px;\n"
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
        self.comboBox.setFont(font5)
        self.comboBox.setMaxVisibleItems(50)

        self.verticalLayout_12.addWidget(self.comboBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.bn_databaseInfo = QPushButton(self.page_database)
        self.bn_databaseInfo.setObjectName(u"bn_databaseInfo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bn_databaseInfo.sizePolicy().hasHeightForWidth())
        self.bn_databaseInfo.setSizePolicy(sizePolicy5)
        self.bn_databaseInfo.setFont(font2)
        self.bn_databaseInfo.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(150,60,180);\n"
"border-radius:5px;\n"
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
        sizePolicy3.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy3)
        self.page_database_view = QWidget()
        self.page_database_view.setObjectName(u"page_database_view")
        self.verticalLayout_15 = QVBoxLayout(self.page_database_view)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_10)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea = QScrollArea(self.page_database_view)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -211, 358, 504))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_13)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_15)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_16)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_17)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_18)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setOpenExternalLinks(True)

        self.verticalLayout_18.addWidget(self.label_19)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_21)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_22)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_23)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_24)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
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
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.label_39 = QLabel(self.page_database_edit)
        self.label_39.setObjectName(u"label_39")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy6)
        self.label_39.setFont(font2)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_39)

        self.bn_databaseDel = QPushButton(self.page_database_edit)
        self.bn_databaseDel.setObjectName(u"bn_databaseDel")
        sizePolicy4.setHeightForWidth(self.bn_databaseDel.sizePolicy().hasHeightForWidth())
        self.bn_databaseDel.setSizePolicy(sizePolicy4)
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(26)
        self.bn_databaseDel.setFont(font10)
        self.bn_databaseDel.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(200,66,66);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(230,80,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(190,60,60);\n"
"}")

        self.verticalLayout_16.addWidget(self.bn_databaseDel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)


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
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_login)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.page_login)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setFont(font6)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit.setMaxLength(20)

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.page_login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setFont(font6)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.lineEdit_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.bn_login = QPushButton(self.page_login)
        self.bn_login.setObjectName(u"bn_login")
        self.bn_login.setFont(font8)
        self.bn_login.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: #FF6F61;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #FF958A;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #FF6F61;\n"
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
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setMaximumSize(QSize(16777215, 50))
        self.label_26.setFont(font2)
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
        self.stackedWidget_3 = QStackedWidget(self.page_settings)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"")
        self.page_settings_global = QWidget()
        self.page_settings_global.setObjectName(u"page_settings_global")
        self.horizontalLayout_20 = QHBoxLayout(self.page_settings_global)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.bn_settings_set = QPushButton(self.page_settings_global)
        self.bn_settings_set.setObjectName(u"bn_settings_set")
        self.bn_settings_set.setFont(font2)
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

        self.verticalLayout_23.addWidget(self.bn_settings_set)

        self.comboBox_3 = QComboBox(self.page_settings_global)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(0, 0))
        self.comboBox_3.setFont(font5)

        self.verticalLayout_23.addWidget(self.comboBox_3)


        self.horizontalLayout_18.addLayout(self.verticalLayout_23)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_41 = QLabel(self.page_settings_global)
        self.label_41.setObjectName(u"label_41")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy7)
        self.label_41.setMinimumSize(QSize(100, 37))
        self.label_41.setMaximumSize(QSize(100, 16777215))
        self.label_41.setFont(font)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_41)

        self.comboBox_4 = QComboBox(self.page_settings_global)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy5.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy5)
        self.comboBox_4.setFont(font5)

        self.verticalLayout_20.addWidget(self.comboBox_4)


        self.horizontalLayout_18.addLayout(self.verticalLayout_20)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_5)

        self.label_32 = QLabel(self.page_settings_global)
        self.label_32.setObjectName(u"label_32")
        sizePolicy4.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy4)
        self.label_32.setMaximumSize(QSize(300, 16777215))
        self.label_32.setFont(font4)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_32)

        self.lineEdit_8 = QLineEdit(self.page_settings_global)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy2.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy2)
        self.lineEdit_8.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_8.setFont(font2)
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
        self.lineEdit_8.setMaxLength(63)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.lineEdit_8)

        self.label_33 = QLabel(self.page_settings_global)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)
        self.label_33.setMaximumSize(QSize(300, 16777215))
        self.label_33.setFont(font4)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_33)

        self.lineEdit_9 = QLineEdit(self.page_settings_global)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy2.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy2)
        self.lineEdit_9.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_9.setFont(font2)
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

        self.verticalLayout_24.addWidget(self.lineEdit_9)

        self.label_34 = QLabel(self.page_settings_global)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setMaximumSize(QSize(300, 16777215))
        self.label_34.setFont(font4)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_34)

        self.lineEdit_10 = QLineEdit(self.page_settings_global)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy2.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy2)
        self.lineEdit_10.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_10.setFont(font2)
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

        self.verticalLayout_24.addWidget(self.lineEdit_10)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_6)


        self.horizontalLayout_17.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_7)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lineEdit_11 = QLineEdit(self.page_settings_global)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_11.setFont(font5)
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
        self.lineEdit_11.setMaxLength(10)
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.lineEdit_11)

        self.bn_settings_add = QPushButton(self.page_settings_global)
        self.bn_settings_add.setObjectName(u"bn_settings_add")
        self.bn_settings_add.setFont(font2)
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

        self.horizontalLayout_19.addWidget(self.bn_settings_add)


        self.verticalLayout_25.addLayout(self.horizontalLayout_19)

        self.label_42 = QLabel(self.page_settings_global)
        self.label_42.setObjectName(u"label_42")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        self.label_42.setFont(font11)

        self.verticalLayout_25.addWidget(self.label_42)

        self.bn_settings_dell = QPushButton(self.page_settings_global)
        self.bn_settings_dell.setObjectName(u"bn_settings_dell")
        self.bn_settings_dell.setFont(font2)
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

        self.verticalLayout_25.addWidget(self.bn_settings_dell)

        self.bn_settings_save = QPushButton(self.page_settings_global)
        self.bn_settings_save.setObjectName(u"bn_settings_save")
        self.bn_settings_save.setFont(font2)
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

        self.verticalLayout_25.addWidget(self.bn_settings_save)

        self.bn_settings_delprofile = QPushButton(self.page_settings_global)
        self.bn_settings_delprofile.setObjectName(u"bn_settings_delprofile")
        self.bn_settings_delprofile.setFont(font2)
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

        self.verticalLayout_25.addWidget(self.bn_settings_delprofile)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_8)


        self.horizontalLayout_17.addLayout(self.verticalLayout_25)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_17)

        self.stackedWidget_3.addWidget(self.page_settings_global)
        self.page_settings_login = QWidget()
        self.page_settings_login.setObjectName(u"page_settings_login")
        self.verticalLayout_27 = QVBoxLayout(self.page_settings_login)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_35 = QLabel(self.page_settings_login)
        self.label_35.setObjectName(u"label_35")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(32)
        self.label_35.setFont(font12)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_35)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEdit_12 = QLineEdit(self.page_settings_login)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font6)
        self.lineEdit_12.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_12.setEchoMode(QLineEdit.Password)
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_12)

        self.bn_settings_login_bn = QPushButton(self.page_settings_login)
        self.bn_settings_login_bn.setObjectName(u"bn_settings_login_bn")
        self.bn_settings_login_bn.setFont(font6)
        self.bn_settings_login_bn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(50,150,50);\n"
"}")

        self.horizontalLayout_21.addWidget(self.bn_settings_login_bn)


        self.verticalLayout_26.addLayout(self.horizontalLayout_21)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)

        self.checkBox = QCheckBox(self.page_settings_login)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font8)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"    color:black;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.checkBox)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_13)


        self.verticalLayout_27.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_9)

        self.stackedWidget_3.addWidget(self.page_settings_login)

        self.horizontalLayout_9.addWidget(self.stackedWidget_3)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_error = QWidget()
        self.page_error.setObjectName(u"page_error")
        self.horizontalLayout_11 = QHBoxLayout(self.page_error)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_36 = QLabel(self.page_error)
        self.label_36.setObjectName(u"label_36")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy8)
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(100)
        self.label_36.setFont(font13)
        self.label_36.setStyleSheet(u"")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_36)

        self.label_37 = QLabel(self.page_error)
        self.label_37.setObjectName(u"label_37")
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(28)
        self.label_37.setFont(font14)
        self.label_37.setScaledContents(False)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.label_37)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.page_error)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 33))
        font15 = QFont()
        font15.setPointSize(16)
        self.menubar.setFont(font15)
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
        self.menuStronaglowna.addAction(self.actionWybierz_profil)
        self.menuUstawienia.addAction(self.actionUstawienia_globalne_2)
        self.menuUstawienia.addSeparator()
        self.menuUstawienia.addAction(self.actionversion)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)


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
        self.actionversion.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.actionWybierz_profil.setText(QCoreApplication.translate("MainWindow", u"Wybierz profil", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zalogowano jako:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"{name}", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Profil:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"{profil}", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nazwa cz\u0119\u015bci (wymagane)", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nazwa cz\u0119\u015bci (wymagane)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Komentarz (opcjonalny)", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Komentarz (opcjonalny)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Do cz\u0119\u015bci ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"{czesc}", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u" przydzielono numer: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"{num}", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Adres hosta: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"U\u017cytkownik: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Has\u0142o: ", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[127.0.0.1]", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[root]", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[password]", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"O ile nie roz\u0142\u0105czono z baz\u0105 danych nie trzeba wpisywa\u0107 has\u0142a (czyli przy pierwszym uruchomieniu nie trzeba)", None))
        self.bn_databaselogin.setText(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105cz", None))
#if QT_CONFIG(shortcut)
        self.bn_databaselogin.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Szukaj po pe\u0142nej nazwie, numerze, literze lub autorze", None))
        self.db_radiobox.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119\u015b\u0107 nazwy (gdy znamy tylko cz\u0119\u015b\u0107 nazwy)", None))
        self.bn_database_back.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.lineEdit_13.setPlaceholderText("")
        self.bn_database_search.setText(QCoreApplication.translate("MainWindow", u" Szukaj ", None))
        self.bn_databaseSet.setText(QCoreApplication.translate("MainWindow", u" Ustaw ", None))
#if QT_CONFIG(shortcut)
        self.bn_databaseSet.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.comboBox.setPlaceholderText("")
        self.bn_databaseInfo.setText(QCoreApplication.translate("MainWindow", u">\n"
">\n"
">", None))
#if QT_CONFIG(shortcut)
        self.bn_databaseInfo.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Profil:", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Litera i numer:", None))
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
        self.label_39.setText("")
        self.bn_databaseDel.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Kod dost\u0119pu: ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[Imi\u0119 Nazwisko]", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[1234]", None))
        self.bn_login.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Wybierz profil", None))
        self.bn_settings_set.setText(QCoreApplication.translate("MainWindow", u"Ustaw", None))
        self.label_41.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Nazwa profilu", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Min. zakres numeracji", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Max. zakres numeracji", None))
        self.bn_settings_add.setText(QCoreApplication.translate("MainWindow", u" Dodaj liter\u0119 ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"^Dozwolone^ przecinki np. \"a,b,c\" max.5 liter\n"
"*Chwil\u0119 to potrwa, nie wy\u0142acza\u0107 programu!", None))
        self.bn_settings_dell.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 liter\u0119", None))
        self.bn_settings_save.setText(QCoreApplication.translate("MainWindow", u"Zapisz profil", None))
        self.bn_settings_delprofile.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 profil", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Podaj kod dost\u0119pu do zmiany ustawie\u0144", None))
        self.bn_settings_login_bn.setText(QCoreApplication.translate("MainWindow", u" Wprowad\u017a ", None))
#if QT_CONFIG(shortcut)
        self.bn_settings_login_bn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Zapami\u0119taj has\u0142o (do wy\u0142\u0105czenia programu)", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuBaza_danych.setTitle(QCoreApplication.translate("MainWindow", u"Baza danych", None))
        self.menuUstawienia_sesji.setTitle(QCoreApplication.translate("MainWindow", u"Ustawienia sesji", None))
        self.menuStronaglowna.setTitle(QCoreApplication.translate("MainWindow", u"Strona g\u0142\u00f3wna", None))
        self.menuUstawienia.setTitle(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
    # retranslateUi

