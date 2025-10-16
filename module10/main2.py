from abc import ABC, abstractmethod

from module9.main4 import Circle


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, radius):
        self.width = radius


    def area(self):
        return 3.14 + self.radius + self.radius

    class Square(Shape):
        def area(self):
            self.length = length

        def area(self):
            return self.length * self.length

circle1 = Circle(2)

square1 = Square(10)

print(square1.area())
print(square1.area())