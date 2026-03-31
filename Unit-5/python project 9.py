import random

with open("words.txt", "r") as f:
    words = f.read().splitlines()

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Hangman Game")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", ", ".join(used_letters))

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single valid letter.")
        continue

    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Correct")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong")
        attempts -= 1

if "_" not in guessed:
    print("You Win. The word is:", word)
else:
    print("You Lose. The word was:", word)