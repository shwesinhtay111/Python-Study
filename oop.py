# In python everything is an object
print(type(1))
print(type([]))
print(type(()))
print(type({}))

# Create a new object type called Sample
# give classes a name that starts with a capital letter
class Sample:
    pass
# Instance of Sample
x = Sample()
print(type(x))

class Dog:
    # Class Object Attribute
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
sam = Dog(breed='Lab', name='Aung Net')
frank = Dog(breed='Huskie',name="Kaung")
print(sam.breed,sam.name,sam.species)
print(frank.breed,frank.name,sam.species)

class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

c.setRadius(2)
print('Radius is:', c.radius)
print('Area is:',c.area)
print('Circumference is:', c.getCircumference())