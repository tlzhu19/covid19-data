import pandas as pd
from urllib.request import urlopen
import subprocess as cmd
from datetime import datetime


# Filter out a few states
STATES = ['New Jersey', 'California', 'New York', 'Connecticut']
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
counties_df = pd.read_csv(counties_url, dtype=str)
df_filtered = counties_df[counties_df['state'].isin(STATES)]

df_filtered.to_csv('us-counties-filtered.csv', index=False)


# Push to Git
try:
    cmd.run("git add .", check=True, shell=True)
    update_message = '"Update data on {}"'.format(datetime.today().strftime('%Y-%m-%d'))
    cmd.run('git commit -m {}'.format(update_message), check=True, shell=True)
    cmd.run("git push -u origin master -f", check=True, shell=True)
except:
    print("Error git automation")
