from tkinter import *

win = Tk()

window_width = 900
window_height = 500

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

# win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
win.geometry(str(window_width)+"x"+str(window_height)+"+"+str(x_cordinate)+"+"+str(y_cordinate))

t = win.title("Avnish Bharadva")
lbl = Label(win, text="Good Bye Cruel World")
lbl.pack()
ent = Entry(win)
ent.pack()
btn = Button(win, text="Click Me")
btn.pack()
print(win.title())
win.mainloop()