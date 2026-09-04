from abc import ABC, abstractmethod


class GameMode(ABC):
    @abstractmethod
    def play(p1, p2):
        pass
