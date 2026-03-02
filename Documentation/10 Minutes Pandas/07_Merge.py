import pandas as pd
df = pd.read_csv("Housing.csv")

#a. Concat: Concatenating objects together row-wise with concat()
# pieces = [df[:3], df[85:95], df[540:]]  #Break datasets into pieces
# print(pd.concat(pieces))  #Merge the break pieces


#b. Join: merge() enambles SQL style join types along specific columns
#i. Merge on same key: Print twice
left = pd.DataFrame({"area": [1750000, 1750000], "bedrooms": [4, 3]})
right = pd.DataFrame({"area": [1750000, 1750000], "mainroad": ['yes', 'no']})
print(pd.merge(left, right, on='area'))

#ii. On unique keys:  Print once
left = pd.DataFrame({"area": [1750000, 750000], "bedrooms": [4, 3]})
right = pd.DataFrame({"area": [1750000, 750000], "mainroad": ['yes', 'no']})
print(pd.merge(left, right, on='area'))