import numpy as np
import pandas as pd

data = {
    'Date' : pd.date_range(start='2023-01-01', periods=20),
    'Product' : ['A', 'B', 'C', 'D'] * 5,
    'Region' : ['East', 'West', 'North', 'South'] * 5,
    'Sales' : np.random.randint(100, 1000, 20),
    'Units' : np.random.randint(10, 100, 20),
    'Rep' : ['John', 'Jane', 'Jim', 'Jill'] * 5    
}

dataFrame = pd.DataFrame(data)
print(f'Original DataFrame: \n{dataFrame}')

# adding months column in dataFrame
dataFrame['Month'] = dataFrame['Date'].dt.month
dataFrame['Quater'] = dataFrame['Date'].dt.quater.astype(str)




