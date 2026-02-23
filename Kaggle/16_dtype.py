import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

print(reviews.price.dtype) #Print the data type of price column

print(reviews.dtypes) #Print all data types of each columnm.

print(reviews.points.astype('float64'))  #Convert int data type into float data type.