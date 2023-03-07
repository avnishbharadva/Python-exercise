from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry("700x300+300+250")
    
def btn_click():
    msg = messagebox.showinfo("Message Title", "Message Desc")
    # msg = messagebox.showerror("Error","HEHE")
    # msg = messagebox.showwarning("Warning","HEHE Warning")

btn1 = Button(root, text="Click Me", background="red", activebackground="yellow", activeforeground="darkblue", width=30, height=5, font=("Verdana",20,'italic'), command=btn_click)
# font = ("font family", size, "weight")
btn1.pack()

root.mainloop()