import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
print(reviews)   #To get all the cols and rows

print(reviews.country)   #In that only countries in the dataset will be shown
print(reviews['country'])  #Now consider review is a dictionary then output will be same as dataframe in pandas

#Conclusion: Just like python dictionary how we can access key in dictionary is also same in the dataframe in the pandas

#So we give a sample output what we want from both of the line of code.

#But the best is in block [] like a dictionary

#Because if we have a space in column name than [] will be run but other will not run it show an error.