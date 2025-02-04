'''
. g=a-b
• np.subtract (a, b)
45
. _b + an
. p.add (b, a)
. • a/b
. np.divide(a,b)
. a*b
. np.multiply(a,b)
. np.exp(b)
. np.sqrt(b)
. np.pow(b)

'''

# above are the some mathematical operations.
import numpy as np
# init array

arr_1 = np.array([23, 34, 32, 45, 34])

arr_2 = np.array([32, 45, 56, 23, 45])

#addition
# print(arr_1+arr_2)
# print(np.add(arr_1, arr_2))


# #substraction
# print(arr_2-arr_1)
# print(np.subtract(arr_1, arr_2))

# # multiplication
# print(np.multiply(arr_1, arr_2))
# # divison
# print(np.divide(arr_1, arr_2))



arr_2D = np.array([[12, 34, 45, 56], [21, 34, 65,43]])

array = np.array([5])

#power
print(np.power(arr_2D, array))


#square root

print(np.sqrt(arr_1))