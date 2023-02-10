class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

# my_animal = Animal('robert')
# print(my_animal.speak())

class Dog(Animal):
    # If we do not define __init__ it would take the base class one
    # But if we have an __init__ we need to refer also to the base class one
    def speak(self):
        return self.name + ' Says woof!'

linda = Dog(name='Linda')

print(linda.speak())