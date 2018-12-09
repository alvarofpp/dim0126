import sc2

from Resource import *
from starter.Basic1 import *
from starter.Basic2 import *


# Protoss bot class
class ProtossBot(sc2.BotAI):
    def __init__(self):
        self.iteration = None
        self.ITERATIONS_PER_MINUTE = 165
        # self.module = Basic1()
        self.resource = Resource()

    # Execute at every step
    async def on_step(self, iteration):
        self.iteration = iteration
        # await self.module.run(self)
        await self.resource.run(self)
