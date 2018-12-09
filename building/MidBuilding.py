from sc2.constants import NEXUS, PYLON, ASSIMILATOR
from building.Expansion import *


# MidBuilding management
class MidBuilding(ModuleModel):
    def __init__(self):
        self.MAX_WORKERS = 65
        self.expansion = Expansion()

    async def run(self, bot):
        await self.build_pylons(bot)
        await self.build_assimilators(bot)
        await self.expansion.run(bot)

    # Build pylons (PYLON sc2.constants)
    async def build_pylons(self, bot):
        # Supply capacity left provided by bases and pylon building
        if bot.supply_left < 10 and not bot.already_pending(PYLON):
            # Get nexus
            nexuses = bot.units(NEXUS).ready
            # Check nexus exists
            if nexuses.exists:
                # If can afford a PYLON
                if bot.can_afford(PYLON):
                    # Build a PYLON near the first nexus
                    await bot.build(PYLON, near=nexuses.first)

    # Build assimilators (ASSIMILATOR sc2.constants)
    async def build_assimilators(self, bot):
        # For each nexus ready
        for nexus in bot.units(NEXUS).ready:
            # Geysers near the nexus
            vaspenes = bot.state.vespene_geyser.closer_than(10.0, nexus)
            for vaspene in vaspenes:
                # If still can not build the assimilator
                if not bot.can_afford(ASSIMILATOR):
                    break
                # Get workers
                worker = bot.select_build_worker(vaspene.position)
                # If there are no workers
                if worker is None:
                    break
                # If there are no assimilators near the geysers
                if not bot.units(ASSIMILATOR).closer_than(1.0, vaspene).exists:
                    # Build assimilator
                    await bot.do(worker.build(ASSIMILATOR, vaspene))
