from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry("700x350+300+240")

def messageExa():
    # msg = messagebox.showinfo("title","content")
    # msg = messagebox.askyesno("title", "message")
    # msg = messagebox.askquestion("title", "message")
    # msg = messagebox.askokcancel("title","message")
    msg = messagebox.askretrycancel("title","message")
    print(msg)

Button(root,text="Click", command=messageExa).pack()

root.mainloop()