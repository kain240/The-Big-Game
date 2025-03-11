from uuid import UUID, uuid4
import game_interface

class Room:
    _player_ids: list[UUID]
    _owner_id: UUID
    _game: game_interface.Game

    def __init__(self, owner_id: UUID):
        self._id = uuid4()
        self._player_ids = [owner_id]
        self._owner_id = owner_id

    def _announce(self, message: str):
        pass

    def _individual_message(self, player_id: UUID, message: str):
        pass

    def join(self, player_id: UUID):
        if player_id != self._owner_id:
            # validate the join request
            pass

        self._player_ids.append(player_id)

    def add_player(self, player_id: UUID):
        self._player_ids.append(player_id)
        self._announce(f"player {player_id} is added")

    def remove_player(self, player_id: UUID):
        self._player_ids.remove(player_id)

    def start_game(self):
        self._game.start()

    def _allow_player(self, player_id):
        pass

    def end_game(self):
        pass
