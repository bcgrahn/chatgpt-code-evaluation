

# This is a noughts and crosses game for two players

# Create the board
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

# Print the board
def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[6], '|', board[7], '|', board[8])

# Function to check if someone has won
def check_win():
    # Check horizontal
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]
    # Check vertical
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    # Check diagonal
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]
    else:
        return None

# Function to check if the board is full
def check_full():
    for i in board:
        if i != 'X' and i != 'O':
            return False
    return True

# Main game loop
player = 'X'
while True:
    print_board()
    # Get player input
    position = int(input('Player ' + player + ', choose a position (1-9): '))
    # Check if position is valid
    if position > 0 and position < 10:
        if board[position-1] != 'X' and board[position-1] != 'O':
            board[position-1] = player
            # Check for win
            if check_win() == 'X' or check_win() == 'O':
                print_board()
                print('Player', player, 'wins!')
                break
            # Check for draw
            if check_full():
                print_board()
                print('Draw!')
                break
            # Switch player
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print('Position taken!')
    else:
        print('Please choose a valid position (1-9)')