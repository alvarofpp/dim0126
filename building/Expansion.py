from sc2.constants import NEXUS
from model.ModuleModel import ModuleModel


class Expansion(ModuleModel):
    """Gerenciamento de expansão"""

    def __init__(self):
        super().__init__()
        # Constantes
        self.transitions = [4, 8]
        self.number_nexus = [2, 3, 4]
        
    def condition(self, bot):
        """Verifica as condições de expansão e retorna o número de nexus que podem serem feitos"""
        index = 0
        for transition in self.transitions:
            if bot.get_time_iteration() < transition:
                return self.number_nexus[index]

            index += 1

        return self.number_nexus[index]
        
    async def run(self, bot):
        """Executa os métodos indicados de forma assíncrona"""
        number_nexus = self.condition(bot)
        await self.expand(bot, number_nexus)

    async def expand(self, bot, number):
        """Expandir o império"""
        if bot.units(NEXUS).amount < number and bot.can_afford(NEXUS):
            await bot.expand_now()
