from CoinFlipMode import CoinFlip
from dice_mode import dice
from game_mode import GameMode


class GameModeFactory:
    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """

        if cls not in ["coinflip", "dice"]:
            raise ValueError("Requested game_mode is not supported")

        if cls == "dice":
            return dice()
        else:
            return CoinFlip()
