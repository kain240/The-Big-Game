import uuid

class Player:
    current_room: uuid.UUID

    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
        self.is_active = True
