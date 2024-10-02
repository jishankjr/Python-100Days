class Person:
    name = "Jishank"
    occupation = "Student"
    netWorth = 10
    def info(self):
        print(f"{self.name} is {self.occupation}")

a = Person()
b = Person()
c = Person()
a.name = "Shuvam"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"

c.name = "Ram"
c.occupation = "Developer"

a.info()
b.info()
c.info()