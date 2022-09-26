import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonpractical"
)

cursor = db.cursor()

uid = int(input("Enter ID : "))
un = input("\nEnter User Name : ")
upass = input("\nEnter Password : ")
cpass = input("\nConfirm Password : ")
uemail = input("\nEnter Email : ")

if upass==cpass:
    inst = (uid,un,upass,uemail)
    cursor.execute("insert into userdata values(%s,%s,%s,%s)",inst)
    db.commit()
    print("\n",cursor.rowcount,"row inserted successfully...\n")
else:
    print("\nPassword not matched...\n")

cursor.execute("select * from userdata")
res = cursor.fetchall()

for i in res:
    for j in i:
        print(j,end=" ")
    print()