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
                if str(userpassword) == str(myresult[0]):
                    self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
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

                    ################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SET PROFILE #################################
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

        global positions, value, position, values, widthsize, heightsize, logoutses, logout_database, database_connected, config, inipath, userlogin, userpassword, databasehostname, databaseuser, databasepassword, logged, switchEdit, mycursor, profile
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

        print(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

        user = os.getlogin()
        inipath = f"C:/Users/{user}/AppData/LocalLow/PartsID"
        if path.exists(f"{inipath}") == False:
            os.mkdir(f"{inipath}")

        logintoall(self)

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PROFILE !!
        #
        # This############################
        # This
        #
        # This################
        # This################
        # This################################
        # This################################################################
        # This################################################################################################
        # This################################################################################################################################

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)

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
        self.ui.actionOtworzbazedanych.triggered.connect(lambda: ShowDatabase(self))
        self.ui.actionEdytujbazedanych.triggered.connect(lambda: EditDatabase(self))
        # * SettingsPage
        self.ui.actionUstawienia_globalne_2.triggered.connect(
            lambda: SettingsPage(self)
        )

        #! connect to database first!!
        self.reloadButtons()

        # * lineEdit
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()

    def reloadButtons(self):
        global values, valuesmin, valuesmax, mycursor, widthsize, heightsize, values_profiles, values_profiles_letters, values_profiles_min, values_profiles_max

        """if database_connected == True and logged == True:
            mycursor.execute("SELECT * FROM global_settings")
            myresult = mycursor.fetchall()
            values = []
            valuesmin = []
            valuesmax = []

            for row in myresult:
                values.append(row[0])
                valuesmin.append(int(row[1]))
                valuesmax.append(int(row[2]))

            for i in range(len(values)):
                # * create buttons for len of values
                position = positions[i]
                self.createButton(values[i], position)

                size = ((len(values) / 4) - 1) * 50
                widthsize, heightsize = 700 + size, 500 + size
                self.setMinimumSize(widthsize, heightsize)
                self.resize(widthsize, heightsize)
        else:
            self.setMinimumSize(700, 500)
            self.resize(700, 500)"""

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
        global logoutses, logout_database, logged, database_connected, mycursor, mydb
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
        print(var)
        global values, valuesmin, valuesmax, mycursor, mydb
        bufor = self.ui.lineEdit_6.text()
        comment = self.ui.lineEdit_7.text()
        if comment == "":
            comment = " "
        if bufor == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Wymagana jest nazwa części!")
            msg.setWindowTitle("Error")
            msg.exec_()
            return None
        mycursor.execute(
            f"SELECT * FROM `data` WHERE letter LIKE '{var}' AND name LIKE 'None' ORDER BY `number` ASC"
        )
        myresult = mycursor.fetchone()
        date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        mycursor.execute(
            f"UPDATE `data` SET `number`='{myresult[0]}',`letter`='{myresult[1]}',`name`='{bufor}',`comment`='{comment}',`lrange`='{myresult[4]}',`author`='{userlogin}',`datetime`='{date}' WHERE number = {myresult[0]}"
        )
        mydb.commit()


class UserLoginClass:
    def __init__(self, selfui):
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_login)
        try:
            selfui.ui.bn_login.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_login.clicked.connect(lambda: self.login(selfui))

    def login(self, selfui):
        global database_connected, mycursor, logged
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
                    MainWindow.reloadButtons(selfui)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Information")
                    msg.setInformativeText("Zalogowano pomyślnie!")
                    msg.setWindowTitle("Information")
                    msg.exec_()

                    logintoall(selfui)
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
        global mycursor, database_connected
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
                    mycursor.execute(
                        "CREATE TABLE global_settings (letter TEXT, rangemin INTEGER, rangemax INTEGER)"
                    )

                mycursor.execute("SHOW TABLES LIKE 'data'")
                result = mycursor.fetchone()
                if result:
                    pass
                else:
                    mycursor.execute(
                        "CREATE TABLE data (number INTEGER, letter TEXT,name TEXT,comment TEXT, lrange TEXT, author TEXT, datetime TEXT)"
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
                    MainWindow.reloadButtons(selfui)
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


class EditDatabase:
    def __init__(self, selfui):
        MainWindow.reloadButtons(selfui)
        selfui.ui.bn_databaseInfo.setVisible(False)
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_database)
        selfui.ui.stackedWidget_2.setCurrentWidget(selfui.ui.page_database_edit)
        global values, valuesmin, valuesmax
        selfui.ui.comboBox_2.clear()
        selfui.ui.comboBox_2.addItems(values)
        try:
            selfui.ui.bn_databaseSet.clicked.disconnect()
            selfui.ui.bn_databaseDel.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_databaseSet.clicked.connect(lambda: self.databaseSet(selfui))
        selfui.ui.bn_databaseDel.clicked.connect(lambda: self.databaseDel(selfui))

    def databaseSet(self, selfui):
        global values, valuesmin, valuesmax, mycursor
        bufor = selfui.ui.comboBox_2.currentText()
        selfui.ui.comboBox.clear()

        mycursor.execute(
            f"SELECT * FROM `data` WHERE letter LIKE '{bufor}' AND name NOT LIKE 'None' ORDER BY `number` ASC"
        )
        buforr = mycursor.fetchall()
        dblist = []
        for row in buforr:
            dblist.append(bufor + " " + str(row[0]) + " " + str(row[2]))
        selfui.ui.comboBox.addItems(dblist)

    def databaseDel(self, selfui):
        global values, valuesmin, valuesmax, mycursor, mydb
        bufor = selfui.ui.comboBox.currentText()
        splitted = bufor.split(" ")
        splitted = int(splitted[1])
        mycursor.execute(f"SELECT * FROM `data` WHERE number = {splitted}")
        buforr = mycursor.fetchone()

        mycursor.execute(
            f"UPDATE `data` SET `number`='{buforr[0]}',`letter`='{buforr[1]}',`name`='None',`comment`='None',`lrange`='{buforr[4]}',`author`='None',`datetime`='None' WHERE number = {splitted}"
        )
        mydb.commit()
        index = selfui.ui.comboBox.findText(bufor)
        selfui.ui.comboBox.removeItem(index)
        sql = "INSERT INTO logs (action, author, datetime) VALUES (%s, %s, %s)"
        val = (
            f"Del '{bufor}'",
            userlogin,
            datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        )
        mycursor.execute(sql, val)
        mydb.commit()


