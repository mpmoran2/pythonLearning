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