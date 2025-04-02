import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main program
print("Welcome to Rock, Paper, Scissors!")

# Game loop
while True:
    player_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to stop): ").lower()
    
    if player_choice == 'quit':
        print("Thanks for playing!")
        break
    
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input, please choose rock, paper, or scissors.")
        continue
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)
