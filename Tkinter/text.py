from tkinter import *

r = Tk()

def getval():
    f = t.get("1.0",END)
    Label(r,text=f).pack()

t = Text(r,width=30,height=10)
t.pack()
b = Button(r,text="click",command=getval)
b.pack()
r.mainloop()