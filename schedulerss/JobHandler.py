
from tinyscript import *
import requests, os
from schedulerss import Server_Manager as ss
logger = logging.getLogger(__name__)

class JobHandler:
    """
    The JobHandler implements REST API for adding and manipulating jobs. It requires SchedulerSS.Server_Manager to be running to get the HTTP_PORT being used.

    Attributes:
        job_url (URL): the URL used to access the SchedulerSS server
        
    """
    def __init__(self):
        self._job_url = f'http://localhost:{ss.PORT}/api/v1/jobs'
        super().__init__()
    
    @property
    def job_url(self):
        return self._job_url
    
    def get_jobs(self):
        """Gets a list of all scheduled jobs.
        
        Returns:
            jobs (list): list of jobs in JSON format
        """
        try:
            jobs_response = requests.get(self.job_url)
            if jobs_response.ok:
                jobs = jobs_response.json()
                logger.info(f'Jobs returned: {jobs}')
                return jobs['jobs']
            else:
                logger.error(f'FAILED! JobHandler.get_jobs(*): {jobs_response.status_code}')
                jobs_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f'FAILED! JobHandler.get_jobs(*): {e}')
            raise SystemExit(e)
    
    def get_job(self,jid):
        """Gets a specific job from all scheduled jobs.
        
        Attributes:
            jid (string): The job's unique identifier
        
        Returns:
            jobInfo (dictonary): A dictionary of the requested job parameters
        """
        getJob = self.job_url+'/'+str(jid)
        try:
            job_response = requests.get(getJob)
            logger.info(f'Get response status code:\n {job_response.status_code}')
            if job_response.ok:
                jobInfo = job_response.json()
                logger.info(f'Jobs returned: {jobInfo}')
                return jobInfo
            else:
                logger.error(f'FAILED!  JobHandler.get_job(*): {job_response.status_code}')
                job_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f'FAILED! JobHandler.get_job(*): {e}')
            raise SystemExit(e)

    def add_job(self,jobJson):
        """Adds a job to be scheduled.
        
        Attributes:
            jobJson (dictonary): the job in JSON format to be added
        
        Returns:
            jobInfo (dictonary): A dictionary of the added job's parameters
        """
        newJobInfo = jobJson
        try:
            job_response = requests.post(self.job_url,json=newJobInfo)
            if job_response.ok:
                jobInfo = job_response.json()
                logger.info(f'Job added: {jobInfo}')
                return jobInfo
            else:
                logger.error(f'FAILED!  JobHandler.add_job(*): {job_response.status_code}')
                job_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f'FAILED! JobHandler.add_job(*): {e}')
            raise SystemExit(e)

    
    def remove_job(self,jid):
        """Removes a job from the scheduler.
        
        Attributes:
            jid (string): The job's unique identifier
        
        Returns:
            jobInfo (dictonary): A dictionary of the deleted job parameters
        """
        removeJob = self.job_url+'/'+str(jid)
        try:
            job_response = requests.delete(removeJob)
            if job_response.ok:
                jobInfo = job_response.json()
                logger.info(f'Job Removed: {jobInfo}')
                return jobInfo
            else:
                logger.error(f'FAILED! JobHandler.remove_job(*): {job_response.status_code}')
                job_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f'FAILED! JobHandler.remove_job(*): {e}')
            raise SystemExit(e)


    def modify_job(self,jid,jobJson):
        """Modifies and existing scheduled job.
        
        Attributes:
            jid (string): The job's unique identifier
            jobJson (dictonary): the job in JSON format to be added
        
        Returns:
            jobInfo (dictonary): A dictionary of the deleted job parameters
        """
        updatedJobInfo = jobJson
        modJob = self.job_url+'/'+str(jid)
        try:
            job_response = requests.put(modJob,json=updatedJobInfo)
            if job_response.ok:
                jobInfo = job_response.json()
                logger.info(f'Job Modified: {jobInfo}')
                return jobInfo
            else:
                logger.error(f'FAILED! JobHandler.modify_job(*): {job_response.status_code}')
                job_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f'FAILED! JobHandler.modify_job(*): {e}')
            raise SystemExit(e)
            

    def get_job_by_name(self,jobName):
        """Gets a job based on its name.
        
        Attributes:
            jobName (string): job name to find
            
        Returns:
            jobInfo (dictonary): A dictionary of the deleted job parameters
        """
        allJobs = self.get_jobs()
        jobList = []
        for job in allJobs:
            if job['name'] == jobName:
                logger.info(f'Job found with name {jobName}: {job}')
                jobList.append(job)
        if len(jobList)>0:
            logger.info(f'Jobs found: {jobList}')
            return jobList
        else:
            logger.error(f'No job found with name: {jobName}')
            raise ValueError(f'FAILED! JobHandler.get_job_by_name(*) - No job found with name: {jobName}')
        
            

    
	
	
