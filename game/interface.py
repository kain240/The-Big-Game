from abc import ABC, abstractmethod

class Game(ABC):
    _status: str

    @abstractmethod
    def configure(self):
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

    @property
    def status(self):
        return self._status

    @abstractmethod
    def result(self):
        pass
