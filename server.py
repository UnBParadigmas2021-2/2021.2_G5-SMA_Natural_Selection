from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.FoodAgent import FoodAgent
from src.SpecieAgent import SpecieAgent
from src.FastSpecieAgent import FastSpecieAgent
from src.FoodSpecieModel import FoodSpecieModel
from src.CannibalSpecieAgent import CannibalSpecieAgent


def agent_portrayal(agent):
    portrayal = {"Filled": "true", "Layer": 0, "w": 1, "h": 1}
    if type(agent) is FoodAgent:
        if not agent.eated:
            portrayal['Shape'] = "assets/food.png"
    elif type(agent) is SpecieAgent:
        portrayal['Shape'] = "assets/blob.png"
    elif type(agent) is FastSpecieAgent:
        portrayal['Shape'] = "assets/blob_fast.png"
    elif type(agent) is CannibalSpecieAgent:
        portrayal['Shape'] = "assets/blob_cannibal.png"
    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(FoodSpecieModel, [grid], "Natural Selection", {
                       "N": 10, "width": 10, "height": 10})
server.port = 8081
server.launch()
