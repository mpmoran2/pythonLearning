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

    # Say we want to change colors of doggos
    def color_change(self, color): # every class method, we want to pass in self as part of the parameter
        # self is used to access the instance attribute we want to manipulate
        print("Oh wow she changed color!")
        # self.color = "White"
        self.color = color

    def name_change(self):
        print("You've renamed her!")
        self.name = "BabyDog"

# dogo = Dog()
# print(dogo) # This gives us an error because we didn't give arguments of Name or Color
dogo = Dog("Missy","Black")
print(dogo.name)
print(dogo.color)

dogogo = Dog("Tahoe","Mixed")
print(dogogo.name)
print(dogogo.color)

# Implementing Methods in OOP
    # see def color_change
    # to execute the change

dogogo.color_change("Blue")
print(dogogo.name)
print(dogogo.color)

dogo.name_change()
print(dogo.name)
print(dogo.color)