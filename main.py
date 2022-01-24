import base64
import ctypes
import datetime
import os
import random
import sys
import threading
import time
import webbrowser
from multiprocessing import Process
from os import path
import mysql.connector
import psutil
import requests
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

from ui_error import Ui_Error
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

    global userlogin, userpassword, databasehostname, databaseuser, databasepassword, database_connected, mycursor, logged, mydb

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
        and path.exists(f"{inipath}/filedbuser.txt") == True
        and path.exists(f"{inipath}/filedbpassword.txt") == True
    ):
        try:
            request = requests.get(url, timeout=5)
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_error)
            self.ui.label_36.setText("!")
            self.ui.label_37.setText(
                "Brak połączenia z internetem! Połącz się z siecią i zrestartuj program!"
            )
        try:
            mydb = mysql.connector.connect(
                host=databasehostname,
                user=databaseuser,
                password=databasepassword,
                database="partsid-database",
            )
            if mydb.is_connected() == False:
                self.ui.label_3.setText("Nie zalogowano do sesji!")
                self.ui.label_4.setText("")
                MainWindow.errorexec(
                    self,
                    "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych ",
                    "Ok",
                )
            else:
                self.ui.lineEdit_3.setPlaceholderText(databasehostname)
                self.ui.lineEdit_4.setPlaceholderText(databaseuser)
                self.ui.bn_databaselogin.setText("Połączono")
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("SELECT * FROM password")
                myresult = mycursor.fetchone()
                database_connected = True
                if str(userpassword) == str(myresult[0]):
                    logged = True
                    self.ui.bn_login.setText("Zalogowano")
                    self.ui.lineEdit.setPlaceholderText(userlogin)
                    self.ui.label_3.setText("Zalogowano pomyślnie jako:")
                    self.ui.label_4.setText(userlogin)

                    sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
                    val = (
                        f"Logged to database",
                        userlogin,
                        datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
                    )
                    mycursor.execute(sql, val)
                    mydb.commit()

                else:
                    self.ui.label_3.setText("Nie zalogowano do sesji!")
                    self.ui.label_4.setText("")
                    MainWindow.errorexec(
                        self,
                        "Nie zalogowano do sesji. Ustawienia sesji -> Zaloguj",
                        "Ok",
                    )
        except Exception as e:
            print(e)
            self.ui.label_3.setText("Nie zalogowano do sesji!")
            self.ui.label_4.setText("")
            MainWindow.errorexec(
                self,
                "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych ",
                "Ok",
            )

    else:
        self.ui.label_3.setText("Nie zalogowano do sesji!")
        self.ui.label_4.setText("")
        MainWindow.errorexec(
            self,
            "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych ",
            "Ok",
        )


def check_connection(self):
    global checkinternetbool
    while True:
        try:
            self.ui.label_36.setText(self.ui.label_36.text())
        except Exception:
            return None
        try:
            request = requests.get(url, timeout=5)
            if (
                self.ui.stackedWidget.currentIndex() == 6
                and self.ui.label_37.text()
                == "Brak połączenia z internetem! Połącz się z siecią"
            ):
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_error)
                self.ui.label_36.setText("")
                self.ui.label_37.setText(
                    "Połączono z intenetem! Wszystkie opcje odblokowane"
                )
            checkinternetbool = True
        except (requests.ConnectionError, requests.Timeout) as exception:
            if self.ui.stackedWidget.currentIndex() != 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_error)
                self.ui.label_36.setText("!")
                self.ui.label_37.setText(
                    "Brak połączenia z internetem! Połącz się z siecią"
                )
            checkinternetbool = False
        time.sleep(5)


