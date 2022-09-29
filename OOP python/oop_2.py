class Demo:
    roll = 0
    name = ""

    def __init__(self,r,n):
        self.roll = r
        self.name = n
    
    def printData(self):
        print(self.roll,self.name)

obj = Demo(2,"avnish")
obj.printData()