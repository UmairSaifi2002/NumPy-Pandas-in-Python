import pandas as pd
import numpy as np

data = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'math-score' : [85, 90, 70, 95, 80],
    'science-score' : [88, 92, 75, 85, 80],
    'english-score' : [90, 85, 80, 95, 88],
}

df = pd.DataFrame(data)

print('Original DataFrame: \n', df)

# Reshaping the dataFrame  using melt

reshaped_df = pd.melt(df, id_vars=['name'], value_vars=['math-score', 'science-score', 'english-score'], var_name='subject', value_name='score')

print('\nReshaped DataFrame using melt: \n', reshaped_df)


# ------------------------------- Pivoting the reshaped DataFrame to get scores by subject and name ------------------------------- 

data_pivoted = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'subject' : ['math-score', 'science-score', 'english-score', 'math-score', 'science-score'],
    'score' : [85, 90, 70, 95, 80]
}

df_pivoted = pd.DataFrame(data_pivoted)

pivoted_df = df_pivoted.pivot(index='name', columns='subject', values='score')

print(pivoted_df)



