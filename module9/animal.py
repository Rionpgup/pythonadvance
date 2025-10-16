class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("some generic animal sound")
    def desc(self):
        print(f"This is an animal name {self.name}")



class Dog(Animal):
    def __init__(self, name , breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Dog sound")

    def desc(self):
        super().desc()
        print(f"Breed {self.breed} ")


class cat(Animal):
    def __init__(self, name , color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Cat sound")
    def desc(self):
        super().desc()
        print(f'color {self.color}')

animal = Animal("Seneric Animal")
animal.sound()

animal.desc()

dog = Dog("Rex" , "Golden Retriever")
dog.sound()
dog.desc()


cat = cat("Seneric", "Blue")
cat.sound()
cat.desc()