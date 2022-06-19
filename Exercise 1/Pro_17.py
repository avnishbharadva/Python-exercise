num = int(input("Enter Number : "))

ans = 2
fans = 0
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1:
            ans = 2
        else:
            ans = (ans*10)+2
    else:
        # print(ans)
        fans = fans + ans

print(fans)