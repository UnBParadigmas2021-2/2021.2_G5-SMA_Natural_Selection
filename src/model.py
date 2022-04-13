from mesa import Model
from .agent import FoodAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class FoodModel(Model):
    """Uma model com um numero definido de agentes"""

    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # cria agentes
        for i in range(self.num_agents):
            a = FoodAgent(i, self)
            self.schedule.add(a)
            self.running = True

            # Adiciona agentes no mapa
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        """Avance a model em um passo"""
        self.schedule.step()
