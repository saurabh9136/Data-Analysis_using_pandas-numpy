import numpy as np


a = np.array([7, 3, 1, 8, 4, 2, 5, 6])

sorted_array = np.sort(a) # sort

index = np.where(a == 1) # more like we can find odd even as well like (a % 2 ==0)

sorted_search_index = np.searchsorted(sorted_array, 7) # it will search efficiently such as O(log n)



print(sorted_search_index)



data = np.array([10, 15, 20, 25, 30, 35, 40])

# Define a condition for filtering (e.g., select elements greater than 25)
condition = data > 25

# Use the condition to filter the array
filtered_data = data[condition]

# Print the original and filtered arrays
print("Original Array:", data)
print("Filtered Array (elements > 25):", filtered_data)
