"""Settings to override default settings."""

import logging, os

# Change port from default
#HTTP_PORT = 8888

#
# Static Assets
#
# The web UI is a single page app. All javascripts/css files should be in STATIC_DIR_PATH
#
STATIC_DIR_PATH = STATIC_DIR_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
TEMPLATE_DIR_PATH = STATIC_DIR_PATH
APP_INDEX_PAGE = 'index.html'

# Do not change
JOB_CLASS_PACKAGES = ['groundcontrol.jobs']

'''For debugging'''
DEBUG = False
logging.getLogger().setLevel(logging.WARNING)

