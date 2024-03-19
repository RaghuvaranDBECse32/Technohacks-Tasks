import random

def get_user_choice():
    """Get user's choice of rock, paper, or scissors."""
    user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice: ").strip().lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "Congratulations! You win!"
    else:
        return "Computer wins! Better luck next time."

def play_game():
    """Play a single game of rock, paper, scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    return play_again == 'yes'

def main():
    """Main function to play the game."""
    play = True
    while play:
        play = play_game()

if __name__ == "__main__":
    main()
