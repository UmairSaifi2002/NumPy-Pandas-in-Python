import pandas as pd
import numpy as np

data1 = {
    'Id' : [1, 2, 3, 4, 5],
    'Name' : ['Alice', 'Bob', 'Charlie', 'David' ,'Eva']
}

data2 = {
    'Id' : [1, 2, 3, 6, 7],
    'Score' : [85, 90, 95, 80, 75]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='Id', how='outer')  # Merging dataframes on 'Id' column using outer join
# merged_df = pd.merge(df1, df2, on='Id') # Merging dataFrames on 'Id' column using inner join
merged_df = merged_df.set_index('Id')
print('Merged DataFrame: \n', merged_df)


# -------------------------------- joining dataFrames using join method ---------------------------------

data3 = {
    'name' : ['Umair', 'Ali', 'Ahmed', 'Zara'],
    'age' : [25, 30, 35, 28],
}

df3 = pd.DataFrame(data3, index=[1,2,3,4])

data4 = {
    'score' : [88, 92, 85, 90],
}

df4 = pd.DataFrame(data4, index=[1,2,3,5])

joine_df = df3.join(df4, how = 'inner') # Joining dataFrames using inner join

print('\nJoined DataFrame: \n', joine_df)

joined_df_outer = df3.join(df4, how = 'outer') # Joining dataFrames using outer join
print('\nJoined DataFrame with outer join: \n', joined_df_outer)

# -------------------------------- concatenating dataFrames ---------------------------------

data5 = {
    'name' : ['Umair', 'Ali', 'Ahmed'],
    'age' : [25, 30, 35],
}

data6 = {
    'name' : ['Zara', 'John'],
    'age' : [28, 32],
}

df5 = pd.DataFrame(data5)
df6 = pd.DataFrame(data6)

concatnated_df = pd.concat([df5, df6])

print('\nConcatenated DataFrame: \n', concatnated_df)
