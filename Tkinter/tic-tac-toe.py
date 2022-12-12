import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

window_width = 448
window_height = 550

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry(str(window_width)+"x"+str(window_height)+"+"+str(x_cordinate)+"+"+str(y_cordinate))
win.resizable(False,False)

title = win.title("Tic Tac Toe")

player = "X"
count = 0

def restart():
    global player,count
    count=0
    player = "X"
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "
    b1["bg"] = "white"
    b2["bg"] = "white"
    b3["bg"] = "white"
    b4["bg"] = "white"
    b5["bg"] = "white"
    b6["bg"] = "white"
    b7["bg"] = "white"
    b8["bg"] = "white"
    b9["bg"] = "white"
    l["text"] = "Turn : " + player
    print("Restart called")
    print("Count : " , count , "Player : " , player)

def clearVar():
    global count,player
    count=0
    player="X"
    print("Clear called")
    print("Count : " , count , "Player : " , player)

def check_win(user):
    global count,player

    if b1["text"] == user and b2["text"] == user and b3["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b4["text"] == user and b5["text"] == user and b6["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b7["text"] == user and b8["text"] == user and b9["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b1["text"] == user and b4["text"] == user and b7["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b2["text"] == user and b5["text"] == user and b8["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b3["text"] == user and b6["text"] == user and b9["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b1["text"] == user and b5["text"] == user and b9["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()
    if b3["text"] == user and b5["text"] == user and b7["text"] == user:
        clearVar()
        messagebox.showinfo("Winner",user + " is Winner...")
        restart()

def btn_click(b):
    global player,count
    print("Count : " , count , "Player : " , player)

    if b["text"] == " " and count<9:
        if player == "X":    
            b["text"] = player
            b.configure(bg="red")
            check_win("X")
            player = "O"
            count+=1
            if count==9:
                messagebox.showinfo("Match Tie","Everyone is Loser...")
                restart()
        else:
            b["text"] = player
            check_win("O")
            b.configure(bg="pink")
            player = "X"
            count+=1
            if count==9:
                messagebox.showinfo("Match Tie","Everyone is Loser...")
                restart()
    else:
        messagebox.showwarning("Warning","Already Clicked...")
    l["text"] = "Turn : " + player


    
b1 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b1))
b2 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b2))
b3 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b3))
b4 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b4))
b5 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b5))
b6 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b6))
b7 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b7))
b8 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b8))
b9 = tk.Button(win,text=" ",width="20",height="10",command=lambda : btn_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

l = tk.Label(win,text="Turn : " + player,font=("Helvetica", 18))
l.grid(row=4,column=0,ipady=14)

br = tk.Button(win,text="Restart Game",font=("Helvetica",14),background="aqua",foreground="darkblue",command=restart)
br.grid(row=4,column=2)

win.mainloop()