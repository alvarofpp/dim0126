from sc2.constants import NEXUS, PYLON, ASSIMILATOR, ZEALOT, MOTHERSHIPCORE

from building.MidBuilding import *
from military.MilitaryPreparation import *

# StarterBuilding management
class StarterBuilding(ModuleAISC):
    def __init__(self):
        self.pylon1 = False
        self.gateway1 = False
        self.gas1 = False
        self.nexus = False
        self.adepts = False
        self.cybercore = False
        self.pylon2 = False
        self.mothership = False
        self.gateway2 = False
        self.gateway3 = False
        self.gas2 = False

    async def run(self, bot):
        if self.gateway1 and not bot.already_pending(GATEWAY) and not self.cybercore:
            if bot.units(GATEWAY).ready.noqueue.exists:
                gateway = bot.units(GATEWAY).ready.noqueue.first
                if bot.can_afford(ZEALOT) and bot.supply_left > 0:
                    await bot.do(gateway.train(ZEALOT))
        elif self.gateway1 and self.cybercore and not bot.already_pending(CYBERNETICSCORE):
            if bot.units(GATEWAY).ready.noqueue.exists:
                gateway = bot.units(GATEWAY).ready.noqueue.first
                if bot.can_afford(ADEPT) and bot.supply_left > 0:
                    await bot.do(gateway.train(ADEPT))
        if not self.pylon1:
            nexuses = bot.units(NEXUS).ready
            if bot.can_afford(PYLON):
                await bot.build(PYLON, near=nexuses.first)
                self.pylon1 = True
        elif not self.gateway1:
            if bot.can_afford(GATEWAY) and not bot.already_pending(PYLON):
                pylon = bot.units(PYLON).ready.random
                await bot.build(GATEWAY, near=pylon)
                self.gateway1 = True
        elif not self.gas1:
            nexus = bot.units(NEXUS).ready.first
            vaspenes = bot.state.vespene_geyser.closer_than(10.0, nexus)
            if not vaspenes.empty and bot.can_afford(ASSIMILATOR):
                worker = bot.select_build_worker(vaspenes.first.position)
                if not worker is None:
                    if not bot.units(ASSIMILATOR).closer_than(1.0, vaspenes.first).exists:
                        await bot.do(worker.build(ASSIMILATOR, vaspenes.first))
                        self.gas1 = True
        elif not self.nexus:
            if bot.can_afford(NEXUS):
                await bot.expand_now()
                self.nexus = True
        elif not self.cybercore:
            if bot.can_afford(CYBERNETICSCORE):
                pylon = bot.units(PYLON).ready.random
                await bot.build(CYBERNETICSCORE, near=pylon)
                self.cybercore = True
        elif not self.pylon2:
            nexuses = bot.units(NEXUS).ready
            if nexuses.exists:
                if bot.can_afford(PYLON):
                    await bot.build(PYLON, near=nexuses.first)
                    self.pylon2 = True
        elif self.pylon2 and bot.vespene >= 100 and not self.gateway2:
            if bot.can_afford(MOTHERSHIPCORE):
                nexuses = bot.units(NEXUS).ready
                if nexuses.exists:
                    await bot.do(nexuses.first.train(MOTHERSHIPCORE))
        elif not self.gateway2:
            if bot.can_afford(GATEWAY):
                pylon = bot.units(PYLON).ready.random
                await bot.build(GATEWAY, near=pylon)
                self.gateway2 = True
        elif not self.gateway3:
            if bot.can_afford(GATEWAY):
                pylon = bot.units(PYLON).ready.random
                await bot.build(GATEWAY, near=pylon)
                self.gateway3 = True
        elif not self.gas2:
            nexus = bot.units(NEXUS).ready.first
            vaspenes = bot.state.vespene_geyser.closer_than(10.0, nexus)
            if not vaspenes.empty and bot.can_afford(ASSIMILATOR):
                worker = bot.select_build_worker(vaspenes.first.position)
                if not worker is None:
                    if not bot.units(ASSIMILATOR).closer_than(1.0, vaspenes.first).exists:
                        await bot.do(worker.build(ASSIMILATOR, vaspenes.first))
                        self.gas2 = True
                        bot.building = MidBuilding()
                        bot.military = MilitaryPreparation()