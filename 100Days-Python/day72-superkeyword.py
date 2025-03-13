# super keyword
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Jishank.")
        super().parent_method()

    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
        

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "42345", "Python")
print(rohan.name)
print(harry.name)
print(harry.id)
print(harry.lang)