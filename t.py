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


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        global positions, value, position, values

        values = ["D", "M", "C", "96", "5", "69", "7", "36"]

        self.buttons = {}

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QGridLayout(self.centralwidget)

        positions = [(r, c) for r in range(3) for c in range(3)]

        for i in range(len(values)):
            position = positions[i]
            self.createButton(values[i], position)

    def createButton(self, text, position):
        self.buttons[text] = QPushButton("New Button{}".format(text), self)
        self.buttons[text].clicked.connect(
            lambda: print("\nclicked===>> {}".format(self.buttons[text].text()))
        )
        self.buttons[text].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.buttons[text].resizeEvent = self.resizeText
        self.lay.addWidget(self.buttons[text], *position)

    def resizeText(self, event):
        defaultSize = 20
        for i in range(len(values)):
            if self.rect().width() // defaultSize > defaultSize:
                f = QFont("Segoe UI", self.rect().width() * 0.035)
            else:
                f = QFont("Segoe UI", defaultSize)

            self.buttons[values[i]].setFont(f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
