import mysql.connector as con 

db = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythonpractical"
)

cursor = db.cursor()

did = input("Enter Name for Delete : ")

updt = (did,)
cursor.execute("delete from userdata where username=%s",updt)
db.commit()
print("\n",cursor.rowcount,"deleted successfully...\n")

cursor.execute("select * from userdata")
res = cursor.fetchall()

for i in res:
    for j in i:
        print(j,end=" ")
    print()