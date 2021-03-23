# function that calls itself within it

# 3  factorial is 3*2*1
# 5  factorial is 5*4*3*2*1

def factorial(x):
    if(x == 1):
        return 1
    else:
        return x*(factorial(x-1)) # here is where recursion happens. This is were we call on the function within itself

result = factorial(5)
print(result)