num = int(input("Enter any number : "))

chk=0
while num>0:
    num = int(num/10)
    chk += 1

print(chk)