from sc2.constants import PYLON, CYBERNETICSCORE, STARGATE
from model.MilitaryModel import *


class Stargate(MilitaryModel):
    """Classe que definirá as ações referentes aos Stargate."""

    def __init__(self):
        super().__init__()
        # Constantes
        self.STARGATE_PER_MINUTES = 2

    async def build(self, bot):
        """Construir Stargate (STARGATE sc2.constants)."""
        if bot.units(PYLON).ready.exists:
            # Get a random pylon
            pylon = bot.units(PYLON).ready.random
            # Build a Stargate
            if bot.units(CYBERNETICSCORE).ready.exists \
                    and len(bot.units(STARGATE)) < (bot.get_time_iteration()/self.STARGATE_PER_MINUTES) \
                    and bot.can_afford(STARGATE) and not bot.already_pending(STARGATE):
                        await bot.build(STARGATE, near=pylon)

    async def train(self):
        pass
