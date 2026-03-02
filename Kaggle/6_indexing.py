import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#Indexing are of two type:
#1. Index Based Selection
#2. Level Based Selection

#1. INDEX Based Selection - Selecting data based on its numerical position in the data.
#To obtain complete row
print(reviews.iloc[0])  #To obtain complete one row we use iloc[column number]

print(reviews.iloc[0:9])  #To obtain more than one row in a sequence then we use iloc[start:end]

print(reviews.iloc[0:9:2])  #Tol obtain specific row with same diffrence then we use iloc[start:end:step]

#To obtain a specific column of the dataframe

#1. To obtain a single column we use iloc[index, column]
print(reviews.iloc[0:3, 1]) #reviews.iloc[[0, 1, 2], 1] it is also possible

#2. To obtain a more than one column we use iloc[index, [column1, 2,....]]
print(reviews.iloc[1:3, [1, 3]])
