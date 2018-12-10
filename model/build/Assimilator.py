from sc2.constants import NEXUS, ASSIMILATOR
from model.BuildModel import *


class Assimilator(BuildModel):
    """Classe que definirá o comportamento dos Assimilators."""

    def __init__(self):
        super().__init__()

    async def build(self, bot):
        """Constroi assimiladores (ASSIMILATOR sc2.constants)"""
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
