from sc2.constants import NEXUS, PYLON
from model.BuildModel import *


class Pylon(BuildModel):
    """Classe que definirá as ações referentes aos Pylons."""

    def __init__(self):
        super().__init__()
        # Constantes
        self.PYLON_PER_NEXUS = 5

    async def build(self, bot):
        """Construir Pylon (PYLON sc2.constants)."""
        # Supply capacity left provided by bases and pylon building
        # print(bot.supply_left, bot.already_pending(PYLON))
        if bot.supply_left < 10 and not bot.already_pending(PYLON):
            print(bot.supply_left, bot.already_pending(PYLON))
            # Get nexus
            nexuses = bot.units(NEXUS).ready
            # Check nexus exists
            if nexuses.exists:
                # If can afford a PYLON
                if bot.can_afford(PYLON):
                    # Build a PYLON near the first nexus
                    await bot.build(PYLON, near=nexuses.first)
