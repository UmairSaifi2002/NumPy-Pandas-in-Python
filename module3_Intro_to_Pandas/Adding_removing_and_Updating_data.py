import pandas as pd

df = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age' : [25, 30, 24, 34, 29],
    'city' : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'course' : ['Math', 'Science', 'History', 'Art', 'Physics'],
})

print("Original DataFrame:")
print(df)

# Adding a new row to the DataFrame
# This how we can add the row in the last of the DataFrame
df.loc[len(df)] = ['Frank', 28, 'Seattle', 'Biology']
print("\nDataFrame after adding a new row:")
print(df)

# Adding the new row at first position
df.loc[0] = ['Grace', 22, 'Miami', 'Chemistry']
print("\nDataFrame after adding a new row at the first position:")
print(df)

# Adding a new row at a specific index
df.loc[3] = ['Hannah', 26, 'Dallas', 'Economics']
print("\nDataFrame after adding a new row at index 3:")
print(df)

# now we will learn how to add the column in the DataFrame
# Adding a new column to the DataFrame
df['grade'] = ['A', 'B', 'C', 'D', 'E', 'F']
print("\nDataFrame after adding a new column:")
print(df)


# Removing the row fromt he DataFrame
df = df.drop(0)  # Dropping the first row
print("\nDataFrame after removing the first row:")
print(df)

# Removing a specific row by index
df = df.drop(3)  # Dropping the row at index 3
print("\nDataFrame after removing the row at index 3:")
print(df)

# Removing the column from the DataFrame
df = df.drop('grade', axis=1) # Dropping the 'grade' column
print("\nDataFrame after removing the 'grade' column:")
print(df)

# Updating a specific cell in the DataFrame
df.at[1, 'age'] = 31  # Updating the age of the second row
print("\nDataFrame after updating the age of the second row:")
print(df)

# Updating multiple cells in a column
df['city'] = df['city'].replace({'Chicago': 'San Francisco'})
df['course'] = df['course'].replace({'History': 'Geography'})
print('\nDataFrame after updating multiple cells in the city column: ')
print(df)

