import sc2

from Resource import *
from building.StarterBuilding import *
from military.MilitaryPreparation import *
from military.MilitaryTatics import *


# Protoss bot class
class ProtossBot(sc2.BotAI):
    def __init__(self):
        self.iteration = None
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 65
        self.resource = Resource()
        self.building = StarterBuilding()
        self.military_preparation = MilitaryPreparation()
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
        await self.military_preparation.run(self)
        # - Tatics
        await self.tatics.run(self)
