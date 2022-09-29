class First:
    x = 100

class Second(First):
    y = 200

class Third(First):
    z = 300

o1 = Second()
print(o1.x,o1.y)
o2 = Third()
print(o2.x,o2.z)