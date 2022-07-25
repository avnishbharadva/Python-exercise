l = [20,56,2,89,-8,66,99,45]
print(l)
f = int(input("Enter Value For Find : "))

for i in range(len(l)):
    if l[i]==f:
        print(f,"is placed on",i,"index")
        break