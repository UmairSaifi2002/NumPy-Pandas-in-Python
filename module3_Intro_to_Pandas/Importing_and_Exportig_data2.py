# here we will learn how to import and export the data from any file
# using pandas

import pandas as pd

df = pd.read_csv('data.csv') # Reading the CSV File
print("DataFrame from CSV: ")
print(df)

# exporting the DataFrame to a new CSV file
df.to_csv('exported_data.csv', index=False)
print('\nData exported to -> exported_data.csv <- file')

# -------------------------------------------------------------------------------- #
# now we will learn about how to read and write Excel files
df_excel = pd.read_excel('data.xlsx')  # Reading the Excel File
print("\nDataFrame from Excel: ")
print(df_excel)

# exporting the DataFrame to a new Excel file
df_excel.to_excel('exported_data.xlsx', index=False)

# -------------------------------------------------------------------------------- #
# now we will learn about how to read and write JSON files
df_json = pd.read_json('data.json') # Reading the JSON File
print("\nDataFrame from JSON: ")
print(df_json)

# exporting the DataFrame to a new JSON file
df_json.to_json('exported_data.json', orient='records', lines=True)
