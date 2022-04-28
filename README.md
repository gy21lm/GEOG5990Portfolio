# GEOG5990Porfolio
## INTRODUCTION
This project initiates an agent based model which:
* builds agents in a space
* reads in environmental data 
* allows agents to interact with one another and the environment they're in   
* displays the model as an animation 
* is contained within a GUI (Graphical User Interface)
* is initialised with data from the web

The code has created a model containing agents that roam around within an environment, interacting both with each other and with the environment. To help conceptualise this, it could be imagine the agents are sheep roaming around in an environment, such as uneven amounts of grass. At each spot they move to, they 'eat' (store) a little bit of the grass and potentially share their store with any other sheep that are close to them (within their neighbourhood). The animation itself will run until all sheep hold a certain amount of grass (either the default amount or this value can be set via user input). 

## CONTENTS LIST  
* LICENCE.txt - licence for the project 
* model.py - python script which runs the model
* agentframework.py - python script which stores the information about the agents
* in.txt - a text file containing the values of the environment
* [agentframework.html](https://htmlpreview.github.io/?https://github.com/gy21lm/GEOG5990Portfolio/blob/main/agentframework.html) - documentation for agentframework.py

## HOW TO RUN 
Download model.py, agentframework.py and in.txt into the same directory.

Run model.py in order to get the GUI output in which an animation can be run showing how the agents move around and alter the environment as they move.
It is not necessary to run agentframework.py or read in.txt since model.py reads in the information it requires from both these files. 
in.txt is just a file containing values of a particular environment - it is possible to change the contents of this file and have the agents roam around in a different environment or use your own file for the environment (provided it is also called in.txt in order to be read into the model correctly and placed in the same directory that holds model.py and agentframework.py). 

If model.py is run within an IDE (e.g. Spyder) then default paramaters will be used to determine the number of agents, the number of iterations, the neighbourhood size and how many units all agents have to hold until the animation stops (the stopping condition).

The model paramaters can be changed without changing the source code defaults by running model.py in the command prompt as follows:
* python model.py num_of_agents num_of_iterations neighbourhood stopping_condition

All arguments in the above line should be integers. In the case that an integer wasn't passed or nothing was passed at all, then the model will run using the default parameters. The parameters that end up being used in the model will be printed to the screen for confirmation. 

## DEVELOPMENT ISSUES 
There are two known issues with model.py:
1. When the window containing the GUI is closed, the python script continues to run in the background (possibly due to tkinter.mainloop()?).
      * To circumvent this problem, the model can be stopped by clicking the 'Stop running model' button in the menu of the GUI. This initiates the tkinter quit function. However it should be noted that whilst this was able to stop the script from continuing to run, it would also cause the window running the GUI to crash. 
2. When running the model.py, two windows will pop up instead of only one. The Figure window is empty, however closing the Figure window before running the model in the GUI window (Model) doesn't allow the animation to to be displayed within the GUI. Therefore, until the problem is fixed, keep both windows open to show the animation of the model in the GUI.

A third issue will materialise when changing the model parameters:

3. Some combinations of model parameters will cause the animation to take a very large amount of time to complete. Future development of the code could look at also limiting the length of time the animation can take. 
