import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pythondb"
)

mycursor = mydb.cursor()

def insert(**args):
    targ = (args["id"],args["name"],args["city"])
    mycursor.execute("insert into students (id,name,city) values(%s,%s,%s)",targ)
    mydb.commit()
    print(mycursor.rowcount,"Record Inserted Successfully...")
    
def update(sid,args):
    uargs = (args,sid)
    mycursor.execute("update students set name=%s where id=%s",uargs)
    mydb.commit()
    print(mycursor.rowcount,"Record Updated Successfully...")

def delete(sid):
    did = (sid,)
    mycursor.execute("delete from students where id=%s",did)
    mydb.commit()
    print(mycursor.rowcount,"Record Deleted Successfully...")

def get_all_data():
    mycursor.execute("select * from students")
    res = mycursor.fetchall()
    for i in res:
        print(i)

def search(sid):
    ssid = (sid,)
    mycursor.execute("select * from students where id=%s",ssid)
    res = mycursor.fetchall()
    print(res)