import os, subprocess, sys
import logging
from datetime import datetime
from tinyscript import *
from tinyscript.helpers import ts
from groundcontrol.JobInfo import JobInfo
from groundcontrol.JobHandler import JobHandler

logger = logging.getLogger(__name__)


class UpdateJob(JobInfo,JobHandler):
	"""
    A class used to update an existing job in GroundControl server
    Inherits attributes from JobInfo and JobHandler
    """
	def check_id(self):
		"""Check if the job ID exists"""
		if self.job_id in [j['job_id'] for j in JobHandler().get_jobs()]:
			return True
		else:
			return False


	def update_using_id(self):
		"""Check if the job ID exists"""
		if self.job_id == None:
			return False
		else:
			return self.check_id()


	def update_job_name(self):
		"""Update the job - using job id
        
        Returns
        -------
            dictionary: A dictionary of job's parameters
        
		Raises
        ------
		ValueError
			if job cannot be found
        """
		jobJson = self.get_job_info()
		if self.update_using_id():
			jid = self.job_id
			if self.check_id():
				logger.info(f'Updating job to {jobJson} using job id {jid}.')
				return self.modify_job(jid,jobJson)
			else:
				logger.info(f'FAILED! UpdateJob.update_job_name(): No job was found with job ID: {jid}')
				raise ValueError(f'FAILED! UpdateJob.update_job_name(): No job was found with job ID: {jid}')	
		else:
			logger.info(f'FAILED! UpdateJob.update_job_name(): Require job ID to update job name.')
			raise ValueError(f'FAILED! UpdateJob.update_job_name(): Require job ID to update job name.')	
			
	
	def update_job(self):
		"""Update the job - search for the job by name
        
        Returns
        -------
            dictionary: A dictionary of job's parameters
        
		Raises
        ------
		ValueError
			if job cannot be found
        """
		jobJson = self.get_job_info()
		if self.update_using_id():
			jid = self.job_id
			message = f'Updating job to {jobJson} using job id {jid}.'
		else:
			oldJob = JobHandler().get_job_by_name(self.job_name)
			if oldJob != None and len(oldJob)>1:
				logger.info(f'FAILED! UpdateJob.update_job(): Job name is not unique ({self.job_name}). Use job ID.')
				raise ValueError(f'FAILED! UpdateJob.update_job(): Job name is not unique ({self.job_name}). Use job ID.')	
			else:
				jid = oldJob[0]['job_id']
				message = f'Updating job to {jobJson} using job name {self.job_name}.'
			
		if jid in [j['job_id'] for j in JobHandler().get_jobs()]:
			logger.info(message)
			return self.modify_job(jid,jobJson)
		else:
			logger.info(f'FAILED! UpdateJob.update_job(): No job was found with job ID: {jid}')
			raise ValueError(f'FAILED! UpdateJob.update_job(): No job was found with job ID: {jid}')		

	
	def commit(self,new_name=False):
		"""Update the job in GroundControl server - explicitly state when updating the job name
		        
        Parameters
        ----------
        new_name : bool 
            explicitly state when updating the job name
        
        Returns
        -------
            dictionary: A dictionary of job's parameters
        """
		if new_name:
			self.update_job_name()
		else:
			self.update_job()
			
			
		
		
