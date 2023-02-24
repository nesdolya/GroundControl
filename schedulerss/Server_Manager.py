

import os, subprocess, sys
import logging
from datetime import datetime
from tinyscript import *
from tinyscript.helpers import ts

logger = logging.getLogger(__name__)

PORT = 8888

def main():
	global PORT
	STATIC_PATH   = "../static"

	sparsers = parser.add_subparsers(dest="command", help="command to be executed")
    # run & clear command arguments
	run = sparsers.add_parser("run", help="Run the server")
	run.add_argument("-p", "--port", type=ts.port_number, default=8888, help="Server's port number (default is 8888)")
	run.add_argument("--debug", action="store_true", default=False, help="run the server in debug mode")
	clear = sparsers.add_parser("clear", help="Clear server of all job history. CAUTION: Removes all scheduled jobs")
	
	initialize(noargs_action='help')
	args.static_path = STATIC_PATH
	
	if args.command == 'run':
		logger.info('Installing required packages...')
		os.environ["NDSCHEDULER_SETTINGS_MODULE"]='schedulerss.soundspace_settings'
		#os.environ["DISABLE_SQLALCHEMY_CEXT"]='1'
		#subprocess.check_call([sys.executable, "-m", "pip", "install", "SQLAlchemy==1.4.41"])
		from ndscheduler.server.server import SchedulerServer as SoundSpaceServer
		from ndscheduler import settings
		#settings.JOB_CLASS_PACKAGES = ['schedulerss.jobs']
		settings.HTTP_PORT = args.port
		settings.DEBUG = args.debug
		PORT = args.port
		logger.info(f'Running SoundSpace Local Server: http://localhost:{PORT}...')
		SoundSpaceServer.run()

	elif args.command ==  "clear":
		# move the SQLite datastore DB to graveyard
		archive = os.path.join(os.getcwd(),'archive')
		if not os.path.exists(archive):
			os.makedirs(archive)
		
		f = os.path.join(os.getcwd(),'datastore.db')
		if os.path.isfile(f):
			timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%S')
			db_archive = os.path.join(archive,f'datastore{timestamp}.db')
			os.rename(f,db_archive)
			logger.info(f'Archived datastore to {db_archive}')
		

if __name__ == "__main__":
	main()
