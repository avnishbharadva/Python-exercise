from tkinter import *

root = Tk()

def getval():
    val = "Value is " + str(s.get())
    l.config(text=val)

var = DoubleVar()

s = Scale(root,variable=var,from_=1, to=50, orient="horizontal")
s.pack()

Button(root,text="Click",command=getval).pack()

l = Label(root,text="")
l.pack()
root.mainloop()