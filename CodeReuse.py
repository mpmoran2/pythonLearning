# Coding Reuse
# Large code, to be effecient, call on code from one place vs having it repeat over and over
# Example: We have code that we want to use multiple times in our code
print("example1")
print("example2")
print("example3")

# We can instead make this a function
def function1():
    print("example1")
    print("example2")
    print("example3")

# To execute the lines of code, we need to call on it
function1() # this is a Function Call

# This is code reuse. Allows code to be elegent, effecient, easy to read, and easy to edit by using functions as place holders for code you want to use multiple times