class errorUi(QDialog):
    def __init__(self, parent=None):

        super(errorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.e.bn_ok.clicked.connect(lambda: self.close())

        self.dragPos = self.pos()

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.e.frame_top.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def errorConstrict(self, heading, btnOk):
        self.e.lab_heading.setText(heading)
        self.e.bn_ok.setText(btnOk)


def loginerror(self):
    time.sleep(1)
    self.ui.stackedWidget.setCurrentWidget(self.ui.page_error)
    self.ui.label_36.setText("!")
    self.ui.label_37.setText("Zaloguj się do bazy danych i profilu aby kontynuować")


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.error = errorUi()

        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

        global positions, value, position, values, widthsize, heightsize, logoutses, logout_database, database_connected, config, inipath, userlogin, userpassword, databasehostname, databaseuser, databasepassword, logged, switchEdit, mycursor, profile, defaultSize, database_profile, iterablebool, checkinternetbool, url

        (
            logoutses,
            logout_database,
            database_connected,
            logged,
            switchEdit,
            checkinternetbool,
        ) = (
            False,
            False,
            False,
            False,
            False,
            True,
        )
        (
            userlogin,
            userpassword,
            databasehostname,
            databaseuser,
            databasepassword,
            database_profile,
            url,
        ) = (
            "",
            "",
            "",
            "",
            "",
            "",
            "https://www.google.com",
        )

        defaultSize = 50

        print(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

        PROCNAME = "partsID.exe"

        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()

        user = os.getlogin()
        inipath = f"C:/Users/{user}/AppData/LocalLow/PartsID"
        if path.exists(f"{inipath}") == False:
            os.mkdir(f"{inipath}")

        logintoall(self)
        threading.Thread(target=check_connection, args=(self,)).start()

        if logged == False:
            threading.Thread(target=loginerror, args=(self,)).start()

        self.ui.buttons = {}

        self.setWindowTitle("Parts ID's")
        self.setStyleSheet("background:rgb(91,90,90);")

        self.setCentralWidget(self.ui.centralwidget)
        self.ui.centralwidget = QWidget()

        self.ui.label.setVisible(False)
        self.ui.label_2.setVisible(False)
        self.ui.label_30.setVisible(False)
        self.ui.label_31.setVisible(False)

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
        self.ui.actionOtworzbazedanych.triggered.connect(lambda: ShowDatabase(self))
        self.ui.actionEdytujbazedanych.triggered.connect(lambda: EditDatabase(self))
        # * SettingsPage
        self.ui.actionUstawienia_globalne_2.triggered.connect(
            lambda: SettingsPage(self)
        )

        f = open(f"{inipath}/version.txt", "r")
        bufor = f.read().replace(" ", "").split("==")
        f.close()
        bufor = bufor[1]
        self.ui.actionversion.setText(f"v{bufor}")
        self.ui.actionversion.triggered.connect(
            lambda: webbrowser.open("https://id-parts.readthedocs.io/pl/latest/")
        )

        #! connect to database first!!
        self.reloadButtons2()

        # * lineEdit
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()

    def reloadButtons2(self):
        global values, valuesmin, valuesmax, mycursor, widthsize, heightsize, values_profiles, values_profiles_letters, values_profiles_min, values_profiles_max

        for i in reversed(range(self.ui.gridLayout_3.count())):
            self.ui.gridLayout_3.itemAt(i).widget().setParent(None)
        self.ui.buttons2 = {}

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_profil)
        positions2 = [(r, c) for r in range(3) for c in range(3)]
        if database_connected == True and logged == True:
            mycursor.execute("SELECT * FROM global_settings")
            myresult = mycursor.fetchall()
            values2 = []
            valuesmin = []
            valuesmax = []

            for row in myresult:
                values2.append(row[0])

            for i in range(len(values2)):
                # * create buttons for len of values
                position2 = positions2[i]
                self.createButton2(values2[i], position2)

                size = ((len(values2) / 3) - 1) * 50
                widthsize, heightsize = 800 + size, 500 + size
                self.setMinimumSize(widthsize, heightsize)
                self.resize(widthsize, heightsize)
        else:
            self.setMinimumSize(700, 500)
            self.resize(700, 500)

    def createButton2(self, text, position2):
        # * create button
        self.ui.buttons2[text] = QPushButton("{}".format(text), self)

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! KLIKACZE

        self.ui.buttons2[text].clicked.connect(
            lambda: self.loginProfil(self.ui.buttons2[text].text())
        )
        self.ui.buttons2[text].setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        f = QFont("Segoe UI", defaultSize / 2.5)
        self.ui.buttons2[text].setFont(f)

        color = ""
        for i in range(2):
            color += (str(random.randint(0, 150))) + ","
        color += str(random.randint(0, 150))
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
        self.ui.buttons2[text].setStyleSheet(StyleSheet)

        self.ui.gridLayout_3.addWidget(self.ui.buttons2[text], *position2)

    def loginProfil(self, btn):
        global database_profile
        database_profile = btn.lower()
        self.ui.label_28.setText(database_profile)
        self.reloadButtons(database_profile, 1)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)

    def reloadButtons(self, database_profile, var):
        global values, valuesmin, valuesmax, mycursor, widthsize, heightsize, values_profiles, values_profiles_letters, values_profiles_min, values_profiles_max

        for i in reversed(range(self.ui.gridLayout.count())):
            self.ui.gridLayout.itemAt(i).widget().setParent(None)

        self.ui.buttons = {}

        if database_profile == "":
            return None

        if database_connected == True and logged == True:
            mycursor.execute(
                f"SELECT * FROM global_settings WHERE name LIKE '{database_profile}'"
            )
            myresult = mycursor.fetchall()
            values = []
            valuesb = []
            valuesmin = []
            valuesmax = []

            for row in myresult:
                valuesb = row[1]
                valuesmin.append(int(row[2]))
                valuesmax.append(int(row[3]))

            values = valuesb.split(",")
            for i in values:
                try:
                    values.remove("")
                except Exception:
                    pass

            for i in range(len(values)):
                # * create buttons for len of values
                position = positions[i]
                self.createButton(values[i], position)
            if var == 1:
                size = ((len(values) / 4) - 1) * 50
                widthsize, heightsize = 820 + size, 500 + size
                self.setMinimumSize(widthsize, heightsize)
                self.resize(widthsize, heightsize)
        else:
            if var == 1:
                self.setMinimumSize(800, 500)
                self.resize(800, 500)

    def createButton(self, text, position):
        # * create button
        self.ui.buttons[text] = QPushButton("{}".format(text), self)

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! KLIKACZE

        self.ui.buttons[text].clicked.connect(
            lambda: self.addItemtoDB(self.ui.buttons[text].text())
        )
        self.ui.buttons[text].setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.buttons[text].resizeEvent = self.resizeText

        color = ""
        for i in range(2):
            color += (str(random.randint(0, 150))) + ","
        color += str(random.randint(0, 150))
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

    def main_page(self):
        global database_profile
        if checkinternetbool == False:
            return None
        try:
            self.resize(widthsize, heightsize)
        except Exception:
            self.resize(700, 500)
        if database_profile == "":
            self.reloadButtons2()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
            try:
                self.reloadButtons(self, database_profile, 1)
            except Exception:
                pass

    def logout(self, var):
        global logoutses, logout_database, logged, database_connected, mycursor, mydb
        if checkinternetbool == False:
            return None
        if var == 1:
            if logoutses == False:
                self.errorexec("Kliknij raz jeszcze aby się wylogować", "Ok")
                logoutses = True
                threading.Thread(target=self.logout2, args=(var,)).start()
            else:
                logoutses = False
                logged = False
                if path.exists(f"{inipath}/fileuserlogin.txt") == True:
                    os.remove(f"{inipath}/fileuserlogin.txt")

                if path.exists(f"{inipath}/fileuserpassword.txt") == True:
                    os.remove(f"{inipath}/fileuserpassword.txt")

                self.ui.label_3.setText("Nie zalogowano do sesji!")
                self.ui.label_4.setText("")

                for i in reversed(range(self.ui.gridLayout.count())):
                    self.ui.gridLayout.itemAt(i).widget().setParent(None)

                sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
                val = (
                    f"Logout from session",
                    userlogin,
                    datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
                )
                mycursor.execute(sql, val)
                mydb.commit()
        elif var == 2:
            if logout_database == False:
                self.errorexec(
                    "Kliknij raz jeszcze aby wylogować się z bazy danych", "Ok"
                )
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

                self.ui.label_3.setText("Nie zalogowano do bazy danych!")
                self.ui.label_4.setText("")

                for i in reversed(range(self.ui.gridLayout.count())):
                    self.ui.gridLayout.itemAt(i).widget().setParent(None)

                sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
                val = (
                    f"Logout from database",
                    userlogin,
                    datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
                )
                mycursor.execute(sql, val)
                mydb.commit()
            logintoall(self)

    def logout2(self, var):
        global logoutses, logout_database
        time.sleep(10)
        if var == 1:
            logoutses = False
        elif var == 2:
            logout_database = False

    def addItemtoDB(self, var):
        global values, valuesmin, valuesmax, mycursor, mydb, database_profile
        bufor = self.ui.lineEdit_6.text()
        comment = self.ui.lineEdit_7.text()
        if comment == "":
            comment = " "
        if bufor == "":
            self.errorexec("Wymagana jest nazwa części!", "Ok")
            return None
        print(database_profile, var)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute(
            f"SELECT * FROM `{database_profile}` WHERE `letter` LIKE '{var}' AND `name` LIKE 'None'"
        )
        myresult = mycursor.fetchone()
        if myresult is None:
            self.errorexec(f"Brak wolnych numerów dla '{var}'!", "Ok")
            return None
        date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        try:
            mycursor.execute(
                f"UPDATE `{database_profile}` SET `name`='{bufor}',`comment`='{comment}',`author`='{userlogin}',`datetime`='{date}' WHERE `letter` LIKE '{str(myresult[0])}' AND `number`='{int(myresult[1])}'"
            )
            mydb.commit()
            mycursor.execute(
                f"SELECT * FROM `{database_profile}` WHERE `name` LIKE '{bufor}' AND `comment` LIKE '{comment}' AND `datetime`='{date}'"
            )
            myresultt = mycursor.fetchone()
            if myresultt:
                self.ui.label.setVisible(True)
                self.ui.label_2.setVisible(True)
                self.ui.label_30.setVisible(True)
                self.ui.label_31.setVisible(True)
                self.ui.label_30.setText(bufor)
                self.ui.label_2.setText(str(myresult[1]))
            else:
                self.ui.label.setVisible(False)
                self.ui.label_2.setVisible(False)
                self.ui.label_30.setVisible(True)
                self.ui.label_31.setVisible(False)
                self.ui.label_30.setText("Spróbuj jeszcze raz")
        except Exception:
            self.ui.label.setVisible(False)
            self.ui.label_2.setVisible(False)
            self.ui.label_30.setVisible(True)
            self.ui.label_31.setVisible(False)
            self.ui.label_30.setText("Spróbuj jeszcze raz")

    def errorexec(self, heading, btnOk):
        errorUi.errorConstrict(self.error, heading, btnOk)
        self.error.exec_()


