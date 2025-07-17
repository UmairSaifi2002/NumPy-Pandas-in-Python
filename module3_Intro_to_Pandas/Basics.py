# Here we will leran the basis of pandas
import pandas as pd

# Create a simple DataFrame using the dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Creating a simple DataFrame from a list of lists
data_list = [
    ['david', 28, 'Miami'],
    ['Eva', 22, 'Seattle'],
    ['Frank', 40, 'Boston']
]

df1 = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print(df1)
