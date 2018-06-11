import numpy as np


class Agent:

    def __init__(self):

	x_coordinate = np.random.randint(0,26)
	y_coordinate = np.random.randint(0,26)
	
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

	x_coordinate = self.coordinate[0]
	y_coordinate = self.coordinate[1]

	x_coordinate += np.random.randint(-1,1)
	y_coordinate += np.random.randint(-1,1)

	self.update_position(x_coordinate,y_coordinate)

	
    def update_position(self, x_coordinate, y_coordinate):
	"""Update agent position"""

	self.history.append(self.coordinate)
	self.coordinate = (x_coordinate, y_coordinate) 	

	
	

class Welt:
	
    def __init__(self):

	self.agents = []
        for _ in range(10):
	    self.agents.append(Agent())

	self.x_dimension = 25
	self.y_dimension = 25

	self.map = {}
	self.initialise_map()
	

    def initialise_map(self):
	
	for x_coordinate in range(self.x_dimension):
	    for y_coordinate in range(self.y_dimension):
		key = (x_coordinate,y_coordinate)
		self.map[key] = []

    def welt_overview_agents(self):
	
	for agent in self.agents:
	    pass


    #def fight(agent1, agent2):
	

if __name__ == "__main__":
    my_welt = Welt()
    a = 1
    for agent in my_welt.agents:
	pass
	
    print(my_welt.map)
