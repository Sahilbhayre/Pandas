import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)
#Use of apply in grouping

print(reviews.drop(columns=['points']).groupby(reviews['points']).apply(lambda reviews : reviews.title.iloc[0]))   

#we can do this because it show an future warning in code print(reviews.groupby('winery).apply(lambda reviews: reviews.title.iloc[0]))

'''
we use drop(columns=['points]) because remove the future warning
in above print function they print title which is at the given point column 
but it can print only one title which come first it means let take an example:
if point is 89 and title is Sahil
            89              Bhayre
it takes only Sahil at 89
'''

print(reviews.drop(columns=['points']).groupby(reviews['points']).apply(lambda x : x.title.tolist())) #We use this to print all title which occur at points

print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))