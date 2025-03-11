from system import System

game_system = System()

game_system.register_player('vaibhav')
player1 = game_system.player_login('vaibhav')

game_system.register_player('khushi')
player2 = game_system.player_login('khushi')

new_room_id = game_system.create_room(player1.id)
room = game_system.get_rooms(room_id=new_room_id)[0]

room.join(player1)
room.join(player2)

room.start_game()

room.end_game()