class UserLoginClass:
    def __init__(self, selfui):
        if checkinternetbool == False:
            return None
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_login)
        try:
            selfui.ui.bn_login.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_login.clicked.connect(lambda: self.login(selfui))

    def login(self, selfui):
        global database_connected, mycursor, logged, userlogin
        if selfui.ui.lineEdit.text() == "" or selfui.ui.lineEdit_2.text() == "":
            MainWindow.errorexec(selfui, "Login bądź kod dostępu jest pusty!", "Ok")
        else:
            if database_connected == True:
                userlogin = (selfui.ui.lineEdit.text()).title()
                userpassword = selfui.ui.lineEdit_2.text()

                mycursor.execute("SELECT password FROM password")
                myresult = mycursor.fetchone()
                if str(userpassword) == str(myresult[0]):
                    fileUSER = open(f"{inipath}/fileuserlogin.txt", "wb")
                    fileUSER.write(crypto(userlogin, 0))
                    fileUSER.close()
                    fileUSER = open(f"{inipath}/fileuserpassword.txt", "wb")
                    fileUSER.write(crypto(userpassword, 0))
                    fileUSER.close()
                    logged = True
                    selfui.ui.label_3.setText("Zalogowano pomyślnie jako:")
                    selfui.ui.label_4.setText(userlogin)
                    selfui.ui.bn_login.setText("Zalogowano")
                    selfui.ui.lineEdit.setPlaceholderText(userlogin)
                    selfui.ui.lineEdit.setText("")
                    selfui.ui.lineEdit_2.setText("")
                    MainWindow.reloadButtons(selfui, database_profile, 1)
                    MainWindow.errorexec(selfui, "Zalogowano pomyślnie!", "Ok")

                    logintoall(selfui)
                else:
                    selfui.ui.lineEdit_2.setText("")
                    MainWindow.errorexec(
                        selfui,
                        "Nie można się zalogować, nieprawidłowy kod dostępu!",
                        "Ok",
                    )
            else:
                selfui.ui.lineEdit_2.setText("")
                MainWindow.errorexec(
                    selfui,
                    "Nie można się zalogować, nie jesteś połączony z bazą danych!",
                    "Ok",
                )


