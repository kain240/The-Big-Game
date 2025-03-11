import uuid

class Player:

    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
