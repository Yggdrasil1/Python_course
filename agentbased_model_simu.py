# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:22:02 2018

@author: biostudent216
"""

import numpy as np
import math
import copy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Agent:

    def __init__(self,id,world_x_size,world_y_size):

        self.max_x = world_x_size
        self.max_y = world_y_size

        x_coordinate = np.random.randint(0, world_x_size)
        y_coordinate = np.random.randint(0, world_y_size)

        self.id = id
        self.history = []
        self.coordinate = (x_coordinate, y_coordinate)

        self.health = 0
        self.attack = 0
        self.defense = 0

        self.get_skills()

    def get_skills(self):

        for _ in range(15):
            skill = np.random.randint(1,4)
            if skill == 1:
                self.health += 1
            elif skill == 2:
                self.attack += 1
            else:
                self.defense += 1


    def move(self):
        """movement of the agents"""

        if self.health > 0:

            x_coordinate = self.coordinate[0]
            y_coordinate = self.coordinate[1]

            x_coordinate += np.random.randint(-1,2)
            if x_coordinate < 0:
                x_coordinate = self.max_x - 1
            if x_coordinate > self.max_x - 1:
                x_coordinate = 0


            y_coordinate += np.random.randint(-1,2)
            if y_coordinate < 0:
                y_coordinate = self.max_y - 1
            if y_coordinate > self.max_y - 1:
                y_coordinate = 0


            self.update_position(x_coordinate,y_coordinate)


    def update_position(self, x_coordinate, y_coordinate):

        """
        Update agent position
        """

        self.history.append(self.coordinate)
        self.coordinate = (x_coordinate, y_coordinate)

    def __repr__(self):
        return "id.{}".format(self.id)

    def __gt__(self, other):
        if self.id > other.id:
            return True
        else:
            return False

    def apply_dmg(self,damage):
        lifeloss = damage
        for _ in range(self.defense):

            if lifeloss == 1:
                continue
            else:
                if np.random.uniform(0,1) < 0.1:
                    lifeloss -= 1

        self.health -= lifeloss




class Welt:

    def __init__(self):

        self.x_dimension = 20
        self.y_dimension = 20

        self.agents = []
        for id in range(20):
            self.agents.append(Agent(id,self.x_dimension,self.y_dimension))

        self.map = {}
        self.update_world_map()

        self.last_survivor = False


    def update_world_map(self):

        """
        creates a map from a dictionary with coordinates as keys
        """

        for x_coordinate in range(self.x_dimension):
            for y_coordinate in range(self.y_dimension):
                key = (x_coordinate,y_coordinate)
                self.map[key] = ["--"]

        for agent in self.agents:

            if agent.health > 0:
                x_coordinate = agent.coordinate[0]
                y_coordinate = agent.coordinate[1]

                if self.map[(x_coordinate, y_coordinate)] == ["--"]:
                    self.map[(x_coordinate, y_coordinate)]=[]
                self.map[(x_coordinate,y_coordinate)].append(agent)


    def print_map(self):

        """
        representation of the world map
        """

        for row_map in range(self.y_dimension):
            print_string = ""
            for column_map in range(self.x_dimension):
                print_string += str(self.map[(column_map,row_map)])
            print(print_string)
            
    def new_move(self):
        
        """
        moves the agents
        """
        
        for agentx in self.agents:
            x_coordinate = agentx.coordinate[0]
            y_coordinate = agentx.coordinate[1]
            
            move_vector = self.find_movement(agentx)
            
            x_coordinate += move_vector[0]
            y_coordinate += move_vector[1]
            
            if x_coordinate < 0:
                x_coordinate = self.x_dimension - 1
            if x_coordinate > self.x_dimension - 1:
                x_coordinate = 0

            if y_coordinate < 0:
                y_coordinate = self.y_dimension - 1
            if y_coordinate > self.y_dimension - 1:
                y_coordinate = 0
                
            
            agentx.update_position(x_coordinate,y_coordinate)
            
            
    def find_movement(self,agentx):
        
        """
        finds the closest other agent
        if no agent in radius < = 3: random movement
        else: moves towards this agent 
        :returns: direction vector (tupel)        
        """
        
        min_dist = 100
        closest_agent = agentx        
        
        for agenty in self.agents:
            if agentx != agenty:
                dist = self.distance(agentx.coordinate, agenty.coordinate)
                if dist < min_dist:
                    closest_agent = agenty
                    min_dist = dist
        
        if min_dist < 3:            
            x_vec = 0
            y_vec = 0
            
            if closest_agent.coordinate[0] < agentx.coordinate[0]:
                x_vec = -1
            elif closest_agent.coordinate[0] == agentx.coordinate[0]:
                x_vec = 0
            else:
                x_vec = 1
                
                
            if closest_agent.coordinate[1] < agentx.coordinate[1]:
                y_vec = -1
            elif closest_agent.coordinate[1] == agentx.coordinate[1]:
                y_vec = 0
            else:
                y_vec = 1
                
        else:
            
            x_vec = np.random.randint(-1,2)            
            y_vec = np.random.randint(-1,2)
            
        movement_vector = (x_vec,y_vec)
        
        return movement_vector

        
    def distance(self,coordinate1,coordinate2):
        """
        calculates the euclidian distance between two coordinates
        :returns: distance (float)
        """

        delta_x = abs(coordinate1[0] - coordinate2[0])
        delta_y = abs(coordinate1[1] - coordinate2[1])

        distance = math.sqrt(delta_x**2 + delta_y**2)        
        
        return distance


    def fight(self,agent1,agent2):

        """
        Decides which agent wins the fight,
        applies the damage dealt to the loser
        """

        damage = 0
        if agent2.attack > agent1.attack:
            damage = math.ceil(agent2.attack / 3)
            if np.random.uniform(0,agent2.attack) > (agent1.attack / 2):
                agent1.apply_dmg(damage)
            else:
                agent2.apply_dmg(damage)

        elif agent1.attack > agent2.attack:
            damage = math.ceil(agent1.attack / 3)
            if np.random.uniform(0,agent1.attack) > (agent2.attack / 2):
                agent2.apply_dmg(damage)
            else:
                agent1.apply_dmg(damage)

        else:
            damage = agent1.attack / 2
            if np.random.uniform(0,1) > 0.5:
                agent1.apply_dmg(damage)
            else:
                agent2.apply_dmg(damage)




    def improved_fights(self):

        """
        Check if two agents are on the same coordinate
        If so they fight.

        :return: None
        """

        for agentx in self.agents:

            for agenty in self.agents:

                if agentx != agenty:

                    if agentx.coordinate == agenty.coordinate:

                        self.fight(agentx, agenty)
                        #print("{} and {} fought!!!".format(agentx, agenty))

                        if agentx.health <= 0:
                            if agentx in self.agents:
                                self.agents.remove(agentx)


                        if agenty.health <= 0:
                            if agentx in self.agents:
                                self.agents.remove(agenty)
                            #print(self.agents)




    def check_for_survivors(self):
        """
        Check for survivors
        return True when atleast 2 are alive
        return False and the winner when only 1 is alive
        """

        survivors = []

        for agentx in self.agents:
            if agentx.health > 0:

                survivors.append(agentx)

        if len(survivors) <= 1:
            return [False,survivors[0]]
        else:
            return [True]
            
    def simulate(self):
        
        continue_fighting = True
        
        fig = plt.figure(1, figsize=(12, 12))  # create figure with figure size
        ax = plt.subplot()  # create subplot to be able to change plot without changing figure object
        ax.set_xlim(0, 20)  # set limits of plot area
        ax.set_ylim(0, 20)  
        plt.show(block=False) 
        
        t = 0        
        
        while continue_fighting:

            self.new_move()
                
            self.update_world_map()
            self.improved_fights()

            survival_check= self.check_for_survivors()
            continue_fighting = survival_check[0]
            my_welt.update_world_map()
            
            ax.clear()  # clear the drawing/plotting area
            ax.set_title('Time: {} sec'.format(t))  # setting the figure title
            ax.set_xlim(0, 20)
            ax.set_ylim(0, 20)
            for agent in self.agents:
                    ax.scatter(agent.coordinate[0], agent.coordinate[1], color='k')  # plotting current positions
            
                    # getting last positions
                    x_hist = [pos[0] for pos in agent.history]
                    y_hist = [pos[1] for pos in agent.history]
            
                    ax.scatter(x_hist[-2:-1], y_hist[-2:-1], alpha=0.2, color='k')  # plot last 7 timepoints transparantly
            fig.canvas.draw()  # draw plot
            t += 1

if __name__ == "__main__":


    my_welt = Welt()
    
    my_welt.simulate()
	
    
            

   
