import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

A = reviews.groupby(['country', 'province']).description.agg([len])
b = A.reset_index()
#print(A)
#print(b)

#c = b.sort_values(by = 'len', ascending=True) is same as:
c = b.sort_values(by = 'len')  #Sort in descresing to increasing order
print(c)

d = b.sort_values(by = 'len', ascending=False)  #Sort in HIGH to LOW
print(d)

e = b.sort_values(by=['country', 'len'])  #Sort in country(in alphabetical order) and len both, first country sort then length sort of the same countries
print(e)

f = b.sort_index()   #Sort by index
print(f)