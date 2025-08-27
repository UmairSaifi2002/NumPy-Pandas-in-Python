import numpy as np
import pandas as pd

# it is used for Data pre-processing
# and it is called as data pre-processing library

df1 = pd.DataFrame({
    'A':[1, 2, 3, 4, 5],
    'B':[10, 20, 30, 40, 50],
    'C':[100, 200, 300, 400, 500]
})

print(df1)

print(f'\ndataFrame shape : {df1.shape}')

print(f'\nColumns of DataFrame : {df1.columns}')

print(f'\nInformation of DataFrame : \n{df1.info()}')

print(f'\nDataFrame Describe : \n{df1.describe()}')

# now if i want to 10 in a particular row
print(df1['A'] + 10)

def square(x):
    return x*x

df1['B'] = df1['B'].apply(square)
print(df1)

# print(df1['B'].apply(square))

# df['B'] = df1['B'].apply(lambda x: x*x)

# df['B'] = df1['B'].apply(lambda x: x + 10 if x > 20 else x - 10)
