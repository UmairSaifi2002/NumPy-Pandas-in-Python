import pandas as pd
import numpy as np

data = pd.read_csv(r'anime.csv')

# print(data)

# print(f'Top 5 rows of data : \n{data.head()}')

# make a new column for episode count
# data['Episode_count'] = data['Episodes'].apply(lambda x: 0 if x == 'Unknown' else int(x))

print(data.loc[1]['Title'])

def extract_episode_count(x):
    check = False
    data = ''
    for i in x:
        if i == ')':
            break
        if i == '(':
            check = True
            continue
        if check:
            data = data + i
    return data

data['Episode_count'] = data['Title'].apply(extract_episode_count)

print(data)














