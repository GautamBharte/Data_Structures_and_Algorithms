from debugpy import connect
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sakshi@0143'
)

mycursor = mydb.cursor()

mycursor.execute("show databases")

for database in mycursor:
    print(database)