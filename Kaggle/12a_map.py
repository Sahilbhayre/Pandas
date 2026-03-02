#Maps are of two type: 1. map()   2. apply()
#map() = The function you pass to map() should only have single value from the Series
#      = returns a new Series where all the values have been transformed by your function.

import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)
review_points_mean = reviews.points.mean()
print(f"Mean is : {review_points_mean}")
print(reviews.loc[:,'points'])
print(reviews.points.map(lambda p: p - review_points_mean))
#print(reviews.points.map(lambda p: p - reviews.points.mean()))