import random
import string

pl = int(input("Enter Password Length : "))

characters = string.digits + '!@#$%&' + string.ascii_letters
password = "" 

for i in range(pl):
    password = password + random.choice(characters)

print("Password :",password)