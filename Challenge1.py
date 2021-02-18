# accept input from the user for principle, year, and interest
# save value of p, n, and r
# save value of p, n, and r as integer
# calculate simple interest
# print simple interest


p = input('Enter value for p')
n = input('Enter value for n')
r = input('Enter value for r')

p = int(p)
n = int(n)
r = int(r)

si = (p*n*r)/100

print(si)
