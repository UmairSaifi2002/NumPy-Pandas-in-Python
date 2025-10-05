import pandas as pd
import numpy as np
import re
from dateutil.relativedelta import relativedelta 
from datetime import datetime

data = pd.read_csv(r'C:\\Umair\\Numpy Pandas\\NumPy-Pandas-in-Python\\anime.csv')

# print(data)
# print(data.loc[1])
# print(data.loc[1]['Title'])

# ------------------------------------------------------------------------------------------
# Extracting Episode from the Title Column

def extract_episode(title):
    check = False
    data = ''
    for i in title:
        if i == ')':
            break
        if i == '(':
            check = True
        if check:
            data = data + i
    data = data[1:]
    return data


data['Episode'] = data['Title'].apply(extract_episode)

# print(data)

# --------------------------------------------------------------------------------------------
# Convert the Episode column to int
data['Episode'] = data['Episode'].str.replace('eps', ' ')
data['Episode'] = data['Episode'].astype(int)
# print(data)


# --------------------------------------------------------------------------------------------
# Make a new Column for time stamp
# print(data.loc[1]['Title'])

def extraction_time(txt):
    check = False
    data = ''
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1, i+20):
                data = data + txt[j]
            return data

data['Time_Period'] = data['Title'].apply(extraction_time)

# print(data)

# --------------------------------------------------------------------------------------------
# Extract the months from the Time Column

def extract_months(txt):
    try:
        start_str, end_str = txt.split(' - ')
        start_str = datetime.strptime(start_str, '%b %Y')
        end_str = datetime.strptime(end_str, '%b %Y')
        # print(start_str, end_str)
        r = relativedelta(end_str, start_str)
        return r.years * 12 + r.months + 1
    except:
        return None            

data['Months'] = data['Time_Period'].apply(extract_months)
# print(data)

# --------------------------------------------------------------------------------------------
# which anime has the highest score
# print(data[data['Score'] == data['Score'].max()]['Title'])

# --------------------------------------------------------------------------------------------
# Print Top 5 anime with highest score
top_5 = data.sort_values(by='Score', ascending=False).head(5)
# print(top_5[['Title', 'Score']]) 

# --------------------------------------------------------------------------------------------
# Which anime has the highest number of episodes
# print(data[data['Episode'] == data['Episode'].max()]['Title'])

# --------------------------------------------------------------------------------------------
# Print Top 5 anime with highest number of episodes
Top_5_episodes = data.sort_values(by='Episode', ascending=False).head(5)
# print(Top_5_episodes[['Title', 'Episode']])

# --------------------------------------------------------------------------------------------
# Which is the longest running anime
print(data[data['Months'] == data['Months'].max()]['Title'])



