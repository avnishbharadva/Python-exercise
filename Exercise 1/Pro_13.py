num = int(input("Enter Number : "))

ans = 1
for i in range(num,0,-1):
    ans *= i
else:
    print("Factorial of",num,"is",ans)