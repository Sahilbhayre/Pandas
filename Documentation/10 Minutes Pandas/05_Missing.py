import pandas as pd
df = pd.read_csv("winemag-data-130k-v2.csv")
print(pd.isna(df))
print(df.dropna(how="any"))  # Drops any rows that have missing data 
print(df.fillna(value=1))    # Replace missing value with 1
print(pd.isna(df))  #isna() gets the boolean mask where values are nan, if values nan return True
