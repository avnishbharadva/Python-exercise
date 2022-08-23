import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("create table students (id int(7), name varchar(255), city varchar(255))")