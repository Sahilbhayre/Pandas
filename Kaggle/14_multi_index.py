import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)
mi = reviews.groupby(['country', 'province']).description.agg([len])
print(mi)

print(reviews.groupby(['country', 'province']).description.agg([len, min]))
'''
s1: Group by country and province
s2: Focus on the 'description' column
s3: Apply two functions using .agg([len, min])
len() → number of reviews in that region
min() → smallest description text alphabetically (based on string order)
max() → largest description text alphabetically (based on string order)
'''

print(reviews.groupby(['country', 'province']).description.agg([len, min, max]))

print(type(mi.index))

#Converting multi index into regular index we use reset_index()
print(mi.reset_index())