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
            x, y = get_coordinates()
            orientation = v_or_h()
            valid = validate(board, ships[ship], x, y, orientation)

            if not valid:
                print("Cannot place a ship there.\nPlease take a look at the board and try again.")
                input("Hit ENTER to continue...")

        board = place_ship(board, ships[ship], ship[0], x, y, orientation)
        print_board('u', board)

    input("Done placing user ships. Hit ENTER to continue...")
    return board


def get_coordinates():
    while True:
        user_input = input("Please enter coordinates (row,col)?")
        try:
            coords = user_input.split(',')
            if len(coords) != 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            coords[0] = int(coords[0])-1
            coords[1] = int(coords[1])-1

            if coords[0] > 9 or coords[0] < 0 or coords[1] > 9 or coords[1] < 0:
                raise Exception("Invalid entry. Please use values between 1 to 10 only.")

            return coords
        except ValueError:
            print("Invalid entry. Please enter only numeric values for coordinates.")
        except Exception as e:
            print(e)


def v_or_h():
    while True:
        user_input = input("Vertical or horizontal (v or h)?")

        if user_input == 'v' or user_input == 'h':
            return user_input
        else:
            print("Invalid input. Please only enter \"v\" or \"h\"")


def validate(board, ship, x, y, orientation):
    if orientation == 'v' and x + ship > 10:
        return False
    elif orientation == 'h' and y + ship > 10:
        return False
    else:
        if orientation == 'v':
            for i in range(ship):
                if board[x+i][y] != -1:
                    return False
        elif orientation == 'h':
            for i in range(ship):
                if board[x][y+i] != -1:
                    return False


def place_ship(board, ship, s, x, y, orientation):
    if orientation == 'v':
        for i in range(ship):
            board[x+i][y] = s
    elif orientation == 'h':
        for i in range(ship):
            board[x][y+i] = s

    return board
