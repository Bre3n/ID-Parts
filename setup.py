# autoinstaller and autoupdater all files of program

filelink = "https://raw.githubusercontent.com/Bre3n/MLauncher/master/files/links.txt"


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


def pliki(sciezka):
    i = 0
    pathh = f"{sciezka}/logs-setup"

    # * LOGS
    if path.exists(pathh) == False:
        os.mkdir(pathh)
    if path.exists(f"{pathh}/.SORT_BY_MODIFICATION_TIME.txt") == False:
        open(f"{pathh}/.SORT_BY_MODIFICATION_TIME.txt", "w").close()
    if path.exists(f"{pathh}/{now_date}-9.log") == True:
        os.remove(f"{pathh}/{now_date}-9.log")
    if path.exists(f"{pathh}/{now_date}.log") == True:
        while path.exists(f"{pathh}/{now_date}-{i}.log") == True:
            i = i + 1
        os.rename(f"{pathh}/{now_date}.log", f"{pathh}/{now_date}-{i}.log")
    else:
        if path.exists(f"{pathh}/latest.log") == True:
            os.rename(
                f"{pathh}/latest.log",
                f"{pathh}/{now_date}.log",
            )


if __name__ == "__main__":
    import configparser
    import datetime
    import logging
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

    import coloredlogs
    import enlighten
    import requests
    import win32com.client
    import winshell

    root = tk.Tk()
    root.withdraw()

    config = configparser.ConfigParser()

    os.system("cls")

    now_date = str(datetime.date.today())
    user = os.getlogin()
    buffor = False
    sciezka = f"C:/Users/{user}/AppData/LocalLow/PartsID"
    temp = f"C:/Users/{user}/AppData/Local/Temp"
    havetorestart = False

    txtFile = f"{sciezka}/ver.txt"
    if path.exists(sciezka) == False:
        os.mkdir(sciezka)
    if path.exists(f"{sciezka}/bin") == False:
        os.mkdir(f"{sciezka}/bin")

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
        onlyfiles = listdir(sciezka)
        for i in onlyfiles:
            if i != "version.txt" and i != "main.exe":
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
            print(int(len(content) / 2))
            print(int(len(contentv)))
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

        logging.shutdown()
        desktop = winshell.desktop()
        cwd = os.getcwd()
        if path.exists(f"{desktop}/PartsID.lnk") == False:
            path = os.path.join(desktop, "MLauncher.lnk")
            target = f"{sciezka}\\main.exe"
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.save()
            f = open(f"{sciezka}/cache/shortcut.txt", "w")
            f.write("Shortcut created")
            f.close()
        os.chdir(f"{sciezka}/")
        subprocess.call(["python", f"{sciezka}/main.py"])
