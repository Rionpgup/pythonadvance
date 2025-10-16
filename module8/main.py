# def calculate(length, width):
#     return length * width
# def calculate_perimeter(length, width):
#     return 2 * (length  * width)
#
#
#
# length = 5
# width = 3
#
# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
#
# print(f"Area of area is = {area}")
# print(f"Perimeter of area is = {perimeter}")
#
# class Rectangle:
#     def __init__(self, length, width ):
#         self.width = width
#         self.length = length
#
#     def calculate_area(self):
#         return self.length * self.width
#     def calculate_perimeter(self):
#         return self.length + self.width
#
# my_rectangle = Rectangle(10,20)
# area = my_rectangle.calculate_area()
# perimeter = my_rectangle.calculate_perimeter()
# print(f"Area: {area}")
# print(f"Perimeter: {perimeter}")
# class Person:
#      def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#      def greet(self):
#          print(f"Hello {self.name}, you are {self.age} years old.")
#
# person1 = Person("John", 36)
# person2 = Person("Rubik", 15)
#
# person1.greet()
# person2.greet()

# class Student:
#     school_name = "Digital School"
#
# student1 = Student()
#
# print(student1.school_name)


# class Student:
#     school_name ="Digital school"
#
#     def __init__(self,name,age , course):
#         self.name = name
#         self.age = age
#         self.course = course
#
# studenti1 = Student("rion",16 , "Python")
# studenti2 = Student("rion",16 , "Java")
#
# print(studenti1.course)
# print(studenti2.course)


# class MyClass:
#     def __init__(self):
#         self.private_variable = "this is private variable"
#         # self.public_variable = "this is public variable"
#     def __private_method(self):
#          print("this is a private method")
#
#  my_class = MyClass()
#  #print(my_class.private_variable)
#
# my_class.__private_method()
#
class MyClass:
    def __init__(self):
        self._protected_variable = "Hello Wo"

    def protected_method(self):
        print("Protected Method")

print(my_class._protected_variable)
# print(my_class._protected_method())

my_class._protected_method()