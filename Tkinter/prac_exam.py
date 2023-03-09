from tkinter import *
import mysql.connector as db
from tkinter import ttk
from tkinter import messagebox
import os
mydb = db.connect(
    host="localhost",
    user="root",
    password="",
    database="tkinter_prac_6"
)

mycursor = mydb.cursor()

# print("DB Connected...")

# Database Logic 

def show():
    mycursor.execute("select * from data")
    records = mycursor.fetchall()
    # print(records)

    for r in records:
            listBox.insert("","end",values=r)

def Add():
    sid = eid.get()
    snm = enm.get()
    sem = eem.get()
    spw = epw.get()
    # print(sid,snm,sem,spw)
    stp = (sid,snm,sem,spw)

    try:
        mycursor.execute("insert into data values(%s,%s,%s,%s)", stp)
        mydb.commit()
        msg = messagebox.showinfo("Success", "Data Inserted...")
        eid.delete(0,END)
        enm.delete(0,END)
        eem.delete(0,END)
        epw.delete(0,END)
        eid.focus_set()
        root.destroy()
        os.system('prac_exam.py')
    except:
        msg = messagebox.showerror("Error", "Data Not Inserted...")

def delete():
    sid = eid.get()
    
    try:
        mycursor.execute("delete from data where id=%s",(sid,))
        mydb.commit()
        msg = messagebox.showinfo("Success", "Data Deleted...")
        eid.delete(0, END)
        root.destroy()
        os.system('prac_exam.py')
        eid.focus_set()
    except:
        msg = messagebox.showerror("Error", "Data Not Deleted...")

def update():
    sid = eid.get()
    snm = enm.get()
    sem = eem.get()
    spw = epw.get()

    stp = (snm,sem,spw,sid)

    try:
        mycursor.execute("update data set name=%s,email=%s,password=%s where id=%s",stp)
        mydb.commit()
        msg = messagebox.showinfo("Success", "Data Updated...")
        root.destroy()
        os.system('prac_exam.py')
    except:
        msg = messagebox.showerror("Error", "Data Not Updated...")

# Design

root = Tk()
root.geometry("820x500+350+150")

global e1, e2, e3, e4

lh = Label(root, text="Student Registration", font=("Verdana",20,"bold"))
lh.place(x=400,y=5)

lsid = Label(root, text="ID")
lsid.place(x=10,y=10)
lsnm = Label(root, text="Name")
lsnm.place(x=10,y=40)
lsem = Label(root, text="Email")
lsem.place(x=10,y=70)
lspw = Label(root, text="Password")
lspw.place(x=10,y=100)

eid = Entry(root)
eid.place(x=140,y=10)
enm = Entry(root)
enm.place(x=140,y=40)
eem = Entry(root)
eem.place(x=140,y=70)
epw = Entry(root)
epw.place(x=140,y=100)

badd = Button(root, text="ADD",width=13,height=3, command=Add)
badd.place(x=30,y=130)
bdel = Button(root, text="DELETE",width=13,height=3, command=delete)
bdel.place(x=140,y=130)
bup = Button(root, text="UPDATE",width=13,height=3, command=update)
bup.place(x=250,y=130)

cols = ('id','name','email','password')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
# listBox.bind('<Double-Button-1>',Delete)

root.mainloop()