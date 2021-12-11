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
import datetime

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

    global userlogin, userpassword, databasehostname, databaseuser, databasepassword, database_connected, mydb, logged

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
            mydb = mysql.connector.connect(
                host=databasehostname,
                user=databaseuser,
                password=databasepassword,
                database="partsid-database",
            )
            if mydb.is_connected() == False:
                self.ui.label_3.setText("Nie zalogowano do sesji!")
                self.ui.label_4.setText("")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(
                    "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych "
                )
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                self.ui.lineEdit_3.setPlaceholderText(databasehostname)
                self.ui.lineEdit_4.setPlaceholderText(databaseuser)
                self.ui.bn_databaselogin.setText("Połączono")
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("SELECT * FROM password")
                myresult = mycursor.fetchone()
                database_connected = True
                if userpassword == myresult[0]:
                    self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
                    logged = True
                    self.ui.bn_login.setText("Zalogowano")
                    self.ui.lineEdit.setPlaceholderText(userlogin)
                    self.ui.label_4.setText(userlogin)
                else:
                    self.ui.label_3.setText("Nie zalogowano do sesji!")
                    self.ui.label_4.setText("")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(
                        "Nie zalogowano do sesji. Ustawienia sesji -> Zaloguj"
                    )
                    msg.setWindowTitle("Error")
                    msg.exec_()
        except Exception as e:
            print(e)
            self.ui.label_3.setText("Nie zalogowano do sesji!")
            self.ui.label_4.setText("")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(
                "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych "
            )
            msg.setWindowTitle("Error")
            msg.exec_()

    else:
        self.ui.label_3.setText("Nie zalogowano do sesji!")
        self.ui.label_4.setText("")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(
            "Nie zalogowano do bazy danych. Ustawienia sesji -> Połącz z bazą danych "
        )
        msg.setWindowTitle("Error")
        msg.exec_()


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global positions, value, position, values, widthsize, heightsize, logoutses, logout_database, database_connected, config, inipath, userlogin, userpassword, databasehostname, databaseuser, databasepassword, logged, switchEdit, mydb
        logoutses, logout_database, database_connected, logged, switchEdit = (
            False,
            False,
            False,
            False,
            False,
        )
        (userlogin, userpassword, databasehostname, databaseuser, databasepassword,) = (
            "",
            "",
            "",
            "",
            "",
        )

        self.ui.comboBox.setEnabled(False)
        self.ui.lineEdit_6.setEnabled(False)
        self.ui.lineEdit_7.setEnabled(False)
        self.ui.lineEdit_8.setEnabled(False)
        self.ui.bn_settadd.setEnabled(False)
        self.ui.bn_settdel.setEnabled(False)
        self.ui.bn_settsave.setEnabled(False)
        self.ui.label_10.setEnabled(False)

        print(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

        user = os.getlogin()
        inipath = f"C:/Users/{user}/AppData/LocalLow/PartsID"
        if path.exists(f"{inipath}") == False:
            os.mkdir(f"{inipath}")

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

        # * Settings
        self.ui.actionUstawienia_globalne.triggered.connect(lambda: SettingsPage(self))

        #! connect to database first!!
        self.reloadButtons()

    def reloadButtons(self):
        global values, valuesmin, valuesmax, mydb, widthsize, heightsize
        if database_connected == True and logged == True:
            mycursorr = mydb.cursor(buffered=True)
            mycursorr.execute("SELECT * FROM global_settings")
            myresult = mycursorr.fetchall()
            values = []
            valuesmin = []
            valuesmax = []

            for row in myresult:
                print(row)
                values.append(row[0])
                valuesmin.append(row[1])
                valuesmax.append(row[2])
            print(values, valuesmin, valuesmax)

            # values = ["D", "M", "C", "G"]  # * << buttons in layout
            for i in range(len(values)):
                # * create buttons for len of values
                position = positions[i]
                self.createButton(values[i], position)

                size = ((len(values) / 4) - 1) * 50
                widthsize, heightsize = 700 + size, 350 + size
                self.setMinimumSize(widthsize, heightsize)
        else:
            self.setMinimumSize(700, 350)

    def createButton(self, text, position):
        # * create button
        self.ui.buttons[text] = QPushButton("{}".format(text), self)

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! KLIKACZE

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
        try:
            selfui.ui.bn_login.clicked.disconnect()
        except Exception:
            pass
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
                myresult = mycursorr.fetchone()
                if userpassword == myresult[0]:
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
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Information")
                    msg.setInformativeText("Zalogowano pomyślnie!")
                    msg.setWindowTitle("Information")
                    msg.exec_()
                else:
                    selfui.ui.lineEdit_2.setText("")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(
                        "Nie można się zalogować, nieprawidłowy kod dostępu!"
                    )
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                selfui.ui.lineEdit_2.setText("")
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
        try:
            selfui.ui.bn_databaselogin.clicked.disconnect()
        except Exception:
            pass
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

                mycursor.execute("SHOW TABLES LIKE 'global_settings'")
                result = mycursor.fetchone()
                if result:
                    pass
                else:
                    print("asdasd")
                    mycursor.execute(
                        "CREATE TABLE global_settings (letters TEXT, rangemin INTEGER, rangemax INTEGER, author TEXT, datetime TEXT)"
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
                if userpassword == myresult[0]:
                    selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_main)
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(
                        "Nie zalogowano do sesji. Ustawienia sesji -> Zaloguj"
                    )
                    msg.setWindowTitle("Error")
                    msg.exec_()
            except Exception as e:
                print(e)
                selfui.ui.lineEdit_5.setText("")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(
                    "Adres hosta, użytkownik bądź hasło jest nieprawidłowe!"
                )
                msg.setWindowTitle("Error")
                msg.exec_()


class SettingsPage:
    def __init__(self, selfui):
        global logged, database_connected, switchEdit
        try:
            selfui.ui.bn_settswitch.clicked.disconnect()
            selfui.ui.bn_settadd.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_settswitch.clicked.connect(lambda: self.switchEdit(selfui))
        selfui.ui.bn_settadd.clicked.connect(lambda: self.letteradd(selfui))
        if logged == False or database_connected == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Musisz najpierw zalogować się do bazy i do sesji!")
            msg.setWindowTitle("Error")
            msg.exec_()
            return None
        else:
            global mydb
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("SHOW TABLES")
            if "global_settings" in mycursor == False:
                mycursor.execute(
                    "CREATE TABLE global_settings (letters TEXT, rangemin INTEGER, rangemax INTEGER)"
                )
            selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_settings)

    def switchEdit(self, selfui):
        # * PRZEŁĄCZANIE EDYTOWANIA settings_global
        global switchEdit
        if switchEdit == False:
            selfui.ui.bn_settswitch.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(150,150,50);}QPushButton:hover {background-color: rgb(150,180,100);}"
            )
            selfui.ui.bn_settsave.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(190,60,60);}QPushButton:hover {background-color: rgb(220,70,70);}"
            )
            selfui.ui.comboBox.setEnabled(True)
            selfui.ui.lineEdit_6.setEnabled(True)
            selfui.ui.lineEdit_7.setEnabled(True)
            selfui.ui.lineEdit_8.setEnabled(True)
            selfui.ui.bn_settadd.setEnabled(True)
            selfui.ui.bn_settdel.setEnabled(True)
            selfui.ui.bn_settsave.setEnabled(True)
            selfui.ui.label_10.setEnabled(True)
            switchEdit = True

        elif switchEdit == True:
            selfui.ui.bn_settswitch.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(100,180,100);}"
            )
            selfui.ui.bn_settsave.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(100,180,100);}"
            )
            selfui.ui.comboBox.setEnabled(False)
            selfui.ui.lineEdit_6.setEnabled(False)
            selfui.ui.lineEdit_7.setEnabled(False)
            selfui.ui.lineEdit_8.setEnabled(False)
            selfui.ui.bn_settadd.setEnabled(False)
            selfui.ui.bn_settdel.setEnabled(False)
            selfui.ui.bn_settsave.setEnabled(False)
            selfui.ui.label_10.setEnabled(False)
            switchEdit = False

    def letteradd(self, selfui):
        # * DODAWANIE LITEREK DO BAZY DANYCH
        global letterlist
        if (
            selfui.ui.lineEdit_6.text() == ""
            or selfui.ui.lineEdit_7.text() == ""
            or selfui.ui.lineEdit_8.text() == ""
        ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(
                "Litera, minimalny zakres albo maksymalny zakres jest pusty!"
            )
            msg.setWindowTitle("Error")
            msg.exec_()
            return None
        buforletter = {}
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT letters FROM global_settings")
        myresult = mycursor.fetchall()
        values = []
        valuesmin = []
        valuesmax = []
        buforbool = False
        bufor = selfui.ui.lineEdit_6.text()
        buformin = selfui.ui.lineEdit_7.text()
        buformax = selfui.ui.lineEdit_8.text()
        if buformin.isnumeric() == False or buformax.isnumeric():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(
                "Minimalny albo maksymalny zakres nie jest liczbą całkowitą!"
            )
            msg.setWindowTitle("Error")
            msg.exec_()
            return None
        i = 0
        for row in myresult:
            if bufor == row[i]:
                buforbool = True
        if buforbool:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(
                "taka litera już istnije! Jeśli chcesz ją edytować klinik w przycisk 'Edytuj'"
            )
            msg.setWindowTitle("Error")
            msg.exec_()
            return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
