

from groundcontrol.JobInfo import JobInfo
from groundcontrol.JobHandler import JobHandler

class AddJob(JobInfo,JobHandler):
    """
    A class used to add a new job to GroundControl server
    Inherits attributes from JobInfo and JobHandler
    """

    def commit(self):
        """Add job to GroundControl Server
        Calls .add_job() in JobHandler
		        
        Returns:
            jobInfo (dictonary): A dictionary of the added job's parameters
        """
        jobJson = self.get_job_info()
        return self.add_job(jobJson)


    
