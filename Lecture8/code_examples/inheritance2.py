class Professor(Person):
    def __init__(self, name, surname, age, publication):
        super().__init__(name, surname, age)
        self.publication = publication
    def greet(self):
        print("Hello World, I'm a professor!")
    def info(self):
        print("Name: {}\nSurname: {}\nAge: {}\nNumber of Publication: {}\n"
            .format(self.name, self.surname, self.age, self.publication))
