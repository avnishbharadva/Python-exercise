import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "lasttime"
)

mycursor = db.cursor()

mycursor.execute("create table lasttimetable (sid int(5),sname varchar(30),semail varchar(30),spass varchar(30))")

print("Table Create..")