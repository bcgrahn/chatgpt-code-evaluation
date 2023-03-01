

# Noughts and Crosses game in Python

# We will use a 3x3 board
board = [["_","_","_"],["_","_","_"],["_","_","_"]]

# Print the board
def print_board():
  for row in board:
    print(row)

# Check for a winner
def check_win(player):
  # Check for horizontal win
  for row in board:
    if row == [player,player,player]:
      return True
  # Check for vertical win
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # Check for diagonal win
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

# Main game loop
player = "X"
while True:
  print_board()
  # Get input from the player
  valid_input = False
  while not valid_input:
    row = int(input("Enter a row (0, 1, 2): "))
    col = int(input("Enter a column (0, 1, 2): "))
    if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == "_":
      board[row][col] = player
      valid_input = True
    else:
      print("Invalid input. Try again.")
  # Check for a winner
  if check_win(player):
    print_board()
    print(player + " wins!")
    break
  # Switch players
  if player == "X":
    player = "O"
  else:
    player = "X"