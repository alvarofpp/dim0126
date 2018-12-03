from sc2.constants import NEXUS
from model.ModuleModel import ModuleModel


# Expansion management
class Expansion(ModuleModel):
    def __init__(self):
        self.MAX_WORKERS = 65
        
    async def run(self, bot):
        await self.expand(bot)

    # Expand the empire
    async def expand(self, bot):
        # Max 3 nexus
        if bot.units(NEXUS).amount < 3 and bot.can_afford(NEXUS):
            await bot.expand_now()
