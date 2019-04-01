class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def greet(self):
        print("Hello World!")
    def info(self):
        print("Name: {}\nSurname: {}\nAge: {}".format(self.name, self.surname, self.age))

class Student(Person):
    def __init__(self, name, surname, age, year, gpa):
        super().__init__(name, surname, age)
        self.year = year
        self.gpa = gpa
    def info(self):
        print("Name: {}\nSurname: {}\nAge: {}\nYear of Education: {}\nGPA: {}\n"
            .format(self.name, self.surname, self.age, self.year, self.gpa))