from tkinter import *

r = Tk()
r.geometry("700x400")
l1 = Label(r,text="Root Window")

tl = Toplevel()
tl.geometry("500x250")
tl.title("Top Level Window")
l2 = Label(tl,text="TopLevel Window")

l1.pack()
l2.pack()
r.mainloop()