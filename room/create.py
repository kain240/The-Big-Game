from .room import Room

def create_room(owner_id) -> Room:
    return Room(
        owner_id=owner_id
    )
