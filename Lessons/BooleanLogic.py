# How to check for multiple conditions some where
# Simple Login System to understand this
username = "admin"
password = "admin123"

# To Verify if user and pass is correct
if username == "admin" and password == "admin123": #only if BOTH conditions are true will it execute
    print("Valid User")
else: # if either conditions are false, this code will execute instead
    print("Invalid User")


# To Verify if user OR pass is correct
if username == "admin" or password == "admin125": #only if ONE of the conditions are true will it execute
    print("Something is missing!")
else: # if both conditions are false, this code will execute instead
    print("Invalid User")



# boolean opperators:
    # and combines 2 conditions together
    # or checks for 1 condition between multiple conditions