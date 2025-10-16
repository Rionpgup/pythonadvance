class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def get_name(self):
        return self.__name
    def set_name(self , name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

student1 = Student("RUBIK" , 12)

print(student1.get_name())
student1.set_name("Ylli")
print("Update name is:" , student1.get_name())
print("age is:" , student1.get_age())
student1.set_age(18)
print("Update age is" , student1.get_age())
