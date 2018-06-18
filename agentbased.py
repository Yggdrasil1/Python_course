import numpy as np

class Agent:
	def __init__(self):
		x_coordinate = np.random.randint(0, 26)
		y_coordinate = np.random.randint(0, 26)
		self.coordinate = (x_coordinate, y_coordinate)
		self.history = []

	def move(self):
		"""Move the agent"""
		x_coordinate = self.coordinate[0]
		y_coordinate = self.coordinate[1]
		x_coordinate += np.random.randint(-1, 2)
		y_coordinate += np.random.randint(-1, 2)
		self.update_coordinate(x_coordinate, y_coordinate)

	def update_coordinate(self, x_coordinate, y_coordinate):
		"""Update current agent position"""
		self.history.append(self.coordinate)
		self.coordinate = (x_coordinate, y_coordinate)

class Model:
	def __init__(self):
		self.agents = []
		for _ in range(10):
			self.agents.append(Agent())

if __name__ == "__main__":
	my_model = Model()
	for agent in my_model.agents:
		# print(agent.coordinate)
		agent.move()
		print(agent.history)
		print(agent.coordinate)
