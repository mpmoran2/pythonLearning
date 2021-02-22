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

# Range Function