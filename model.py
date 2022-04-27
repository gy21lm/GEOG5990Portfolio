# Import modules.
import random
import matplotlib.pyplot
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
neighbourhood = 20 

# Set up agents list. 
agents = []

# Make the agents. 
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Set axes limits and plot agents. 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()