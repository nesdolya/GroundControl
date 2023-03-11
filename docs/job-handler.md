# Job Handling
This page describes how to use Python to manage jobs. Check out the [Web UI](tutorials.md#web-ui) for additional job handling.

A GroundControl [job](introduction.md#job) class is used to run a user defined Python function. This job class requires the following arguments:

|Arguments | Description|
|----------- |-------------|
|Job Name | The name of the job. It will appear in the web-based user interface. It is NOT a unique identifer. |
|Function Path | The path to the Python script that contains the function to be run. For example: '/path/to/CronMetric_RecEff_func.py'.|
|Function Name | The function to be run. For example: 'CronMetrics_RecEff_exec'.|
|Function Arguements | The argurments that the function being run may require (optional).|
|Cron time expression | The cron expression representing the scheduled time to run the job. |

These parameters need to be JSON serializable, which means they must be strings. It will not work when passing objects, such as a logging object. Modifications to SoundSpace Analytic's functions to accept strings is required. More information on this can be found in [Trouble Shooting](troubleshooting.md#json-serializable)

### Cron time expressions
They can be represented as either a list or as individual parameters. If a list is provided it musth be in this order [minute, hour, month, day, day_of_week]. If individual parameters are provided, any missing will default to '*' .

+ [Understanding Cron Syntax in the Job Scheduler](https://www.netiq.com/documentation/cloud-manager-2-5/ncm-reference/data/bexyssf.html)
+ [crontab guru](https://crontab.guru/)

## Add a Job
Modify the executable Python script for SoundSpace Analytics.

Import the AddJob function:

	from GroundControl.AddJob import AddJob

Create the job to be added by passing the required variables to AddJob. This example is from CronMetri_RecEff_exec.py

    job_name = 'CronMetric_RecEff_v2'
	mod_path = os.path.join(ProgramDir, 'CronMetric_RecEff_func.py')
	mod_name = 'CronMetrics_RecEff_exec'
	exec_args = log_path+'CronMetrics_RecEff.log'
	cron_time = ['*/1','*','*','*','*']
	
	job_to_add = AddJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time)

Add the job to the server for scheduled runs using commit()
	
	job_to_add.commit()

In a single line:
	
	job_to_add = AddJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time).commit()


The updated CronMetri_RecEff_exec.py looks like:

	'''
	/* Copyright (C) 2022 SoundSpace Analytics- All Rights Reserved
	* This code is exclusive property of SoundSpace Analytics.  
	* You may not use, distribute or modify this code, except with the
	* explicit permission of the owner. Please contact benhendricks@soundspace-analytics.ca
	* for further questions.
	*/
	'''

	# LOAD MODULES
	import numpy as np
	import datetime
	from datetime import timedelta
	import os
	import glob
	import tqdm
	import pandas as pd
	import fnmatch
	import matplotlib.pyplot as plt
	import matplotlib.dates as mdates
	from matplotlib.dates import DateFormatter
	import pytz
	from dateutil import tz
	import imp
	import logging

	from GroundControl.AddJob import AddJob

	def main():
		ProgramDir = os.path.abspath(os.path.dirname(__file__))

		CronMetric_RecEff_func = imp.load_source('CronMetric_RecEff_func', os.path.join(ProgramDir, 'CronMetric_RecEff_func.py'))
		CronMetric_RecEff_config = imp.load_source('CronMetric_RecEff_config', os.path.join(ProgramDir, 'CronMetric_RecEff_config.py'))


		# ---- CREATE LOGGING SUBSTRUCTURE
		log_path = os.path.join(ProgramDir, 'data', 'c-log/')
		if os.path.exists(log_path):
			pass
		else:
			os.makedirs(log_path)
		# --- INITIATE DETECTOR LOGGER
		clog_CronMetrics_RecEff = logging.getLogger(__name__)
		clog_CronMetrics_RecEff.setLevel(logging.INFO)
		file_handler = logging.FileHandler(log_path+'CronMetrics_RecEff.log')
		formatter    = logging.Formatter('%(asctime)s %(message)s',"%Y-%m-%d %H:%M:%S")
		file_handler.setFormatter(formatter)
		clog_CronMetrics_RecEff.addHandler(file_handler)
		clog_CronMetrics_RecEff.propagate = False
		# ----
		clog_CronMetrics_RecEff.info(' '+'HYDRA / CRONMETRICS - SPLtimeline now active')
		clog_CronMetrics_RecEff.info(' '+'version: 2022 -beta')
		clog_CronMetrics_RecEff.info(' '+'executed from: %s'%ProgramDir)
		# ----
		clog_CronMetrics_RecEff.info(' '+'On unit: {}'.format(CronMetric_RecEff_config.hid_val))
		clog_CronMetrics_RecEff.info(' '+'Monitoring period: {} - {}'.format(CronMetric_RecEff_config.dt_lookback, CronMetric_RecEff_config.dt_forcequit))
		clog_CronMetrics_RecEff.info(' '+'Exec interval: {}'.format(CronMetric_RecEff_config.interval_val) )
		clog_CronMetrics_RecEff.info(' '+'RootDir p-log: {}'.format(CronMetric_RecEff_config.RootPath_plog) )
		clog_CronMetrics_RecEff.info(' '+'Template p-log: {}'.format(CronMetric_RecEff_config.fname_template_plog) )
		# ----

		# ------------------ GroundControl Execution
		print('Scheduling job...')
		#Declare job parameters
		job_name = 'CronMetric_RecEff_v2'
		mod_path = os.path.join(ProgramDir, 'CronMetric_RecEff_func.py')
		mod_name = 'CronMetrics_RecEff_exec'
		exec_args = log_path+'CronMetrics_RecEff.log'
		cron_time = ['*/1','*','*','*','*']
		
		addJob = AddJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time).commit()


	if __name__ == "__main__":
		main()

## Modify a Job
A job can be modified in two ways: (1) using the job ID, or (2) using the job name. GroundControl and NDScheduler do not require job names to be unique. There can be two or more jobs with the same name. It is recommended that the user ensure each job have a unique name, but this is not enforced in NDScheduler. 

It is likely easiest to modify a job using the Web UI, but it can be done in Python.

Import the UpdateJob fuction

	from GroundControl.UpdateJob import UpdateJob

### Using the Job ID
Job ID can be used to update any of the job parameters including the job name. The job ID can be found easist using the Web UI.

Create the modified job.  
	
	#example of job id
	job_ID = '92259991d0d14cc4a3f2b38383f60b70'

	job_name = 'CronMetric_NewName' #new name
	mod_path = os.path.join(ProgramDir, 'CronMetric_RecEff_func.py')
	mod_name = 'CronMetrics_RecEff_exec'
	exec_args = log_path+'CronMetrics_RecEff.log'
	cron_time = ['*/1','*','*','*','*']

	#be sure to add the job_id to the new job
	job_to_update = UpdateJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time,job_id=job_ID)

