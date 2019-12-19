#   Jordan Chou
#   Dec. 18, 2019
#   A game of Hangman with a random word

import random
import string

# Print the game board
def printHangman(word, letters):
    i = 0
    while i < len(word):    # Iterate through the word
        if word[i] in letters:   # Check if in letters guessed
            print(word[i] + " ", end = '') # print letter
        else:
            print("_ ", end = '')   # print blank
        i += 1
    print("\tGuesses: " + " ".join(letters)) # Separate guesses with a space

# Select a random word from 'words.txt'
file = open("words.txt", "r")
words = file.readlines()
word = random.choice(words).rstrip()

MAX_GUESSES = 6

numGuesses = 0
lettersGuessed = ""

solved = False

print("Welcome to Hangman!")
print("Try to guess the word with less than 6 mistakes!")

while numGuesses < MAX_GUESSES and solved is False:
    print()

    printHangman(word, lettersGuessed)

    print("\n\nNumber of Wrong Guesses: " + str(numGuesses))

    # error check to see if letter was already guessed or not a letter
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in lettersGuessed:
            print("You have already guessed that letter. Try again\n")
        elif guess not in string.ascii_letters:
            print("Invalid entry. Try again\n")
        else:
            break
    lettersGuessed += guess

    if guess in word:
        print("\n\t>> You guessed correctly! <<")
    else:
        print("\n\t-- That letter is not in the word --")
        numGuesses += 1

    # get distinct letters in word and check if is subset of guessed letters
    if set(word) <= set(lettersGuessed):
        solved = True
    else:
        continue

print()
printHangman(word, lettersGuessed)

if numGuesses <= MAX_GUESSES and solved :
    print("\n\nNice! You guessed the word with " + str(numGuesses) + " mistake", end = '')
    if numGuesses == 1:
        print("!")
    else:
        print("s!")
else:
    print("\n\nOh no! You did not guess the word")
    print("The word was " + word)
