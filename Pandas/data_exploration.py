import pandas as pd

data = pd.read_excel("Pandas/sales.xlsx")
top_data = data.head(3) # acess data from top
bottom_date = data.tail(3) # acess data from bottom
print(data.info()) # get all information about
print(data.describe())
print(data.isnull().sum()) # to chceck number of empty rows
print(bottom_date)



# Handling duplicate value in Pandas
print(data['Order ID'].duplicated().sum()) # data['Order ID'] check for particular column


# lets drop/delete the duplicate data in a column

print(data.drop_duplicates("Order ID"))


#### working with missing Datas #####

print(data)
# to delete the rows which has Nan value null value use below syntax
# syntax : data.dropna()

# so now if youi want to know a replace a null value with anpther value use below syntax
import numpy as np
print(data.replace(np.nan, "Hi"))

# but above code will replace all nan value in any column within data which is not correct 

# so lets replace nan value in Total Price column
data["Total Price"] = data["Total Price"].replace(np.nan, 60000)
print(data)


# suppose you want to fill above row data to beloe na then use 1 else for below data use 2

print(data.fillna(method = "bfill")) # 2 backword fill
print(data.fillna(method  = "ffill")) # 1 forword fill]

