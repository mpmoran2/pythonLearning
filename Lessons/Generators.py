# a data structure similar to list
# do not use index structure
# can be created with the yield statement
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

# can be used to create certain types of lists
def evennumbs(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(evennumbs(20)))