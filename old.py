import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QEvent,
    QMetaObject,
    QObject,
    QPoint,
    QPropertyAnimation,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
    Signal,
    Slot,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *
import random
import threading
from ui_main import Ui_MainWindow

# from . import database


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global positions, value, position, values

        values = ["D", "M", "C", "96", "5", "69", "7", "36"]

        positions = [(r, c) for r in range(3) for c in range(3)]

        self.ui.buttons = {}

        for position, value in zip(positions, values):
            self.ui.buttons[value] = QPushButton(str(value))
            self.ui.buttons[value].setSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Expanding
            )
            color = ""
            for i in range(2):
                color += (str(random.randint(0, 255))) + ","
            color += str(random.randint(0, 255))
            QPushButtonStyle = (
                f"border: none;background-color: rgb({color});border-radius: 10px;"
            )
            QPushButton_HoverStyle = f"background-color: rgb(85, 0, 0);"
            QPushButton_PressedStyle = f"background-color: rgb(170, 0, 0);"

            #self.ui.buttons[value].resizeEvent = self.resizeText
            StyleSheet = (
                "QPushButton {"
                + QPushButtonStyle
                + "} QPushButton:hover {"
                + QPushButton_HoverStyle
                + "} QPushButton:pressed {"
                + QPushButton_PressedStyle
                + "}"
            )
            self.ui.buttons[value].setStyleSheet(StyleSheet)
            #if 
            self.ui.buttons[value].clicked.connect(lambda: print(self.ui.buttons[value].text()))
            self.ui.gridLayout.addWidget(self.ui.buttons[value], *position)
        bufor = {}
        for position, value in zip(positions, values):
            print(position, value)
            bufor[value] = self.ui.buttons[value]
            print(bufor[value].text())
            aa = bufor[value].text()
            # bufor[value].clicked.connect(lambda: print(aa))
            bufor[value].setText(bufor[value].text())

    def resizeText(self, event):
        defaultSize = 40
        for position, value in zip(positions, values):
            if self.rect().width() // defaultSize > defaultSize:
                f = QFont("Segoe UI", self.rect().width() * 0.1)
            else:
                f = QFont("Segoe UI", defaultSize)

            self.ui.buttons[value].setFont(f)

    def aa(self, val):
        print(val)


def main():
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())


main()
