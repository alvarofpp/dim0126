from model.ModuleModel import ModuleModel
from model.operation.Probe import Probe
from model.operation.Assimilator import Assimilator


class Resource(ModuleModel):
    """Gerenciador de recursos."""

    def __init__(self):
        super().__init__()
        # Módulos
        self.probe = Probe()
        self.assimilator = Assimilator()

    async def run(self, bot):
        """Executa os métodos indicados de forma assíncrona."""
        await self.probe.build(bot)
        await self.assimilator.build(bot)
