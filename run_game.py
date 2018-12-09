from sc2.player import Bot, Computer
from sc2 import run_game, maps, Race, Difficulty
from ProtossBot import ProtossBot
from examples.SentdeBot import *

# Run the game
run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Protoss, ProtossBot()),
    Computer(Race.Terran, Difficulty.Hard)
], realtime=False)
