import threading
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="secret", database="partsid-database"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM global_settings")
myresult = mycursor.fetchall()
values = []
valuesmin = []
valuesmax = []

for row in myresult:
    print(row)
    values.append(row[0])
    valuesmin.append(int(row[1]))
    valuesmax.append(int(row[2]))

for i in range(len(values)):
    for j in range(valuesmin[i], valuesmax[i] + 1):
        sql = "INSERT INTO data (number, letter, name, comment,lrange,author,datetime) VALUES (%s, %s, %s,%s,%s,%s,%s)"
        val = (
            j,
            values[i],
            "None",
            "None",
            f"{valuesmin[i]}-{valuesmax[i]}",
            "None",
            "None",
        )
        mycursor.execute(sql, val)
        mydb.commit()
