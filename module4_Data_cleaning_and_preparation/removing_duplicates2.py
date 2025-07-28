import numpy as np
import pandas as pd

data = {
    'A' : [1,2,3,2,1],
    'B' : [5,4,3,4,5],
    'C' : [1,2,3,4,5],
    'name' : ['Umair', 'Ali', 'Ahmed', 'Ali', 'Zara'],
}

df = pd.DataFrame(data)

print('Original dataFrame: \n', df)

df_no_duplicates = df.drop_duplicates(subset=['A', 'B'], keep='first')  # Removing duplicates based on columns A and B, keeping the first occurrence
print('\nDataFrame after removing duplicates: \n', df_no_duplicates)


