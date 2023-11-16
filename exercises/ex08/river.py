"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730697392"


class River:
    """Class for river."""
    
    day: int
    bears: list()
    fish: list()

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Updates the lists to have only surviving fish and bears."""
        new_fish_count: list[Fish] = list()
        new_bear_count: list[Bear] = list()
        for f in self.fish:
            if f.age <= 3:
                new_fish_count.append(f)
        for b in self.bears:
            if b.age <= 5:
                new_bear_count.append(b)
        self.fish = new_fish_count
        self.bears = new_bear_count
        return None
    
    def bears_eating(self):
        """Creates values for the bears to eat fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def remove_fish(self, amount: int):
        """Remove amount number of Fish from the River."""
        self.fish = self.fish[amount:]
    
    def check_hunger(self):
        """Updates the list of bears as some die due to hunger."""
        new_bear_count: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bear_count.append(bear)
        self.bears = new_bear_count
        return None
    
    def repopulate_fish(self):
        """Repopulates fish."""
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4
        for x in range(num_new_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """Repopulates bears."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2
        for x in range(num_new_bears):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None

    def view_river(self):
        """Prints the population details."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
     
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulates the River simulation for a length of one week."""
        for day in range(7):
            self.one_river_day()
