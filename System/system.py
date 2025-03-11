from rooms.room import Room
import logging

logger = logging.getLogger()

class System:
    def __init__(self):
        self.rooms = []

    def create_room(self, owner_id):
        room = Room(owner_id)
        self.rooms.append(room.id)
        print(f"room {room.id} created by {owner_id}")

    def search_room(self):
        print("active rooms/n")
        for i in self.rooms:
            print(i)

    def __archive_room__(self):
        pass

    def player_login(self):
        pass
