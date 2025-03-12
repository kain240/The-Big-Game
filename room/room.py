from uuid import UUID, uuid4
import game
import players


class Room:
    _players: list[players.ActivePlayer]
    _owner_id: UUID
    _game: game.Game

    def __init__(self, owner_id: UUID):
        self._id = uuid4()
        self._players = []
        self._owner_id = owner_id

    @property
    def id(self):
        return self._id

    def _announce(self, player: players.ActivePlayer, message: str):
        for active_player in self._players:
            active_player.websocket_connection.send(f"{player.player_info.name} : {message}")

    def _individual_message(self, player_id: UUID, message: str):
        for active_player in self._players:
            if active_player.player_info.id == player_id:
                active_player.websocket_connection.send(message)

    def join(self, active_player: players.ActivePlayer):
        if active_player.player_info.id != self._owner_id:
            # validate the join request
            pass

        self._players.append(active_player)
        self._announce(f"player: {active_player.player_info.name} is added")

    def init_game(self, config: dict):
        self._game.configure(config)

    def start_game(self):
        self._game.start()
        while self._game.status != game.Status.Ended:
            self._game.validate()
            self._game.proceed()

    def result(self):
        self._game.result()

    def remove_player(self, player_id: UUID):
        pass

    def _allow_player(self, player_id):
        pass

    def message(self, player: players.ActivePlayer, message: str):
        self._announce(player, message)
