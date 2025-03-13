# Single Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()


# Quick Quiz: Implement a Cat class by using the animal class. 
# Add some methods specific to cat



class Animall:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")


class Cat(Animall):
    def __init__(self, name, breed):
        Animall.__init__(self, name, species="Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")

c = Cat("Cat", "Catwoman")
c.make_sound()

n = Animall("Cat", "Cat")
n.make_sound()


