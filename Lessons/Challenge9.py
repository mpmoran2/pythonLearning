# Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price to 10%.
# Function number 2 is for additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both the discounts on the products.
#
# Design the above two mentioned functions and apply them both simultaneously on the price.

def student_discount(a):
    a = a - (a * .10)
    return a

def regulars_discount(b):
    b = b - (b * .15)
    return b

zojirushi = 150

print(student_discount(zojirushi))

print(regulars_discount(zojirushi))

print(regulars_discount(student_discount(zojirushi)))