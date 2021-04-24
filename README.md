# covid19-data

* extract_data.py: script that filters data, saves as csv, then push to git
* schedule_cron_job.py: schedules a crontab job to automatically run "extract_data.py everyday"
* us-counties-filtered.csv: the saved data from "extrac_data.py", used in https://github.com/tlzhu19/covid19-dashboard
