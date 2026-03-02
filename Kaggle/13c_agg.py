import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

print(reviews.groupby(['country']).price.agg([len, min, max]))  #It create a summary table of unique country in whuch len , min, max are column