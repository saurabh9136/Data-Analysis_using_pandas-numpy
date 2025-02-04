import numpy as np


a = np.array([7, 3, 1, 8, 4, 2, 5, 6])

# Basic aggregate functions
'''
print(np. sum(a))
print (np.min(a))
print(np.max(a))
print(np.size(a))
print (np.mean(a))
print(np.cumsum(a))
print(np.cumprod(a))

'''


z = [100,150,199, 200, 250, 130] 
b = [10,50,30,40,30,10]

price = np.array(z) 
quantity = np.array(b)

#print(price, "\n", quantity)

# let calculate the total price

totalSum = np.cumprod([price, quantity], axis=0)

print(totalSum[1].sum())
