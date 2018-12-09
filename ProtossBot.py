import sc2

from Resource import *
from military.MilitaryPreparation import *
from military.MilitaryTatics import *
from building.MidBuilding import *

from starter.Basic1 import *
from starter.Basic2 import *


# Protoss bot class
class ProtossBot(sc2.BotAI):
    def __init__(self):
        self.iteration = None
        self.ITERATIONS_PER_MINUTE = 165
        self.resource = Resource()
        self.tatics = MilitaryTatics()
        self.military = MilitaryPreparation()
        self.buiding = MidBuilding()

    # Execute at every step
    async def on_step(self, iteration):
        self.iteration = iteration
        await self.resource.run(self)
        await self.military.run(self)
        await self.tatics.run(self)
        await self.buiding.run(self)
