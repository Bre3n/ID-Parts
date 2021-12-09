# 2*x&FY


import base64
import os
from os import path
import random
import sys
import threading
from multiprocessing import Process
import time
import mysql.connector

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
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

from ui_main import Ui_MainWindow


def crypto(message, var):
    # * get global key
    password_provided = "-5Z#h)7a!_s=x9yT"
    password = password_provided.encode()
    salt = b"\xe1&z\x7f\xad\xf0\xb4\xb6\xa8\xc0\xc5\xd9\xcea\xe6\xdb"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)
    if var == 0:
        # * encrypt
        encoded = message.encode()
        encrypted = f.encrypt(encoded)
        return encrypted
    elif var == 1:
        # * decrypt
        decrypted = f.decrypt(message)
        org = decrypted.decode()
        return org


def logintoall(self):

    global userlogin, userpassword, databasehostname, databaseuser, databasepassword, database_connected, mydb

    # * USER
    if path.exists(f"{inipath}/fileuserlogin.txt") == True:
        fileUSER = open(f"{inipath}/fileuserlogin.txt", "rb")
        userlogin = crypto(fileUSER.read(), 1)
        fileUSER.close()

    if path.exists(f"{inipath}/fileuserpassword.txt") == True:
        fileUSER = open(f"{inipath}/fileuserpassword.txt", "rb")
        userpassword = crypto(fileUSER.read(), 1)
        fileUSER.close()

    # * DATABASE
    if path.exists(f"{inipath}/filedbhostname.txt") == True:
        fileDB = open(f"{inipath}/filedbhostname.txt", "rb")
        databasehostname = crypto(fileDB.read(), 1)
        fileDB.close()

    if path.exists(f"{inipath}/filedbuser.txt") == True:
        fileDB = open(f"{inipath}/filedbuser.txt", "rb")
        databaseuser = crypto(fileDB.read(), 1)
        fileDB.close()

    if path.exists(f"{inipath}/filedbpassword.txt") == True:
        fileDB = open(f"{inipath}/filedbpassword.txt", "rb")
        databasepassword = crypto(fileDB.read(), 1)
        fileDB.close()

    if (
        path.exists(f"{inipath}/filedbhostname.txt") == True
        or path.exists(f"{inipath}/filedbuser.txt") == True
        or path.exists(f"{inipath}/filedbpassword.txt") == True
    ):
        try:
            mydb = mysql.connector.connect(
                host=databasehostname,
                user=databaseuser,
                password=databasepassword,
                database="partsid-database",
            )

            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("SELECT * FROM password")
            myresult = mycursor.fetchone()
            database_connected = True
            print("adsadsdas")
            if userpassword == myresult[0]:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
                logged = True
                self.ui.label_4.setText(userlogin)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(
                    "Nie zalogowano do sesji. Ustawienia sesji -> Zaloguj"
                )
                msg.setWindowTitle("Error")
                msg.exec_()
        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(
                "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych "
            )
            msg.setWindowTitle("Error")
            msg.exec_()

    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(
            "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych "
        )
        msg.setWindowTitle("Error")
        msg.exec_()

    print(userlogin, userpassword)


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global positions, value, position, values, widthsize, heightsize, logoutses, logout_database, database_connected, config, inipath, userlogin, userpassword, databasehostname, databaseuser, databasepassword
        logoutses, logout_database, database_connected = False, False, False
        userlogin, userpassword, databasehostname, databaseuser, databasepassword = (
            "",
            "",
            "",
            "",
            "",
        )

        user = os.getlogin()
        inipath = f"C:/Users/{user}/AppData/LocalLow/PartsID"
        if path.exists(f"{inipath}") == False:
            os.mkdir(f"{inipath}")

        # self.createFiles()

        logintoall(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)

        self.resize(650, 400)
        self.setMinimumSize(600, 300)

        self.setWindowTitle("Parts ID's")
        self.setStyleSheet("background:rgb(91,90,90);")

        self.ui.buttons = {}

        self.setCentralWidget(self.ui.centralwidget)
        self.ui.centralwidget = QWidget()

        positions = [(r, c) for r in range(4) for c in range(4)]
        # * to split to 3

        # * actionBar
        # * Back to main page
        self.ui.actionBacktomain.triggered.connect(self.main_page)
        # * Session
        self.ui.actionZaloguj.triggered.connect(lambda: UserLoginClass(self))
        self.ui.actionWyloguj.triggered.connect(lambda: self.logout(1))
        self.ui.actionConnectDatabase.triggered.connect(lambda: DatabaseLogin(self))
        self.ui.actionDisconnectDatabase.triggered.connect(lambda: self.logout(2))
        # * Database

        #! connect to database first!!
        values = ["D", "M", "C", "G"]  # * << buttons in layout

        size = ((len(values) / 4) - 1) * 50
        widthsize, heightsize = 700 + size, 350 + size
        self.setMinimumSize(widthsize, heightsize)

        for i in range(len(values)):
            # * create buttons for len of values
            position = positions[i]
            self.createButton(values[i], position)

    def createButton(self, text, position):
        # * create button
        self.ui.buttons[text] = QPushButton("{}".format(text), self)
        self.ui.buttons[text].clicked.connect(
            lambda: print("\nclicked===>> {}".format(self.ui.buttons[text].text()))
        )
        self.ui.buttons[text].setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.buttons[text].resizeEvent = self.resizeText

        color = ""
        for i in range(2):
            color += (str(random.randint(0, 200))) + ","
        color += str(random.randint(0, 200))
        QPushButtonStyle = (
            f"border: none;background-color: rgb({color});border-radius: 10px;"
        )
        QPushButton_HoverStyle = f"background-color: rgb(85, 0, 0);"
        QPushButton_PressedStyle = f"background-color: rgb(170, 0, 0);"

        StyleSheet = (
            "QPushButton {"
            + QPushButtonStyle
            + "} QPushButton:hover {"
            + QPushButton_HoverStyle
            + "} QPushButton:pressed {"
            + QPushButton_PressedStyle
            + "}"
        )
        self.ui.buttons[text].setStyleSheet(StyleSheet)

        self.ui.gridLayout.addWidget(self.ui.buttons[text], *position)

    def resizeText(self, event):
        defaultSize = 50
        print((self.rect().width() * self.rect().height()) / 1000)
        print(self.rect().width() // (defaultSize // 10) > defaultSize)
        # * print width * height
        # * print if True or False

        for i in range(len(values)):
            if self.rect().height() > heightsize + 100:
                if ((self.rect().width() * self.rect().height()) / 1000 * 0.2) > 60:
                    f = QFont(
                        "Segoe UI",
                        (self.rect().width() * self.rect().height()) / 1000 * 0.13,
                    )
                else:
                    f = QFont("Segoe UI", defaultSize)
            else:
                f = QFont("Segoe UI", defaultSize)

            self.ui.buttons[values[i]].setFont(f)

    def createFiles(self):
        pass

    def main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)

    def logout(self, var):
        global logoutses, logout_database
        if var == 1:
            if logoutses == False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Information")
                msg.setInformativeText("Kliknij raz jeszcze aby się wylogować")
                msg.setWindowTitle("Error")
                msg.exec_()
                logoutses = True
                threading.Thread(target=self.logout2, args=(var,)).start()
            else:
                logoutses = False
                if path.exists(f"{inipath}/fileuserlogin.txt") == True:
                    os.remove(f"{inipath}/fileuserlogin.txt")

                if path.exists(f"{inipath}/fileuserpassword.txt") == True:
                    os.remove(f"{inipath}/fileuserpassword.txt")

                self.ui.label_4.setText("none")
        elif var == 2:
            if logout_database == False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Information")
                msg.setInformativeText(
                    "Kliknij raz jeszcze aby wylogować się z bazy danych"
                )
                msg.setWindowTitle("Error")
                msg.exec_()
                logout_database = True
                threading.Thread(target=self.logout2, args=(var,)).start()
            else:
                database_connected = False
                if path.exists(f"{inipath}/filedbhostname.txt") == True:
                    os.remove(f"{inipath}/filedbhostname.txt")

                if path.exists(f"{inipath}/filedbuser.txt") == True:
                    os.remove(f"{inipath}/filedbuser.txt")

                if path.exists(f"{inipath}/filedbpassword.txt") == True:
                    os.remove(f"{inipath}/filedbpassword.txt")

    def logout2(self, var):
        global logoutses, logout_database
        time.sleep(10)
        if var == 1:
            logoutses = False
        elif var == 2:
            logout_database = False

    def openList(self):
        pass


