import pandas as pd

df = pd.read_csv("Housing.csv")

#Grouping by a column label, selecting column labels, and then applying the DataFrameGroupBy.sum() function to the resulting groups:
print(df.groupby("area")[['bedrooms', 'bathrooms']].sum())  #Group the rows which has same area and sum of bedrooms and bathrooms in which area is same

#Grouping by multiple columns label forms MultiIndex
print(df.groupby(['area', 'price']).sum())  #group the area and price column