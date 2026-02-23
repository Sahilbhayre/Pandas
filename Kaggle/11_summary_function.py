import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#1. df.indexvalue.describe() : It give summary of the given indexvalue.
print(reviews.points.describe())
print(reviews.country.describe())

#2. df.indexvalue.mean() : It give mean of a given indexvalue (only index which have a numeric value otherwise it give an error)
print(reviews.points.mean())

#3. df.indexvalue.unique() : It give an only unique value which is in given indexvalue
print(reviews.country.unique())

#4. df.indexvalue.value_counts() : To see a list of unique values and how often they occur in the dataset, we can use the value_counts() 
print(reviews.country.value_counts())
print(reviews.taster_name.value_counts())

print(reviews.points.median()) #To find median