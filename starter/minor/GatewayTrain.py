from sc2.constants import GATEWAY
from model.ModuleModel import *

class GatewayTrain(ModuleModel):
    def __init__(self, number):
        self.unit = None
        self.target = number

    async def change_number(self, number):
        self.number = number

    async def change_unit(self, unit):
        self.unit = unit

    async def run(self, bot):
        for gateway in bot.units(GATEWAY).ready.noqueue:
            if (bot.units(self.unit).amount < self.target or self.target == 0) and not bot.already_pending(self.unit):
                if bot.can_afford(self.unit) and bot.supply_left > 0:
                        await bot.do(gateway.train(self.unit))
