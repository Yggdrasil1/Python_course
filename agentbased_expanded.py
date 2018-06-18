import numpy as np
import matplotlib.pyplot as plt


class Agent:
    def __init__(self):
        x_coordinate = np.random.randint(0, 200)
        y_coordinate = np.random.randint(0, 200)
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
    def __init__(self, N=5):
        self.agents = []
        self.N = N
        for _ in range(self.N):
            self.agents.append(Agent())

    def update_timestep(self):
        for agent in self.agents:
            agent.move()

    def simulate(self, time_steps=100, visualize=False):
        if visualize:
            fig = plt.figure(1, figsize=(12, 12))  # create figure with figure size
            ax = plt.subplot()  # create subplot to be able to change plot without changing figure object
            ax.set_xlim(0, 200)  # set limits of plot area
            ax.set_ylim(0, 200)  
            plt.show(block=False)  # enables changing figure object while opened  
        
        for t in range(time_steps):
            self.update_timestep()
            if visualize:
                ax.clear()  # clear the drawing/plotting area
                ax.set_title('Time: {} sec'.format(t))  # setting the figure title
                ax.set_xlim(0, 200)
                ax.set_ylim(0, 200)
                for agent in self.agents:
                    ax.scatter(agent.coordinate[0], agent.coordinate[1], color='k')  # plotting current positions
            
                    # getting last positions
                    x_hist = [pos[0] for pos in agent.history]
                    y_hist = [pos[1] for pos in agent.history]
            
                    ax.scatter(x_hist[-7:-1], y_hist[-7:-1], alpha=0.2, color='k')  # plot last 7 timepoints transparantly
                fig.canvas.draw()  # draw plot


if __name__ == "__main__":
    my_model = Model(N=10)
    my_model.simulate(time_steps=50, visualize=True)
