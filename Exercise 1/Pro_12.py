f = 0
s = 1

for i in range(1,11):
    print(f,end=" ")
    ans = f + s
    f = s
    s = ans
