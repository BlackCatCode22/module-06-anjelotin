# Angelo Andrade
# 10-3-24
# animal_classes.py

# animal class (template)
class Animal:
    def __init__(self, name, age, weight, color, species):
        # attributes
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.species = species

# Hyena subclass
class Hyena(Animal):
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.species = "hyena"

    def giggles(self):
        print(f"{self.name} the Hyena is giggling.")

# Lion subclass
class Lion(Animal):
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.species = "lion"


    def roar(self):
        print(f"{self.name} the Lion is roaring.")

# Tiger subclass
class Tiger(Animal):
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.species = "tiger"

    def growl(self):
        print(f"{self.name} the Tiger growling.")

# Bear subclass
class Bear(Animal):
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.species = "bear"

    def grunt(self):
        print(f"{self.name}, the Bear is grunting")

# Testing the classes
if __name__ == "__main__":
    # Create instances
    hyena = Hyena("Harry", 3, 60, "brown")
    lion = Lion("Leo", 5, 190, "tan")
    tiger = Tiger("Tara", 4, 220, "orange")
    bear = Bear("Baloo", 7, 300, "brown")

    # Print object information
    print(f"{hyena.name} is a {hyena.color} {hyena.species}, aged {hyena.age} and weighs {hyena.weight}kg.")
    print(f"{lion.name} is a {lion.color} {lion.species}, aged {lion.age} and weighs {lion.weight}kg.")
    print(f"{tiger.name} is a {tiger.color} {tiger.species}, aged {tiger.age} and weighs {tiger.weight}kg.")
    print(f"{bear.name} is a {bear.color} {bear.species}, aged {bear.age} and weighs {bear.weight}kg.")

    # Testing subclass-specific methods
    hyena.giggles()
    lion.roar()
    tiger.growl()
    bear.grunt()
