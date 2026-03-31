number = 7
guesses = []

print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter number: "))
    guesses.append(guess)

    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print("Correct!")
        break

print("Total attempts:", len(guesses))
print("Your guesses:", guesses)