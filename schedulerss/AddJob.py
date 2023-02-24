

from schedulerss.JobInfo import JobInfo
from schedulerss.JobHandler import JobHandler

class AddJob(JobInfo,JobHandler):
    """
    A class used to add a new job to SchedulerSS server
    Inherits attributes from JobInfo and JobHandler
    """

    def commit(self):
        """Add job to SchedulerSS server"""
        jobJson = self.get_job_info()
        return self.add_job(jobJson)


    
