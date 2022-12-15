import tkinter as tk
import random

win = tk.Tk()

t = win.title("Puzzle Game")

window_width = 479
window_height = 600

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry(str(window_width)+"x"+str(window_height)+"+"+str(x_cordinate)+"+"+str(y_cordinate))
win.resizable(False,False)

#Generate 16 random numbers between 1 and 17

randomlist = random.sample(range(1, 16), 15)
# print(randomlist)

moves = 0

def check_blank(x):
    global moves
    moves += 1
    l["text"] = moves
    b16["text"] = x["text"]
    b16["bg"] = "hotpink"
    x["text"] = " "
    x["bg"] = "white"

# for i in range(1,5):
#     b = tk.Button(win, text=randomlist[i-1], width=10, height=5, bg="hotpink", font=("Helvetica", 14), command=check_blank)
#     b.grid(row=0, column=i-1)

# for i in range(5,9):
#     b = tk.Button(win, text=randomlist[i-1], width=10, height=5, bg="hotpink", font=("Helvetica", 14), command=check_blank)
#     b.grid(row=1, column=i-5)

# for i in range(9,13):
#     b = tk.Button(win, text=randomlist[i-1], width=10, height=5, bg="hotpink", font=("Helvetica", 14), command=check_blank)
#     b.grid(row=2, column=i-9)

# for i in range(13,17):
#     if i==16:
#         b = tk.Button(win, text=" ", width=10, height=5, font=("Helvetica", 14))
#         b.grid(row=3, column=3)
#     else:
#         b = tk.Button(win, text=randomlist[i-1], width=10, height=5, bg="hotpink", font=("Helvetica", 14), command=lambda : check_blank(b))
#         b.grid(row=3, column=i-13)

b1 = tk.Button(win,text=randomlist[0],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b1))
b2 = tk.Button(win,text=randomlist[1],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b2))
b3 = tk.Button(win,text=randomlist[2],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b3))
b4 = tk.Button(win,text=randomlist[3],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b4))
b5 = tk.Button(win,text=randomlist[4],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b5))
b6 = tk.Button(win,text=randomlist[5],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b6))
b7 = tk.Button(win,text=randomlist[6],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b7))
b8 = tk.Button(win,text=randomlist[7],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b8))
b9 = tk.Button(win,text=randomlist[8],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b9))
b10 = tk.Button(win,text=randomlist[9],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b10))
b11 = tk.Button(win,text=randomlist[10],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b11))
b12 = tk.Button(win,text=randomlist[11],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b12))
b13 = tk.Button(win,text=randomlist[12],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b13))
b14 = tk.Button(win,text=randomlist[13],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b14))
b15 = tk.Button(win,text=randomlist[14],width="10",height="5", bg="hotpink", font=("Helvetica", 14),command=lambda : check_blank(b15))
b16 = tk.Button(win,text=" ",width="10",height="5", font=("Helvetica", 14))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=0,column=3)
b5.grid(row=1,column=0)
b6.grid(row=1,column=1)
b7.grid(row=1,column=2)
b8.grid(row=1,column=3)
b9.grid(row=2,column=0)
b10.grid(row=2,column=1)
b11.grid(row=2,column=2)
b12.grid(row=2,column=3)
b13.grid(row=3,column=0)
b14.grid(row=3,column=1)
b15.grid(row=3,column=2)
b16.grid(row=3,column=3)

l = tk.Label(win, text=moves, width=10, height=5, font=("Helvetica", 14))
l.grid(row=4, column=1)

win.mainloop()