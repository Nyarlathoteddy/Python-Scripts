"""
1) Create a python class and subclasses to make a script that meets all the following criteria. Be sure to include the example data and strings in your code. Return a description for each pet (all 4) and the generic welcome message for each type of pet as well as the pet total (not statically coded)

We need to automate our existing pet processing solution. We want to start by gathering the pet’s name, the owner’s name, and the pet’s age.

We also want to keep track of how many pets have been processed, create a pet total that can be referenced.

We then want to have specific welcome messages for each type of pet including Dog, Cat, and Bird. We welcome our dogs by saying ‘What a cute dog!’, we welcome our cats by saying “Looks like they’re about to cough up a hairball!” and we welcome our birds by saying “We have enough of those already!”.

We also want to be able to describe each pet if need be. We want to return all the information gathered about the pet in a sentence format and what type of pet they are.

Sometimes our pet information is given to us nicely like:

Dog – Pluto, Mickey Mouse, 93

Cat – Tom, Mammy, 84

Bird – Tweety, Grandma, 81

Other times the information is in a format like:

Cat - Duchess;Madame Bonfamille;54
"""

class Animal:
    animal_counter = 0
    def __init__(self, pet_name, owner_name, age):
        self.pet_name = pet_name
        self.owner_name = owner_name
        self.age = age
        Animal.animal_counter += 1
    @classmethod
    def total_animals():
        print(Animal.animal_counter)
    @classmethod
    def from_string(cls, animal_string):
        pet_name, owner_name, age = animal_string.split(';')
        return cls(pet_name,owner_name, age)
    def describe_pet(self):
        print(f"{self.pet_name} is a {type(self).__name__} that is owned by {self.owner_name} and is {self.age} years old.")


class Dog(Animal):
    @staticmethod
    def welcome():
        print('What a cute dog!')
class Cat(Animal):
    @staticmethod
    def welcome():
        print('Looks like they’re about to cough up a hairball!')
class Bird(Animal):
    @staticmethod
    def welcome():
        print('We have enough of those already!')

print(Animal.animal_counter)
print()
pluto = Dog("Pluto", "Mickey Mouse", 93)
print(pluto.animal_counter)
pluto.describe_pet()
pluto.welcome()

tom = Cat("Tom", "Mammy", 84)
print(tom.animal_counter)
tom.describe_pet()
tom.welcome()

tweety = Bird("Tweety", "Grandma", 81)
print(tweety.animal_counter)
tweety.describe_pet()
tweety.welcome()

duchess = Cat.from_string("Duchess;Madame Bonfamille;54")
print(duchess.animal_counter)
duchess.describe_pet()
duchess.welcome()