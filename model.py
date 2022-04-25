# Import modules.
import random
import operator 
import matplotlib.pyplot

# Set up agent list. 
agents = []

# Set up random coordinates (y0 and x0) to be placed in list. 
agents.append([random.randint(0,99),random.randint(0,99)])

# Move y0 one step.
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
print(agents[0][0])

# Move x0 one step.
if random.random() < 0.5:
    agents[0][1] += 1 
else:
    agents[0][1] -= 1

print(agents[0][1])

print(agents)



# Set up second set of random coordinates (y1 and x1) to be placed in list. 
agents.append([random.randint(0,99),random.randint(0,99)])

# Move y1 one step.
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
print(agents[1][0])

# Move x1 one step. 
if random.random() < 0.5:
    agents[1][1] += 1 
else:
    agents[1][1] -= 1

print(agents[1][1])

print(agents)



# Work out pythagorian distance between two points. 
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5

#Print answer.
print(answer)

# Print max y value.
print(max(agents))

# Print max x value.
print(max(agents, key=operator.itemgetter(1)))

# Matplotlib 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()
