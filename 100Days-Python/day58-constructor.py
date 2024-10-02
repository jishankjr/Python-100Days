class Person:
    def __init__(self, name, occ):
        print("This is default!")
        self.name = name
        self.occupation = occ


    def info(self): 
        print(f"{self.name} is a {self.occupation}")

a = Person("Harry", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# print(a.name)
# a.name = "Krishna"
# a.occupation = "HR"
# a.info()