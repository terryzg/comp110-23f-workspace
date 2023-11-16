"""EX02 - Wordle."""

__author__ = "730697392"

secret_word: str = "python"

numb: int = 0

guess_word: str = input("What is your 6 letter guess?")

color_boxes = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#  input "" if the length of the guess word is not 6
while len(guess_word) != 6:
    guess_word = input("That was not 6 letters! Try Again:")

#  print out white, yellow, or white boxes depending on whether or not the character matches or is in the secret word
while numb < len(secret_word):
    if guess_word[numb] == secret_word[numb]:
        color_boxes += GREEN_BOX
    else:
        falsa = False
        int = 0
        while not falsa and int < len(secret_word):
            if secret_word[int] == guess_word[numb]:
                falsa = True
            else:
                int += 1
        if falsa:
            color_boxes += YELLOW_BOX
        else:
            color_boxes += WHITE_BOX
    numb = numb + 1
print(color_boxes)

#  print "" if the guess is correct
if guess_word == secret_word:
    print("Woo! You got it!")

#  print "" if guess is incorrect
if guess_word != secret_word:
    print("Not quite. Play again soon!")