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
