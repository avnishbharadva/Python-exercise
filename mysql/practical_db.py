import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = db.cursor()

cursor.execute("create database pythonpractical")

print("Data Base Created Successfully...")