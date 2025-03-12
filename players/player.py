import uuid

class Player:

    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name

    def set_online(self, websocket):
        return ActivePlayer(self, websocket)


class ActivePlayer:
    player_info: Player
    websocket_connection: any

    def __init__(self, player_info: Player, websocket):
        self.websocket_connection = websocket
        self.player_info = player_info
