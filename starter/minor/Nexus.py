from sc2.constants import NEXUS, PYLON
from model.ModuleModel import *

class Nexus(ModuleModel):
    def __init__(self, number):
        self.ready = 0
        self.target = number

    async def run(self, bot):
        if self.ready < self.target and not bot.already_pending(NEXUS) and bot.can_afford(NEXUS):
            await bot.expand_now()
            self.ready += 1