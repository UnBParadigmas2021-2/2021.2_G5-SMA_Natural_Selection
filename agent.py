from mesa import Agent

class FoodAgent(Agent):
    """Agente com a saude inicial fixada."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.food = 1

    def step(self):
       self.move()
       if self.food > 0:
           self.give_food()

    def give_food(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.food += 1
            self.food  -= 1
    
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore = True, include_center = False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)