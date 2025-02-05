import pandas as pd


# data1 = {"Emp Id":["E01", "E02","E03", "E04", "E05","E06"],
#         "Names":["Ram", "Shyam", "Rahul", "Vishal", "Ravi", "Kunal"],
#         "Age" : [34,56,23,44,32, 24]}

# data2 = {"Emp Id":["E01", "E02", "E03", "E04", "E05","E06"],
#         "Salary": [45000, 56000, 34000, 30000, 50000, 20000]}


# lets take a datafram whicn has some null values

data1 = {"Emp Id":["E01", "E02","E03", "E04", "E05","E06"],
        "Names":["Ram", "Shyam", "Rahul", "Vishal", "Ravi", "Kunal"],
        "Age" : [34,56,23,44,32, 24]}

data2 = {"Emp Id":["E01", "E07", "E03", "E04", "E08","E06"],
        "Salary": [45000, 56000, 34000, 30000, 50000, 20000]}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# merge on the basis on employee id
print(pd.merge(left = df1,right =  df2, on="Emp Id", how="right"))

# for concatenation it is important that data is in same format 

data_1 = {"Emp Id":["E01", "E02","E03", "E04", "E05","E06"],
        "Names":["Ram", "Shyam", "Rahul", "Vishal", "Ravi", "Kunal"],
        "Age" : [34,56,23,44,32, 24]}

data_2 = {"Emp Id":["E07", "E08","E09", "E10", "E11","E12"],
        "Names":["John", "Rayn", "seema", "geeta", "avya", "Amit"],
        "Age" : [20,29,25,32,33, 41]}

df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)


print(pd.concat([df_1, df_2]))