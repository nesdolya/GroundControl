# Running GroundControl
GroundControl requires a server to be running before any jobs can be scheduled. Only on instance of the server needs to be running. Jobs are managed after the server is running. 

There is no configuration neccesary (See [Configuration](running-groundcontrol.md#configuration) for more information).

# Server Management
The [server](introduction.md#server) runs using the command prompt (terminal). This window must always stay open. **Closing the terminal, or stopping GroundControl using Ctrl+C will stop all scheduled jobs from running.** Jobs scheduled in the future will continue to run as expected once the server has be started again. Jobs that were running when the server stopped will not be completed.

## Start the Server
Open a command prompt, activate the virtual environment and start the server with the following command:

    python -m groundcontrol.Server_Manager run

Open the web-based user interface using the localhost URL. GroundControl defaults to: [http://localhost:8888](http://localhost:8888) 

The HTTP_PORT can be updated by using the -p or --port argument.

    python -m groundcontrol.Server_Manager run -p 7777

Debugging for NDScheduler is automatically turned off. It can be turned on using the --debug argument if required.

    python -m groundcontrol.Server_Manager run -p 7777 --debug

## Stop the Server
In the terminal where GroundControl server is running type Ctrl+C or close the terminal window.

Stopping the server may be valuable when performing system updates, stopping a job that is currently running (i.e. force stopping a job), or restarting the server during debugging.

## Clear the Datastore
It may be valuable to clear the [datastore](introduction.md#datastore) during beta testing, and inialization of GroundControl, or if the datastore is growing too large, due to numerous jobs running hourly/daily. If the datastore gets too large it may impact performance of the web-based user interface, such as filtering executions by date range. Clearing the datastore will remove all scheduled jobs from GroundControl along with their execution and modification history. Clearing the datastore does not permanently delete these data, instead it is archived to datastorage.

To clear the datastore [stop the server](running-groundcontrol.md#stop-the-server), then type the following into the terminal:

    python -m groundcontrol.Server_Manager clear

# Job Management
Once the server is running, basic job scheduling functions can be approached using the customized [Job Scheduler Functions](job-handler.md) or through the [web-based user interface](tutorials.md). 

To ensure that a job runs smoothly install any Python libraries that are required by the Python functions to the same virtual environment where GroundControl is installed (i.e. the virtual environment used to run the server).

There are certain job handling functions that can only be used in the web-based user interface (Web UI).

Job Scheduling Function | Python  | Web UI
-----------: |:-------------:| :-----------:
Add Job | &#10004;| &#10004;
Pause Job (Inactive) | &#10006;| &#10004;
Modify Job | &#10004; | &#10004;
Remove Job | &#10006; | &#10004;

*Note: Remove Job is not part of the basic job scheduling functions, but had been implemented as additional functionality.*

Additional functionalities are described in [Python API Reference](python-modules.md). 

# Configuration
No configuration is required for GroundControl. Instead Server_Manager accepts arguments for HTTP_PORT and DEBUG and automatically sets all required [NDScheduler settings](https://github.com/Nextdoor/ndscheduler/blob/d31016aaca480e38a69d75a66a9978a937c6a0b0/ndscheduler/default_settings.py). 

The HTTP port default is 8888, and the web-based user interface can be accessed using this URL: [http://localhost:8888](http://localhost:8888)

**Do not change JOB_CLASS_PACKAGES**

Contact Andrea Nesdoly (<andreanesdoly@gmail.com>) for instruction on how to update settings other than HTTP_PORT. 