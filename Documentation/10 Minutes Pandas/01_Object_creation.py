import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.nan, 5, 6], index=['A', 'B', 'C', 'D', 'E', 'F'], name='Numeric')
print(s)
print()
#df = pd.DataFrame([1, 2, 3, 4, 5], columns=['number'])
df = pd.DataFrame({
    'A' : 10,
    'B' : pd.date_range("20250214", periods=6),
    'C' : pd.Series(1, index=list(range(6))),
    'D' : np.array([3]*6),
    'E' : pd.Categorical(["test", "train","traibbs", "train", 'test', 'test']),
    'F' : 'foo'
})
print(df)
print()
print(df.dtypes)