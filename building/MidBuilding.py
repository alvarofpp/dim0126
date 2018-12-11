from sc2.constants import GATEWAY

from building.Expansion import *
from model.build.Pylon import *
from model.build.Assimilator import *


# MidBuilding management
class MidBuilding(ModuleModel):
    def __init__(self):
        super().__init__()
        self.pylons = Pylon()
        self.assimilators = Assimilator()
        self.expansion = Expansion()

    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        await self.pylons.build(bot)
        await self.expansion.run(bot)
        if bot.units(GATEWAY).ready.exists:
            await self.assimilators.build(bot)

        
