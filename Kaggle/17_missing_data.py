import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#To print null value in df using   pd.isnull()
a = pd.isnull(reviews.country) 
print(reviews[a])

#Replacing missing with the help of fillna()
#Ex. NaN value replace with Unknown
b = reviews.region_2.fillna("Unknown")
print(b)

#If datasets is publics and we want to replace reviewer Kerin O'Keefe twitter handle from @kerinokeefe to @kerino thenn we use replace() method
c = reviews.taster_twitter_handle.replace("@kerinokeefe","@kerino")
print(c)
