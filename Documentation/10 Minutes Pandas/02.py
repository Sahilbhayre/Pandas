import pandas as pd
import numpy as np
df = pd.read_csv("Housing.csv")

print(f"Top 5 rows are: \n{df.head()}")  #Use to print rows, if we do not paas value inside bracket then it will print 5 rows
print(f'\nLast 5 rows are: \n{df.tail()}')

# print(df.to_numpy())  Use to convert dataset into array
print(df.dtypes)  #check data types

print(df.describe())  #use to find count, mean, std, min, 25%, 50%, 75% and max
# print(df.T) use to transpose the data

#Sorting:
#1. Index based sorting
print(df.sort_index(axis=1))  #Sort in ascending orer
print(df.sort_index(axis=1, ascending=False)) #Sort in descending order

#2. Value based sorting
print(df.sort_values(by='area')) #sort values in area column in increasing order


#Selection
#1. GETITEM []
print(df['area']) #or df.area,  both are same but first is more appropriate
print(df['area'].sort_values())  #Selection with sorting
print(df[['area', 'price']])  #Multiple selection
print(df[:2])  #Selection using slicinig, select two rows

#2. Selection by position: iloc and iat
print(df.iloc[1]) #select rows by index
print(df.iloc[0:3, 1:2])  #select rows and columns both first will be for select rows and second will be for column
print(df.iloc[[1, 5, 2], [3, 7]]) #Select selective rows using direct index
print(df.iloc[1, 1])  #To getting a specific value
print(df.iat[1, 5])  #iat is only for singular valuee