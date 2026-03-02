import pandas as pd
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Carol']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [90, 80, 95]})

#1 concat
combined = pd.concat([df1, df2], axis=0) 
print(combined)

combined1 = pd.concat([df1, df2], axis = 1)
print(combined1)

#2 merge
merged = pd.merge(df1, df2, on='ID', how='inner')
print(merged)

#3 join
df3 = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
df4 = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'w'])

joined = df3.join(df4, how='outer')
print(joined)

#4 combine first
df5 = pd.DataFrame({'A': [1, None, 3]})
df6 = pd.DataFrame({'A': [10, 20, 30]})

combined = df5.combine_first(df6)
print(combined)