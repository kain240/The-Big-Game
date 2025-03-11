from .player import Player

def register(name: str) -> Player:
    return Player(name)
