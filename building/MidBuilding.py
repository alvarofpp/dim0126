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

    async def run(self, bot):
        await self.pylons.build(bot)
        await self.assimilators.build(bot)
        await self.expansion.run(bot)
