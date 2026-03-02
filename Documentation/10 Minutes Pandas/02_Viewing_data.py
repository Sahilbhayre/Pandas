import pandas as pd
import numpy as np
df = pd.read_csv("Housing.csv")

#For return some rows
print("Starting 5 rows are:")
print(df.head())  #return starting 5 rows
print("\nLast 5 rows are:")
print(df.tail())  #return last 5 rows
print("\nStarting 3 rows are:")
print(df.head(3)) #return starting 3 rows
print("\nLast 7 rows are:")
print(df.tail(7))


print("\n",df.columns) #Print columns name
print("\n",df.index)  #Print number of cols

print("\n",df.to_numpy())  #Convert dataset into array

print("\n",df.describe())  #For print some common factor like count, mean, std, max, 25%, 50%, 75% and min

print("\n",df.T) #Transpose the data: Change rows into columns and viceversa
