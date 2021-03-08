# allows to operate on a list/ perform an operation on a singular list

def add2(x):
    return x+2

newlist = [10, 20, 30, 40, 50]

result = list(map(add2, newlist))
# use list() function
# map() function uses 2 arguments. add2() function and newlist as the parameters
    # this states we want to perform the add2() function on the list newlist
# to store the result, we save this to a variable

print(result)

# we can do this with lambdas as well

alist = [2,4,6,8,10]

results = list(map(lambda x: x*2, alist))

print(results)