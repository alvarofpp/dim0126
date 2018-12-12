from sc2.constants import STALKER, GATEWAY 
from model.ModuleModel import *
from starter.minor.Pylon import *
from starter.minor.Gateway import *
from starter.minor.GatewayTrain import *


class Mid1(ModuleModel):
    def __init__(self):
        self.ok = False
        self.gateway = Gateway(2)
        self.train = GatewayTrain(2)
        self.pylon = Pylon(1)
        self.train.change_unit(STALKER)

    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        await self.gateway.run(bot)
        await self.train.run(bot)
        await self.pylon.run(bot)
        if bot.units(GATEWAY).amount == 3:
            self.ok = True

    