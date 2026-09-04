from datetime import datetime

from business_object.player import Player


class Game:
    def __init__(
        self,
        id_game: int,
        player1: Player,
        player2: Player,
        game_mode: str,
        winner: Player,
        description: str,
        timestamp: datetime,
    ):
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        return (
            f"Mode : {self.game_mode}\n"
            f"Match : {self.player1.username} vs {self.player2.username}\n"
            f"Vainqueur : {self.winner}"
        )
