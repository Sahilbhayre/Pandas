import pandas as pd
import numpy as np
df = pd.read_csv("Housing.csv")

#a. Stats
print(df.select_dtypes(include='number').mean())  #It only takes numeric column and calculate their mean.
print(df['area'].mean())  #Calculate the mean of area column
print(df['price'].mean())  #and price column
print(df[['price', 'area', 'bedrooms']].mean())  #Calculate the mean of multiple column

print(df.select_dtypes(include='number').mean(axis=1))  #Calculate the mean of each row


#b. User defined functions
print(df.select_dtypes(include='number').agg(lambda x: np.mean(x) * 2))