# adding and removing arrays

import numpy as np

'''
np.append (h, g) - Append items to an array
np.insert (a, 1, 5) - Inserts items in particular index of an array
np.delete (a, [1]) - Delete items from an array
'''

a = np.array([1, 2, 3, 4, 5, 6, 7])

a = np.append(a, [8, 9]) # syntax to append value

# syntax to insert value at particular index - 

a = np.insert(a, 2, 5) # a- array, 2- index, 5-value



b = np.array([[20,40], [60,80]])

print(np.insert(b,1,[50,60], axis = 1)) #array, index, value
