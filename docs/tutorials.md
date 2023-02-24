# Web-based User Interface
SchedulerSS web UI format is identical to [NDScheduler](https://github.com/Nextdoor/ndscheduler) with three tabs: [Jobs](tutorials.md#job-handling), [Executions](tutorials.md#executions), and [Audit Logs](tutorials.md#audit-logs). 

# Job Handling
All job handling is done under the Jobs tab, which lists all scheduled jobs, their schedule, next run action, and will indicate if a job is paused (inactive). Once a job has been added, it will be listed under the Jobs tab.

If there are any errors while handling jobs using the web UI they will either appears in [Executions](tutorials.md#executions), or immediately as a red box at the top of the web browser.
## Add a Job
Click the New Job button, fill in the form, and click the Add button.

+ **Job Name:** It is recommended that this be unique for each job

+ **Job Class:** There is only one option for job class. It should read: 

        schedulerss.jobs.SoundSpaceJob.SoundSpaceJob

+ **Arguments:** Arguments must be formatted as a list of strings with double quotes (" "). Single quotes are not accepted. Full absolue paths to to the Python function script are recommended (not relative paths). For example:
    
        ["/path/to/CronMetric_RecEff_func.py","CronMetric_RecEff_exec","/path/to/CronMetrics_RecEff.log"]

+ **Scheduling:** Modify as desired. See [cron time expressions](job-handler.md#cron-time-expressions) for more information.

## Modify a Job
Click on the job name to modify its parameters, which are the same as the parameters desribed above, then click Modify.

## Remove a Job
Click on the job name then click Delete. 

*Note: Deleting a job stops future scheduled runs from occurring. If a job is currently running it will run to completion. That is, removing a job does NOT force stop a job that is currently running.*

## Pause a Job
Click on the job name then click Active at the bottom of the form. This will render the job Inactive, which stops future scheduled runs from occurring. If a job is currently running it will run to completion.

Jobs can be toggled back on by clicking Inactive.

# Executions
The Executions tab lists the job name, status (e.g. Scheduled, Running, Success, Scheduled Error, Failed), Scheduled time, Last updated time, and Description. If there are any errors in job execution, they will appear to the right of the Description. Click on the report button to see the errors. They will appear as they would in the command prompt.

# Audit Logs
Any job modifications are added to the audit logs which are displayed here.