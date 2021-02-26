# Module is a set of code written by others (or you) that you can use in your own code
# How do we use these?
# Import the module we want to use. We will use Random
import random

for x in range(5):
    result = random.randint(1,6) # to use a function from the module we call on the module.function (functions in the module will show up in a list to choose from)
    # we use randint(a,b) that gives us a random integer value
    print(result)
