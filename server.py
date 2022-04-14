from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.Food.FoodAgent import FoodAgent

from src.Food.FoodSpecieModel import FoodSpecieModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "True", "r": 0.5, "Layer": 0}

    if type(agent) is FoodAgent:
        if agent.food > 0:
            portrayal["Color"] = "red"
            portrayal["Layer"] = 0
            portrayal["r"] = 0.2
    else:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(FoodSpecieModel, [grid], "Natural Selection", {
                       "N": 5, "width": 10, "height": 10})
server.port = 8081
server.launch()
