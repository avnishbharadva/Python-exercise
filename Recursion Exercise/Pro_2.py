num = int(input("Enter number : "))

ans = 0
def sum_of_num(n):
    if n==1:
        return 1
    else:
        ans = n + sum_of_num(n-1)
        return ans

print("Sum of 1 to",num,"is : ",sum_of_num(num))