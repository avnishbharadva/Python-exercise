import tkinter as tk

win = tk.Tk()

t = win.title("CRUD")

window_width = 448
window_height = 550

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry(str(window_width)+"x"+str(window_height)+"+"+str(x_cordinate)+"+"+str(y_cordinate))
win.resizable(False,False)

msg = tk.Label(win, text="UserName",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=2, relief="solid")
msg.grid(column=0, row=0)

txt = tk.Entry(win,width=40)
txt.grid(column=1, row=0)

pwd = tk.Label(win, text="Password",width=16,height=3,font=("Helvetica",14),foreground="#fff",bg="#972aad",borderwidth=2, relief="solid")
pwd.grid(column=0, row=2)

passtxt = tk.Entry(win,width=40)
passtxt.grid(column=1, row=2)

# def btn_click():
#     t = txt.get()
#     l = tk.Label(win , text=t)
#     l.grid(column=0, row=4)

btn = tk.Button(win, text="Click Me")
btn.grid(column=0, row=6)

win.mainloop()