class Shape:
    def area(self):
        pass

class Circle(Shape):
    def init(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def init(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return  self.width * self.height

class Triangle(Shape):
    def init(self,base,height):
        self.base = base
        self.height = height
        def area(self):
        return 8.5 self.base self.height


circle = Circle(5)
rectangle = Rectangle(4,6)
triangle = Triangle(3,4)

print("Area of the circle", circle.area())
print("Area of the circle", rectangle.area())
print("Area of the circle", triangle.area())