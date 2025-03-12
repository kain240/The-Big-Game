from abc import ABC, abstractmethod
from players import Player
from .move import Move


class Game(ABC):
    _status: str
    _players: list[Player]
    _state: any
    _turn: list[Move]

    @abstractmethod
    def configure(self, config: dict):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def proceed(self):
        pass

    @abstractmethod
    def result(self):
        pass

    @property
    def status(self):
        return self._status
