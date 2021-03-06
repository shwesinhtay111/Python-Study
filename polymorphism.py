# polymorphism refers to the way in which different object classes can share the same method name
class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says Woof!'
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name+' says Meow!'
niko = Dog('Niko')
felix = Cat('Felix')
print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(pet.speak())
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)
