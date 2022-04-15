from pyexpat import model
from mesa import Agent
from src.Food.FoodAgent import FoodAgent


class SpecieAgent(Agent):
    energy = None  # personagem morre quando chega a 0
    grid = None  # matrix com o tabuleiro
    moore = None  # para função de andar
    radius = None  # visão do personagem
    walk_radius = None  # quadrados andados por passo('velocidade')
    energy_loss = None  # perda de energia por passo

    def __init__(self, unique_id, model, energy=20, moore=True, radius=3, walk_radius=1, energy_loss=1):
        super().__init__(unique_id, model)
        self.specie = 1
        self.energy = energy
        self.moore = moore
        self.radius = radius
        self.walk_radius = walk_radius
        self.energy_loss = energy_loss

    def step(self):
        self.energy -= self.energy_loss
        self.walk_search_food()
        self.check_got_food()

    def walk_search_food(self):
        possible_walk_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=True, radius=self.radius)
        new_position = self.get_new_position(possible_walk_pos, self.pos)
        self.model.grid.move_agent(self, new_position)
        print("Procurar comida")

    def get_new_position(self, possible_walk_pos, current_pos):
        next_pos = None
        current_best_pos = None
        minimum_distance = 10**6
        step_x = 0
        step_y = 0
        for walk_pos in possible_walk_pos:
            this_cell = self.model.grid.get_cell_list_contents([walk_pos])
            food = [obj for obj in this_cell if isinstance(obj, FoodAgent)]

            if len(food) > 0:
                current_distance = (
                    current_pos[0] - walk_pos[0])**2 + (current_pos[1] - walk_pos[1])**2
                if current_distance < minimum_distance:
                    minimum_distance = current_distance
                    current_best_pos = walk_pos
        if current_best_pos != None:
            if current_pos[0] < current_best_pos[0]:
                step_x = 1
            elif current_pos[0] > current_best_pos[0]:
                step_x = -1

            if current_pos[1] < current_best_pos[1]:
                step_y = 1
            elif current_pos[1] > current_best_pos[1]:
                step_y = -1

            next_pos = (current_pos[0] + min(self.walk_radius, abs(current_pos[0] - current_best_pos[0])) *
                        step_x, current_pos[1] + min(self.walk_radius, abs(current_pos[1] - current_best_pos[1]))*step_y)

            return next_pos

        next_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=False, radius=self.walk_radius)
        return self.random.choice(next_pos)

    def check_got_food(self):
        # a = SpecieAgent(self.model.next_id(), self.model)
        # self.model.schedule.add()
        print("Se achou food, aumentar o self.food")
        print("Se self.food > 1, ele reproduz")
