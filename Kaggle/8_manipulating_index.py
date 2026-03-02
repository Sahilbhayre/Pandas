import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#If we want to change the index with any present index we use df.set_index("index value")
print(reviews.set_index('title'))  #It make a title as index.
#print(reviews.set_index('tittle)) tittle is not the any index value in dataframe so it can show an error