num = [12,75,150,180,145,525,50]

for i in num:
    if i%5==0:
        if i>500:
            break
        elif i>150:
            continue
        else:
            print(i)