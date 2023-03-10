from tkinter import *

root = Tk();
root.geometry("800x")
def btn_click():
    curindex = lb.curselection()
    print(curindex)
    for i in curindex:
        lb2.insert(0,lb.get(i))

def btn_remove():
    curindex = lb2.curselection()
    for i in curindex:
        lb2.delete(i,i)

lb = Listbox(root,selectmode=MULTIPLE)
lb.insert(1,'BCA')
lb.insert(2,'B.Sc.IT')
lb.insert(3,"PGDCA")
lb.pack()

lb2 = Listbox(root)
lb2.pack()

btn = Button(root, text="ADD", command=btn_click)
btn.pack()
btn2 = Button(root, text="REMOVE", command=btn_remove)
btn2.pack()

root.mainloop()