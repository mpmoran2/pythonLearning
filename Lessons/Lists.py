# Intro to lists
# Similar to Arrays
names =["Pilahi", "Juan", "Nathan", "Samantha", "Hannah"]
print(names)
# To find out index
print(names[1]) #like arrays, index starts at 0 so 1=Juan while Pilahi is at 0
# Numerical List
numbers =[2,3,4,9]
print(numbers)
#empty lists
empty =[]


# List Operations
nums =[1,1,1,1]
# Inserting Values
nums[2] = 5 # name of list, the position you want to insert to (can also be used to change) and the new value
print(nums)
# Adding a list to another
newnums = [2,2,2,2]
print(nums+newnums)
# Multiply a list
print(nums*3)
# Check if an item is present in the list
fruits =["Lilikoi", "Mango", "Papaya"]
print("Mango" in fruits) # To check if an item is present to get a true or false
print("Orange" in fruits)


# List Functions
favfruits =["Lychee", "Guava", "Mango", "Peach"]
# To add fruit to the end of the list
favfruits.append("Pineapple")
print(favfruits)
# To give the length of the list
print(len(favfruits))
# To insert an item at a specific position
favfruits.insert(1, "Banana") # Inserts Banana at index 1
print(favfruits)
# find the index value of an item
print(favfruits.index("Peach"))


# List Slicing
numbers = [0, 10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5]) # list[starting index:ending index]
# this gives us 20, 30, 40
# if we want to just get the first half of the list, we can use the following
print(numbers[:4]) # print everything before the 3rd index
# The same goes for the other side of the list
print(numbers[4:])
# we can also specify intervals
print(numbers[1:6:2]) # list[start:stop:interval]


# List comprehension: a way to create a list by defining a certain set of rules in a list
list = [x**2 for x in range(5)]
# We give a rule to find the square of numbers 0-5 in a for loop
print(list)

# can include if statements in the rule
lists = [x**2 for x in range(5) if x**2 % 2 == 0] # We want to find the square of numbers 0-5 and add them to the list IF they are even
print(lists)