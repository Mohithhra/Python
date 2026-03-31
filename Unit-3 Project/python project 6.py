import random

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Rock – Paper – Scissors Game")

    while True:
        user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user == "exit":
            print("Game ended.")
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer = computer_choice()

        print("You chose:", user)
        print("Computer chose:", computer)

        result = check_winner(user, computer)
        print(result)
        print()

play_game()