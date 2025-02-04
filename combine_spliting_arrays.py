import numpy as np

# combining and splitting arrays

arr_1 = np.array([23, 34, 32, 45, 34])

arr_2 = np.array([32, 45, 56, 23, 45])

#print(np.concatenate([arr_1, arr_2]))


# concatenating 2D arrays with axis
arr_2D = np.array([[12, 34, 45, 56], [21, 34, 65,43]])
arr_2D_1 = np.array([[3,4, 6, 7], [4, 2, 6, 5]])

#print(np.concatenate([arr_2D, arr_2D_1], axis=1))

''' reskult ||
[[12 34 45 56  3  4  6  7]
 [21 34 65 43  4  2  6  5]]

'''

# There is also a more ways to conacatenate - >  horizonatl and vertical

#print(np.hstack([arr_2D, arr_2D_1])) # horizontal concatenation

'''
[[12 34 45 56  3  4  6  7]
 [21 34 65 43  4  2  6  5]]
'''

#print(np.vstack([arr_2D, arr_2D_1])) # vertical concatenation

'''
[[12 34 45 56  3  4  6  7]
 [21 34 65 43  4  2  6  5]]
'''


# now split array

print(np.array_split(arr_1, 3)) # it will split the arrays in 3 parts 