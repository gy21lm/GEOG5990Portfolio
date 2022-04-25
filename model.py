import random

# Set up y0 and x0 variables.
y0 = 50
x0 = 50

# Move y0 one step.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
print(y0)

# Move x0 one step.
if random.random() < 0.5:
    x0 += 1 
else:
    x0 -= 1

print(x0)




# Set up y1 and x1 variables.
y1 = 50
x1 = 50

# Move y1 one step.
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
print(y1)

# Move x1 one step. 
if random.random() < 0.5:
    x1 += 1 
else:
    x1 -= 1

print(x1)

# Work out pythagorian distance between two points. 
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5

#Print answer.
print(answer) 
