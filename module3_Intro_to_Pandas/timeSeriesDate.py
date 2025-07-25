# now we will learn something abou the date and time

import pandas as pd

data = {
    'date' : ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05', '2025-01-06'],
    'value' : [10, 20 , 30 , 20 , 10 ,5],
}

df = pd.DataFrame(data)
print('original DataFrame: \n',df)

df['date'] = pd.to_datetime(df['date']) # Converting the date column to date-time format
df.set_index('date', inplace = True) # Setting the date column as index
print('\nDataFrame with date as index: \n', df)

monthly_data = df.resample('M').sum()  # Resampling the data to monthly frequency and summing the values
print('\nMonthly resampled data: \n', monthly_data)

# now we 

