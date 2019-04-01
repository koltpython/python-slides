person = Person(age = 30)
print(person.name) # => NoInfo
print(person.age) # => 30
print(person.languages) # => []

person.addLanguage("English")
print(person.languages) # => ['English']

person.setName("John")
person.increaseAge()
person.increaseAge()

person.info() # => Name: John
              #    Age: 32
              #    Languages: ['English']