"""
Script to read new data, save as csv. Then push new file to git.
"""

import pandas as pd
from urllib.request import urlopen
import subprocess as cmd
from datetime import datetime
import os

github_dir = '/Users/tiffanyzhu/projects/covid19-projects/covid19-data/'

# Filter out a few states
STATES = ['New Jersey', 'California', 'New York', 'Connecticut']
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
counties_df = pd.read_csv(counties_url, dtype=str)
df_filtered = counties_df[counties_df['state'].isin(STATES)]

# Save filtered file
df_filtered.to_csv(github_dir+'us-counties-filtered.csv', index=False)


# Push to Git
try:
    cmd.run("/usr/local/bin/git -C {} add .".format(github_dir), check=True, shell=True)
    update_message = '"Update data on {}"'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    cmd.run('/usr/local/bin/git -C {} commit -m {}'.format(github_dir, update_message), check=True, shell=True)
    cmd.run("/usr/local/bin/git -C {} push -u origin master".format(github_dir), check=True, shell=True)
except Exception as e:
    print("Error with extract_data.py")
    print("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
