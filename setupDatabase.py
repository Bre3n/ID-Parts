if __name__ == "__main__":
    import mysql.connector
    import getpass

    address, username, password = "", "", ""
    while address == "":
        address = input("Podaj adres bazy danych: ")
    while username == "":
        username = input("Podaj hasło do bazy danych: ")
    while password == "":
        password = getpass.getpass("Podaj hasło do bazy danych: ")
    try:
        mydb = mysql.connector.connect(
            host=address,
            user=username,
            password=password,
        )
        print("Zalogowano do bazy")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("CREATE DATABASE `partsid-database`")
        mycursor.execute("USE `partsid-database`")
        mycursor.execute("CREATE table password (password TEXT, secret TEXT)")
        userpass = getpass.getpass(
            "Podaj jakim hasłem mają się logować użytkownicy do sesji (np. 1234): "
        )
        adminpass = getpass.getpass(
            "Podaj jakim hasłem ma logować się admin do zarządzania profilami (np. 654321): "
        )
        sql = "INSERT INTO password (password, secret) VALUES (%s, %s)"
        val = (
            userpass,
            adminpass,
        )
        mycursor.execute(sql, val)
        mydb.commit()
        print("Utworzono niezbędne tabele i katalogi.")
        a = input("")
    except mysql.connector.Error as err:
        print("Coś poszło nie tak, może są niepoprawne dane logowania ", err)
