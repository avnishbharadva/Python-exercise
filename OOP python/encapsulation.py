class Base:
    
    def __init__(self):
        self.nm = "Avnish"
        self.__roll = 2
        print(self.__roll)

class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print(self.nm)
        # print(self.__roll)

obj = Derived()
# print(obj.__roll)