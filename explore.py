import pandas as pd

df= pd.read_csv("IPL.csv")
print(df.shape)
print(df.columns.tolist())
print(df.head(10))