from abc import ABC, abstractmethod

class Game(ABC):
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

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def result(self):
        pass
