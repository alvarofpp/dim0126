from sc2.constants import PYLON, GATEWAY, CYBERNETICSCORE, VOIDRAY, STALKER
from model.MilitaryModel import *


class Gateway(MilitaryModel):
    """Classe que definirá as ações referentes aos Gateway."""

    def __init__(self):
        super().__init__()
        # Constantes
        self.GATEWAY_PER_MINUTES = 2

    async def condition(self, bot):
        pass

    async def build(self, bot):
        """Construir Gateway (GATEWAY sc2.constants)."""
        if bot.units(PYLON).ready.exists:
            # Get a random pylon
            pylon = bot.units(PYLON).ready.random
            # Build a Gateway
            if len(bot.units(GATEWAY)) < (bot.get_time_iteration()/self.GATEWAY_PER_MINUTES) \
                    and bot.can_afford(GATEWAY) and not bot.already_pending(GATEWAY):
                    await bot.build(GATEWAY, near=pylon)

    async def train(self, bot):
        """Treinar Stalkers (STALKERS sc2.constants)"""
        for gateway in bot.units(GATEWAY).ready.noqueue:
            # Train stalker
            if not bot.units(STALKER).amount > bot.units(VOIDRAY).amount:
                if bot.can_afford(STALKER) and bot.supply_left > 0:
                    await bot.do(gateway.train(STALKER))
