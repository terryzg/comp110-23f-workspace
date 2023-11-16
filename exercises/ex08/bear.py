"""File to define Bear class."""

__author__ = "730697392"


class Bear:
    """Class for bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes a new Fish object with a default age and hunger score of 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increases the age of the bear and decreases the hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases the hunger score of the bear based on the number of fish."""
        self.hunger_score += num_fish
        return None