
try: # Try Statement/Try Block
    a = 20
    b = 10
    print(a/b)
except ZeroDivisionError: # Needs an Except Block. This will not make our code crash because we have handled the exception error. This only executes if there is a Divide by Zero Error
    print('You cannot divide by zero')
finally: # Finally Block. Will happen no matter what
    print('This always shall pass')