import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

'''groupby(): created a group of reviews whuch have same points value to the given wine
followed by points column and points.count to count the points how many times it repeat'''

print(reviews.groupby('points').points.count()) 

print(reviews.groupby('points').price.min())  #price.min() to get the minimum price of the given points in the datafram
print(reviews.groupby('taster_name').taster_name.count())
