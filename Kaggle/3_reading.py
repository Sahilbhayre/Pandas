import pandas as pd

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape)   # Returns shape of the csv file
print(wine_reviews.head())  # Print 5 rows of the csv file and it also return shape of the file 

#In this print you can see a word which is unnamed but when you use index_col = 0 the unnamed is remove

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)
print(wine_reviews.head())