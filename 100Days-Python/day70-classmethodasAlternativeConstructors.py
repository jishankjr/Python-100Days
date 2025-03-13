#  class methods as Alternative Constructors

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
    def showDetails(self):
        print(f"\nThe name is {self.name} and salary is {self.salary}\n")

# data in form of simple
e1 = Employee("Harry", 35000)
print(e1.name)
print(e1.salary)

# data in string form below
string = "Jishank-25000"
e2 = Employee.fromStr(string)
e2.showDetails()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
    def details(self):
        print(f"Name = {self.name} and Age = {self.age}")
    
person = Person.from_string("John Doe, 30")
person.details()