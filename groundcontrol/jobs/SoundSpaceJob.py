"""A job to run executable programs."""

import os, sys
import imp
import logging

from ndscheduler.corescheduler import job
logger = logging.getLogger(__name__)

class SoundSpaceJob(job.JobBase):

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': ('This will run an executable program. You can specify as many '
                      'arguments as you want. This job will pass these arguments to the '
                      'program in order.'),
            'arguments': [
                {'type': 'string', 'description': 'Module path with extension'},
                {'type': 'string', 'description': 'Module name'},
                {'type': 'string', 'description': 'Additional arguments'}
            ],
            'example_arguments': '["/path/to/module.py", "function_name", [parameters] (optional)]'
        }

    def run(self, mod_path, mod_name, add_params=[], *args, **kwargs):
        basename = os.path.basename(mod_path).replace('.py','')
        try:
            funct = imp.load_source(basename, mod_path)
            logger.info(f'Running function {funct}\t with parameters {add_params}')
            if add_params != []:
                getattr(funct, f'{mod_name}')(add_params)
            else:
                getattr(funct, f'{mod_name}')
        except ValueError as e:
            raise ValueError(f'\n\n******** !FAILED TO EXECUTE JOB! *******\nError in parameters passed: {e}\nRunning: {funct} \t {mod_name} \t {add_params}\n*****************\n')

