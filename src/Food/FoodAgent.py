from mesa import Agent


class FoodAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.food = 1

    def step(self):
        self.give_food()

    def give_food(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.food += 1
            self.food -= 1
