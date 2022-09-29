class Parent:
    x = 10

class Child(Parent):
    y = 20

obj = Child()
print(obj.x,obj.y)