# list all the odd numbers from 1 to 100 using lists in python
alist = list(range(1, 100))

for x in alist:
    if x % 2 != 0:
        print(x)