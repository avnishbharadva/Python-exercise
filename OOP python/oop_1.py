class Demo:
    x = 10

    def __init__(self,a=99):
        self.x = a 
        print("constructor")

obj = Demo()
print(obj.x)