import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonpractical"
)

cursor = db.cursor()

cursor.execute("create table userdata (id int(6),username varchar(30),password varchar(30),email varchar(30))")

print("Table Created Successfully")