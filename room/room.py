from uuid import UUID, uuid4
import game
import player


class Room:
    _players: list[player.ActivePlayer]
    _owner_id: UUID
    _game: game.Game

    def __init__(self, owner_id: UUID):
        self._id = uuid4()
        self._players = []
        self._owner_id = owner_id

    def _announce(self, message: str):
        pass

    def _individual_message(self, player_id: UUID, message: str):
        pass

    def join(self, active_player: player.ActivePlayer):
        if active_player.player_info.id != self._owner_id:
            # validate the join request
            pass

        self._players.append(active_player)
        self._announce(f"player: {active_player.player_info.name} is added")

    # def remove_player(self, player_id: UUID):
    #     self._players.remove(player_id)

    def start_game(self):
        self._game.start()
        while self._game.status != game.Status.Ended:
            self._game.validate()
            self._game.proceed()

    def _allow_player(self, player_id):
        pass

    def end_game(self):
        pass

    @property
    def id(self):
        return self._id
