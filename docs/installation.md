# Installation

Download the latest version of GroundControl as a .tar.gz file.

Create a virtual environment using Python version >= 3.8.0 and < 3.10 (See [MAC Mini Installation Errors](installation.md#mac-mini-installation-errors)). This can be don in Anaconda or through Python virtenv.

Install GroundControl with one of the pip commands below. Anaconda does not handle .tar.gz files. 

    python -m pip install GroundControl-0.1.3.tar.gz

or

    pip install GroundControl-0.1.3.tar.gz

This installation includes the customized version of NDSceduler for SoundSpace Analytics. 

## MAC Mini Installation Errors

### Error: module 'collections' has no attribute 'mutablemapping'
This error is related to NDScheduler, Tornado 5.1.1 and Python 3.8.10 version requirements. NDScheduler requires an older version of Tornado to work. Tornado 5.1.1 is the most recent version that works with NDScheduler. Tornado 5.1.1 is not compatible with Python 3.10, which was used to create the SSP3 virtual environment on the MAC mini tested. 

The current workaround is the use a Python 3.8.10 environment to run GroundControl. 

### ImportError: Failed to find libmagic
Uninstall python-magic and possibley python-magic-bin:
    
    pip uninstall python-magic
    pip uninstall python-magic-bin

Re-install:
    
    pip install python-magic-bin==0.4.14