# Name : Avnish Bharadva
# Roll NO : 2
# Date : 21/8/2022
# BCA 5th A

month = int(input("Enter Month : "))
year = int(input("Enter Year : "))

# 1/1/2000 - Saturday

day = {
    5 : "Th",
    6 : "Fr",
    0 : "Sa",
    1 : "Su",
    2 : "Mo",
    3 : "Tu",
    4 : "We"
}
monthday = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31 
}

if year%4==0:
    monthday[2] = 29

daynum = -1 + 1

for i in range(1,month):
    daynum = daynum + monthday[i]

for i in range(2000,year):
    if i%4==0:
        daynum = daynum + 2
    else:
        daynum = daynum + 1

daynum = daynum%7
print()
print(month," ",year)
print()

if daynum == 0:
    for i in range(0,7):
        print(day[i],end=" ")
else:
    k = daynum
    while k!=daynum-1:
        if k == 7:
            k = 0
        else:
            print(day[k] , end=" ")
            k=k+1
    else:
        print(day[k])

print()

for i in range(1,10):
    if i==7:
        print(i)
    else:
        print(i,end="  ")

for i in range(10,(monthday[month]+1)):
    if i%7==0:
        print(i)
    else:
        print(i,end=" ")