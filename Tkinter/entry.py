from tkinter import *

r = Tk()

def add():
    d = e.get()
    Label(r,text=d).pack()
    
e = Entry(r)
e.pack()
Button(r,text="Click",command=add).pack()
r.mainloop()