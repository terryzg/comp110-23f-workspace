"""EX02 - Structured Wordle."""

__author__ = "730697392"


def contains_char(string1: str, character: str) -> bool:
    """Find out if a character is in the word."""
    assert len(character) == 1
    int = 0
    while int < len(string1):
        if string1[int] == character:
            return True
        int += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret_word: str) -> str:
    """Shows the color boxes for the word."""
    assert len(guess) == len(secret_word)
    index: int = 0
    emoji = ""
    while index < len(guess):
        if secret_word[index] == guess[index]: 
            emoji += GREEN_BOX
            index += 1
        elif contains_char(secret_word, guess[index]):
            emoji += YELLOW_BOX
            index += 1
        else:
            emoji += WHITE_BOX
            index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Tells you the length and if the length is wrong."""
    guess_word = input(f"Enter a {expected_length} character word:")
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 0
    max_turns: int = 6
    game_over: bool = False
    secret_word: str = "codes"
    while turns < max_turns and not game_over:
        print(f"=== Turn {turns + 1}/{max_turns} ===")
        guess_word = input_guess(len(secret_word))
        emoji_return = emojified(secret_word, guess_word)
        print(emoji_return)
        if emoji_return == GREEN_BOX * len(secret_word):
            print(f"You won in {turns + 1}/{max_turns} turns!")
            game_over = True
        turns += 1
        
        if not game_over:
            print(f"X/{max_turns} - Sorry, try again tommorow")


if __name__ == "__main__":
    main()