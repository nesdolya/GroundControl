"""Settings to override default settings."""

import logging, os

# Change port from default
#HTTP_PORT = 8888

# Do not change
JOB_CLASS_PACKAGES = ['schedulerss.jobs']

'''For debugging'''
DEBUG = False
logging.getLogger().setLevel(logging.WARNING)

