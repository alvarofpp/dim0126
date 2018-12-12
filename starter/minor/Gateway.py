from sc2.constants import PYLON, GATEWAY
from model.ModuleModel import *


class Gateway(ModuleModel):
    def __init__(self, number):
        super().__init__()
        self.ready = 0
        self.target = number

    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        if self.ready < self.target and not bot.already_pending(GATEWAY):
            pylons = bot.units(PYLON).ready
            if pylons.exists and bot.can_afford(GATEWAY): 
                await bot.build(GATEWAY, near=pylons.random)
                self.ready += 1