class DatabaseLogin:
    def __init__(self, selfui):
        if checkinternetbool == False:
            return None
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_database_login)
        try:
            selfui.ui.bn_databaselogin.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_databaselogin.clicked.connect(lambda: self.database_login(selfui))

    def database_login(self, selfui):
        global mycursor, database_connected
        if (
            selfui.ui.lineEdit_3.text() == ""
            or selfui.ui.lineEdit_4.text() == ""
            or selfui.ui.lineEdit_5.text() == ""
        ):
            MainWindow.errorexec(
                selfui, "Adres hosta, użytkownik bądź hasło jest puste!", "Ok"
            )
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

                mycursor.execute("SHOW TABLES LIKE 'global_settings'")
                result = mycursor.fetchone()
                if result:
                    pass
                else:
                    mycursor.execute(
                        "CREATE TABLE global_settings (name TEXT, letters TEXT, rangemin INTEGER, rangemax INTEGER)"
                    )

                mycursor.execute("SHOW TABLES LIKE 'logs'")
                result = mycursor.fetchone()
                if result:
                    pass
                else:
                    mycursor.execute(
                        "CREATE TABLE logs (action TEXT, author TEXT, datetime TEXT)"
                    )

                selfui.ui.lineEdit_3.setPlaceholderText(selfui.ui.lineEdit_3.text())
                selfui.ui.lineEdit_3.setText("")
                selfui.ui.lineEdit_4.setPlaceholderText(selfui.ui.lineEdit_4.text())
                selfui.ui.lineEdit_4.setText("")
                selfui.ui.lineEdit_5.setText("")
                mycursor.execute("SELECT * FROM password")
                myresult = mycursor.fetchone()
                database_connected = True
                selfui.ui.bn_databaselogin.setText("Połączono")
                logintoall(selfui)
                if logged == True:
                    MainWindow.reloadButtons(selfui, database_profile, 1)
                    selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_main)
                else:
                    pass
            except Exception as e:
                print(e)
                selfui.ui.lineEdit_5.setText("")
                MainWindow.errorexec(
                    selfui,
                    "Adres hosta, użytkownik bądź hasło jest nieprawidłowe!",
                    "Ok",
                )


