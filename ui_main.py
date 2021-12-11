# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 300)
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
        font.setFamily(u"Segoe UI")
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
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

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
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_9 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.comboBox = QComboBox(self.page_settings)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setFont(font1)

        self.horizontalLayout_8.addWidget(self.comboBox)

        self.lineEdit_6 = QLineEdit(self.page_settings)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy1)
        self.lineEdit_6.setFont(font1)
        self.lineEdit_6.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_6.setMaxLength(3)

        self.horizontalLayout_8.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.page_settings)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy1)
        self.lineEdit_7.setFont(font1)

        self.horizontalLayout_8.addWidget(self.lineEdit_7)

        self.label_10 = QLabel(self.page_settings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(40)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.page_settings)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setFont(font1)

        self.horizontalLayout_8.addWidget(self.lineEdit_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.bn_settadd = QPushButton(self.page_settings)
        self.bn_settadd.setObjectName(u"bn_settadd")
        self.bn_settadd.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bn_settadd.sizePolicy().hasHeightForWidth())
        self.bn_settadd.setSizePolicy(sizePolicy1)
        self.bn_settadd.setFont(font1)
        self.bn_settadd.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.bn_settadd)

        self.bn_settdel = QPushButton(self.page_settings)
        self.bn_settdel.setObjectName(u"bn_settdel")
        self.bn_settdel.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bn_settdel.sizePolicy().hasHeightForWidth())
        self.bn_settdel.setSizePolicy(sizePolicy1)
        self.bn_settdel.setFont(font1)
        self.bn_settdel.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.bn_settdel)


        self.horizontalLayout_10.addLayout(self.verticalLayout_11)

        self.bn_settswitch = QPushButton(self.page_settings)
        self.bn_settswitch.setObjectName(u"bn_settswitch")
        self.bn_settswitch.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bn_settswitch.sizePolicy().hasHeightForWidth())
        self.bn_settswitch.setSizePolicy(sizePolicy1)
        self.bn_settswitch.setFont(font1)
        self.bn_settswitch.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.bn_settswitch)

        self.bn_settsave = QPushButton(self.page_settings)
        self.bn_settsave.setObjectName(u"bn_settsave")
        self.bn_settsave.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bn_settsave.sizePolicy().hasHeightForWidth())
        self.bn_settsave.setSizePolicy(sizePolicy1)
        self.bn_settsave.setFont(font1)
        self.bn_settsave.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.bn_settsave)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.page_settings)
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
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(36)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.page_database_login)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.page_database_login)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_3 = QLineEdit(self.page_database_login)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setFont(font3)

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.page_database_login)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setFont(font3)

        self.verticalLayout_9.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.page_database_login)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setFont(font3)
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
"")

        self.verticalLayout_7.addWidget(self.bn_databaselogin)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.page_database_login)
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
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_login)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.page_login)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setFont(font3)
        self.lineEdit.setMaxLength(20)

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.page_login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.lineEdit_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.bn_login = QPushButton(self.page_login)
        self.bn_login.setObjectName(u"bn_login")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(22)
        self.bn_login.setFont(font4)
        self.bn_login.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")
        self.bn_login.setFlat(True)

        self.verticalLayout_6.addWidget(self.bn_login)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_login)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        font5 = QFont()
        font5.setPointSize(16)
        self.menubar.setFont(font5)
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
        self.menuUstawienia = QMenu(self.menubar)
        self.menuUstawienia.setObjectName(u"menuUstawienia")
        self.menuStronaglowna = QMenu(self.menubar)
        self.menuStronaglowna.setObjectName(u"menuStronaglowna")
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
        self.menuUstawienia.addAction(self.actionUstawienia_globalne)
        self.menuStronaglowna.addAction(self.actionBacktomain)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zalogowano pomy\u015blnie jako:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"{name}", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Do cz\u0119\u015bci {button} przydzielono numer: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"{num}", None))
        self.comboBox.setPlaceholderText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Litera (max3 znaki)", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Min. zakres", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Max. zakres", None))
        self.bn_settadd.setText(QCoreApplication.translate("MainWindow", u"Dodaj liter\u0119", None))
        self.bn_settdel.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 liter\u0119", None))
        self.bn_settswitch.setText(QCoreApplication.translate("MainWindow", u"Prze\u0142\u0105cz edytowanie", None))
        self.bn_settsave.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Adres hosta:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"U\u017cytkownik:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Has\u0142o:", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[127.0.0.1]", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[root]", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[password]", None))
        self.bn_databaselogin.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Kod/Has\u0142o:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[Imi\u0119 Nazwisko]", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[123456]", None))
        self.bn_login.setText(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.menuBaza_danych.setTitle(QCoreApplication.translate("MainWindow", u"Baza danych", None))
        self.menuUstawienia_sesji.setTitle(QCoreApplication.translate("MainWindow", u"Ustawienia sesji", None))
        self.menuUstawienia.setTitle(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.menuStronaglowna.setTitle(QCoreApplication.translate("MainWindow", u"Strona g\u0142\u00f3wna", None))
    # retranslateUi

