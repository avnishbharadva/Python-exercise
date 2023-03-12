from tkinter import *

r = Tk()

sb = Scrollbar(r)
sb.pack(side=RIGHT,fill=Y)

lb = Listbox(r,yscrollcommand=sb.set)
for i in range(80):
    lb.insert(i,"Value " + str(i))
lb.pack(side=LEFT,fill=BOTH)

sb.config(command=lb.yview)
r.mainloop()