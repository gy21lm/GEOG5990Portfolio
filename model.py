# Import modules.
import random
import operator 
import matplotlib.pyplot

# Set up agents.
num_of_agents = 10 
agents = []

# Make the agents (random y and x values). 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

print(agents)

# Move the agents.
for i in range(num_of_agents):
    
    #Move one step in y direction.
    if random.random() < 0.5:
        agents[i][0] += 1
    else:
        agents[i][0] -= 1
    
    # Move one step in x direction.
    if random.random() < 0.5:
        agents[i][1] += 1 
    else:
        agents[i][1] -= 1

print(agents)


'''# Work out pythagorian distance between two points. 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5

#Print answer.
print(answer)'''

# Print agent with the max y value.
print(max(agents))

# Print agent with the max x value.
print(max(agents, key=operator.itemgetter(1)))

# Matplotlib 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
# Colour the most easterly agent red. 
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
# Plot data. 
matplotlib.pyplot.show()
