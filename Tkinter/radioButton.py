# from tkinter import *

# win = Tk()
# win.title("Message Widget Example")
# win.geometry("200x200")

# r_radio = StringVar()

# def radio_click():
#     txt = r_radio.get()
#     lbl = Label(win,text=txt)
#     lbl.pack()

# radio1 = Radiobutton(win,text="C Language",value=1,variable=r_radio,
#                                                 command=radio_click)
# radio2 = Radiobutton(win,text="C++",value=2,variable=r_radio,
#                                                 command=radio_click)
# radio3 = Radiobutton(win,text="Python",value=3,variable=r_radio,
#                                                 command=radio_click)

# radio1.pack()
# radio2.pack()
# radio3.pack()
# win.mainloop()

from tkinter import *

root = Tk()
root.geometry("700x400+250+200")

var1 = StringVar()

def r_click():
    l.config(text= var1.get())    

r1 = Radiobutton(root, text="Cricket", variable=var1, value="Cricket", command=r_click)
r1.pack()
r2 = Radiobutton(root, text="Football", variable=var1, value="Football", command=r_click)
r2.pack()
r3 = Radiobutton(root, text="Hockey", variable=var1, value="Hockey", command=r_click)
r3.pack()

l = Label(root, text="")
l.pack()

root.mainloop()