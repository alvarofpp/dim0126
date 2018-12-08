from sc2.constants import PYLON, GATEWAY, CYBERNETICSCORE
from model.ModuleModel import *

class TechSearch(ModuleModel):
    def __init__(self, building, times = 1):
        self.building = building
        self.times = times
        self.techs = List()

    async def add_tech(tech):
        techs.insert(tech)

    async def run(self, bot):
        for tech in self.techs:
            