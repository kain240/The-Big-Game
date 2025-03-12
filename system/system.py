from room import create_room, Room
import players
import logging
import uuid

logger = logging.getLogger()

class System:
    _active_rooms: list[Room]
    _archived_rooms: list[Room]

    _registered_players: list[players.Player]
    _active_players_id: dict[uuid.UUID: any]

    def __init__(self):
        self._active_rooms = []
        self._active_players_id = []
        self._registered_players = []

    def create_room(self, owner_id: uuid.UUID) -> str:
        new_room = create_room(owner_id)
        self._active_rooms.append(new_room)
        logger.info(f"room {new_room.id} created by {owner_id}")
        return new_room.id.hex

    def get_rooms(self, room_id: str):
        if room_id is None:
            return self._active_rooms
        else:
            return [room for room in self._active_rooms if room.id.hex == room_id]

    def _archive_room(self, room_id: uuid.UUID):
        for room in self._active_rooms:
            if room.id == room_id or room.id.hex == room_id:
                self._archived_rooms.append(room)
                self._active_rooms.remove(room)
                break

    def player_login(self, player_name: str) -> players.ActivePlayer:
        for registered_player in self._registered_players:
            if registered_player.name == player_name:
                return players.ActivePlayer(registered_player, None)

    def register_player(self, name: str):
        new_player = players.register(name)
        self._registered_players.append(new_player)
