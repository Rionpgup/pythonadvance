class Dog:
    def __init__(self,name,):
        self.name = name
       



class
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} says hello")

class Bird:
    def __init__(self,name,):
        self.name = name

    def sound(self):
        print(f"{self.name} says Pershendetje")


dog = Dog("Dog")
cat = Cat("Cat")
bir = Bird("Bird")


for animal in (dog , cat , bir):
    animal.sound()