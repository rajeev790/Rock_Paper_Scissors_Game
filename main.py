
import random

# Function to determine the winner based on user's choice and computer's choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    return "Computer wins!"

# Main game loop
def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # Get the user's choice
        user_choice = input("Enter rock, paper, or scissors (or type 'quit' to stop playing): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        # Get the computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

if __name__ == "__main__":
    play_game()
