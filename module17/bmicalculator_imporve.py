import streamlit as st
from abc import ABC, abstractmethod


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

    def get_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        return {
            "Name": self.name,
            "Age": self.age,
            "Weight (kg)": self.weight,
            "Height (m)": self.height,
            "BMI": round(bmi, 2),
            "Category": category
        }


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"


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


def main():
    st.set_page_config(page_title="BMI Calculator", layout="centered")
    st.title(" BMI Calculator App")
    st.markdown("Enter your details below to calculate your **Body Mass Index (BMI)**.")

    with st.form("bmi_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
        height = st.number_input("Height (m)", min_value=0.3, max_value=3.0, step=0.01)
        submitted = st.form_submit_button("Calculate BMI")

    if submitted:
        try:
            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            info = person.get_info()

            st.success(" BMI Calculation Successful!")
            st.subheader("Results:")
            st.write(f"**Name:** {info['Name']}")
            st.write(f"**Age:** {info['Age']}")
            st.write(f"**Weight:** {info['Weight (kg)']} kg")
            st.write(f"**Height:** {info['Height (m)']} m")
            st.write(f"**BMI:** {info['BMI']}")
            st.write(f"**Category:** {info['Category']}")

            # Add visual indicator for category
            if info["Category"] == "Underweight":
                st.warning("You are underweight. Consider consulting a nutritionist.")
            elif info["Category"] == "Normal weight":
                st.success(" You have a healthy weight!")
            elif info["Category"] == "Overweight":
                st.warning(" You are overweight. Try to maintain a balanced diet.")
            else:
                st.error(" You are obese. Please consult your doctor.")

        except ValueError as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
import streamlit as st
from abc import ABC, abstractmethod


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

    def get_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        return {
            "Name": self.name,
            "Age": self.age,
            "Weight (kg)": self.weight,
            "Height (m)": self.height,
            "BMI": round(bmi, 2),
            "Category": category
        }


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        adjustment_factor = 1.1
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


def main():
    st.set_page_config(page_title="BMI Calculator", layout="centered")
    st.title("💪 BMI Calculator App")
    st.markdown("Enter your details below to calculate your **Body Mass Index (BMI)**.")

    with st.form("bmi_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
        height = st.number_input("Height (m)", min_value=0.3, max_value=3.0, step=0.01)
        submitted = st.form_submit_button("Calculate BMI")

    if submitted:
        try:
            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            info = person.get_info()

            st.success(" BMI Calculation Successful!")
            st.subheader("Results:")
            st.write(f"**Name:** {info['Name']}")
            st.write(f"**Age:** {info['Age']}")
            st.write(f"**Weight:** {info['Weight (kg)']} kg")
            st.write(f"**Height:** {info['Height (m)']} m")
            st.write(f"**BMI:** {info['BMI']}")
            st.write(f"**Category:** {info['Category']}")


            if info["Category"] == "Underweight":
                st.warning(" You are underweight. Consider consulting a nutritionist.")
            elif info["Category"] == "Normal weight":
                st.success(" You have a healthy weight!")
            elif info["Category"] == "Overweight":
                st.warning(" You are overweight. Try to maintain a balanced diet.")
            else:
                st.error(" You are obese. Please consult your doctor.")

        except ValueError as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
