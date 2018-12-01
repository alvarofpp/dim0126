import random
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, \
 GATEWAY, CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY

from ModuleAISC import ModuleAISC

# MilitaryTatics management
class MilitaryTatics(ModuleAISC):
    def __init__(self):
        self.MAX_WORKERS = 65
        
    async def run(self, bot):
        
        await self.attack(bot)

    # Find location of the enemy (army, structure, etc)
    def find_target(self, bot):
        # Army or common unit
        if len(bot.known_enemy_units) > 0:
            return random.choice(bot.known_enemy_units)
        # Structure
        elif len(bot.known_enemy_structures) > 0:
            return random.choice(bot.known_enemy_structures)
        # First location known
        else:
            return bot.enemy_start_locations[0]

    # Attack the enemy
    async def attack(self, bot):
        # {UNIT: [n to fight, n to defend]}
        aggressive_units = {
            STALKER: [15, 5],
            VOIDRAY: [8, 3]
        }

        for UNIT in aggressive_units:
            # Attack the base
            if bot.units(UNIT).amount > aggressive_units[UNIT][0] and bot.units(UNIT).amount > aggressive_units[UNIT][1]:
                for unit in bot.units(UNIT).idle:
                    await bot.do(unit.attack(self.find_target(bot)))

            # Attack the enemy army or common unit
            elif bot.units(UNIT).amount > aggressive_units[UNIT][1]:
                if len(bot.known_enemy_units) > 0:
                    for unit in bot.units(UNIT).idle:
                        await bot.do(unit.attack(random.choice(bot.known_enemy_units)))
