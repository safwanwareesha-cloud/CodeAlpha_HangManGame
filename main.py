import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "keyboard"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses available.")

# Main game loop
while incorrect_guesses < max_incorrect_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    # Check if the player has guessed the whole word
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The word was:", word)