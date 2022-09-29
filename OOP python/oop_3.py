class Demo:

    def setData(self):
        self.roll = int(input("Enter Roll NO : "))
        self.name = input("Enter Name : ")

    def getData(self):
        print(self.roll,self.name)

obj = Demo()
obj.setData()
obj.getData()