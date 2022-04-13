from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from .model import FoodModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "True", "r": 0.5}

    if agent.food > 0:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(FoodModel, [grid], "Natural Selection", {
                       "N": 100, "width": 10, "height": 10})
server.port = 8521
server.launch()
