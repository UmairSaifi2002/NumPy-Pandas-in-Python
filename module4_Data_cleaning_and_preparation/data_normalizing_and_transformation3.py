# now i will tell you something about the data normalization and tanformation using python
import pandas as pd
import numpy as np

data = {
    'value' : [10, 20, 300, 200, 10, 5],
}

df = pd.DataFrame(data)

df['log_value'] = np.log(df['value']) # Applying log transformation

print('DataFrame after log transformation: \n', df)

data2 = {
    'Score' : [100, 200, 300, 400, 500],
}

df2 = pd.DataFrame(data2)

df2['normalization_score'] = (df2['Score'] -df2['Score'].min()) / (df2['Score'] - df2['Score'].max()) # Normalizing the score between 0 and 1

print('\nDataFrame after normalization: \n', df2)