Update the job on the server with commit(new_name=True)

	job_to_update.commit(new_name=True)

In one line:
 
	job_to_update = UpdateJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time,job_id=job_ID).commit(new_name=True)

### Using the Job Name
Job ID is not required to update a job using the job name. Becuase job names do not have to be unique this could raise an error if more than one job has the same name.

Create the modified job
	
	job_name = 'CronMetric_RecEff_v2' 
	mod_path = os.path.join(ProgramDir, 'CronMetric_RecEff_func.py')
	mod_name = 'CronMetrics_RecEff_exec'
	exec_args = log_path+'RecEff_NewFile.log' #new arguments
	cron_time = ['0','*/1','*','*','*'] #new arguments

	job_to_update = UpdateJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time)

Update the job on the server with commit(), which searches for the job ID using the job name. 

	job_to_update.commit()

In one line:
 
	job_to_update = UpdateJob(job_name,mod_path,mod_name,exec_args,cron_time=cron_time).commit()

If more than one job have the same name it will throw an error.

	FAILED! UpdateJob.update_job(): Job name is not unique (Test3 Job). Use job ID.


## Remove a Job
Removing a job using the Python functions requires the job ID, which is easiest found using the Web UI.

	#import JobHandler
	from GroundControl.JobHandler import JobHandler

	#example of job id
	job_ID = '92259991d0d14cc4a3f2b38383f60b70'
	
	#create Job Handler object then remove job using id
	handler = JobHandler()
	handler.remove_job(job_ID)

	#or in a single line
	JobHandler().remove_job(job_ID)

## Pause a Job
This is not implemeted in Python. See the [Web UI Pause a Job](tutorials.md#pause-a-job).