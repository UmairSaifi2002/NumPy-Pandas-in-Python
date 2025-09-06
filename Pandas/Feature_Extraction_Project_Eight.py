import pandas as pd
import numpy as np
import re
from dateutil.relativedelta import relativedelta 

data = pd.read_csv(r'anime.csv')

# print(data)

# print(f'Top 5 rows of data : \n{data.head()}')

# make a new column for episode count
# data['Episode_count'] = data['Episodes'].apply(lambda x: 0 if x == 'Unknown' else int(x))

# print(data.loc[1]['Title'])

def episode_count(x):
    check = False
    data = ''
    for i in x:
        if i == ')':
            break
        if i == '(':
            check = True
        if check:
            data += i
    if data == '':
        return 0
    # return int(data[1:3])
    return data[1:-1]

# ----------------------------------------------------------------------
# manually entering the episode count to the data frame
# print(episode_count(data.loc[1]['Title']))
# print(len(data))

# episode_count_list = []

# for i in range(len(data)):
#     # print(f'Index : {i} | Title : {data.loc[i]['Title']} | Episode Count : {episode_count(data.loc[i]['Title'])} ')
#     episode_count_list.append(episode_count(data.loc[i]['Title']))

# data['Episode_count'] = episode_count_list

# print(data)

# ----------------------------------------------------------------------
# using apply function to enter the episode count to the data frame
data['Episode_count'] = data['Title'].apply(episode_count)
# print(data)

data['Episode_count'] = data['Episode_count'].str.replace(' ep','')
data['Episode_count'] = data['Episode_count'].astype(int)
# print(data)

#-------------------------------------------------------------------------------
# Extracting the time stamp from the Episodes 
def extract_episode_time_stamp(x):
    check = False
    data = ''
    for i in x:
        if i == ',':
            break
        if i == ')':
            check = True
        if check:
            data += i
    data = data.replace(')', '')
    data = data[0:19]
    return data
# print(data.loc[0]['Title'])
# print(extract_episode_time_stamp(data.loc[1]['Title']))
        
data['Episode_time_stamp'] = data['Title'].apply(extract_episode_time_stamp)
# print(data)

# -------------------------------------------------------------------------------
# Extracting a total months from the time stamp

def total_months_count(x):
    match = re.match(r'(\w+ \d+) - (\w+ \d+)', x)
    # print(match)
    if not match:
        raise ValueError(f"Input string format not valid: {x}")
    start_date, end_date = match.groups()
    start_date = pd.to_datetime(start_date, format='%b %Y')
    end_date = pd.to_datetime(end_date, format='%b %Y')
    rd = relativedelta(end_date, start_date)
    total_months = rd.years * 12 + rd.months + 1 # +1 to include the starting month
    return total_months
    
data ['Total_months'] = data['Episode_time_stamp'].apply(total_months_count)
# print(data)

# print(total_months_count('Jan 2020 - Dec 2021'))

# ---------------------------------------------------------------------------------
# Which anime has the highest score

high_score_anime = data[data['Score'] == data['Score'].max()]['Title']
# print(str(high_score_anime))

# ---------------------------------------------------------------------------------
# Top five anime
# print(data['Title'].head(5)) # because our data is sorted

# ---------------------------------------------------------------------------------
# which anime has the highest episode count
highest_episode = data[data['Episode_count'] == data['Episode_count'].max()]
# print(highest_episode)

# ---------------------------------------------------------------------------------
# anime with top 5 episode count
# first sort the data 
data_sec = data.sort_values(by='Episode_count', ascending=False)
# print(data_sec)
# print(data_sec['Title'].head(5))

# ---------------------------------------------------------------------------------
# which is the longest running anime
print(data[data['Total_months'] == data['Total_months'].max()])
    

