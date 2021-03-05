# Accepts name of a product and returns respective prices
# Use dictionary and must have 5 elements

food = {"Tea":2, "Mochi":2, "Sushi":12, "Ramen":10, "Ramune":2}
newfood = input('Enter drink name')
if(newfood in food):
    print(food.get(newfood))
else:
    print('We do not have that')




