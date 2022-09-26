import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonpractical"
)

cursor = db.cursor()

cursor.execute("show databases")

for i in cursor:
    print(i)

print()

cursor.execute("show tables")

for x in cursor:
    print(x)