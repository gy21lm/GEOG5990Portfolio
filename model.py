# Import modules.
import random
import operator 
import matplotlib.pyplot

# Set up agents.
num_of_agents = 10
num_of_iterations = 100 
agents = []

# Make the agents (random y and x values). 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

print(agents)

# Move the agents.
for i in range(num_of_agents):
    
    for j in range(num_of_iterations):
    
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

'''
# Work out pythagorian distance between two points. 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5

#Print answer.
print(answer)
'''

# Print agent with the max y value.
print(max(agents))

# Print agent with the max x value.
print(max(agents, key=operator.itemgetter(1)))

# Set axes limits and plot agents. 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
# Colour the most easterly agent red. 
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
# Display all open figures. 
matplotlib.pyplot.show()