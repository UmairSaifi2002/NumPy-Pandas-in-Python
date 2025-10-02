# In this i will learn about how to find and handle the missing data in pandas

# Finding the missing data
import numpy as np
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'Age': [24, 27, np.nan, 32, np.nan],
    'City': ['New York', np.nan, 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 60000, np.nan, 75000]
}

df = pd.DataFrame(data)
print(f"Original DataFrame with missing values: \n{df}")

print(f'\nChecking for missing values : \n{df.isna().sum()} ')

# if i want to check for non missing values in a dataframe
print(f'\nChecking for non-missing values : \n{df.isna().any()}')
# here True indicates that there is at least one missing value in that particular column

# ------------------------------------------------------------------------------------------------
# Handling missing data
# mainly here i will learn about how to Remove missing data in a DataFrame

# .dropna() function is used to remove the rows with missing data
# by default it removes the rows with any missing values
print(f'\nDataFrame after dropping rows with any missing values: \n{df.dropna()}')

# threshold parameter is used to specify the minimum number of non-missing values required to keep a row
print(f'\nDataFrame after dropping rows with less than 3 non-missing values: \n{df.dropna(thresh=3)}')

# ------------------------------------------------------------------------------------------------
# Filling missing data in a DataFframe
# .fillna() function is used to fill the missing values with a specified value
print(f'\nDataFrame after filling missing values with 0: \n{df.fillna(0)}')

# now if i want to fill the missing values with custom values for each column
fill_values = {'Name' : 'Unknown', 'Age': 0, 'City' : 'Unknown', 'Salary': 0}
print(f'\nDataFrame after filling missing values with custom values: \n{df.fillna(fill_values)}')

