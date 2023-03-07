from tkinter import *

root = Tk()

xf = root.winfo_screenwidth()  # 1536
yf = root.winfo_screenheight()  # 864

x = int((xf/2) - (700/2))
y = int((yf/2) - (400/2))

print(xf,yf,x,y)

root.geometry("700x400+"+str(x)+"+"+str(y))

root.mainloop()