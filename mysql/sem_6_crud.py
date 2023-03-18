import mysql.connector as con

mydb = con.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "radha"
)

mycursor = mydb.cursor()

# mycursor.execute("create database radha")

# mycursor.execute("create table studinfo (sid int (5),sname varchar (30),spassword varchar (30))")

# sid = input("Enter ID : ")
# name = input("Enter Name : ")
# password = input("Enter Password : ")

# st = (sid,name,password)

# mycursor.execute("insert into studinfo values(%s,%s,%s)",st)

# mydb.commit()

# print(mycursor.rowcount , " added...")

mycursor.execute("select * from studinfo")
res = mycursor.fetchall()
# res = mycursor.fetchone()
# res = mycursor.fetchmany(size=2)
print(res)
# for r in res:
#     print(r)

# sid = input("Enter ID : ")

# st = (sid,)

# mycursor.execute("delete from studinfo where sid=%s",st)
# mydb.commit()
# print(mycursor.rowcount," row deleted...")

# sid = input("Enter ID : ")
# name = input("Enter Name : ")
# password = input("Enter Password : ")

# sp = (name,password,sid)

# mycursor.execute("update studinfo set sname=%s,spassword=%s where sid=%s",sp)
# mydb.commit()
# print(mycursor.rowcount , " row updated...")
