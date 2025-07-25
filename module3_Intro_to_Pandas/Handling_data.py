# Handling data in Pandas
import pandas as pd

data = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age' : [25, 30, None, 34, 29],
    'city' : ['New York', 'Los Angeles', 'Chicago', 'Houstan' , 'Phoenix'],
    'course' : ['Math', None, 'History', 'Art', 'Physics'],
}

df = pd.DataFrame(data)
print(f'Original DataFrmae: \n{df}')

# now we will learn how to handle the missing values in the DataFrmaes
# first we will check for the missing values
print(f'\nThe Missing values in the DataFrame : \n{df.isna()}')

# if we donot want the missing values so we can frop it 
print(f'\nDataFrame after dropping the missing values: \n{df.dropna()}')

# if we want to fill the missing values with some value
print(f'\nDataFrame after filling the missing values with 0: \n{df.fillna({"age": 19, "course": "Unknown"} )}')


