class Person():
    def __init__(self, name = "NoInfo", age = 18, languages = []):
        self.name = name
        self.age = age
        self.languages = languages

    def addLanguage(self, new_language):
        self.languages.append(new_language)
    
    def setName(self, name):
        self.name = name
    
    def increaseAge(self):
        self.age += 1

    def info(self):
        print("Name: {}\nAge: {}\nLanguages: {}".format(self.name, self.age, self.languages))