from tkinter import *

root = Tk()

root.geometry("700x400+300+200")

c = Canvas(root, width=500, height=300, bg="yellow", bd=30, relief=GROOVE, cursor="circle")

l = c.create_line(200,200,400,250, fill="blue")

o = c.create_oval(100,100,200,200, fill="aqua")

r = c.create_rectangle(300,100,450,200, fill="aqua")

c.pack()

root.mainloop()