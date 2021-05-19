import sc2

from Resource import *
from military.MilitaryPreparation import *
from military.MilitaryTatics import *
from building.MidBuilding import *

from building.Expansion import Expansion


# Protoss bot class
class ProtossBot(sc2.BotAI):
    def __init__(self):
        super().__init__()
        self.iteration = None
        self.ITERATIONS_PER_MINUTE = 165
        self.resource = Resource()
        self.expansion = Expansion()
        self.tatics = MilitaryTatics()
        self.military = MilitaryPreparation()
        self.buiding = MidBuilding()

    async def on_step(self, iteration):
        """Execute at every step"""
        self.iteration = iteration
        await self.resource.run(self)
        await self.expansion.run(self)
        await self.tatics.run(self)
        await self.military.run(self)
        await self.buiding.run(self)

    def get_time_iteration(self):
        """Retorna a quantidade de tempo passado a partir da quantidade de iterações"""
        return self.iteration / self.ITERATIONS_PER_MINUTE
