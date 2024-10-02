# public access -> Normal accessing class are by default public access
print("\nPublic access modifier:")
class Employee:
    def __init__(self):
        self.name = "Jishank"

a = Employee()
print(a.name)
print("\nPrivate access modifier:")

# private access -> Cannot be accessed by outside unless name mangling

class Employee:
    def __init__(self):
        self.__name = "Jishank"

a = Employee()
# print(a.name)               -> Cannot be accessed directly
# In order to access
print(a._Employee__name)    # Mangling -> Can be accessed indirectly
# print(a.__dir__()) 

print("\nProtected access modifier:")
# protected access

class Student:
    def __init__(self):
        self._name = "Jishank"

    def _funName(self):                 # protected method
        return "CodeWithHarry"
    
class Subject(Student):                 # inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# print(dir(obj))

# calling by object of Subject class

print(obj1._name)
print(obj1._funName())

