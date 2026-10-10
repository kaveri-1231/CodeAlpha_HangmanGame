
import random

# List of predefined words
words = ["python", "computer", "program", "developer", "coding"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses allowed
max_attempts = 6
wrong_guesses = 0

print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)
print("Guess the hidden word one letter at a time!")
print("You can make a maximum of 6 incorrect guesses.")

while wrong_guesses < max_attempts:
    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - wrong_guesses)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("You won the game!")
        break

    guess = input("Enter a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Display the final result
else:
    print("\nYou have used all 6 incorrect guesses.")
    print("The correct word was:", secret_word)
    print("Game over! Better luck next time.")
