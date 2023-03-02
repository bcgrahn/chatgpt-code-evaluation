

#Define the board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

#Define the print board function
def print_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#Define the check win function
def check_win():
  #Check for row wins
  row_win = ((board[0] == board[1] == board[2] != "_") or 
             (board[3] == board[4] == board[5] != "_") or 
             (board[6] == board[7] == board[8] != "_"))
  #Check for column wins
  col_win = ((board[0] == board[3] == board[6] != "_") or 
             (board[1] == board[4] == board[7] != "_") or 
             (board[2] == board[5] == board[8] != "_"))
  #Check for diagonal wins
  diag_win = ((board[0] == board[4] == board[8] != "_") or 
              (board[2] == board[4] == board[6] != "_"))
  #Return the result
  if row_win or col_win or diag_win:
    return True
  else:
    return False

#Define the main game loop
game_on = True
player = "X"
while game_on:
  print_board()
  #Get the player input
  position = int(input("Player " + player + ", choose a position (1-9): "))
  #Check if the position is valid
  if board[position-1] == "_":
    board[position-1] = player
    #Check if the player has won
    if check_win():
      print("Player " + player + " has won!")
      game_on = False
    #Switch players
    if player == "X":
      player = "O"
    else:
      player = "X"
  else:
    print("Position already taken!")