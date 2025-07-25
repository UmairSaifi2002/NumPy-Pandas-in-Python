# now we will learn about the indexing in the DataFrame
# using pandas
import pandas as pd

data = {
    'name' : ['Alice', 'Bob', 'Charlie'],
    'age' : [25, 30, 35],
    'city' : ['New York', 'Los Angles', 'Chicago']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Accessing a single row by index
print("\nAccessing the row at index 1:")
print(df.loc[1])

# Accessing multiple rows by index
print("\nAccessing rows at index 0 and 2:")
print(df.loc[[0, 2]])