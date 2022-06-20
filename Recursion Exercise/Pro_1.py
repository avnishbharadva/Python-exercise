num = int(input("Enter number : "))

ans = 0
def sum_of_digit(no):
    if no%10==0:
        return 0
    else:
        l = int(no%10)
        ans = l + int(sum_of_digit(no/10))
        return ans

print("sum of digit :",sum_of_digit(num))

