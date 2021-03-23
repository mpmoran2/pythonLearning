# Data Structure
    # a type of collection, similar to lists
    # diff is in way they are declared and you can have only unique elements in a set(no doubles)

numbers = {1, 2, 3, 4, 5, 6}
print(numbers)
#to see if something is in a particular set
print(5 in numbers) # True if it is, False if it is not

#add a new element
numbers.add(9)
print(numbers)

#remove element
numbers.remove(4)
print(numbers)

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

# Union Operation
    # gives us a combined set with no duplicates
print(seta | setb)

# Intersection Operation
    # gives us a set of common elements between sets
print(seta & setb)

# Difference Operation
    # takes elements that are uniqe to the set
print(seta - setb)
print(setb - seta)