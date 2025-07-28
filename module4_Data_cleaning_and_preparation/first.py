import pandas as pd
import numpy as np

data = {
    'A' : [1, 2, np.nan, 4, 5],
    'B' : [5, np.nan, 3, 4, 2],
    'C' : [np.nan, 1, 2, 3, np.nan]
}

df = pd.DataFrame(data)
print('Original DataFrame: \n', df)

print('Missing values ')
print(df.isna())

df_filled = df.fillna(value=0)

print('\nDataFrame after filling missing values with 0: \n', df_filled)



