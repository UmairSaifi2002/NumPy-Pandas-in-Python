import numpy as np
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store' : ['s1', 's1', 's2', 's2', 's1', 's2', 's2', 's1'],
    'Sales' : [100, 200, 150, 300, 250, 400, 350, 500],
    'Quantity' : [10, 15, 12 , 18, 8, 20, 15, 25],
    'Date' : ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08']
}

df = pd.DataFrame(data)
print(f"Original DataFrame: \n{df}")

# ------------------------------------------------------------------------------
# groupping = df.groupby('Category')
# Sales_sum = groupping['Sales'].sum()
# print(f"\nSum of Sales for each Category: \n{Sales_sum}")

# All this in a single line
print(f'\nSales sum for each Category : \n{df.groupby('Category')['Sales'].sum()}')


# groupping by multiple columns
print(f'\nSales sum for each Category and Store : \n{df.groupby(['Category', 'Store'])['Sales'].sum()}')

# ------------------------------------------------------------------------------
# Aggregation function

# mean()
# print(df['Sales'].mean())
# print(df['Sales'].median())
# print(df['Sales'].mode())
# print(df['Sales'].min())
# print(df['Sales'].max())
# print(df['Sales'].count())
# print(df['Sales'].std())

# All this above in a single line using agg() function
# print(f'\nDifferent aggregation functions on Sales column : \n{df['Sales'].agg(['mean', 'median', 'mode', 'min', 'max', 'count', 'std'])}')
# print(df['Sales'].agg(['mean', 'median', 'mode', 'min', 'max', 'count', 'std']))
print(df['Sales'].agg(['mean', 'median', 'min', 'max', 'count', 'std']))





