from uuid import UUID, uuid4
import game_interface

class Room:
    player_ids: list[UUID]
    owner_id: UUID
    game: game_interface.Game

    def __init__(self, owner_id):
        self.id = uuid4()
        self.player_ids = [owner_id]
        self.owner_id = owner_id

    def announce(self, message: str):
        pass

    def individual_message(self, player_id: UUID, message: str):
        pass

    def add_player(self, player_id: UUID):
        self.player_ids.append(player_id)
        self.announce(f"player {player_id} is added")

    def remove_player(self, player_id: UUID):
        self.player_ids.remove(player_id)

    def start_game(self):
        self.game.start()

    def allow_player(self, player_id):
        pass
