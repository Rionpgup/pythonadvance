class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.name=name
        self.courses=courses
        self.city=city
        self.state=state

@property
def name(self):
    return self.name

@name.setter
def name(self, value):
        self.name=value

@property
def city(self):
        return self.__city

@city.setter
def city(self, value):
    self.__city = value

@property
def state(self):
         self.__city.__state

@property
def courses(self):
    return self.__courses

@courses.setter
def courses(self, value):
    self.__courses = value

def show_school_info(self):
    retun{
        "School Name":self.name,
        "School City":self.city,
        "School State":self.state,
        "Courses":self.courses

   }

def organize_hackathon(self):

    raise NotImplementedError("This method is not implemented")

class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name, city, state, courses)
        self.student_number = student_number

        @