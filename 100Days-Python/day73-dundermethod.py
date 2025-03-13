# Magic/Dunder Methods

# __len__
class Employee:
    name = "Jishank"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

e = Employee()
print(e.name)
print(len(e))


from emp import Employee

e1 = Employee("Harry")
print(str(e1))
print(repr(e1))
e1()        #   -> call method