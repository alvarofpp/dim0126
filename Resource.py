from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR
from ModuleAbstract import ModuleAISC

# Resource management
class Resource(ModuleAISC):
    def __init__(self):
        self.MAX_WORKERS = 65
        self.MAX_WORKERS_PER_NEXUS = 16

    async def run(self, bot):
        # Initially are 12 workers
        await bot.distribute_workers()

        await self.build_workers(bot)

    # Build workers (PROBE sc2.constants)
    async def build_workers(self, bot):
        units_nexus = len(bot.units(NEXUS))
        units_probe = len(bot.units(PROBE))

        if (units_nexus*self.MAX_WORKERS_PER_NEXUS) > units_probe and units_probe < self.MAX_WORKERS:
            # Nexus built and without production
            for nexus in bot.units(NEXUS).ready.noqueue:
                # If can afford a PROBE
                if bot.can_afford(PROBE):
                    # Train the probe
                    await bot.do(nexus.train(PROBE))
