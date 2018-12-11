from sc2.constants import PYLON, GATEWAY, CYBERNETICSCORE
from model.ModuleModel import *


class TechSearch(ModuleModel):
    def __init__(self, building, times=1):
        super().__init__()
        self.building = building
        self.times = times
        self.techs = []
        self.done = []

    async def condition(self, bot):
        pass
        
    def add_tech(self, tech):
        if not tech in self.done:
            self.techs.append(tech)

    async def run(self, bot):
        for tech in self.techs:
            if bot.units(self.building).ready.exists and bot.can_afford(tech):
                await bot.do(research(tech))
                self.techs.remove(tech)
                self.done.append(tech)
