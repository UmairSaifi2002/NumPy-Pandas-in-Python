# Now we will learn about filtering, sorting, and grouping data in Pandas
import pandas as pd

data = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age' : [25, 30, 35, 34, 29],
    'salary' : [50000, 60000, 70000, 80000, 90000],
    'city' : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
}

df = pd.DataFrame(data)
print(f'Original DataFrame: \n{df}')

# now i will tell you how to filter the data in the DataFrame
# for example, if we want to filter the DataFrame where age is greater than 30
filtered_data = df[df['age'] > 30]
print(f'\nFiltered DataFrame where age > 30: \n{filtered_data}')

sorted_data = df.sort_values(by='salary', ascending=False)
print(f'\nDataFrame sorted by salary in descending Order: \n{sorted_data}')

sorted_age_data = df.sort_values(by='age', ascending=True)
print(f'\nDataFrame sorted by age in ascending Order: \n{sorted_age_data}')

# now i will tell you how to group the data in the dataframe
df['department'] = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
grouped_data = df.groupby('department')['salary'].mean()
print(f'\nAverage salary by department: \n{grouped_data}')

# You can also group by multiple columns
grouped_multi_data = df.groupby(['city', 'department'])['salary'].sum()
print(f'\nTotal salary by city and department: \n{grouped_multi_data}')

# You can reset the index after grouping
grouped_multi_data_reset = grouped_multi_data.reset_index()
print(f'\nTotal salary by city and department with reset index: \n{grouped_multi_data_reset}')


