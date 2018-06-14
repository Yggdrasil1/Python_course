import numpy as np
import math
import copy

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

            x_coordinate += np.random.randint(-1,1)
            if x_coordinate < 0:
                x_coordinate = self.max_x - 1
            if x_coordinate > self.max_x - 1:
                x_coordinate = 0


            y_coordinate += np.random.randint(-1,1)
            if y_coordinate < 0:
                y_coordinate = self.max_y - 1
            if y_coordinate > self.max_y - 1:
                y_coordinate = 0


            self.update_position(x_coordinate,y_coordinate)


    def update_position(self, x_coordinate, y_coordinate):
        """Update agent position
        :type self: Agent
        """

        self.history.append(self.coordinate)
        self.coordinate = (x_coordinate, y_coordinate)

    def __repr__(self):
        return "id.{}".format(self.id)

    def apply_dmg(self,damage):
        lifeloss = damage
        for _ in range(self.defense):
            if lifeloss == 1:
                continue
            else:
                if np.random.uniform(0,1) < 0.1:
                    lifeloss -= 1

        self.health -= lifeloss
	if self.health < 0:
	    print("{} has died".format(self))



class Welt:

    def __init__(self):

        self.x_dimension = 10
        self.y_dimension = 10

        self.agents = []
        for id in range(10):
            self.agents.append(Agent(id,self.x_dimension,self.y_dimension))

        self.map = {}
        self.update_world_map()

        self.last_survivor = False


    def update_world_map(self):

        """creates a map from a dictionary with coordinates as keys"""

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

        for row_map in range(self.y_dimension):
            print_string = ""
            for column_map in range(self.x_dimension):
                print_string += str(self.map[(column_map,row_map)])
            print(print_string)


    def fight(agent1,agent2):
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


    def check_for_fights(self):
        for x_coordinate in range(self.x_dimension):
            for y_coordinate in range(self.y_dimension):
                if len(self.map[(x_coordinate,y_coordinate)]) > 1:
		    
		    agentx_list = copy.deepcopy(self.map[(x_coordinate,y_coordinate)])
		    agenty_list = copy.deepcopy(self.map[(x_coordinate,y_coordinate)])

                    for agentx in agentx_list:
			if agentx.health > 0 and len(agentx_list)> 1:
			    print(agentx_list)
			    print(agentx)
			    agenty_list = list(agentx_list).remove(agentx)
			    print(agenty_list)
			    for agenty in agenty_list:
			        if agenty.health > 0:
			            fight(agentx,agenty)
				    print("{} and {} fight".format(agentx,agenty))
			agentx_list.remove(agentx)

        

if __name__ == "__main__":
    my_welt = Welt()

    my_welt.print_map()

    for _ in range(100):
        for agent in my_welt.agents:
          agent.move()
	my_welt.update_world_map()
	my_welt.check_for_fights()          



    print("::::::::::::::::::::::::::::::::::::::::::::")
    print(my_welt.agents[0].history)
