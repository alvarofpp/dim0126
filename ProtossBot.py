import sc2

from Resource import *
from Building import *
from MilitaryPreparation import *
from MilitaryTatics import *

# Protoss bot class
class ProtossBot(sc2.BotAI):
    def __init__(self):
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 65
        self.resource = Resource()
        self.building = Building()
        self.military = MilitaryPreparation()
        self.tatics = MilitaryTatics()

    # Execute at every step
    async def on_step(self, iteration):
        self.iteration = iteration

        # Resources
        await self.resource.run(self)

        # Building & Expansion
        await self.building.run(self)

        # War
        # - MilitaryPreparation
        await self.military.run(self)
        # - Tatics
        await self.tatics.run(self)