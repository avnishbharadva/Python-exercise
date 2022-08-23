import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()

mycursor.execute("create database pythondb")

# mycursor.execute("create table student (id int(7), name varchar(255), city varchar(255))")
# print(mydb)