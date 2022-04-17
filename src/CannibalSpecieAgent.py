from src.SpecieAgent import SpecieAgent
from src.FoodAgent import FoodAgent

class CannibalSpecieAgent(SpecieAgent):
    breed="Cannibal"
    energy=20
    moore=True
    radius=3
    walk_radius=1
    energy_loss=1

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, self.breed, self.energy, self.moore, self.radius, self.walk_radius, self.energy_loss)

    def step(self):
        try:
            self.energy -= self.energy_loss
            self.eat_specie()
            self.walk_search_food()
            self.check_got_food(2)
            self.check_got_energy()
        except:
            pass


    def eat_specie(self):
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        mates = [obj for obj in this_cell if not isinstance(obj, FoodAgent) and obj != self]
        if len(mates) > 0:
            specie = self.random.choice(mates)
            self.energy += 1
            specie.energy += 0
