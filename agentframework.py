# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:56:22 2022

@author: Lena
"""
import random

class Agent():
    """Provides methods for agents. 
    
    move -- agent moves in the y and x direction and 'eats' from new 
        environment its positioned on 
    eat -- agent 'eats' the environment it's positioned on
    share_with_neighbours -- agent shares its store with another agent if the 
        second agent is within its neighbourhood
    """
    def __init__(self, environment, rowlist, agents, y, x):
        """Initialises the object's attritbutes when an object is created from
        a class.

        Parameters
        ----------
        environment -- list
        rowlist -- list
        agents -- list
        y -- number
        x -- number 
        """
        self.environment = environment
        self.rowlist = rowlist
        self.store = 0
        self.agents = agents
        
        if (y == None):
            self._y = random.randint(0,len(environment))
        else:
            self._y = y 
            
        if (x == None):
            self._x = random.randint(0,len(rowlist))
        else:
            self._x = x 
    
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "I'm the 'y' property.")
    
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")
    
    def move(self, speed):
        """Moves the agent one step in the y and x direction, as well as 
        running the eat function as many times as determined by 'speed'.
        
        Parameters
        ----------
        speed -- integer
        """            
        for i in range(speed):    
            #Move one step in y direction.
            if random.random() < 0.5:
                self.y = (self.y + 1) % len(self.environment)
                self.eat()

            else:
                self.y = (self.y - 1) % len(self.environment)
                self.eat()
            
            # Move one step in x direction.
            if random.random() < 0.5:
                self.x = (self.x + 1) % len(self.rowlist)
                self.eat()

            else:
                self.x = (self.x - 1) % len(self.rowlist)
                self.eat()
            
    def eat(self):
        """Agent 'eats' 10 units, storing them within itself, and removing 
        them from the environment where the agent is positioned IF the 
        environment has a value larger than 10 at the position of the agent.
        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
    def share_with_neighbours(self, neighbourhood):
        """Agent shares its store if another agent is located within its
        neighbourhood.
        
        Store is shared by taking the sum of both agents' stores and 
        allocating each agent half of the sum. 

        Parameters
        ----------
        neighbourhood -- number 
            The distance from the agent defining the neighbourhood
        """
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
            
    def distance_between(self, agent):
        """Calculates the pythagorian distance between two agents. 

        Parameters
        ----------
        agent -- a list containing coordinate values 

        Returns
        -------
        floating-point number 
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 