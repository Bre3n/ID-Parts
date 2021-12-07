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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bn_first = QPushButton(self.widget)
        self.bn_first.setObjectName(u"bn_first")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(36)
        self.bn_first.setFont(font1)
        self.bn_first.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: red;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.bn_first, 0, 0, 1, 1)

        self.bn_second = QPushButton(self.widget)
        self.bn_second.setObjectName(u"bn_second")
        self.bn_second.setFont(font1)
        self.bn_second.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:blue;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(85, 0, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 127);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.bn_second, 0, 1, 1, 1)

        self.bn_third = QPushButton(self.widget)
        self.bn_third.setObjectName(u"bn_third")
        self.bn_third.setFont(font1)
        self.bn_third.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: green;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(0, 85, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.bn_third, 0, 2, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.menubar.setFont(font2)
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
        self.menuZaloguj = QMenu(self.menubar)
        self.menuZaloguj.setObjectName(u"menuZaloguj")
        self.menuZaloguj.setFont(font2)
        self.menuZaloguj.setStyleSheet(u"")
        self.menuWyloguj = QMenu(self.menubar)
        self.menuWyloguj.setObjectName(u"menuWyloguj")
        self.menuOtw_rz_list = QMenu(self.menubar)
        self.menuOtw_rz_list.setObjectName(u"menuOtw_rz_list")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuZaloguj.menuAction())
        self.menubar.addAction(self.menuWyloguj.menuAction())
        self.menubar.addAction(self.menuOtw_rz_list.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zalogowano jako:", None))
        self.bn_first.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.bn_second.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.bn_third.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.menuZaloguj.setTitle(QCoreApplication.translate("MainWindow", u"Zaloguj", None))
        self.menuWyloguj.setTitle(QCoreApplication.translate("MainWindow", u"Wyloguj", None))
        self.menuOtw_rz_list.setTitle(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz list\u0119", None))
    # retranslateUi

