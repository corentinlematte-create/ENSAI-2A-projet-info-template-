import datetime
import random

from game import Game
from game_mode import GameMode


class dice(GameMode):
    def play(p1, p2):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None

        return Game(
            p1, p2, "dice roll", winner, "game", datetime.now())
