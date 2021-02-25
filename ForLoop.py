# Loop in python
# What is the sytax of a For loop?
for x in range(1,11):
    print(x) # for the first iteration of the loop, value is stored in x per loop execution

# Example
for x in range(1,6):
    print("Pilahi")

# For loop can also be used to print out elements of a list
fruits = ["Mango", "Lychee", "Rabutan", "Peach", "Pineapple", "Cherry", "Tangerine"]

for x in fruits:
    print(x) # for every iteration, one fruit will be printed until the list is printed

for x in range(0,21,2):
    print(x) # for evey iteration it will print the evens (starting from 0, intervals of 2)
