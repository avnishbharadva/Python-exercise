from tkinter import *

r = Tk()

def value_changed():
    d = current_value.get()
    l.config(text=d)
    
current_value = IntVar()

s = Spinbox(r,from_=1,to=40,textvariable=current_value,command=value_changed)
s.pack()

l = Label(r,text="")
l.pack()

r.mainloop()