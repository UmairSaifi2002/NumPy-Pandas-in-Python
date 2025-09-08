import numpy as np
import pandas as pd

data = pd.read_csv(r'Countries.csv')
# print(data)

# -------------------------------------------------------------------------------------
# now its time to learn 
# Data Pre - Processing
# knowing the shape of data
# print(data.shape)

# knowing the info
# print(data.info())

# using the describe the data
# print(data.describe())

# -------------------------------------------------------------------------------------
# which country has the highest population
highest_populatin_country = data[data['population'] == data['population'].max()]
# print(highest_populatin_country)

# what is the capital of the country having a highest population
# print(highest_populatin_country['capital_city'])

# -------------------------------------------------------------------------------------
# Which country has the least population
lowest_population_country = data[data['population'] == data['population'].min()]
# print(lowest_population_country)

# what is the capital of the country having a lowest population
# print(lowest_population_country['capital_city'])

# -------------------------------------------------------------------------------------
# Top 5 Countries with highest democratic score
sorted_data = data.sort_values(by='democracy_score',ascending=False)
# print(sorted_data.head(5)['country'])

# -------------------------------------------------------------------------------------
# how many total regions are there
# print(data['region'].value_counts().count())

# -------------------------------------------------------------------------------------
# how many country lie in Eastern Euarope region
# it givd count of a country
# print(data['region'].value_counts()['Eastern Europe'])

# print(data[data['region'] == 'Eastern Europe']['country'])

# -------------------------------------------------------------------------------------
# who is the political leader of the second highest populated country
sorted_data_by_population = data.sort_values(by='population', ascending=True)
# print(sorted_data_by_population.iloc[1]['political_leader'])
# print(data[data['population'] == data['population'].nlargest(2).iloc[1]]['political_leader'])

# ------------------------------------------------------------------------------------
# how many countries are there whose political leaders are unknown
# print(data.loc[data['political_leader'].isna()])
# print(data[data['political_leader'].isnull()]['country'])
# print(f'There are {(data[data['political_leader'].isnull()]['country']).count()} countries whose political leader are unknown')

# ------------------------------------------------------------------------------------
# how many country have Republic in their Full Name
# count = 0
# def counting(txt):
#     global count
#     if 'republic' in txt.lower():
#         count += 1
#     return txt
# data['country_long'] = data['country_long'].apply(counting)
# print(count)

# ------------------------------------------------------------------------------------
# which country in african region has highest population
africa_data = data[data['continent'] == 'Africa']
africa_data_population = africa_data.sort_values(by='population', ascending=False)
print(africa_data_population.head(5))

    





