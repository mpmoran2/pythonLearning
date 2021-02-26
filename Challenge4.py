# BMI Calculator
# Formula is BMI = (weight in kg)/(height in Meters)^2

#Write python code which can accept the weight and height of a person and calculate his BMI.
    #note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

def give_bmi(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height,2))
    return new_bmi

weight = float(input("Please enter your weight in kilograms"))
height = float(input("Please enter your height in meters"))
bmi = give_bmi(weight, height)

print(bmi)