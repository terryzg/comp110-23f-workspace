"""Combining two lists into a dictionary."""

__Author__ = "730697392"


def zip(word: list[str], number: list[int]) -> dict[str, int]:
    """Produces a dictionary with a string and int values."""
    if len(word) != len(number):
        return {}
    if len(word) == 0 and len(number) == 0:
        return {}
    dict = {word[i]: number[i] for i in range(len(word))}
    return dict