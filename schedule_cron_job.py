from crontab import CronTab
import os 
# from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
python_script = os.path.join(dir_path, 'extract_data.py')
python_environment = '/Users/tiffanyzhu/anaconda3/bin/python3'

"""
In terminal:
* To check jobs: crontab -l
* To delete all jobs: crontab -r
* To check errors: vim /var/mail/tiffanyzhu
"""

cron = CronTab(user='tiffanyzhu')
# cron.remove_all()

job_command = '{} {}'.format(python_environment, python_script)
job = cron.new(command=job_command, comment='coviddata')

# Run job every 1 minute (to test)
job.minute.every(1)

# Run job 8am every day
# job.minute().on(0)
# job.hour().on(8)
print(job)



# # Git pushing command
# job_command_git = 'cd /Users/tiffanyzhu/projects/covid19-projects/covid19-data/ && git add . && git commit -m {} && git push -u origin master -f'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# job_git = cron.new(command=job_command_git, comment='coviddatagit')
# job_git.minute.every(1)
# print(job_git)

cron.write()