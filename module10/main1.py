class Student:
    def init(self, name, age):
        self.name = name
        self.age = age


    @property
    def name(self):
        return  self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def age(self):
         return self.age
    @age.setter
    def age(self, age):
         self.age = age

s = Student("John", 19)
print("Name of student",s.name)
print(" Age of student ",s.age)

s.name = "Deon"
s.age = 14
print("Update name  of student",s.name)
print("Update age of student ",s.age)