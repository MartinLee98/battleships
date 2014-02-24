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
	'aircraft carrier':5,
	'battleship':4,
	'submarine':3,
	'destroyer':3,
	'patrol boat':2
}