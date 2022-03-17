# autoinstaller and autoupdater all files of program

filelink = "https://raw.githubusercontent.com/Bre3n/ID-Parts/master/files/links.txt"


def downloader(url, path, var):
    if var == 1:
        MANAGER = enlighten.get_manager()
        r = requests.get(url, stream=True)
        assert r.status_code == 200, r.status_code
        dlen = int(r.headers.get("Content-Length", "0")) or None

        with MANAGER.counter(
            color="green",
            total=dlen and math.ceil(dlen / 2 ** 20),
            unit="MiB",
            leave=False,
        ) as ctr, open(path, "wb", buffering=2 ** 24) as f:
            for chunk in r.iter_content(chunk_size=2 ** 20):
                print(chunk[-16:].hex().upper())
                f.write(chunk)
                ctr.update()
    else:
        with open(path, "wb") as f:
            response = requests.get(url, stream=True)
            total = response.headers.get("content-length")

            if total is None:
                f.write(response.content)
            else:
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    f.write(data)


if __name__ == "__main__":
    import configparser
    import datetime
    import math
    import os
    import shutil
    import subprocess
    import sys
    import time
    import tkinter as tk
    import zipfile
    from os import listdir, path
    from os.path import isfile, join
    from tkinter import messagebox
    import sys, os, traceback, types

    import coloredlogs
    import enlighten
    import requests
    import win32com.client
    import winshell

    root = tk.Tk()
    root.withdraw()

    config = configparser.ConfigParser()

    os.system("cls")

    import psutil

    PROCNAME = "partsID_main.exe"

    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()

    now_date = str(datetime.date.today())
    user = os.getlogin()
    roaming = os.getenv("APPDATA")
    buffor = False
    sciezka = f"{roaming}/PartsID"
    havetorestart = False

    txtFile = f"{sciezka}/ver.txt"
    if path.exists(sciezka) == False:
        os.mkdir(sciezka)

    havetorestart = False
    downloader(
        filelink,
        txtFile,
        0,
    )

    with open(txtFile) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    os.remove(f"{sciezka}/ver.txt")

    if path.exists(f"{sciezka}/version.txt") == False:
        f = open(f"{sciezka}/version.txt", "w")
        for i in range(int(len(content) / 2)):
            f.write(f"{content[i]}\n")
        f.close()
        print("asd")
        onlyfiles = listdir(sciezka)
        for i in onlyfiles:
            if i != "version.txt" and i != "partsID_main.exe":
                try:
                    os.remove(f"{sciezka}/{i}")
                except OSError:
                    shutil.rmtree(f"{sciezka}/{i}")
        os.execv(sys.executable, ["python"] + sys.argv)
    else:
        with open(f"{sciezka}/version.txt") as f:
            contentv = f.readlines()
            contentv = [x.strip() for x in contentv]
        if int(len(content) / 2) != int(len(contentv)):
            f = open(f"{sciezka}/version.txt", "w")
            for i in range(int(len(content) / 2)):
                f.write("None\n")
        with open(f"{sciezka}/version.txt") as f:
            contentv = f.readlines()
            contentv = [x.strip() for x in contentv]
        for i in range(int(len(content) / 2)):
            if content[i] != contentv[i]:
                bufor = content[i].replace(" ", "")
                bufor = bufor.split("==")
                checkzip = bufor[0].split(".")
                downloader(
                    content[i + (int(len(content) / 2))],
                    f"{sciezka}/{bufor[0]}",
                    1,
                )
                print(" ")
                if checkzip[1] == "zip":
                    with zipfile.ZipFile(f"{sciezka}/{bufor[0]}", "r") as zipObj:
                        zipObj.extractall(f"{sciezka}/{checkzip[0]}")
                    os.remove(f"{sciezka}/{bufor[0]}")
        f = open(f"{sciezka}/version.txt", "w")
        for i in range(int(len(content) / 2)):
            f.write(f"{content[i]}\n")
        f.close()
        for i in range(int(len(content) / 2)):
            bufor = content[i].replace(" ", "")
            bufor = bufor.split("==")
            checkzip = bufor[0].split(".")
            buforr = bufor[0]
            if checkzip[1] == "zip":
                bufor[0] = checkzip[0]
            if path.exists(f"{sciezka}/{bufor[0]}") == False:
                downloader(
                    content[i + (int(len(content) / 2))],
                    f"{sciezka}/{buforr}",
                    1,
                )
                print(" ")
                havetorestart = True
                if checkzip[1] == "zip":
                    with zipfile.ZipFile(f"{sciezka}/{buforr}", "r") as zipObj:
                        zipObj.extractall(f"{sciezka}/{checkzip[0]}")
                    os.remove(f"{sciezka}/{buforr}")
        if havetorestart == True:
            os.execv(sys.executable, ["python"] + sys.argv)
        os.chdir(f"{sciezka}/")
        os.system(f"{sciezka}/partsID_main.exe")