class UserLoginClass:
    def __init__(self, selfui):
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_login)
        selfui.ui.bn_login.clicked.connect(lambda: self.login(selfui))

    def login(self, selfui):
        global database_connected, mydb, logged
        if selfui.ui.lineEdit.text() == "" or selfui.ui.lineEdit_2.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Login bądź kod dostępu jest pusty!")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            if database_connected == True:
                userlogin = (selfui.ui.lineEdit.text()).title()
                userpassword = selfui.ui.lineEdit_2.text()

                mycursorr = mydb.cursor(buffered=True)
                mycursorr.execute("SELECT * FROM password")
                myresultt = mycursorr.fetchone()
                if userpassword == myresultt[0]:
                    fileUSER = open(f"{inipath}/fileuserlogin.txt", "wb")
                    fileUSER.write(crypto(userlogin, 0))
                    fileUSER.close()
                    fileUSER = open(f"{inipath}/fileuserpassword.txt", "wb")
                    fileUSER.write(crypto(userpassword, 0))
                    fileUSER.close()
                    logged = True
                    selfui.ui.label_4.setText(userlogin)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Information")
                    msg.setInformativeText("Zalogowano pomyślnie!")
                    msg.setWindowTitle("Information")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(
                        "Nie można się zalogować, nieprawidłowy kod dostępu!"
                    )
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(
                    "Nie można się zalogować, nie jesteś połączony z bazą danych!"
                )
                msg.setWindowTitle("Error")
                msg.exec_()


