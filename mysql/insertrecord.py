import mysql.connector as con

sid = int(input("Enter Student ID : "))
sname = input("Enter Name : ")
scity = input("Enter City : ")

mydb = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythondb"
)

mycursor = mydb.cursor()

args = (sid,sname,scity)
mycursor.execute("insert into students (id,name,city) values(%s,%s,%s)",args)

mydb.commit()

print(mycursor.rowcount,"record inserted")

mycursor.execute("select * from students")

res = mycursor.fetchall()

for i in res:
    print(i)