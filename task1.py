import random

# List of 5 predefined words
words = ["python", "computer", "program", "student", "coding"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
incorrect_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect guesses allowed.")
print()

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Attempts left:", max_attempts - incorrect_guesses)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You Win!")
        print("The word was:", secret_word)
        break

    # Take input from the player
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        print()
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You have already guessed this letter.")
        print()
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

    print()

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
