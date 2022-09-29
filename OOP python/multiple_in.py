class First:
    x = 10

class Second:
    y = 20

class Third(First,Second):
    z = 30

obj = Third()
print(obj.x,obj.y,obj.z)