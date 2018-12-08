from sc2.constants import ZEALOT
from model.ModuleModel import *
from starter.Pilon import *
from starter.Gateway import *
from starter.GatewayTrain import *
from starter.Assimilator import *


class Basic1(ModuleModel):
    def __init__(self):
        self.ok = False
        self.pilon = Pilon(1)
        self.gateway = Gateway(1)
        self.train = GatewayTrain(10)
        self.gas = Assimilator(1)

    async def run(self, bot):
        await self.train.change_unit(ZEALOT)
        await self.pilon.run(bot)
        await self.gateway.run(bot)
        await self.train.run(bot)
        if bot.units(GATEWAY).ready.exists:
            await self.gas.run(bot)
            self.ok = True

    