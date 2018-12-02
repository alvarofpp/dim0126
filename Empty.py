from sc2.constants import NEXUS, GATEWAY, PYLON, ASSIMILATOR, ZEALOT, WARPGATE, MOTHERSHIPCORE
from ModuleAISC import ModuleAISC

class Empty(ModuleAISC):
    def __init__(self):
        self.ok = 1
    
    async def run(self, bot):
        for gateway in bot.units(GATEWAY).ready.noqueue:
            if bot.can_afford(ZEALOT) and bot.supply_left > 0:
                await bot.do(gateway.train(ZEALOT))