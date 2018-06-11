import numpy as np


class Agent:

    def __init__(self):

	x_coordinate = np.random.randint(0,25)
	y_coordinate = np.random.randint(0,25)
	
	self.history = []
        self.coordinate = (x_coordinate, y_coordinate)

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

if __name__ == "__main__":
    my_welt = Welt()
    a = 1
    for agent in my_welt.agents:
	print("%d. Agent: " %a)	
	print(agent.coordinate)
	agent.move()
	print(agent.coordinate)
	a += 1
	

