import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#2. Level Based Selection - In this selection is based on data index value not it's position matters

#Difference between both of them are:
#Assume we want to print the value at first index of the country(0th index) column(Value at 1st index is Portugal)
#Index Based Selection: reviews.iloc[1, 0]
#Level Based Selection: reviews.loc[1, 'country']
#Both return the same value, you can see the difference in index based selection we give index position but in level based we give index value.
#One more difference is iloc[0:10] selecting 0,1,2...,9 while loc[0:10] select 0,1,2,3....,10

print(reviews.iloc[1, 0]) #Index Based Selection
print(reviews.loc[1, 'country'])  #Level Based Selection


print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])  #Selecting more than one column and complete row.

print(reviews.loc[1:6, ['country', 'taster_twitter_handle', 'points']])  #Selecting more than one column as well as select rows from 1 to 6.
print(reviews.loc[1, 'country':'points']) #It is an advantage because we can directly print the coulumn which want.
print(reviews.iloc[0:3, 1:6]) #It is also same but in this came first we know the column position the operate.