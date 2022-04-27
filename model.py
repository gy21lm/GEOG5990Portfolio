# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:21:44 2022

@author: Lena
"""

# Import modules.
import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

# Read in data and create environment. 
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        
# Set up model parameters. 
num_of_agents = 10
num_of_iterations = 100
stopping_condition = 25000
neighbourhood = 20 

# Set up agents list. 
agents = []

# Set up figure size 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents. 
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, rowlist, agents))
    
carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on

    # Move the agents.
    for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    
    store = []
    for i in range(num_of_agents):
        store.append(agents[i].store)
    print(store)
 
    for i in range(len(store)):
        if all(store[i] > stopping_condition for store[i] in store):
            carry_on = False
    
    # Set axes limits and plot agents.
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.xlim(0, len(rowlist))
    matplotlib.pyplot.imshow(environment)       
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='white')
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 1, repeat=False, frames=gen_function)

matplotlib.pyplot.show()

'''
# Set axes limits and plot agents. 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
'''