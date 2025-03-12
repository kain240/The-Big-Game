import players

class Message:
    player: players.Player
    message: str

    def __init__(self, player_info, message):
        self.player = player_info
        self.message = message

class Chat:
    _messages: list[Message]

    def __init__(self):
        self._messages = []

    def new_message(self, player_info: players.Player, message: str):
        new_message = Message(
            player_info,
            message
        )
        self._messages.append(new_message)

