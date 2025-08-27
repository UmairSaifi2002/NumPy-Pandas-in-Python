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
dataFrame['Quater'] = 'Q' + dataFrame['Date'].dt.quarter.astype(str)
print(f'Original DataFrame: \n{dataFrame}')

# using Groupby for the data
# print(f'GroupBy Result: \n{dataFrame.groupby(["Product", "Region"]).agg({"Sales": "sum", "Units": "sum"})}')

# making a pivort table
pivotTable = pd.pivot_table(dataFrame, values='Sales', index='Region', columns='Product', aggfunc='sum')
print(f'\nPivot Table: \n{pivotTable}')

pivotTable2 = pd.pivot_table(dataFrame, values=['Sales', 'Units'], index='Region', columns='Product')
print(f'\nPivot Table 2: \n{pivotTable2}')

# ------------------------------------------------------------------------------------------------------------------
# Cross Tabs
# cross Tabs is used for Counting purpose
# Cross Tab is different from Pivot Table as it is used for counting purpose
# but Pivot Tables is used for aggregation purpose
crossTab = pd.crosstab(dataFrame['Region'], dataFrame['Product'])
print(f'\nCross Tab: \n{crossTab}')