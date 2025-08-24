# Now i will tell you about the Series in pandas
# Series is a one-dimensional array-like object that can hold various data types, including integers, floats, strings, and Python objects. \
# It is similar to a column in a DataFrame or a one-dimensional array in NumPy.
# Each element in a Series is associated with an index, which allows for easy access and manipulation of data. 
# If no index is provided, pandas will create a default integer index starting from 0.

import numpy as np
import pandas as pd

# Creating a Series from a list
labels = ['a', 'b', 'c', 'd', 'e']
data = [10, 20, 30, 40, 50]
series1 = pd.Series(data,index=labels)
print(f"Series from a list: \n{series1}")

# cresting series from a dictionary
data_dict = {'a': 100, 'b': 200, 'c': 300}
series2 = pd.Series(data_dict)
print(f"\nSeries from a dictionary: \n{series2}")




