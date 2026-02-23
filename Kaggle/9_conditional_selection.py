import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

#For example, suppose that we're interested specifically in better-than-average wines produced in Italy.

#1We can start by checking if each wine is Italian or not: This operation produced a Series of True/False booleans based on the country of each record.
print(reviews.country == 'Italy')

#2 The result which is obtained from above can then be used inside of loc to select the relevant data:
print(reviews.loc[reviews.country == 'Italy'])

#3. We also wanted to know which ones are better than average. Wines are reviewed on a 80-to-100 point scale, so this could mean wines that accrued at least 90 points.
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])

#Not take null value
print(reviews.loc[reviews.price.notnull()])

#For example selecting Italy and France then we use isin
print(reviews.country.isin(['Italy', 'France']))