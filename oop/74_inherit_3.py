#example of hierarchical inheritance 
#parent/super/base class
class MyMath:
    def getPi(self):
        pi = 22/7
        return pi 
    def getSquare(self,number):
        square = number * number
        return square
class Circle(MyMath):
    def __init__(self,radius):
        self.radius = radius 
    def getArea(self):
        area = super().getPi() * super().getSquare(self.radius)
        return area 
class Square(MyMath):
    def __init__(self,size):
        self.size = size
    def getArea(self):
        area = super().getSquare(self.size)
        return area 
    

#create circle class object 
radius = int(input("Enter radius"))
c1 = Circle(radius)

size = int(input("Enter size of square"))
s1 = Square(size)

print("Circle area",c1.getArea())
print("Square area",s1.getArea())

