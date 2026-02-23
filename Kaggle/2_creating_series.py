import pandas as pd

#In Series their is only one column and in series we can automatically get a dtype
a = pd.Series([1, 2, 3, 4, 5, 6])
print(a) #dtype: int64

#In the above dtype is int64 but the dtype of the below is object
b = pd.Series(['1', '2', '3', '4', '5'])
print(b)

#Index in a and b is 0 1 2 3 4 but the index in c is given by ourselves
#And also give the name
c = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(c)