from sc2.constants import NEXUS

from model.ModuleModel import ModuleModel

# Expansion management
class Expansion(ModuleModel):
    def __init__(self):
        self.transition1 = 4
        self.transition2 = 8
        
    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        if bot.iteration / bot.ITERATIONS_PER_MINUTE < self.transition1:
            await self.expand(bot, 2)
        elif bot.iteration / bot.ITERATIONS_PER_MINUTE < self.transition2:
            await self.expand(bot, 3)
        else:
            await self.expand(bot, 4)

    # Expand the empire
    async def expand(self, bot, number):
        # Max 3 nexus
        if bot.units(NEXUS).amount < number and bot.can_afford(NEXUS):
            await bot.expand_now()
