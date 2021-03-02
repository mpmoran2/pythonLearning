# Write a function which would divide two numbers
# Design the function in a manner that handles the divide by zero exception
def challenge5(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Unable to divide by 0, please adjust your formula')

x = float(input('Please enter a number'))
y = float(input('Please give a number to divide by'))
result = challenge5(x,y)
print(result)