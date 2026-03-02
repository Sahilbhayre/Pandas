import pandas as pd
df = pd.read_csv("Housing.csv")

# Sorting by an index
print(df.sort_index(axis=1)) # Sort index by alphabet order in increasing order

print(df.sort_index(axis=1, ascending=False)) #Sort in decreasingt order

#Sorting by an value
print(df.sort_values(by="price")) #Sorting based on values sort the dataset in increasing order based on price column
print(df.sort_values(by='price', ascending=False)) #In decreasing order
