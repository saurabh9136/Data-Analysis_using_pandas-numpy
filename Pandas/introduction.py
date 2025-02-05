'''
Pandas is a Python library used for working with data. It helps you organize, analyze, and 
manipulate data easily, like an Excel spreadsheet but in code. It works well with tables, 
making it easy to sort, filter, and process large datasets.

Application of Pandas

Automatically align the data for you in computations.
Powerful, flexible group by functionality.
Intelligent label-based slicing, fancy indexing, and subsetting of large data sets.
Intuitive merging and joining data sets.
Flexible reshaping and pivoting of data sets.

Data Structure - 
The best way to think about the pandas data structures is as flexible containers for lower 
dimensional data. For example, DataFrame is a container for Series, and Series is a container for 
scalars. We would like to be able to insert and remove objects from these containers in a 
dictionary-like fashion

Series in Pandas - 
Pandas Series is a one-dimensional labeled array capable of holding data of any type 
(integer, string, float, python objects, etc.). The axis D labels are collectively called index. 
Pandas Series is nothing but a column in an excel sheet.

The object supports both integer and label-based indexing and provides a host of methods for 
performing operations involving the index.


Data Frames : 
Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure 
with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data 
is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal 
components, the data, rows, and columns
'''

# creation of DataFrames in pnadas

import pandas as pd

data = {"Name " : ["Saurabh", "Avinash", "Amit"],
        "Age" : [23, 24, 24],
        "Salary" : [20000, 14000, 18000]}

df  = pd.DataFrame(data) # df stands for data frame


# to import csv file in data frame
csv_df = pd.read_csv("C:/Users/SUFI/Downloads/Highest Bid History Lot Wise Report -7155.csv")

# to manipulate excel file install openpyxl
xl_df = pd.read_excel("Pandas/sales.xlsx", engine="openpyxl")

# Print with correct encoding
print(xl_df.to_string())