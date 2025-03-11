import uuid

class Player:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.is_owner = False

    def join_room(self):
        pass

    def leave_room(self):
        pass

    def interact_with_room(self):
        pass

    def adjust_room_settings(self):
        pass