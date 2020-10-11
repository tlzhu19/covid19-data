import pandas as pd
from urllib.request import urlopen


# Filter out a few states
STATES = ['New Jersey', 'California', 'New York', 'Connecticut']
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
counties_df = pd.read_csv(counties_url, dtype=str)
df_filtered = counties_df[counties_df['state'].isin(STATES)]

df_filtered.to_csv('us-counties-filtered.csv', index=False)

