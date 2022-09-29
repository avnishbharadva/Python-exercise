try:
    a = 20
    b = 0
    # c = a/b
    c = 30+"asss"

except ZeroDivisionError:
    print("not divide by zero")
except:
    print("other error")
else:
    print(c)
finally:
    print("finaalllyyyy")

# a = 10
# b = 0
# c = 30 + "asa"
# print(c)