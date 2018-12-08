from sc2.constants import PYLON, ADEPT, SENTRY, CYBERNETICSCORE, PROTOSSGROUNDWEAPONSLEVEL1, ADEPTSHIELDUPGRADE # RESONATINGGLAIVES
from model.ModuleModel import *
from starter.minor.Pylon import *
from starter.minor.Cybercore import *
from starter.minor.GatewayTrain import *
from starter.minor.Nexus import *
from starter.minor.TechSearch import *


class Basic2(ModuleModel):
    def __init__(self):
        self.ok = False
        self.nexus = Nexus(1)
        self.cyber = Cybercore(1)
        self.train = GatewayTrain(1)
        self.pylon = Pylon(1)
        self.tech = TechSearch(CYBERNETICSCORE)

        self.tech.add_tech(PROTOSSGROUNDWEAPONSLEVEL1)
        self.tech.add_tech(ADEPTSHIELDUPGRADE)
        self.train.change_unit(SENTRY)

    async def run(self, bot):
        if bot.units(SENTRY).amount == 1:
            train.change_unit(ADEPT)
            train.change_number(10)
        await self.nexus.run(bot)
        await self.cyber.run(bot)
        await self.train.run(bot)
        if bot.units(CYBERNETICSCORE).ready.exists:
            await self.pylon.run(bot)
            if bot.units(PYLON).amount >= 2:
                self.ok = True

    