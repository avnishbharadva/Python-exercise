import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "lasttime"
)

mycursor = db.cursor()

# insert code

sid = int(input("Enter ID : "))
snm = input("Enter Name : ")
sem = input("Enter Email : ")
spass = input("Enter Password : ")

instup = (sid,snm,sem,spass)

mycursor.execute("insert into lasttimetable values(%s,%s,%s,%s)",instup)

print(mycursor.rowcount,"row inserted...")

db.commit()

# Update Code

# sid = int(input("Enter ID for Update : "))

# snm = input("New Name : ")
# sem = input("New EMail : ")
# spass = input("New Password : ")

# uptu = (snm,sem,spass,sid)

# mycursor.execute("update lasttimetable set sname=%s,semail=%s,spass=%s where sid=%s",uptu)

# print(mycursor.rowcount,"row updated")

# db.commit()

# Delete Code

# sid = int(input("Enter ID for Delete : "))

# dt = (sid,)

# mycursor.execute("delete from lasttimetable where sid=%s",dt)

# print(mycursor.rowcount,"row deleted...")
# db.commit()

mycursor.execute("select * from lasttimetable")

res = mycursor.fetchall()

for r in res:
    for j in r:
        print(j,end=" ")
    print()