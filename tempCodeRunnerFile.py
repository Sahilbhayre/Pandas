print(reviews.groupby('points').apply(lambda x: x['title'].tolist()))
