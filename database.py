import threading
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="secret", database="partsid-database"
)

mycursor = mydb.cursor()

"""for i in range(10000):
    sql = "INSERT INTO lettera (letter, number, part, comment,lrange,author,datetime) VALUES (%s, %s, %s,%s,%s,%s,%s)"
    val = (f"A", i, "name", "comment", "102-499", "Mateusz Goinda", "18:30:23")
    mycursor.execute(sql, val)
    mydb.commit()
    """

query = "SELECT COUNT(*) from `lettera` where letter='A'"
mycursor.execute(query)
res = mycursor.fetchone()
total_rows = res[0]
print(total_rows)
