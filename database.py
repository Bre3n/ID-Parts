import threading
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="secret", database="partsid-database"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM password")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
