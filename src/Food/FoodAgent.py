from mesa import Agent

class FoodAgent(Agent):
    # def __init__(self, unique_id, pos, model, fully_grown, countdown):
    #     """
    #     Creates a new patch of grass
    #     Args:
    #         grown: (boolean) Whether the patch of grass is fully grown or not
    #         countdown: Time for the patch of grass to be fully grown again
    #     """
    #     super().__init__(unique_id, model)
    #     self.fully_grown = fully_grown
    #     self.countdown = countdown
    #     self.pos = pos

    # def step(self):
    #     if not self.fully_grown:
    #         if self.countdown <= 0:
    #             # Set as fully grown
    #             self.fully_grown = True
    #             self.countdown = self.model.grass_regrowth_time
    #         else:
    #             self.countdown -= 1


    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.food = 1

    def step(self):
        self.give_food()

    def give_food(self):
        print("Give food")
    #     print("GIVE FOOD")
    #     cellmates = self.model.grid.get_cell_list_contents([self.pos])
    #     if len(cellmates) > 1:
    #         other = self.random.choice(cellmates)
    #         other.food += 1
    #         self.food -= 1
