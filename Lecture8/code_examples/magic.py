class Person():
    def __init__(self, name = "NoInfo", age = 0):
        self.name = name
        self.age = age

    def __lt__(self,other):
        return self.age < other.age

p1 = Person(age = 22)
p2 = Person(age = 25)

print(p1 < p2) # => True