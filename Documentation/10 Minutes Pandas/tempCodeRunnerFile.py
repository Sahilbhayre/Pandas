import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.nan, 5, 6], index=['A', 'B', 'C', 'D', 'E', 'F'])
print(s)