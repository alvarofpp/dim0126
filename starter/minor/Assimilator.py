from sc2.constants import NEXUS, ASSIMILATOR
from model.ModuleModel import *


class Assimilator(ModuleModel):
    """Classe que definirá o comportamento de um Assimilator."""

    def __init__(self, number):
        super().__init__()
        self.ready = 0
        self.target = number

    async def run(self, bot):
        if self.ready < self.target and not bot.already_pending(ASSIMILATOR):
            nexuses = bot.units(NEXUS).ready
            if nexuses.exists and bot.can_afford(ASSIMILATOR):
                vaspenes = bot.state.vespene_geyser.closer_than(10.0, nexuses.first)
                if vaspenes.exists:
                    vaspene = vaspenes.random
                    worker = bot.select_build_worker(vaspene.position)
                    if not worker is None and not bot.units(ASSIMILATOR).closer_than(1.0, vaspene).exists:
                        await bot.do(worker.build(ASSIMILATOR, vaspene))
                        self.ready += 1