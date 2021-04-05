class Computer:
    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor

    def getspecs(self):
        print('Please enter your computer details')
        self.ram = input('Enter Ram:')
        self.processor = input('Enter Processor:')

    def displayspecs(self):
        print('Here are your specs:')
        print('Ram: ' +self.ram +  '\nProcessor: ' + self.processor)

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

lappy = Laptop('')
lappy.getspecs()
lappy.getsize()
lappy.displayspecs()
lappy.displaysize()