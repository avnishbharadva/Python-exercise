class First:
    x = 10

class Second(First):
    y = 20

class Third(Second):
    z = 30

obj = Third()
print(obj.x,obj.y,obj.z)