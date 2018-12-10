from sc2.constants import PYLON, GATEWAY, CYBERNETICSCORE
from model.MilitaryModel import *


class CyberneticsCore(MilitaryModel):
    """Classe que definirá as ações referentes aos Cybernetics Core."""

    def __init__(self):
        super().__init__()

    async def build(self, bot):
        """Construir Cybernetics Core (CYBERNETICSCORE sc2.constants)."""
        if bot.units(PYLON).ready.exists:
            # Get a random pylon
            pylon = bot.units(PYLON).ready.random
            # Build a Cybernetics Core
            if bot.units(GATEWAY).ready.exists and not bot.units(CYBERNETICSCORE) \
                    and bot.can_afford(CYBERNETICSCORE) and not bot.already_pending(CYBERNETICSCORE):
                    await bot.build(CYBERNETICSCORE, near=pylon)

    async def train(self):
        pass
