import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

#To accessing a single value

a = reviews.country[0]  #Italy
b = reviews['country'][0]  #Italy
print(a)
print(b)

#To accessing a specific part of a single value we can use like this:
#To obtain a single word in a dataframe or if we want some specific part of the word then we use this 

#print(reviews.country[0][2])  #a(2nd second index of Italy)
print(reviews.country[0][1:2])  #ta(1st and 2nd index of Italy) 
print(reviews.country[9][0:6])  #France
print(reviews.country[9][0:5:2]) #Fac(0 then 2 then 5 because index increase with 2)
print(reviews['country'][1][1:4]) #ort(Portugal st index 1)