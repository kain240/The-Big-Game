import uuid
from .room import Room

def create_room(owner_id: uuid.UUID) -> Room:
    return Room(
        owner_id=owner_id
    )
