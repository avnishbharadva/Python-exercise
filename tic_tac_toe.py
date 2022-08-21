# Name : Avnish Bharadva
# Roll NO : 2
# Date : 21/8/2022
# BCA 5th A

lst = [0,1,2,3,4,5,6,7,8]

ptrn = 0

def print_board():
    for i in range(0,9):
        if i==2 or i==5 or i==8:
            print(lst[i])
        else:
            print(lst[i],end=" | ")

def check_pattern(no):
    global ptrn
    if lst[0]=='X' and lst[1]=='X' and lst[2]=='X':
        ptrn = 1
    elif lst[0]=='X' and lst[4]=='X' and lst[8]=='X':
        ptrn = 1
    elif lst[0]=='X' and lst[3]=='X' and lst[6]=='X':
        ptrn = 1
    elif lst[2]=='X' and lst[4]=='X' and lst[6]=='X':
        ptrn = 1
    elif lst[1]=='X' and lst[4]=='X' and lst[7]=='X':
        ptrn = 1
    elif lst[2]=='X' and lst[5]=='X' and lst[8]=='X':
        ptrn = 1
    elif lst[3]=='X' and lst[4]=='X' and lst[5]=='X':
        ptrn = 1
    elif lst[6]=='X' and lst[7]=='X' and lst[8]=='X':
        ptrn = 1

    elif lst[0]=='O' and lst[1]=='O' and lst[2]=='O':
        ptrn = 2
    elif lst[0]=='O' and lst[4]=='O' and lst[8]=='O':
        ptrn = 2
    elif lst[0]=='O' and lst[3]=='O' and lst[6]=='O':
        ptrn = 2
    elif lst[2]=='O' and lst[4]=='O' and lst[6]=='O':
        ptrn = 2
    elif lst[1]=='O' and lst[4]=='O' and lst[7]=='O':
        ptrn = 2
    elif lst[2]=='O' and lst[5]=='O' and lst[8]=='O':
        ptrn = 2
    elif lst[3]=='O' and lst[4]=='O' and lst[5]=='O':
        ptrn = 2
    elif lst[6]=='O' and lst[7]=='O' and lst[8]=='O':
        ptrn = 2

# def check_valid_num(n):
#     if i[n]=='X' or i[n]=='O':
#         print("Enter Valid Position")
def dec_winner():
    if ptrn==1:
        print("User 1 Winner")
        return 1
    if ptrn==2:
        print("User 2 Winner")
        return 2

print_board()

for i in range(9):        
    if i%2==0:
        u1 = int(input("User 1 : "))
        # check_valid_num(u1)
        lst[u1] = 'X'
        check_pattern(u1)
        res = dec_winner()
        if res==1:
            break
        print_board()
    else:
        u2 = int(input("User 2 : "))
        # check_valid_num(u2)
        lst[u2] = 'O'
        check_pattern(u2)
        res = dec_winner()
        if res==2:
            break
        print_board()
else:
    print("Game Over")