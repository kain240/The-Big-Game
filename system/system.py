from room import create_room, Room
import player
import logging
import uuid

logger = logging.getLogger()

class System:
    active_rooms: list[Room]
    archived_rooms: list[Room]

    registered_players: list[player.Player]
    active_players: dict[uuid.UUID: any]

    def __init__(self):
        self.active_rooms = []
        self.active_players_id = []
        self.registered_players = []

    def create_room(self, owner_id):
        new_room = create_room(owner_id)
        self.active_rooms.append(new_room)
        logger.info(f"room {new_room.id} created by {owner_id}")

    def get_rooms(self, room_id: str):
        if room_id is None:
            return self.active_rooms
        else:
            return [room for room in self.active_rooms if room.id.hex == room_id]

    def __archive_room__(self, room_id: uuid.UUID):
        for room in self.active_rooms:
            if room.id == room_id or room.id.hex == room_id:
                self.archived_rooms.append(room)
                self.active_rooms.remove(room)
                break

    def player_login(self, player_id: str) -> player.Player:
        for player in self.registered_players:
            if player.id.hex == player_id:
                return player

    def register_player(self, name: str):
        player.
