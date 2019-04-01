class Person():
    def __init__(self, name = "NoInfo", age = 18, education = "NoInfo"):
        self.name = name
        self.age = age
        self.education = education

person = Person(age = 30)
print(person.name) # => NoInfo
print(person.age) # => 30
print(person.education) # => NoInfo