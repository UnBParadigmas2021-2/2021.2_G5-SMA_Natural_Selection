from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model
from src.Specie.AbstractSpecieAgent import SpecieAgent

from src.Food.FoodAgent import FoodAgent


class FoodSpecieModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        for i in range(self.num_agents):
            a = FoodAgent(i, self)
            self.schedule.add(a)
            random_x = self.random.randrange(self.grid.width)
            random_y = self.random.randrange(self.grid.height)
            x = self.replace_edgy_pos(random_x, self.grid.width)
            y = self.replace_edgy_pos(random_y, self.grid.width)
            self.grid.place_agent(a, (x, y))
        
        random_x = 0
        random_y = 0
        for i in range(self.num_agents):
            a = SpecieAgent(i+self.num_agents, self)
            self.schedule.add(a)
            random_x = self.random.randrange(self.grid.width)
            random_y = self.random.randrange(self.grid.height)
            # x = self.place_in_border()
            x = self.replace_edgy_pos(random_x, self.grid.width)
            y = self.replace_edgy_pos(random_y, self.grid.width)
            self.grid.place_agent(a, (x, y))


    def replace_edgy_pos(self, pos, axis_limit):
        if pos == 0:
            return 1
        if axis_limit-1 == pos:
            return pos - 1
        return pos

    def step(self):
        self.schedule.step()