class EditDatabase:
    def __init__(self, selfui):
        if checkinternetbool == False:
            return None
        if logged == False:
            MainWindow.errorexec(selfui, f"Musisz się najpierw zalogować!", "Ok")
            return None
        if database_profile == "":
            MainWindow.errorexec(selfui, f"Musisz najpierw wybrać profil!", "Ok")
            return None
        MainWindow.reloadButtons(selfui, database_profile, 0)
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_database)
        selfui.ui.stackedWidget_2.setCurrentWidget(selfui.ui.page_database_edit)
        global values, valuesmin, valuesmax
        selfui.ui.comboBox_2.clear()
        selfui.ui.comboBox_2.addItems(values)
        try:
            selfui.ui.bn_databaseSet.clicked.disconnect()
            selfui.ui.bn_databaseDel.clicked.disconnect()
            selfui.ui.bn_databaseInfo.clicked.disconnect()
            selfui.ui.bn_database_search.clicked.disconnect()
            selfui.ui.bn_database_back.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_databaseSet.clicked.connect(lambda: self.databaseSet(selfui))
        selfui.ui.bn_databaseDel.clicked.connect(lambda: self.databaseDel(selfui))
        selfui.ui.bn_databaseInfo.clicked.connect(lambda: self.databaseInfo(selfui))
        selfui.ui.bn_database_search.clicked.connect(
            lambda: self.databaseSearch(selfui)
        )
        selfui.ui.bn_database_back.clicked.connect(
            lambda: self.bn_database_backk(selfui)
        )

    def bn_database_backk(self, selfui):
        selfui.ui.comboBox.clear()
        selfui.ui.comboBox_2.clear()
        selfui.ui.comboBox_2.addItems(values)
        selfui.ui.lineEdit_13.clear()
        selfui.ui.comboBox_2.setVisible(True)
        selfui.ui.bn_databaseSet.setVisible(True)
        selfui.ui.comboBox.clear()

    def databaseSearch(self, selfui):
        global mycursor
        selfui.ui.bn_databaseSet.setVisible(False)
        selfui.ui.comboBox_2.setVisible(False)
        selfui.ui.comboBox.clear()
        bufor = selfui.ui.lineEdit_13.text()
        variables = ["name", "number", "letter", "author"]
        if selfui.ui.db_radiobox.isChecked():
            mycursor.execute(
                f"SELECT *, LOCATE('{bufor}', name) AS IfExist FROM `{database_profile}` ORDER BY `number` ASC"
            )
            buforr = mycursor.fetchall()
            dblist = []
            for row in buforr:
                if str(row[8]) == "1" and str(row[2]) != "None":
                    dblist.append(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            selfui.ui.comboBox.addItems(dblist)
            if selfui.ui.comboBox.count() != 0:
                selfui.ui.comboBox.insertSeparator(selfui.ui.comboBox.count())
        else:

            for i in variables:
                mycursor.execute(
                    f"SELECT * FROM `{database_profile}` WHERE {i} LIKE '{bufor}'  AND name NOT LIKE 'None' ORDER BY `number` ASC"
                )
                buforr = mycursor.fetchall()
                dblist = []
                for row in buforr:
                    text = f"{row[0]} {row[1]} {row[2]}"
                    index = selfui.ui.comboBox.findText(text)
                    if index == -1:
                        dblist.append(text)
                selfui.ui.comboBox.addItems(dblist)
                if selfui.ui.comboBox.count() != 0:
                    selfui.ui.comboBox.insertSeparator(selfui.ui.comboBox.count())
        if selfui.ui.comboBox.count() == 0:
            selfui.ui.comboBox.addItem("Nie znaleziono żadnych wyników")

    def databaseInfo(self, selfui):
        global mycursor
        bufor = selfui.ui.comboBox.currentText()
        if bufor != "" and bufor != "Nie znaleziono żadnych wyników":
            splitted = bufor.split(" ")
            mycursor.execute(
                f"SELECT * FROM `{database_profile}` WHERE number = {splitted[1]} AND letter LIKE '{splitted[0]}'"
            )
            buforr = mycursor.fetchone()
            selfui.ui.label_39.setText(
                f"{buforr[0]} {buforr[1]}\n {buforr[2]} \n{buforr[6]}\n {buforr[7]}"
            )

    def databaseSet(self, selfui):
        global mycursor
        bufor = selfui.ui.comboBox_2.currentText()
        selfui.ui.comboBox.clear()

        mycursor.execute(
            f"SELECT * FROM `{database_profile}` WHERE letter LIKE '{bufor}' AND name NOT LIKE 'None' ORDER BY `number` ASC"
        )
        buforr = mycursor.fetchall()
        dblist = []
        for row in buforr:
            dblist.append(bufor + " " + str(row[1]) + " " + str(row[2]))
        selfui.ui.comboBox.addItems(dblist)

    def databaseDel(self, selfui):
        global mycursor, mydb
        bufor = selfui.ui.comboBox.currentText()
        if (
            selfui.ui.label_39.text() != ""
            and bufor != "Nie znaleziono żadnych wyników"
        ):
            if bufor != "":
                splitted = bufor.split(" ")
                mycursor.execute(
                    f"UPDATE `{database_profile}` SET `name`='None',`comment`='None',`author`='None',`datetime`='None' WHERE `number` = {int(splitted[1])} AND `letter` LIKE '{splitted[0]}'"
                )
                mydb.commit()
                index = selfui.ui.comboBox.findText(bufor)
                selfui.ui.comboBox.removeItem(index)
                selfui.ui.label_39.clear()
                sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
                val = (
                    f"Del '{bufor}' from '{database_profile}'",
                    userlogin,
                    datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
                )
                mycursor.execute(sql, val)
                mydb.commit()


class ShowDatabase:
    def __init__(self, selfui):
        if checkinternetbool == False:
            return None
        if logged == False:
            MainWindow.errorexec(selfui, f"Musisz się najpierw zalogować!", "Ok")
            return None
        if database_profile == "":
            MainWindow.errorexec(selfui, f"Musisz najpierw wybrać profil!", "Ok")
            return None
        MainWindow.reloadButtons(selfui, database_profile, 0)
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_database)
        selfui.ui.stackedWidget_2.setCurrentWidget(selfui.ui.page_database_view)
        global values, valuesmin, valuesmax
        selfui.ui.comboBox_2.clear()
        selfui.ui.comboBox_2.addItems(values)
        try:
            selfui.ui.bn_databaseSet.clicked.disconnect()
            selfui.ui.bn_databaseInfo.clicked.disconnect()
            selfui.ui.bn_database_back.clicked.disconnect()
            selfui.ui.bn_database_search.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_databaseSet.clicked.connect(lambda: self.databaseSet(selfui))
        selfui.ui.bn_databaseInfo.clicked.connect(lambda: self.databaseInfo(selfui))
        selfui.ui.bn_database_back.clicked.connect(
            lambda: self.bn_database_backk(selfui)
        )
        selfui.ui.bn_database_search.clicked.connect(
            lambda: self.databaseSearch(selfui)
        )

    def bn_database_backk(self, selfui):
        selfui.ui.comboBox.clear()
        selfui.ui.comboBox_2.clear()
        selfui.ui.comboBox_2.addItems(values)
        selfui.ui.lineEdit_13.clear()
        selfui.ui.comboBox_2.setVisible(True)
        selfui.ui.bn_databaseSet.setVisible(True)
        selfui.ui.comboBox.clear()

    def databaseSearch(self, selfui):
        global mycursor
        selfui.ui.bn_databaseSet.setVisible(False)
        selfui.ui.comboBox_2.setVisible(False)
        selfui.ui.comboBox.clear()
        bufor = selfui.ui.lineEdit_13.text()
        variables = ["name", "number", "letter", "author"]
        if selfui.ui.db_radiobox.isChecked():
            mycursor.execute(
                f"SELECT *, LOCATE('{bufor}', name) AS IfExist FROM `{database_profile}` ORDER BY `number` ASC"
            )
            buforr = mycursor.fetchall()
            dblist = []
            for row in buforr:
                if str(row[8]) == "1" and str(row[2]) != "None":
                    dblist.append(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            selfui.ui.comboBox.addItems(dblist)
            if selfui.ui.comboBox.count() != 0:
                selfui.ui.comboBox.insertSeparator(selfui.ui.comboBox.count())
        else:
            for i in variables:
                mycursor.execute(
                    f"SELECT * FROM `{database_profile}` WHERE {i} LIKE '{bufor}'  AND name NOT LIKE 'None' ORDER BY `number` ASC"
                )
                buforr = mycursor.fetchall()
                dblist = []
                for row in buforr:
                    text = f"{row[0]} {row[1]} {row[2]}"
                    index = selfui.ui.comboBox.findText(text)
                    if index == -1:
                        dblist.append(text)
                selfui.ui.comboBox.addItems(dblist)
                if selfui.ui.comboBox.count() != 0:
                    selfui.ui.comboBox.insertSeparator(selfui.ui.comboBox.count())
        if selfui.ui.comboBox.count() == 0:
            selfui.ui.comboBox.addItem("Nie znaleziono żadnych wyników")

    def databaseSet(self, selfui):
        global values, valuesmin, valuesmax, mycursor
        bufor = selfui.ui.comboBox_2.currentText()
        selfui.ui.comboBox.clear()

        mycursor.execute(
            f"SELECT * FROM `{database_profile}` WHERE letter LIKE '{bufor}' AND name NOT LIKE 'None' ORDER BY `number` ASC"
        )
        buforr = mycursor.fetchall()
        dblist = []
        for row in buforr:
            dblist.append(bufor + " " + str(row[1]) + " " + str(row[2]))
        selfui.ui.comboBox.addItems(dblist)

    def databaseInfo(self, selfui):
        global mycursor
        bufor = selfui.ui.comboBox.currentText()
        if bufor != "" and bufor != "Nie znaleziono żadnych wyników":
            splitted = bufor.split(" ")
            mycursor.execute(
                f"SELECT * FROM `{database_profile}` WHERE number = {splitted[1]} AND letter LIKE '{splitted[0]}'"
            )
            buforr = mycursor.fetchone()
            selfui.ui.label_13.setText(f"{buforr[1]}")
            selfui.ui.label_15.setText(f"{buforr[0]}")
            selfui.ui.label_17.setText(f"{buforr[2]}")
            selfui.ui.label_19.setText(f"{buforr[3]}")
            selfui.ui.label_21.setText(f"{buforr[4]}-{buforr[5]}")
            selfui.ui.label_23.setText(f"{buforr[6]}")
            selfui.ui.label_25.setText(f"{buforr[7]}")


class SettingsPage:
    def __init__(self, selfui):
        global values_profiles, values_profiles_letters, values_profiles_min, values_profiles_max, mydb, mycursor
        if logged == False:
            MainWindow.errorexec(selfui, f"Musisz się najpierw zalogować!", "Ok")
            return None
        if checkinternetbool == False:
            return None
        selfui.resize(950, 500)
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_settings)
        selfui.ui.stackedWidget_3.setCurrentWidget(selfui.ui.page_settings_login)
        try:
            selfui.ui.bn_settings_set.clicked.disconnect()
            selfui.ui.bn_settings_dell.clicked.disconnect()
            selfui.ui.bn_settings_add.clicked.disconnect()
            selfui.ui.bn_settings_save.clicked.disconnect()
            selfui.ui.bn_settings_delprofile.clicked.disconnect()
            selfui.ui.bn_settings_login_bn.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_settings_set.clicked.connect(lambda: self.setProfile(selfui))
        selfui.ui.bn_settings_dell.clicked.connect(lambda: self.delLetter(selfui))
        selfui.ui.bn_settings_add.clicked.connect(lambda: self.addLetter(selfui))
        selfui.ui.bn_settings_save.clicked.connect(lambda: self.SaveProfile(selfui))
        selfui.ui.bn_settings_delprofile.clicked.connect(
            lambda: self.delProfile(selfui)
        )
        selfui.ui.bn_settings_login_bn.clicked.connect(
            lambda: self.settingslogin(selfui)
        )

        selfui.ui.comboBox_3.clear()
        selfui.ui.comboBox_4.clear()
        self.reloadCombo(selfui)

    def settingslogin(self, selfui):
        mycursor.execute("SELECT secret FROM password")
        myresult = mycursor.fetchone()
        if str(selfui.ui.lineEdit_12.text()) != str(myresult[0]):
            MainWindow.errorexec(selfui, f"Niepoprawny kod dostępu!", "Ok")
            return None
        else:
            selfui.ui.stackedWidget_3.setCurrentWidget(selfui.ui.page_settings_global)
        selfui.ui.lineEdit_12.setText("")

    def reloadCombo(self, selfui):
        global values_profiles, values_profiles_letters, values_profiles_min, values_profiles_max, mydb, mycursor
        mycursor.execute("SELECT * FROM global_settings")
        myresult = mycursor.fetchall()
        values_profiles = []
        values_profiles_letters = []
        values_profiles_min = []
        values_profiles_max = []

        for row in myresult:
            values_profiles.append(row[0])
            values_profiles_letters.append(row[1])
            values_profiles_min.append(row[2])
            values_profiles_max.append(row[3])
        selfui.ui.comboBox_3.clear()
        selfui.ui.comboBox_3.addItems(values_profiles)

    def setProfile(self, selfui):
        global mydb, mycursor
        bufor = selfui.ui.comboBox_3.currentText()
        selfui.ui.comboBox_4.clear()
        mycursor.execute(f"SELECT letters FROM global_settings WHERE name='{bufor}'")
        myresult = mycursor.fetchone()
        myresult = (
            str(myresult)
            .replace("(", "")
            .replace(")", "")
            .replace("'", "")
            .replace(" ", "")
        )
        myresult = myresult.split(",")
        for i in range(len(myresult)):
            try:
                myresult.remove("")
            except Exception:
                pass
        selfui.ui.comboBox_4.addItems(myresult)

    def delLetter(self, selfui):
        global mydb, mycursor
        bufor = selfui.ui.comboBox_3.currentText()
        bufor2 = selfui.ui.comboBox_4.currentText()
        mycursor.execute(f"SELECT letters FROM global_settings WHERE name='{bufor}'")
        myresult = mycursor.fetchone()
        myresult = (
            str(myresult)
            .replace("(", "")
            .replace(")", "")
            .replace("'", "")
            .replace(" ", "")
        )
        myresult = myresult.split(",")
        for i in range(len(myresult)):
            try:
                myresult.remove("")
            except Exception:
                pass
        myresult.remove(f"{bufor2}")
        bufor3 = ""
        for i in myresult:
            bufor3 += f"{str(i)},"
        mycursor.execute(
            f"UPDATE `global_settings` SET `letters`='{bufor3}' WHERE name='{bufor}'"
        )
        sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
        val = (
            f"DELETE letter `{bufor2}` from `{bufor}`",
            userlogin,
            datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        )
        mycursor.execute(sql, val)
        date = datetime.datetime.now().strftime("m%m_d%d_h%H_s%S")
        mycursor.execute(
            f"UPDATE `{bufor}` SET letter='{date}_{bufor2}' WHERE letter='{bufor2}'"
        )
        mydb.commit()
        self.setProfile(selfui)
        MainWindow.errorexec(
            selfui, f"Usunięto literę '{bufor2}' z profilu '{bufor}'", "Ok"
        )

        MainWindow.reloadButtons(selfui, database_profile, 0)

    def addLetter(self, selfui):
        global mydb, mycursor
        if (
            selfui.ui.lineEdit_11 == ""
            or selfui.ui.lineEdit_11.text().isalpha() == False
        ):
            return None
        bufor = selfui.ui.comboBox_3.currentText()
        bufor2 = selfui.ui.lineEdit_11.text().upper()

        mycursor.execute(f"SELECT * FROM global_settings WHERE name='{bufor}'")
        myresult = mycursor.fetchall()

        valuesl = []
        valueslmin = []
        valueslmax = []

        for row in myresult:
            valuesl = row[1]
            valueslmin = int(row[2])
            valueslmax = int(row[3])
        valuesl = (
            str(valuesl)
            .replace("(", "")
            .replace(")", "")
            .replace("'", "")
            .replace(" ", "")
        )
        valuesl = valuesl.split(",")
        for i in range(len(valuesl)):
            try:
                valuesl.remove("")
            except Exception:
                pass

        if bufor2 in valuesl:
            MainWindow.errorexec(selfui, "Już istnieje taka litera", "Ok")
            return None
        bufor3 = ""
        for i in valuesl:
            bufor3 += f"{str(i)},"
        bufor3 += bufor2

        mycursor.execute(
            f"UPDATE `global_settings` SET `letters`='{bufor3}' WHERE name='{bufor}'"
        )
        selfui.ui.lineEdit_11.setText("")

        for i in range(valueslmin, valueslmax + 1):
            sql = f"INSERT INTO {bufor} (letter,number, name, comment,rangemin,rangemax,author,datetime) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
            val = (
                bufor2,
                i,
                "None",
                "None",
                valueslmin,
                valueslmax,
                "None",
                "None",
            )
            mycursor.execute(sql, val)
        sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
        val = (
            f"Add letter `{bufor2}` to `{bufor}` with {valueslmax-valueslmin} rows",
            userlogin,
            datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        )
        mycursor.execute(sql, val)
        mydb.commit()

        self.setProfile(selfui)
        MainWindow.errorexec(
            selfui, f"Dodano literę '{bufor2}' do profilu '{bufor}'", "Ok"
        )

        MainWindow.reloadButtons(selfui, database_profile, 0)

    def SaveProfile(self, selfui):
        mycursor.execute(f"SELECT name FROM global_settings")
        myresult = mycursor.fetchall()
        bufor = selfui.ui.lineEdit_8.text()
        for i in myresult:
            if bufor in i:
                MainWindow.errorexec(selfui, "Już istnieje taki profil", "Ok")
        if (
            selfui.ui.lineEdit_8.text() == ""
            or selfui.ui.lineEdit_9.text() == ""
            or selfui.ui.lineEdit_10.text() == ""
            or selfui.ui.lineEdit_9.text().isnumeric() == False
            or selfui.ui.lineEdit_10.text().isnumeric() == False
        ):
            MainWindow.errorexec(
                selfui,
                "Nazwa, zakres minimalny albo maksymalny jest pustym polem",
                "Ok",
            )
            return None
        if int(selfui.ui.lineEdit_10.text()) < int(selfui.ui.lineEdit_9.text()):
            MainWindow.errorexec(
                selfui,
                "Maksymalny zakres nie może być mniejszy od minimalnego!",
                "Ok",
            )
            return None
        bufor = selfui.ui.lineEdit_8.text().replace(" ", "_")
        mycursor.execute(
            f"INSERT INTO `global_settings`(`name`, `letters`, `rangemin`, `rangemax`) VALUES ('{bufor}','','{selfui.ui.lineEdit_9.text()}','{selfui.ui.lineEdit_10.text()}')"
        )
        mycursor.execute(
            f"CREATE TABLE {bufor} (letter TEXT, number INTEGER, name TEXT, comment TEXT, rangemin INTEGER, rangemax INTEGER, author TEXT, datetime TEXT)"
        )
        sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
        val = (
            f"Saved profile `{bufor}`",
            userlogin,
            datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        )
        mycursor.execute(sql, val)
        mydb.commit()

        self.reloadCombo(selfui)
        self.setProfile(selfui)
        selfui.ui.lineEdit_8.setText("")
        selfui.ui.lineEdit_9.setText("")
        selfui.ui.lineEdit_10.setText("")
        MainWindow.errorexec(selfui, f"Dodano profil {bufor}", "Ok")

    def delProfile(self, selfui):
        global database_profile
        bufor = selfui.ui.comboBox_3.currentText()
        mycursor.execute(f"DELETE FROM `global_settings` WHERE name='{bufor}'")
        date = datetime.datetime.now().strftime("m%m_d%d_h%H_s%S")
        mycursor.execute(f"RENAME TABLE {bufor} TO del_{date}_{bufor}")
        sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
        val = (
            f"DELETE DATABASE `{bufor}`",
            userlogin,
            datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        )
        mycursor.execute(sql, val)

        mydb.commit()

        database_profile = ""

        self.reloadCombo(selfui)
        self.setProfile(selfui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
