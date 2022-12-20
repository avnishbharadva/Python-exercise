import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

t = win.title("CRUD")

window_width = 448
window_height = 550

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry(str(window_width)+"x"+str(window_height)+"+"+str(x_cordinate)+"+"+str(y_cordinate))
win.resizable(False,False)

def insbtn_click():
    messagebox.showinfo("Insert","Data Inserted Successfully...")

lblempid = tk.Label(win, text="Emp ID",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=1, relief="solid")
lblempid.grid(column=0, row=0)

txtempid = tk.Entry(win,width=40,font=("Helvetica",28))
txtempid.grid(column=1, row=0)

lblempnm = tk.Label(win, text="Emp Name",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=1, relief="solid")
lblempnm.grid(column=0, row=1)

txtempnm = tk.Entry(win,width=40,font=("Helvetica",28))
txtempnm.grid(column=1, row=1)

lbldes = tk.Label(win, text="Designation",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=1, relief="solid")
lbldes.grid(row=2,column=0)

txtdes = tk.Entry(win,width=40,font=("Helvetica",28))
txtdes.grid(row=2,column=1)

lblsal = tk.Label(win, text="Emp Salary",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=1, relief="solid")
lblsal.grid(row=3,column=0)

txtsal = tk.Entry(win,width=40,font=("Helvetica",28))
txtsal.grid(row=3,column=1)

insbtn = tk.Button(win, text="Insert",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=1, relief="solid",command=insbtn_click)
insbtn.grid(row=4,column=0)

disbtn = tk.Button(win, text="Display",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=1, relief="solid")
disbtn.grid(row=5,column=0)

win.mainloop()