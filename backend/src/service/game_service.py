import os
import secrets

from fastapi import HTTPException

from business_object.game_mode import GameMode
from business_object.GameModeFactory import GameModeFactory
from dao.player_dao import PlayerDao
from utils.log_utils import log


class GameService:
    """Service that manages games."""

    @log
    def play(self, id_player: int, id_opponent: int, game_mode: str, **kwargs):
        """Executes a single round of a coin-flip game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
            choice (str, optional): The player's choice ('heads' or 'tails'). Defaults to "heads".
        Returns:
            dict: A dictionary containing the match details and new elo
        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found in the database.
        """
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        if not p1 or not p2:
            raise HTTPException(status_code=404, detail="Player not found")

        game_factory = GameModeFactory.get_mode(game_mode)
        game = game_factory.play(id_player, id_opponent, **kwargs)

        self.update_player_ratings(p1, p2, game.winner)

        PlayerDao().update(p1)
        PlayerDao().update(p2)

        return {
            "player1": p1.username,
            "player2": p2.username,
            "description": game.description,
            "winner": game.winner.username,
            "new_elo1": p1.elo,
            "new_elo2": p2.elo,
        }
