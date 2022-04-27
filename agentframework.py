# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:56:22 2022

@author: Lena
"""


import random

class Agent():
    def __init__(self, environment, agents):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment 
        self.store = 0
        self.agents = agents
        
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
    
    def move(self):
        #Move one step in y direction.
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        
        # Move one step in x direction.
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 