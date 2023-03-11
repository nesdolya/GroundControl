
import os,json


CRON_LABELS = "minute","hour","month","day","day_of_week"
class JobInfo:
    """
    A class used to manage GroundControl jobs information

    Attributes:
        job_class (function path): GroundControl.jobs.SoundSpaceJob.SoundSpaceJob (do not change)
        funct_path (string): the path to the Python script to be run
        funct_name (string): the name of the Python function to be executed
        job_name (string): the name of the job
        funct_args (string): the arguments to be passed to the Python function
        minute (string): cron expression for minute (optional, default: '*')
        hour (string): cron expression for hour (optional, default: '*')
        month (string): cron expression for month (optional, default: '*')
        day (string): cron expression for day (optional, default: '*')
        day_of_week (string): cron expression for day_of_week (optional, default: '*')
        cron_time (string): cron expression for ["minute","hour","month","day","day_of_week"] in this order, if provided do not pass arguements for minute, hour, month, day, day_of_week (optional)
        json_path (path): output for writing json (optional, default: os.path.join(os.getcwd(),'SoundSpaceJobInfo.json'))
        job_id (string): the job id if known (typically used for updating jobs) (optional, default: None)
    
    """
    
    def __init__(self,job_name='',funct_path='',funct_name='',funct_args='',minute='*',hour='*',month='*',day='*',day_of_week='*',cron_time=[],job_id=None):
        self._job_class = 'groundcontrol.jobs.SoundSpaceJob.SoundSpaceJob'
        self._function_path = funct_path
        self._function_name = funct_name
        self._job_name = job_name
        self._exec_args = funct_args
        self._time_step = dict(zip(CRON_LABELS,cron_time)) if cron_time!=[] else dict(zip(CRON_LABELS, [minute,hour,month,day,day_of_week]))
        self._json_path = os.path.join(os.getcwd(),'SoundSpaceJobInfo.json')
        self._job_id = job_id
        super().__init__()
		
    @property
    def job_class(self):
        return self._job_class

    @property
    def function_path(self):
        return self._function_path
    
    @property
    def function_name(self):
        return self._function_name
    
    @property
    def job_name(self):
        return self._job_name
	
    @property
    def exec_args(self):
        return self._exec_args

    @property
    def json_path(self):
        return self._json_path

    @property
    def time_step(self):
        return self._time_step

    @property
    def job_id(self):
        return self._job_id

    def update_job_class(self,newJobClass):
        self._job_class = newJobClass

    def update_function_path(self,functionPath):
        self._function_path = functionPath
    
    def update_function_name(self,functionName):
        self._function_name = functionName
    
    def update_job_name(self,jobName):
        self._job_name = jobName
	
    def update_exec_args(self,execArgs):
        self._exec_args = execArgs

    def update_time_step(self,timeDict):
        for key in timeDict:
            self._time_step[key]=timeDict[key]

    def update_json_path(self,newJson):
        self._json_path = newJson

    def get_job_info(self):
        """Get the job info as dictionary
        
        Returns:
            job_info (dictionary): A dictionary of job parameters
        """
        return {"job_class_string":self.job_class,
                "name": self.job_name,
                "pub_args":[self.function_path,
                            self.function_name,
                            self.exec_args],
                "month": self.time_step["month"],
                "day_of_week":self.time_step["day_of_week"],
                "day":self.time_step["day"],
                "hour":self.time_step["hour"],
                "minute":self.time_step["minute"],
                }

    def save_to_json(self):
        """Save job info to json file."""
        filename = self._json_path
        listObj = self.get_job_info()
        
        if self.is_created():
            print(f'JSON already created. Deleting!')
            os.remove(filename)
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
