from sc2.constants import NEXUS, PROBE
from model.BuildModel import *


class Probe(BuildModel):
    """Classe que definirá as ações referentes aos Probes"""

    def __init__(self):
        super().__init__()
        # Constantes
        self.MAX_WORKERS = 66
        self.MAX_WORKERS_PER_NEXUS = 16

    async def condition(self, bot):
        pass

    async def build(self, bot):
        """Treina trabalhadores (PROBE sc2.constants)"""
        # Quantidade de Nexus
        units_nexus = len(bot.units(NEXUS))
        # Quantidade de Probes
        units_probe = len(bot.units(PROBE))

        # Verifica se a quantidade de PROBE não chegou ao limite atual
        if (units_nexus*self.MAX_WORKERS_PER_NEXUS) > units_probe \
                and units_probe < self.MAX_WORKERS:
            # NEXUS construido e sem fila
            for nexus in bot.units(NEXUS).ready.noqueue:
                # Se pode proporcionar um PROBE
                if bot.can_afford(PROBE):
                    # Treinar um PROBE
                    await bot.do(nexus.train(PROBE))
