# Dictionaries are data structures used to map arbitrary keys to values.
# They help you capture data and store it in the code
# Taking that data, manipulating it, and giving a certian output
# Ex: You want to find the meaning of cloud. You would look it up in the dictionary and get the meaning of the word
# In pairs. Key and value

# EX Code: Saving the ages of people in code
people = {"Pilahi":29, "Morgan":28} # Dictionaries are in curly braces and come in key:value pairs
print(people["Morgan"]) # To look up the value of a key you need to state the dictionary name[key]
# We are telling python to map the key we give to the value that is associated to it

# fun example
cute = {"Sheep":"Yes", "Otter":"Yes", "Mole Rat":"Hell No"}
print(cute["Mole Rat"])

# Dictionary Functions
numbers = {1:"One", 2:"two", 3:"three"}
# See if 1 in in our dictionary
print(1 in numbers)
# Should give us true (SIMILAR TO LISTS)
print(5 in numbers)
# This should give us false

# GET Function
print(numbers.get(2)) # This gets us the value of 2 in our dictionary
print(numbers.get(5, "Not in Numbers")) # The second parameter here is what we want to be printed if 5 is not found vs the 'None' we would usually get
