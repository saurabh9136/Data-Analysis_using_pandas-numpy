import pandas as pd

# write a code to fetch csv data and and to find average of each equipment without using loops

df = pd.read_csv("Pandas/sample_event_detection (3).csv")

gp = df.groupby("equipment_name").agg({"temperature" : "mean"})
print(gp)

'''
                temperature
equipment_name             
Alpha-1           19.559656
Alpha-2           27.565269
Alpha-3           34.424395
'''