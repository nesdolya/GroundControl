# Troubleshooting

# Modifying Python Function
Edits to the SoundSpace Python function can be made without impacting SchedulerSS as long as there are not changes to the name of the Python script and function, nor the path to the Python script. The updated version of the Python function will be used for the next scheduled run. If there are changes to the function name, location, or required arguments the job will need to be modified before the next scheduled run. (See [Web UI Modifying a Job](tutorials.md#modify-a-job), or [Python Modifying a Job](job-handler.md#modify-a-job))

# Force Stopping a Running Job (Python Script)
[Stop the server](running-schedulerss.md#stop-the-server) using Ctrl+C or by closing the terminal window to force stop a Python script (i.e. job) from completing its execution. When the server is started again the job will still be scheduled to run in the future, it is recommended to [pause the job](tutorials.md#pause-a-job) or [remove the job](tutorials.md#remove-a-job) until it is ready to be executed once more.

# JSON serializable
SoundSpace Analytic's functions that were provided for development were passed a Python logging object, but the job scheduler cannot handle passing objects - only strings. Therefore, the functions being executed need to updated to accept strings for the path to the logging file, then re-open the logging file and append to it. The below example is from the CronMetric_RecEff_func.py


    """Edits By ADN
    Logger object could not be serialized for web use. Can only pass a string
    """
    # WITHOUT DAILY SPL
    #def CronMetrics_RecEff_exec(clog_CronMetrics_RecEff):
    def CronMetrics_RecEff_exec(logger_path):
        '''
        '''
        # --- INITIATE DETECTOR LOGGER
        clog_CronMetrics_RecEff = logging.getLogger(logger_path)
        clog_CronMetrics_RecEff.setLevel(logging.INFO)
        file_handler = logging.FileHandler(logger_path,mode='a')
        formatter    = logging.Formatter('%(asctime)s %(message)s',"%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        clog_CronMetrics_RecEff.addHandler(file_handler)
        clog_CronMetrics_RecEff.propagate = False
        """End Edits by ADN"""

        dt_now = datetime.datetime.utcnow()
        dt_stop = min(dt_now, CronMetric_RecEff_config.dt_forcequit) - pd.DateOffset(days=0)
        # --- grab all plog files
        df_plog = cct_rootPath_sources(rootPath_source = CronMetric_RecEff_config.RootPath_plog, fname_template = CronMetric_RecEff_config.fname_template_plog)
        ...

