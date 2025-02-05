import pandas as pd

dict = {"Fruits" : ["apples", "banana", "papaya", "mangos"],
        "Price" : [54, 90, 100, 150],
        "quantity" : [15, 10, 5, 5]}

df = pd.DataFrame(dict)

df2  = df.copy()

df2.loc[0,"Price"]=120
df2.loc[1, "Price"] = 175
df2.loc[3, "Price"] = 30 

df2.loc[0,"quantity"]=10
df2.loc[1, "quantity"] = 7
df2.loc[3, "quantity"] = 2   

print(df.compare(df2))