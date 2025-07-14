# now we learn about the library instalation
# To install a library
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'names': ['Alice', 'Bob', 'Charlie', 'David'],
    'ages': [24, 30, 22, 35],
    'salaries': [50000, 60000, 55000, 70000]
})

print(data.head())
#      names  ages  salaries
# 0    Alice    24     50000
# 1      Bob    30     60000
# 2  Charlie    22     55000
# 3    David    35     70000

print(data.describe())
#             ages      salaries
# count   4.000000      4.000000
# mean   27.750000  58750.000000
# std     5.909033   8539.125638
# min    22.000000  50000.000000
# 25%    23.500000  53750.000000
# 50%    27.000000  57500.000000
# 75%    31.250000  62500.000000
# max    35.000000  70000.000000

filtered_data = data[data['ages'] > 25]
print(filtered_data)
