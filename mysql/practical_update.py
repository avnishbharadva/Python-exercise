import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonpractical"
)

cursor = db.cursor()

uid = int(input("Enter ID for Update : "))
unm = input("Enter Name : ")
upass = input("Enter Password : ")
cpass = input("Confirm Password : ")
uemail = input("Enter Email : ")

if upass==cpass:
    updt = (unm,upass,uemail,uid)
    cursor.execute("update userdata set username=%s,password=%s,email=%s where id=%s",updt)
    db.commit()
    print("\n",cursor.rowcount,"updated successfully...\n")
else:
    print("\nUpdate failed...\n")

cursor.execute("select * from userdata")
res = cursor.fetchall()

for i in res:
    for j in i:
        print(j,end=" ")
    print()