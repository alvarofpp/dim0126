from sc2.constants import NEXUS
from model.ModuleModel import ModuleModel
from model.build.Pylon import Pylon


class Expansion(ModuleModel):
    """Gerenciamento de expansão"""

    def __init__(self):
        super().__init__()
        # Constantes
        self.MAX_NEXUS = 3
        self.BUILD_NEXUS = True
        # Módulos
        self.pylon = Pylon()
        
    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        """Executa os métodos indicados de forma assíncrona."""
        await self.pylon.build(bot)
        await self.expand(bot)

    async def expand(self, bot):
        """Expandir o império."""
        if bot.units(NEXUS).amount < self.MAX_NEXUS and bot.can_afford(NEXUS):
            await bot.expand_now()
