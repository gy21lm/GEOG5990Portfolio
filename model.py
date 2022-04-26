# Import modules.
import random
import operator 
import matplotlib.pyplot

# Calculate distance between a pair of agents (fucntion declaration)
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
    return (((agents_row_a[0] - agents_row_b[0])**2) 
            + ((agents_row_a[1] - agents_row_b[1])**2))**0.5


# Set up agents.
num_of_agents = 10
num_of_iterations = 100 
agents = []

# Make the agents (random y and x values). 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

print(agents)

# Move the agents.
for j in range(num_of_iterations):

    for i in range(num_of_agents):
       
        #Move one step in y direction.
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        
        # Move one step in x direction.
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

print(agents)

# Print agent with the max y value.
print(max(agents))

# Print agent with the max x value.
print(max(agents, key=operator.itemgetter(1)))

# Set axes limits and plot agents. 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

#Calculate distance between all agents 
distance = []
for agents_row_a in agents:
    for agents_row_b in agents:
        # Optimising search
        if agents_row_a > agents_row_b: 
            distance.append(distance_between(agents_row_a, agents_row_b))
            
# Min and max distance between agents 
print(max(distance))
print(min(distance))

# Check the search has been optimised correctly.
print(len(distance))