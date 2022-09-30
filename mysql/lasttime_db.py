import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
)

mycursor = db.cursor()

mycursor.execute("create database lasttime")

print("Database Created...")