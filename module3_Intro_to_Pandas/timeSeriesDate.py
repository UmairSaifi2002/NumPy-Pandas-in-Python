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

df1 = pd.DataFrame(data)
df1['date'] = pd.to_datetime(df1['date'])
print('\nDataFrame with date as index: \n', df1 )

df1['year'] = df1['date'].dt.year  # Extracting the year from the date
df1['month'] = df1['date'].dt.month # Extracting the month from the date
df1['day'] = df1['date'].dt.day     # Extracting the day from the date
df1['weekday'] = df1['date'].dt.weekday  # Extracting the weekday from the date

print(df1)

data1 = {
    'date' : pd.date_range(start='2025-01-01', periods = 6, freq = 'D'),
    'value' : [10, 20 , 30 , 20 , 10 ,5],
}

df2 = pd.DataFrame(data1)
df2.set_index('date', inplace=True)  # Setting the date column as index
print('\nDataFrame with date as index: \n', df2)

df2['shift_value'] = df2['value'].shift(1) # Shifting the values by 1 day
print('\nDataFrame with shifted values: \n', df2)