class DatabaseLogin:
    def __init__(self, selfui):
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_database_login)
        selfui.ui.bn_databaselogin.clicked.connect(lambda: self.database_login(selfui))

    def database_login(self, selfui):
        global mydb, database_connected
        if (
            selfui.ui.lineEdit_3.text() == ""
            or selfui.ui.lineEdit_4.text() == ""
            or selfui.ui.lineEdit_5.text() == ""
        ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Adres hosta, użytkownik bądź hasło jest puste!")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            try:
                mydb = mysql.connector.connect(
                    host=f"{str(selfui.ui.lineEdit_3.text())}",
                    user=f"{str(selfui.ui.lineEdit_4.text())}",
                    password=f"{str(selfui.ui.lineEdit_5.text())}",
                    database="partsid-database",
                )

                fileDB = open(f"{inipath}/filedbhostname.txt", "wb")
                fileDB.write(crypto(selfui.ui.lineEdit_3.text(), 0))
                fileDB.close()
                fileDB = open(f"{inipath}/filedbuser.txt", "wb")
                fileDB.write(crypto(selfui.ui.lineEdit_4.text(), 0))
                fileDB.close()
                fileDB = open(f"{inipath}/filedbpassword.txt", "wb")
                fileDB.write(crypto(selfui.ui.lineEdit_5.text(), 0))
                fileDB.close()

                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("SELECT * FROM password")
                myresult = mycursor.fetchone()
                database_connected = True
                if userpassword == myresult[0]:
                    selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_main)
                else:
                    selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_login)
            except Exception as e:
                print(e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(
                    "Adres hosta, użytkownik bądź hasło jest nieprawidłowe!"
                )
                msg.setWindowTitle("Error")
                msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
