def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the player has won the game."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def get_empty_positions(board):
    """Get a list of empty positions on the board."""
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def player_move(board, player):
    """Prompt the player to make a move."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if board[row][col] == " ":
                return row, col
            else:
                print("Position already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def computer_move(board, player):
    """Generate a random move for the computer."""
    row, col = random.choice(get_empty_positions(board))
    print(f"Computer ({player}) chooses row {row} and column {col}.")
    return row, col

def play_game():
    """Play a single game of Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)
    print_board(board)

    for _ in range(9):
        for player in players:
            if player == 'X':
                row, col = player_move(board, player)
            else:
                row, col = computer_move(board, player)
            board[row][col] = player
            print_board(board)
            if check_winner(board, player):
                print(f"Player {player} wins!")
                return
    else:
        print("It's a tie!")

def main():
    """Main function to start the game."""
    print("Welcome to Tic Tac Toe!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
