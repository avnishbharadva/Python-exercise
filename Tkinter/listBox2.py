from tkinter import *

root = Tk()
root.geometry("700x400+250+200")

lb1 = Listbox(root)
lb1.insert(1,"Avnish")
lb1.insert(2,"Shivam")
lb1.insert(3,"Ruchit")
lb1.insert(4,"Krupesh")
lb1.pack()

lb2 = Listbox(root)
lb2.pack()

def b1_single():
    curindex = lb1.curselection()
    lb2.insert(0,lb1.get(curindex))
    lb1.delete(curindex,curindex)

def b2_all():
    len = lb1.size()
    # print(len)
    for i in range(0,len):
        # print("cur",i)
        lb2.insert(1,lb1.get(i))
        # lb1.delete(ACTIVE)
    
    lb1.delete(0,len)

def b3_single():
    curindex = lb2.curselection()
    lb1.insert(0,lb2.get(curindex))
    lb2.delete(curindex,curindex)

def b4_all():
    len = lb2.size()

    for i in range(0,len):
        lb1.insert(1,lb2.get(i))

    lb2.delete(0,len)

b1 = Button(root, text=">", command=b1_single)
b1.pack()
b2 = Button(root, text=">>", command=b2_all)
b2.pack()
b3 = Button(root, text="<", command=b3_single)
b3.pack()
b4 = Button(root, text="<<", command=b4_all)
b4.pack()
root.mainloop()