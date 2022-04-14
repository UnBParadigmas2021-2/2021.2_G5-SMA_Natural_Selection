from pyexpat import model
from mesa import Agent


class SpecieAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.specie = 1

    def step(self):
        self.walk_search_food()
        self.check_got_food()

    def walk_search_food(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=False, include_center=False)
        print("Steps possiveis do ponto na pos ", self.pos)
        print(possible_steps)
        self.get_new_position(possible_steps, self.pos)
        new_position = self.random.choice(possible_steps)
        
        self.model.grid.move_agent(self, new_position)
        print("Procurar comida")

    def get_new_position(self, possible_steps, current_pos):
        while(True):
            new_position = self.random.choice(possible_steps)
            curr_x, curr_y = current_pos
            x, y = new_position
            if abs(x-curr_x) <= 1 and abs(y-curr_y) <= 1:
                return new_position

    def check_got_food(self):
        # a = SpecieAgent(self.model.next_id(), self.model)
        # self.model.schedule.add()
        print("Se achou food, aumentar o self.food")
        print("Se self.food > 1, ele reproduz")

