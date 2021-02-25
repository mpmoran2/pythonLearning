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

# WHILE Loops Similar to For Loops
counter = 0

while(counter<10): # condition given to do the loop
    print(counter)
    counter +=1
    # this prints the counter value then goes up by 1 increment until counter hits 10 where it stops