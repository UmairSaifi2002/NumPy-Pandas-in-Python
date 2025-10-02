# Now i will learn about DataFrames in pandas
# A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axis (rows and columns).
# It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.

import numpy as np
import pandas as pd

# Creating a DataFrame from a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 60000, 90000]
}

df1 = pd.DataFrame(data)
print(f"DataFrame from a dictionary of lists: \n{df1}")

# ------------------------------------------------------------------------------
# Creating a DataFrame from a list of dictionaries
data_list = [
    ['Name', 'Age', 'City', 'Salary'],
    ['Alice', 24, 'New York', 70000],   
    ['Bob', 27, 'Los Angeles', 80000],
    ['Charlie', 22, 'Chicago', 60000],
    ['David', 32, 'Houston', 90000]
]

df2 = pd.DataFrame(data_list[1:], columns=data_list[0])
print(f"\nDataFrame from a list of lists: \n{df2}")


# ------------------------------------------------------------------------------
# Creating a DataFrame from a NumPy array
array_data = np.array([
    ['Alice', 24, 'New York', 70000],
    ['Bob', 27, 'Los Angeles', 80000],
    ['Charlie', 22, 'Chicago', 60000],
    ['David', 32, 'Houston', 90000]
])
df3 = pd.DataFrame(array_data, columns=['Name', 'Age', 'City', 'Salary'])
print(f"\nDataFrame from a NumPy array: \n{df3}")


# ------------------------------------------------------------------------------
# indexing and selecting data in DataFrame
print(f"\nSelecting the 'Name' column: \n{df1['Name']}")
print(f"\nSelecting the 'Name' & 'Salary' columns: \n{df1[['Name', 'Salary']]}")

# ------------------------------------------------------------------------------
# Creating a new column
df1['Experience'] = [2, 5, 1, 7]
df1['Designation'] = ['Engineer', 'Manager', 'Intern', 'Director']
print(f"\nDataFrame after adding a new column's: \n{df1}")

# ------------------------------------------------------------------------------
# Dropping a column
df1.drop('Experience', axis=1)
print(f"\nDataFrame after dropping the 'Experience' column: \n{df1}")
# in above two  lines of code the column is not dropped permanently
# to drop the column permanently we have to use inplace=True or we have to assign the result to the same dataframe
df1.drop('Experience', axis=1, inplace=True)
print(f"\nDataFrame after dropping the 'Experience' column permanently: \n{df1}")

# ------------------------------------------------------------------------------
# Selecting a row by index
print(f'\nSelecting the first row: \n{df1.loc[0]}')
print(f'\nSelecting the row using iloc: \n{df1.iloc[3]}')

# ------------------------------------------------------------------------------
# Selecting a particular needed value from a row
print(f'\nSelecting the Name,City of the First row: \n{df1.loc[0, ['Name', 'City']]}')
# selection a two roars and two columns
print(f'\nSelecting the Name,City of the First two rows: \n{df1.loc[[0, 1], ["Name", "City"]]}')

print(f'\nSelecting rows based on condition: \n{df2[df2["Salary"] > 60000]}')

print(f'\nSelecting rows based on multiple conditions: \n{df2[(df2["Salary"] > 60000) & (df2["Age"] < 30)]}')

