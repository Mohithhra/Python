import random

print("Dice Game: Player vs Computer")

player_score = 0
computer_score = 0
rounds = 5

for i in range(1, rounds + 1):
    print("\nRound", i)
    input("Press Enter to roll the dice...")

    player = random.randint(1, 6)
    computer = random.randint(1, 6)

    print("Your dice:", player)
    print("Computer dice:", computer)

    if player > computer:
        print("You win this round")
        player_score += 1
    elif player < computer:
        print("Computer wins this round")
        computer_score += 1
    else:
        print("Round is a tie")

print("\nFinal Score")
print("You:", player_score)
print("Computer:", computer_score)

if player_score > computer_score:
    print("You are the overall winner!")
elif player_score < computer_score:
    print("Computer is the overall winner!")
else:
    print("The game is a tie!")