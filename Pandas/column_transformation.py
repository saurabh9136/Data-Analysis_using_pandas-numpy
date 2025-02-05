import pandas as pd

data = pd.read_excel("Pandas/sales.xlsx")

# print(data)
# Add a new column "IsMaharashtra" and set "True" if Customer City is Mumbai, else "False"
data.loc[(data['Customer City'] == 'Mumbai'), "IsMaharashtra"] = "True"
data.loc[(data['Customer City'] != 'Mumbai'), "IsMaharashtra"] = "False"

# lets create a column with concatenation of qty and price Name total Price
data["Total_price"] = data["Quantity"] * data["Price"]


# Now write a code to create a GST price on price for each product
data["GST amount"] = (data["Price"] / 100)*18 #18 % gst 


# write a program to create a months dict and then create another column which consist first 3 words

# created a dict
months_dict = {"Months" : ["Janauary", "February", "March", "April", "May", "June", "July"]}

# converted it to data frame
months_df = pd.DataFrame(months_dict)

def extract(value):
    return value[0:3]

# Adding a new column 'Short_months' by applying the extract function to each value in 'Months'
months_df["Short_months"] = months_df["Months"].map(extract)  # .map() applies the function to each row

print(months_df)