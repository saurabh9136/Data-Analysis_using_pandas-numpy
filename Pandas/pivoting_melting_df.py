
import pandas as pd

'''Pivoting reshapes data by converting unique values from one column into multiple columns. It is 
used to reorganize data for better readability.
'''
dict = {"keys":["k1", "k2", "k1","k2"],
    "Names":["John", "Ben", "David", "Peter"],
    "Houses" : ["red", "blue", "green","red"],
    "Grades":["3rd","8th","9th","8th"]}

df = pd.DataFrame (dict)
# print (df.pivot (index="keys", columns="Names", values = ["Houses", "Grades"]))

''' output
      Houses                   Grades                 
Names    Ben  David John Peter    Ben David John Peter
keys                                                  
k1       NaN  green  red   NaN    NaN   9th  3rd   NaN
k2      blue    NaN  NaN   red    8th   NaN  NaN   8th
'''


################ Melting ###################3
'''
Melting does the opposite of pivoting—it converts multiple columns into rows, making data 
long format.
'''

dict_2 = {
    "Names":["John", "Ben", "David", "Peter"],
    "Houses" : ["red", "blue", "green","red"],
    "Grades":["3rd","8th","9th","8th"]}

data_frame = pd.DataFrame(dict_2)

print(pd.melt(df, id_vars=["Names"], value_vars=["Houses"]))