class ShowDatabase:
    def __init__(self, selfui):
        MainWindow.reloadButtons(selfui)
        selfui.ui.bn_databaseInfo.setVisible(True)
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_database)
        selfui.ui.stackedWidget_2.setCurrentWidget(selfui.ui.page_database_view)
        global values, valuesmin, valuesmax
        selfui.ui.comboBox_2.clear()
        selfui.ui.comboBox_2.addItems(values)
        try:
            selfui.ui.bn_databaseSet.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_databaseSet.clicked.connect(lambda: self.databaseSet(selfui))
        selfui.ui.bn_databaseInfo.clicked.connect(lambda: self.databaseInfo(selfui))

    def databaseSet(self, selfui):
        global values, valuesmin, valuesmax, mycursor
        bufor = selfui.ui.comboBox_2.currentText()
        selfui.ui.comboBox.clear()

        mycursor.execute(
            f"SELECT * FROM `data` WHERE letter LIKE '{bufor}' AND name NOT LIKE 'None' ORDER BY `number` ASC"
        )
        buforr = mycursor.fetchall()
        dblist = []
        for row in buforr:
            dblist.append(bufor + " " + str(row[0]) + " " + str(row[2]))
        selfui.ui.comboBox.addItems(dblist)

    def databaseInfo(self, selfui):
        bufor = selfui.ui.comboBox.currentText()
        if bufor != "":
            splitted = bufor.split(" ")
            splitted = int(splitted[1])
            mycursor.execute(f"SELECT * FROM `data` WHERE number = {splitted}")
            buforr = mycursor.fetchone()
            selfui.ui.label_13.setText(f"{buforr[0]}")
            selfui.ui.label_15.setText(f"{buforr[1]}")
            selfui.ui.label_17.setText(f"{buforr[2]}")
            selfui.ui.label_19.setText(f"{buforr[3]}")
            selfui.ui.label_21.setText(f"{buforr[4]}")
            selfui.ui.label_23.setText(f"{buforr[5]}")
            selfui.ui.label_25.setText(f"{buforr[6]}")


class SettingsPage:
    def __init__(self, selfui):
        global values_profiles, values_profiles_letters, values_profiles_min, values_profiles_max, mydb, mycursor
        selfui.ui.stackedWidget.setCurrentWidget(selfui.ui.page_settings)
        try:
            selfui.ui.bn_settings_set.clicked.disconnect()
            selfui.ui.bn_settings_dell.clicked.disconnect()
            selfui.ui.bn_settings_add.clicked.disconnect()
        except Exception:
            pass
        selfui.ui.bn_settings_set.clicked.connect(lambda: self.setProfile(selfui))
        selfui.ui.bn_settings_dell.clicked.connect(lambda: self.delLetter(selfui))
        selfui.ui.bn_settings_add.clicked.connect(lambda: self.addLetter(selfui))
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
        print(myresult)
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
        mydb.commit()
        self.setProfile(selfui)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Information")
        msg.setInformativeText(f"Usunięto literę '{bufor2}' z profilu '{bufor}'")
        msg.setWindowTitle("Information")
        msg.exec_()

    def addLetter(self, selfui):
        global mydb, mycursor
        if (
            selfui.ui.lineEdit_11 == ""
            or selfui.ui.lineEdit_11.text().isalpha() == False
        ):
            return None
        bufor = selfui.ui.comboBox_3.currentText()
        bufor2 = selfui.ui.lineEdit_11.text()

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

        if bufor2 in myresult:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Już istnieje taka litera")
            msg.setWindowTitle("Error")
            msg.exec_()
            return None
        bufor3 = ""
        for i in myresult:
            bufor3 += f"{str(i)},"
        bufor3 += bufor2

        mycursor.execute(
            f"UPDATE `global_settings` SET `letters`='{bufor3}' WHERE name='{bufor}'"
        )
        mydb.commit()
        selfui.ui.lineEdit_11.setText("")
        self.setProfile(selfui)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Information")
        msg.setInformativeText(f"Dodano literę '{bufor2}' do profilu '{bufor}'")
        msg.setWindowTitle("Information")
        msg.exec_()
        
    def SaveProfile(self, selfui):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
