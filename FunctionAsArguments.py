# Passing Functions as Arguments

def add(a, b):
    return a + b

def square(c):
    return c*c

result = square(add(2,5)) # calling on the square function, we pass in the add function. From there the resuld of add will be the argument for square
print(result) # by assigning the variable result to square allows us to print the outcome


# basically 2 + 5 = 7 * 7