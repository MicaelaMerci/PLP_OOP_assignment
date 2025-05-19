# Base class for Animals
class Animal:
    def move(self):
        pass  # This method will be overridden by subclasses


# Car class (Vehicle)
class Car(Animal):
    def move(self):
        print("Driving 🚗")


# Plane class (Vehicle)
class Plane(Animal):
    def move(self):
        print("Flying ✈️")


# Bird class (Animal)
class Bird(Animal):
    def move(self):
        print("Flying 🦅")


# Fish class (Animal)
class Fish(Animal):
    def move(self):
        print("Swimming 🐠")


# Creating a list of different animals and vehicles
creatures = [Car(), Plane(), Bird(), Fish()]

# Looping through each creature/vehicle and calling their move() method
for creature in creatures:
    creature.move()
