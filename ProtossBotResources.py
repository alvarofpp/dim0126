import sc2

from Resource import *
from building.Expansion import Expansion


# Protoss bot class
class ProtossBot(sc2.BotAI):
    def __init__(self):
        self.iteration = None
        self.ITERATIONS_PER_MINUTE = 165
        self.resource = Resource()
        self.expansion = Expansion()

    # Execute at every step
    async def on_step(self, iteration):
        self.iteration = iteration
        await self.resource.run(self)
        await self.expansion.run(self)
