import tkinter as tk

win = tk.Tk()

t = win.title("CRUD")
win.geometry("400x400")

msg = tk.Label(win, text="UserName")
msg.grid(column=0, row=0)
# msg.pack()

txt = tk.Entry(win)
txt.grid(column=1, row=0)
# btn.pack()

def btn_click():
    t = txt.get()
    l = tk.Label(win , text=t)
    l.pack()
    # l.grid(column=2, row=1)

btn = tk.Button(win, text="Click Me", command=btn_click())
btn.grid(column=1, row=1)

win.mainloop()