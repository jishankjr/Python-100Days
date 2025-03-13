# dir
print("\n~~~~~~~~~~~~~~~~~~~~~Dir~~~~~~~~~~~~~~~~~~~~~~~~~~~")
x = [1, 2, 3]
print(dir(x))
print(x.__add__)

x = (1, 2, 3)
# print(dir(x))
# print(x.__add__)

# __dict__
print("\n~~~~~~~~~~~~~~~~~~__dict__~~~~~~~~~~~~~~~~~~~~~~~~~\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

# help method
print("\n~~~~~~~~~~~~~~~~~~help method~~~~~~~~~~~~~~~~~~~~~~")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("John", 30)
print(help(Person))