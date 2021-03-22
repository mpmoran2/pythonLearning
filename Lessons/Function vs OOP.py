# Function Based
# def get_stats():
#     name = input("Enter Name")
#     age = input("Enter Age")
#     print(name)
#     print(age)
#
# get_stats()

# OOP
# ALT VERSION OOP
# # class Person:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #
# #     def get_info(self,name,age):
# #         self.name = name
# #         self.age = age
# #
# #     def give_info(self):
# #         print(self.name)
# #         print(self.age)
# #
# # person1 = Person("", "")
# # name = input("Enter Name")
# # age = input("Enter Age")
# # person1.get_info(name,age)
# # person1.give_info()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_info(self):
        self.name = input("Please Enter Name:")
        self.age = input("Please Enter Age:")

    def give_info(self):
        print(self.name)
        print(self.age)
#
# person1 = Person("", "")
# person1.get_info()
# person1.give_info()

# Inheritance: One class can inherit the methods and properties of another class
class Student(Person): # We add the class we want to inherit from

    def grade(self):
        print("They are doing well.")

a = Student("","")
a.get_info()
a.grade()

