"""File to define Fish class."""

__author__ = "730697392"


class Fish:
    """Class for fish."""

    age: int

    def __init__(self):
        """Initializes a new Fish object with a default age of 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increases the age of the fish."""
        self.age += 1
        return None