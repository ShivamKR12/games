"dhruv secret code dont leak it"
# Set up the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Set up the players
players = [":)", ":("]
current_player = 0

# Set up the game loop
while True:
    # Print the board
    print("-------------")
    for row in range(3):
        print("|", end="")
        for col in range(3):
            print(board[row][col], end="|")
        print()
        print("-------------")

    # Check for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            print(f"Player {players[current_player]} wins!")
            break
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            print(f"Player {players[current_player]} wins!")
            break
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f"Player {players[current_player]} wins!")
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"Player {players[current_player]} wins!")

    # Check for a tie
    if all(all(cell != " " for cell in row) for row in board):
        print("It's a tie!")
        break

    # Get the player's move
    while True:
        try:
            row = int(input(f"Player {players[current_player]}, enter the row (0-2): "))
            col = int(input(f"Player {players[current_player]}, enter the column (0-2): "))
            if board[row][col] == " ":
                break
            else:
                print("That space is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

    # Make the move
    board[row][col] = players[current_player]

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Clean up
print("Thanks for playing!")