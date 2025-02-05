import numpy as np
import SciPy as stats

baked_food = [200, 150, 150, 130, 200, 220, 170, 188]
a = np.array(baked_food)
print(np.mean(a))  # Calculates the mean (average): sum of all values / number of values

print(np.median(a))  # Finds the median (middle value) after sorting the array

print(stats.mode(a))  # Finds the mode (most frequently occurring value) using SciPy

print(np.std(a))  # Computes the standard deviation (measure of data dispersion)

print(np.var(a))  # Computes the variance (spread of data from the mean)



# -1 represent inversely proportional relationship
# 1 represents proportional relationship
# 0 means no relationship
tobacco_consumption = [30,50,10,30,50,40]
deaths = [100, 120, 70, 100, 120, 112]
print(np.corrcoef ([tobacco_consumption, deaths]))


prices =[100, 200, 300, 150, 80]
sales = [10, 5, 2, 7, 18]

print(np.corrcoef([prices, sales]))