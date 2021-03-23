# AKA Encapsulation
    # Able to hide sensitive data from external users and only certian amount of code can access it

class Myclass:
    __hiddenvariable = 0 #using this fomat hides the data

    def add(self, increment):
        self.__hiddenvariable+= increment
        print(self.__hiddenvariable)

object1 = Myclass()
object1.add(3)
# print(object1.__hiddenvariable) # because we have it hidden, we will get an error because python protects the variable data outside the class
