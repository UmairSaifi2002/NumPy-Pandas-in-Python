import numpy as np
import pandas as pd

# Creating a DataFrame from a dictionary of lists
employee_data = {
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing']
}

salary_data = {
    'EmployeeID': [3, 4, 5, 6],
    'Salary': [60000, 90000, 75000, 80000],
    'Bonus': [5000, 7000, 6000, 8000]
}

df1 = pd.DataFrame(employee_data)
df2 = pd.DataFrame(salary_data)

print(f"Employee DataFrame: \n{df1}")
print(f"\nSalary DataFrame: \n{df2}")

# Merging DataFrames
# Merging on a single column
print(pd.merge(df1, df2, on='EmployeeID', how='outer'))

# -------------------------------------------------------------------------------------------------------------
# Concatenation of DataFrames

print(f'\n Concatinating Two DataFrames : \n{pd.concat([df1, df2])}') # it is based on columns
print(f'\n Concatinating Two DataFrames : \n{pd.concat([df1, df2], axis=1)}') # it is based on rows
print(f'\n Concatinating Two DataFrames : \n{pd.concat([df1, df2], axis=1)}') # it is based on rows

# -------------------------------------------------------------------------------------------------------------
# Joining of DataFrames
data1 = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie'],
}, index=[1,2,3])

data2 = pd.DataFrame({
    'score' : [85, 90, 95],
}, index=[2,3,4])

print(f'\nJoining Two DataFrames : \n{data1.join(data2)}') # default is left join
print(f'\nJoining Two DataFrames : \n{data1.join(data2, how="outer")}') # outer join

