import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

reviews['s'] = 'everyone'
print(reviews['s']) #You can assign either a constant value.

reviews['country'] = 'India'
print(reviews['country'])

#Reverse the index
reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])