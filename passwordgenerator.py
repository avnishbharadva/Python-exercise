# Name : Avnish Bharadva
# Roll NO : 2
# Date : 21/8/2022
# BCA 5th A

import random
import string

pl = int(input("Enter Password Length : "))

characters = string.digits + '!@#$%&' + string.ascii_letters
password = "" 

for i in range(pl):
    password = password + random.choice(characters)

print("Password :",password)