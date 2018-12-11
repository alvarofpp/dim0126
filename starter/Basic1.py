from sc2.constants import ZEALOT, ASSIMILATOR
from model.ModuleModel import *
from starter.minor.Pylon import *
from starter.minor.Gateway import *
from starter.minor.GatewayTrain import *
from starter.minor.Assimilator import *

class Basic1(ModuleModel):
    def __init__(self):
        self.ok = False
        self.pylon = Pylon(1)
        self.gateway = Gateway(1)
        self.train = GatewayTrain(10)
        self.gas = Assimilator(1)
        
        self.train.change_unit(ZEALOT)

    async def condition(self, bot):
        pass

    async def run(self, bot):
        await self.pylon.run(bot)
        await self.gateway.run(bot)
        await self.train.run(bot)
        if bot.units(GATEWAY).ready.exists:
            await self.gas.run(bot)
            if bot.units(ASSIMILATOR).ready.exists:
                self.ok = True

    