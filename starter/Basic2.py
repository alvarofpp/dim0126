from sc2.constants import ADEPT, SENTRY, CYBERNETICSCORE
from model.ModuleModel import *
from starter.minor.Pilon import *
from starter.minor.Gateway import *
from starter.minor.GatewayTrain import *
from starter.minor.Assimilator import *


class Basic1(ModuleModel):
    def __init__(self):
        self.ok = False
        self.nexus = Nexus(1)
        self.cyber = Cybercore(1)
        self.train = GatewayTrain(1)
        self.pilon = Pilon(1)

    async def run(self, bot):
        await self.train.change_unit(SENTRY)
        if bot.units(SENTRY).amount == 1:
            await train.change_unit(ADEPT)
            await train.change_number(10)
        await self.nexus.run(bot)
        await self.cyber.run(bot)
        await self.train.run(bot)
        if bot.units(CYBERNETICSCORE).ready.exists:
            await self.pilon.run(bot)
            if bot.units(PILON).amount >= 2:
                self.ok = True

    