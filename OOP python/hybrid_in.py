class First:
    x = 100

class Second(First):
    y = 200

class Third(First):
    z = 300

class Fourth(Second,Third):
    a = 500

obj = Fourth()
print(obj.x,obj.y,obj.z,obj.a)