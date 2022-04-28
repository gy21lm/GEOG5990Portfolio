# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:21:44 2022

@author: Lena
"""

# Import modules.
import random
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import requests
import bs4
import sys 

# Scraping a web page in order to get x and y values for the agents. 
page = requests.get("https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html")
content = page.text 
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


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
default_num_of_agents = 10
default_num_of_iterations = 100
default_neighbourhood = 20
default_stopping_condition = 5000

try:
    num_of_agents = int(sys.argv[1])
except ValueError:
    num_of_agents = default_num_of_agents
except Exception: 
    num_of_agents = default_num_of_agents
finally:
    if num_of_agents == None: num_of_agents = default_num_of_agents
print("Number of Agents:", num_of_agents)
    
try:
    num_of_iterations = int(sys.argv[2])
except ValueError:
    num_of_iterations = default_num_of_iterations
except Exception: 
    num_of_iterations = default_num_of_iterations
finally:
    if num_of_iterations == None: num_of_iterations = default_num_of_iterations
print("Number of Iterations:", num_of_iterations)

try:
    neighbourhood = int(sys.argv[3])
except ValueError:
    neighbourhood = default_neighbourhood
except Exception: 
    neighbourhood = default_neighbourhood
finally:
    if neighbourhood == None: neighbourhood = default_neighbourhood
print("Neighbourhood Size:", neighbourhood)
    
try:
    stopping_condition = int(sys.argv[4])
except ValueError:
    stopping_condition = default_stopping_condition
except Exception: 
    stopping_condition = default_stopping_condition
finally:
    if stopping_condition == None: stopping_condition = default_stopping_condition
print("Stopping Condition:", stopping_condition)

# Set up agents list. 
agents = []

# Set up figure size 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents. 
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, rowlist, agents, y, x))
    
carry_on = True

def update(frame_number):
    """Updates the animation with a new frame."""
    
    fig.clear()
    global carry_on

    # Run the agents' functions. 
    for j in range(num_of_iterations):
        random.shuffle(agents)
        # Attempt to model agent being able to move and (and therefore eat) 
        # more when it has less units stored inside itself. 
        for i in range(num_of_agents):
            if agents[i].store <= stopping_condition/2:
                agents[i].move(5)
            elif (stopping_condition*3)/4 > agents[i].store > stopping_condition/2:
                agents[i].move(3)
            else:
                agents[i].move(1)
            agents[i].share_with_neighbours(neighbourhood)
    
    # Set up a list contatining the values of the agents' stores in order to
    # determine when to stop running the animation. 
    store = []
    for i in range(num_of_agents):
        store.append(agents[i].store)
 
    # Animation will stop running when all agents have a value stored within 
    # them that is larger than the stopping_condition. 
    for i in range(len(store)):
        if all(store[i] > stopping_condition for store[i] in store):
            carry_on = False
    
    # Set axes limits and plot agents within the environment.
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.xlim(0, len(rowlist))
    matplotlib.pyplot.imshow(environment) 
              
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='white')
        
def gen_function():
    """Determines whether to keep running the animation"""
    a = 0
    global carry_on 
    while (carry_on) :
        yield a			
        a = a + 1
    
def run():
    """Runs the animation in the GUI"""
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 

# Initialise the window manager. 
root = tkinter.Tk() 
root.wm_title("Model")

# Insert some text into the window. 
label = tkinter.Label(root, text = "Run or quit the model using the menu bar").pack()

# Configure where animation will go. 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# Configure menu bar.
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Stop running model", command=root.quit)

# Displays window until manually closed. Runs an infinite loop in the backend. 
tkinter.mainloop()