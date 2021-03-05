# Take code and divide them into functions to pass in data from function to function
#Example
def add_ten(x):
    return x+10

def run_twice(func, arg):
    return func(func(arg))

print(run_twice(add_ten, 10)) # This will give us 30 as 10+10=20+10=30