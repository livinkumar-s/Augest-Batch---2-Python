# class 
class Bottle:
    version="1.0.0.0"
    def __init__(self,c,r,h):
        print("We are creating water bottle...!")
        self.color=c #b1.color="Blue"
        self.radius=r
        self.height=h

    def findVolume(self,a,b): #b2
        print((22/7)*(self.radius**2)*(self.height))
        print(a+b)
    @classmethod
    def showVersion(cls): #Bottle
        print(cls.version)

    @staticmethod
    def greet():
        print("Hello")
    

# 4 attr, 3 method 

b1=Bottle("Blue",3,30) #4 attr 3 meth #Bottle.__init__(b1,"Blue",3,30)
# b2=Bottle("Black",5,25) #4 attr 3 meth



# b2.findVolume() # Bottle.findVolume(b2)
# b2.showVersion() # Bottle.showVersion(Bottle)
# b2.greet() # Bottle.greet()
# b2.findVolume(5,6)

# b2.findVolume()

# b1.color="Blue"
# b2.capacity=1200

# print(b1.color)
# print(b2.capacity)

# print(b1.color)
# print(b2.color)
# print(Bottle.version)
# print(b2.version)

# b1.findVolume()
# b2.findVolume()

# b1.showVersion()

# b1.greet()

# a=1
# b=4.4
# c="Hello"
# d=[1,2,3] 


# print(type(b1)) #<class "__main__.Bottle">
# from Functions import printSteps

# printSteps()

