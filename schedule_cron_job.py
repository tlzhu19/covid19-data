"""
Run this script to schedule a cron job to run everyday.
Job is to run script "extract_data.py"
"""
from crontab import CronTab
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
python_script = os.path.join(dir_path, 'extract_data.py')
python_environment = '/Users/tiffanyzhu/anaconda3/bin/python3'

"""
In terminal:
* To check jobs: crontab -l
* To delete all jobs: crontab -r
* To check errors: `vim /var/mail/tiffanyzhu` or `mail`
* Delete mail: `cat /dev/null >/var/mail/tiffanyzhu` or `mail` -> `delete *`
"""

cron = CronTab(user='tiffanyzhu')
# cron.remove_all()  # to delete the job

job_command = '{} {}'.format(python_environment, python_script)
job = cron.new(command=job_command, comment='coviddata')

# Run job every 1 minute (to test)
# job.minute.every(1)

# Run job 10:30am every day
job.minute.on(30)
job.hour.on(10)
print(job)

cron.write()
