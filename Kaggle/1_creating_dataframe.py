import pandas as pd


# Yes and no are columns and 50,21 is the value in the column Yes and in column No 131, 2 is the value
a = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(a)


#String is also stored in the array and also the name of column.
b = pd.DataFrame({'Bob' : ['Hii', 'Hello'], 'Sue' : ['Sam', 'Rohit']})
print(b)


#In terminal you can see 0 1 it is default index if we do not give an index then 0 and 1 is the index
#In c we can give an  index so in the terminal you see Product A and Product B at the place of 0 1 or index
c = pd.DataFrame({'Bob' : ['I liked it.', 'It was awful.'], 'Sue' : ['Preety good.', 'Bland.']}, index = ['Product A', 'Product B'])
print(c)