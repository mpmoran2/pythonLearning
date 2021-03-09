# Class
    # how we make Objects
#Class Methods
    # a way to manipulate the attribute of your object
class Sheep: # a template or "mould" of our objects
    # add class attributes
    herd = 50

sheepy = Sheep() # this created the object
sheepies = Sheep()

print(sheepy.herd)
print(sheepies.herd)


# Instance Attributes
class Dog:
    good_baby = 2
    # constructor = a method to define the instance attribute
    def __init__(self,name,color):
        self.name = name
        self.color = color

# dogo = Dog()
# print(dogo) # This gives us an error because we didn't give arguments of Name or Color
dogo = Dog("Missy","Black")
print(dogo.name)
print(dogo.color)

dogogo = Dog("Tahoe","Mixed")
print(dogogo.name)
print(dogogo.color)