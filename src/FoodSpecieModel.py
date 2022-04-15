from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model
from src.SpecieAgent import SpecieAgent
from src.FoodAgent import FoodAgent


class FoodSpecieModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        for i in range(self.num_agents):
            self.init_agent(i, FoodAgent)
            self.init_agent(i+self.num_agents, SpecieAgent)

    def init_agent(self, index, Agent):
        agent = Agent(index, self)
        self.schedule.add(agent)
        position = self.get_random_position(Agent)
        self.grid.place_agent(agent, position)

    def get_random_position(self, Agent):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        if type(Agent) is FoodAgent:
            x = self.replace_edgy_pos(x, self.grid.width)
            y = self.replace_edgy_pos(y, self.grid.width)
        return (x, y)

    def replace_edgy_pos(self, pos, axis_limit):
        if pos == 0:
            return 1
        if axis_limit-1 == pos:
            return pos - 1
        return pos

    def step(self):
        self.schedule.step()
