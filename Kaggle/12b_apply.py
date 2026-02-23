import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#apply() = is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

def remean_points(row):
    review_points_mean = reviews.points.mean()
    row.points = row.points - review_points_mean
    return row

print(reviews.apply(remean_points, axis = 'columns'))
print(reviews.head(1))

#If we had called reviews.apply() with axis='index', then instead of passing a function to transform each row, we would need to give a function to transform each column.

#Note that map() and apply() return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on. If we look at the first row of reviews, we can see that it still has its original points value.