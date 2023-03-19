class Dog():
    # Class object attribute (SAME FOR ANY INSTANCE OF A CLASS)
    species = 'mammal'

    # Attributes
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # Methods (function inside of a Class)
    def bark(self, number):
        print(f'{self.name} is barking... WOOF WOOF! and the number is {number}')

my_dog = Dog(breed='dog brand', name='Linda', spots=True)

print(my_dog.breed) # dog brand
print(my_dog.name) # Linda
print(my_dog.spots) # True
print(my_dog.species) # mammal
my_dog.bark(10)
print(type(my_dog)) # <class '__main__.Dog'>


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius ** 2 * Circle.pi     # We can use self.pi too
    
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)

print(my_circle.get_circumference())
print(my_circle.area)

"""Inheritance"""
class Animal():
    def __init__(self):
        print('Animal created')
    
    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cat created')
    
    def meow(self):
        print('Meow meow!')

    # Replace inherited method
    def who_am_i(self):
        print('I am a cat!')

my_cat = Cat()

my_cat.who_am_i()
my_cat.meow()
my_cat.eat()
print(Cat.__dict__)