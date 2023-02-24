# Introduction

[SchedulerSS](index.md) can be broken down into four components: the [job](introduction.md#job), the [job handler](introduction.md#job-handler), the [server](introduction.md#server), and the [web-based user interface](introduction.md#web-based-user-interface). 

## Job

There is one type of SchedulerSS job, which runs a function within a Python script at the user-defined time, which is based on cron-system time. It was developed with SoundSpace Analytics' current program implementation in mind, which includes three Python scripts: (i) configuration, (ii) functions, and (iii) executable. 

The user-defined time for a scheduled job is accepted as cron expression (e.g. every minute as a cron expression would be '*/1'). SchedulerSS accepts cron expressions for month, day of the week, day, hour, minute. For more information on cron expressions try these links:   
    
+ [Understanding Cron Syntax in the Job Scheduler](https://www.netiq.com/documentation/cloud-manager-2-5/ncm-reference/data/bexyssf.html)
+ [crontab guru](https://crontab.guru/)

## Job Handler

SchedulerSS contains a Python library customized for SoundSpace Analytics that encases NDScheduler's job and server manager classes and utilizes REST API to manage the scheduled jobs (e.g. add, remove, or modify jobs). 

## Server
SchedulerSS requires a Tornado server to be continuously running. Picture it as the job manager that takes in the user commands (e.g. add, update, pause, or delete jobs), runs and records the status of all scheduled jobs(e.g. success, failure, running, and errors), handles all the background processes needed for running and managing these jobs, and gathers and shares this content on web-based user interface. A job cannot run without the server, but the server can run when there are no jobs scheduled. 

### Datastore
A relational database is requried for the server to run, which stores the information being passed to and from SchedulerSS. This includes information on each job scheduled, its execution history, and modification history. 

The database is stored in the same location as SchedulerSS as *database.db*. If it is moved, renamed, or deleted, the server and scheduled jobs will fail. 

## Web-based User Interface
SchedulerSS web-based user interface contains three pages for Jobs, Executions, and Audit logs. Each of these pages is linked to the server's database, allowing the user to display, filter, and manipulate the stored information. 

The default web-based user interface is: [http://localhost:8888](http://localhost:8888)

