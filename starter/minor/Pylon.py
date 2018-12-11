from sc2.constants import NEXUS, PYLON
from model.ModuleModel import *


class Pylon(ModuleModel):
    def __init__(self, number):
        super().__init__()
        self.ready = 0
        self.target = number

    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        if self.ready < self.target and not bot.already_pending(PYLON):
            nexuses = bot.units(NEXUS).ready
            if nexuses.exists and bot.can_afford(PYLON):
                await bot.build(PYLON, near=nexuses.first)
                self.ready += 1
