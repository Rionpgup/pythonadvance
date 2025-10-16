from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be a positive number.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

# Adult Class
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 65 <= bmi < 75:
            return "Normal weight"
        elif 76<= bmi < 100:
            return "Overweight"
        else:
            return "Obese"

# Child Class
class Child(Person):
    def calculate_bmi(self):
        adjustment_factor = 1.1  # Arbitrary adjustment factor for children
        return (self.weight / (self.height ** 2)) * adjustment_factor

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"

# BMIApp Class
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person: Person):
        self.people.append(person)

    def collect_user_data(self):
        while True:
            try:
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                weight = float(input("Enter your weight (kg): "))
                height = float(input("Enter your height (m): "))

                if age >= 18:
                    person = Adult(name, age, weight, height)
                else:
                    person = Child(name, age, weight, height)

                self.add_person(person)
                print("Person added successfully.\n")

                cont = input("Do you want to add another person? (yes/no): ").strip().lower()
                if cont != 'yes':
                    break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.\n")

    def print_results(self):
        print("\n--- BMI Results ---")
        if not self.people:
            print("No people to show.")
        for person in self.people:
            person.print_info()
            print("-" * 30)

    def run(self):
        print("Welcome to the BMI Calculator App!")
        self.collect_user_data()
        self.print_results()


# Run the application
if __name__ == "__main__":
    app = BMIApp()
    app.run()
