class Animal:
    def __init__(self):
        print('Animal created')
    def whoAnI(self):
        print('Animal')
    def eat(self):
        print('Eating')
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    def whoAmI(self):
        print('Dog')
    def bark(self):
        print('Whoof!')
d = Dog()
d.whoAmI()
d.eat()
d.bark()