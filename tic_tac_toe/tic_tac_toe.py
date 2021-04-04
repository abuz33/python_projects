# --------------- Global Variables ---------------
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_is_still_going = True
current_player = 'X'
winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display initial board
    display_board()

    # While the game is still going
    while game_is_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player.
        flip_player()

    # game has ended
    if winner == "X" or winner == 'O':
        print(f"{winner} won the the game. Congrats!!!!")
    elif winner is None:
        print('Tie.')


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # Set up global variables
    global game_is_still_going

    # check if any of the rows ave all the same value(and it is not '-'
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_is_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return False


def check_columns():
    # Set up global variables
    global game_is_still_going

    # check if any of the rows ave all the same value(and it is not '-'
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_is_still_going = False

    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return False


def check_diagonals():
    # Set up global variables
    global game_is_still_going

    # check if any of the rows ave all the same value(and it is not '-'
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    if diagonal_1 or diagonal_2:
        game_is_still_going = False

    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return False


def check_if_tie():
    global game_is_still_going
    if '-' not in board:
        game_is_still_going = False
        return

    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def handle_turn(player):
    print(player+"'s turn.")
    while True:
        try:
            position = int(input("Choose a position from 1-9: ")) - 1
            if position > 9 or position < 0:
                print('You have to add a number between 1 and 9.')
                continue
            elif board[position] != '-':
                print('Choose an empty place!!!!')
            else:
                break
        except ValueError:
            print('You have to write a number.')

    board[position] = player
    display_board()


play_game()

# board
# display board

# play game
# handle turn
# check win
# check row
# check column
# check diagonals
# check tie
# flip player
