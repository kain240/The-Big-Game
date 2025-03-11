import uuid
from Players.players import Player

class Room:
    def __init__(self, owner_id):
        self.id = str(uuid.uuid4())
        self.players = []
        self.owner_id = owner_id
        self.game_instance = None
        self.status = "waiting"

    def add_player(self):
        player = Player()
        self.players.append(player.id)
        print(f"player {player.id} is added")

    def remove_player(self):
        self.players.remove(id)

    def start_game(self):
        pass

    def update_game_status(self):
        pass

    def allow_player(self, player_id):
        pass


