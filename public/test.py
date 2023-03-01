import random

def print_board(board):
   
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print("+---+---+---+")

def get_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def play_game():
  
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print("Player", current_player)
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = get_winner(board)
            if winner:
                print_board(board)
                print(winner, "wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board(board)
                print("Draw!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That space is already taken. Please try again.")

if __name__ == "__main__":
    play_game()
 