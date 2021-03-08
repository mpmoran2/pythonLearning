# Similar to functions but dont have to name them
# AKA anon functions as they have no name

# Normal Function
def square(x):
    return x**2

print(square(2))

# Lambdas
result = (lambda x: x ** 2)(30)
print(result)

# Do not even need variable
print((lambda x: x ** 2)(79))



# Filters: functions used with lambdas to filter out a list

numbs = [1,3,4,5,7,2,9,11,13]

result = list(filter(lambda x: x%2 == 0, numbs))
# takes in the lambda and the list as arguments as you want to perform the lambda function on the list

print(result)

