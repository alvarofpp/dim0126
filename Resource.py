from sc2.constants import NEXUS, ASSIMILATOR, GATEWAY
from model.ModuleModel import ModuleModel
from model.build.Probe import Probe
from model.build.Assimilator import Assimilator


class Resource(ModuleModel):
    """Gerenciador de recursos."""

    def __init__(self):
        super().__init__()
        # Módulos
        self.probe = Probe()
        self.assimilator = Assimilator()

    async def condition(self, bot):
        pass
        
    async def run(self, bot):
        """Executa os métodos indicados de forma assíncrona."""
        await bot.distribute_workers()
        await self.probe.build(bot)
        if bot.units(GATEWAY).ready.exists:
            await self.assimilator.build(bot)
