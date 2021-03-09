# Consider a list in Python which includes prices of all the items in a store.#
# Build a function to discount the price of all the products by 10%.#
# Use map to apply the function to all the elements of the list so that all the product prices are discounted.

def discounts(price):
    price = price - (price*.10)
    return  price

products = [10,20,30,40,50]

discounted = list(map(discounts, products))

print(discounted)
