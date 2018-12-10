import sc2

from Resource import *
from building.Expansion import Expansion


# Protoss bot class
class ProtossBotResources(sc2.BotAI):
    def __init__(self):
        self.iteration = None
        self.ITERATIONS_PER_MINUTE = 165
        self.resource = Resource()
        self.expansion = Expansion()

    async def on_step(self, iteration):
        """Execute at every step"""
        self.iteration = iteration
        await self.resource.run(self)
        await self.expansion.run(self)

    def get_time_iteration(self):
        """Retorna a quantidade de tempo passado a partir da quantidade de iterações"""
        return self.iteration / self.ITERATIONS_PER_MINUTE
