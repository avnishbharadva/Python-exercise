num = int(input("Enter Number : "))

def total_digit(no,t):
    if no==0:
        return t
    else:
        ans = total_digit(int(no/10),t+1)
        return ans
        
print("Total Digit :",total_digit(num,0))