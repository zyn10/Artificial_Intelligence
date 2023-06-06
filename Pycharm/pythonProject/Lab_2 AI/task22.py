class Shape():
    def __init__(self):
        print("Shape Class Called")
    def printRect(self):
        print("***Rectangle Class ***")
    def printCircle(self):
        print("*** Circle Class Called ***")

class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__()#ya mena nai kea compiler na suggestion d ha k super class add kro agr opar access krna ha
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def circle_area(self):
        return 3.14*self.radius*self.radius
    def circle_perimeter(self):
        return 3.14 *2* self.radius
rect = Rectangle(10,10)
rect.printRect()

print ("Rectangle Area :- ",rect.rectangle_area())
print ("Circle Area :- ",rect.rectangle_perimeter())
circ = Circle(10)
circ.printCircle()
print ("Circle Area :- ",circ.circle_area())
print ("Circle Perimeter :- ",circ.circle_perimeter())
