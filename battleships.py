import copy


board = []

for i in range(10):
	board_row = []
	for j in range(10):
		board_row.append(-1)
	board.append(board_row)

user_board = copy.deepcopy(board)
comp_board = copy.deepcopy(board)
ships = {
	'aircraft carrier': 5,
	'battleship': 4,
	'submarine': 3,
	'destroyer': 3,
	'patrol boat': 2
}

def user_place_ships(board, ships):
	for ship in ships.keys():
		valid = False

		while not valid:
			print_board('u', board)
			print("Placing a/an " + ship)
			x,y = get_coords()
			orientation = v_or_h()
			valid = validate(board, ships[ship], x, y, orientation)

			if not valid:
				print("Cannot place a ship there.\nPlease take a look at the board and try again.")
				raw_input("Hit ENTER to continue...")

		board = place_ship(board, ships[ship], ship[0], x, y, orientation)
		print_board('u', board)

	raw_input("Done placing user ships. Hit ENTER to continue...")
	return board