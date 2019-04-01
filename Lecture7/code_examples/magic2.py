class Person():
    def __init__(self, name = "NoInfo", age = 0):
        self.name = name
        self.age = age

    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

p1 = Person("Jane", 22)
p2 = Person("Jane", 22)

print(p1 == p2) # => True