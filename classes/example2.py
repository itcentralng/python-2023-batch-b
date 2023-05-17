class Animal:

    def __init__(self, name, cry):
        self.name = name
        self.cry = cry


class Dog(Animal):
    cry = 'Whooph!!!'
    def __init__(self, name, color, purpose):
        super().__init__(name, self.cry)
        self.color = color
        self.purpose = purpose

dog1 = Dog('Winter', 'Brown', 'Security')
animal1 = Animal('Winter', 'Meow')

print(dog1.purpose)