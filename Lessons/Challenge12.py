# Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.
#
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
#
# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.
#
# Make sure that the sub classes have their own methods to get and display their special specification.
#
# Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class

class Computer:
    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor

    def getspecs(self):
        print('Please enter your computer details')
        self.ram = input('Enter Ram:')
        self.memory = input('Enter Memory:')
        self.processor = input('Enter Processor:')

    def displayspecs(self):
        print('Here are your specs:')
        print('Ram: ' + self.ram+ ' Memory: ' + self.memory + ' Processor: ' + self.processor)

class Desktop(Computer):
    def __init__(self, monitors):
        self.monitors = monitors

    def getmonitors(self):
        print("How many monitors do you have?")
        self.monitors = input("Monitors:")

    def displaymonitors(self):
        print('You have' + self.monitors + 'monitors for your computer')

class Laptop(Computer):
    def __init__(self, size):
        self.size = size

    def getsize(self):
        print("How big is your laptop")
        self.size = input("Inches:")

    def displaysize(self):
        print('You have a ' + self.size + ' inch laptop')

comp = Laptop('')
comp.getspecs()
comp.getsize()
comp.displayspecs()
comp.displaysize()