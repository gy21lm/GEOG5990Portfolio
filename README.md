# GEOG5990Porfolio
## INTRODUCTION
This project initiates an agent based model which:
* builds agents in a space
* allows them to interact with one another 
* reads in environmental data 
* gets agents to interact with the environment 
* displays the model as an animation 
* is contained within a GUI (Graphical User Interface)
* is initialised with data from the web 

## CONTENTS LIST  
* LICENCE.txt - licence for the project 
* model.py - python script which runs the model
* agentframework.py - python script which stores the information about the agents
* in.txt - a text file containing the values of the environment
* [agentframework.html](https://htmlpreview.github.io/?https://github.com/gy21lm/GEOG5990Portfolio/blob/main/agentframework.html) - documentation for agentframework.py

## HOW TO RUN 
Download model.py, agentframework.py and in.txt into the same directory.

Run model.py in order to get the GUI output in which an animation can be run showing how the agents move around and alter the environment as they move.

If model.py is run as it is (e.g. in an IDE (Spyder)), then default paramaters will be used to determine the number of agents, the number of iterations, the neighbourhood size and how many units all agents have to hold until the animation stops (the stopping condition).

The model paramaters can be changed without changing the source code defaults by running model.py in the command prompt as follows:
* python model.py num_of_agents num_of_iterations neighbourhood stopping_condition

All arguments in the above line should be integers. In the case that an integer wasn't passed or nothing was passed at all, then the model will run using the default parameters. 

## DEVELOPMENT ISSUES 
There are two known issues with model.py:
1. When the window containing the GUI is closed, the python script continues to run in the background (possibly due to tkinter.mainloop()?).
      * To circumvent this problem, the model can be stopped by clicking the 'Stop running model' button in the menu of the GUI. This initiates the tkinter quit function However it should be noted that whilst this was able to stop the model from continuing to run, it would also cause the window running the GUI to crash. 
2. When running the model.py, two windows will pop up instead of only one. Closing the Figure window before running the model in the GUI (Model) doesn't allow the animation to to be displayed within the GUI. Therefore, until the problem is fixed, keep both windows open to show the animation of the model in the GUI.

A third issue will materialise when changing the model parameters:

3. Some comibiations of model parameters will cause the animation to take a very large amount of time to complete. Future development of the code could look at also limiting the length of time the animation can take. 
