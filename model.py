# Import modules.
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    '''Calculate the pythagorian distance between a pair of agents.
    
    Parameters
    ----------
    agents_row_a : two integers in a list
        Integer coordinates. 
    agents_row_b : two integers in a list
        Second integer coordinates.

    Returns
    -------
    float
        Pythagorian distance between first coordinate and second coordinate. 

    '''
    return (((agents_row_a.y - agents_row_b.y)**2) 
            + ((agents_row_a.x - agents_row_b.x)**2))**0.5

# Read in data and create environment. 
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Set up agents.
num_of_agents = 10
num_of_iterations = 100 
agents = []

# Make the agents. 
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):

    for i in range(num_of_agents):
       
        agents[i].move()

# Set axes limits and plot agents. 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#Calculate distance between all agents 
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)