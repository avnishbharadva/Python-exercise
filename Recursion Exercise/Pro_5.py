num = int(input("Enter Number : "))

i = 0

def rev_num(no):
    global i
    if no==0:
        return 1
    else:
        l = no%10
        i = (i *10) + l
        rev_num(no//10)
        return i

print("Reverse Number :",rev_num(num))