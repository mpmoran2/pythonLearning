# The correct way to do code
def function1(a,b):
    print(a + b)

function1(3,29)

# Incorrect syntax that will give a syntax error
# def function1(a,b) < no colon
#     print(a + b)
#
# function1(3,29)

# Logical Error: Harder to debug as the code runs but was an error in the programmers logic
def function2(a,b):
    print(a*b) # we wanted to add but accidentally put a multiply symbol. It will run but it will be wrong for what you want

function2(3,29)

# Exceptions: Will cause a code to terminate
def function3(a,b):
    print(a/b)

function3(20,0)
#this causes a 0 exception error.

