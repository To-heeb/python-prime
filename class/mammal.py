# Animal: Parent, Based
# Mammal: Child, Sub


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 10

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    """This is ust an experiment on multi-level inheritance.

    Args:
        Bird (_type_): _description_
    """

    def lay(self):
        print("lay")


mammal = Mammal()
animal = Animal()
mammal.eat()
print(mammal.age)
print(mammal.weight)
print(isinstance(mammal, object))
print(issubclass(Mammal, Animal))
