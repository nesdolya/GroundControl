# Web-based User Interface Simple Modifications
Simple modifications to the web-based UI can be made by editing the index.html for the site. This file is located within the python environment site-packages where GroundControl is installed. 

Anaconda typically stores virtual environments here: home/USERNAME/anaconda3/envs/ENV_NAME

You can print the list of virtual environments and their location by typing the following command into the command prompt (you may need to activate the environment first):

    conda info --envs

Open the file explorer and navigate to the virtual environment. Within the site-packages, find the groundcontrol folder, then the statis folder. It will typically be found here: home/USERNAME/anaconda3/envs/ENV_NAME/lib/pythonVERSION/site-packages/groundcontrol/static

Web-page colours, text, and the logo location can be edited within the index.html file within the static folder.
