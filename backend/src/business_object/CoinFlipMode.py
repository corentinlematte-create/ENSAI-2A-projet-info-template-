import datetime
from random import choice

from game import Game
from game_mode import GameMode


class CoinFlip(GameMode):
    def play(p1, p2, choice_player):
        result = choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        return Game(
            p1, p2, "coin flip", winner, "game", datetime.now())
