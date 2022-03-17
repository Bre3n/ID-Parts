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


def isUserAdmin():

    if os.name == "nt":
        import ctypes

        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False


def runAsAdmin(cmdLine=None, wait=True):

    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType, types.ListType):
        raise ValueError
    cmd = '"%s"' % (cmdLine[0],)
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ""
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = "runas"
    procInfo = ShellExecuteEx(
        nShow=showCmd,
        fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
        lpVerb=lpVerb,
        lpFile=cmd,
        lpParameters=params,
    )

    if wait:
        procHandle = procInfo["hProcess"]
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
    else:
        rc = None

    return rc


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
    buffor = False
    sciezka = f"C:/Users/{user}/AppData/Roaming/PartsID"
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
