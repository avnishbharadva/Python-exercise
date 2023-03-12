from tkinter import *

r = Tk()

menubar = Menu(r)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = r.destroy)

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo",command=None)
edit.add_cascade(label="Redo",command=None)

window = Menu(menubar, tearoff=0)
menubar.add_cascade(label="KSNjbjbws",menu=window)
window.add_command(label="ffs",command=None)
window.add_command(label="fdd",command=None)

r.config(menu=menubar)

r.mainloop()