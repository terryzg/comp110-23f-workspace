"""EX06 - Dictionaries-tests."""

__Author__ = "730697392"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


# tests for invert
def test_invert_empty() -> None:
    """Testing a dictionary with 0 elements."""
    input_dict = {}
    expected_dict = {}
    assert invert(input_dict) == expected_dict


def test_invert_1() -> None:
    """Testing a dictionary with 1 element for the key and value."""
    input_dict = {'dog': 'happy'}
    expected_dict = {'happy': 'dog'}
    assert invert(input_dict) == expected_dict


def test_invert_multiple() -> None:
    """Testing a dictionary with multiple elements."""
    input_dict = {'dog': 'happy', 'life': 'living', 'TV': 'watching'}
    expected_dict = {'happy': 'dog', 'living': 'life', 'watching': 'TV'}
    assert invert(input_dict) == expected_dict


# tests for favorite_color
def test_favorite_color_empty() -> None: 
    """Testing a dictionary with 0 elements."""
    input = {}
    output = (str)
    assert favorite_color(input) == output


def test_favorite_color_multiple() -> None:
    """Testing a dictionary with multiple elements and with 1 pair of the same values."""
    input = {'Mary': 'blue', 'Ezri': 'yellow', 'Kris': 'blue', 'John': 'green'}
    output = ('blue')
    assert favorite_color(input) == output


def test_favorite_color_tie() -> None:
    """Testing a dictionary with multiple elements and with 2 pairs of the same values."""
    input = {'Mary': 'blue', 'Ezri': 'yellow', 'Kris': 'blue', 'John': 'yellow'}
    output = ('blue')
    assert favorite_color(input) == output


# tests for count
def test_count_empty() -> None:
    """Testing a list with 0 elements."""
    input = []
    output = {}
    assert count(input) == output


def test_count_multiple() -> None:
    """Testing a list with multiple different elements."""
    input = ['Water', 'Bread', 'Meat', 'Vegetables']
    output = {'Water': 1, 'Bread': 1, 'Meat': 1, 'Vegetables': 1}
    assert count(input) == output


def test_count_1() -> None:
    """Testing a list with multiple element, with some being the same."""
    input = ['Water', 'Bread', 'Meat', 'Vegetables', 'Water']
    output = {'Water': 2, 'Bread': 1, 'Meat': 1, 'Vegetables': 1}
    assert count(input) == output


# tests for alphabetizer
def test_alphabetizer_empty() -> None:
    """Testing a list with 0 elements."""
    input = []
    output = {}
    assert alphabetizer(input) == output


def test_alphabetizer_multiple() -> None:
    """Testing a list with multiple different elements."""
    input = ['class', 'homework', 'study']
    output = {'c': ['class'], 'h': ['homework'], 's': ['study']}
    assert alphabetizer(input) == output


def test_alphabetizer_multiple_same() -> None:
    """Testing a list with multiple elements with some of them being the same."""
    input = ['class', 'homework', 'study', 'celebration', 'happy']
    output = {'c': ['class', 'celebration'], 'h': ['homework', 'happy'], 's': ['study']}
    assert alphabetizer(input) == output


# tests for update_attendance
def test_update_attendance_empty() -> None:
    """Testing a dict with 0 elements and is updated with elements."""
    input = {}
    update = update_attendance(input, "Monday", "Beyonce")
    output = {'Monday': ['Beyonce']}
    assert update == output


def test_update_attendance_update() -> None:
    """Testing a dict with multiple elements and is updated with elements."""
    input = {'Monday': ['Beyonce', 'Tommy'], 'Tuesday': ['James']}
    update = update_attendance(input, "Tuesday", "Beyonce")
    output = {'Monday': ['Beyonce', 'Tommy'], 'Tuesday': ['James', 'Beyonce']}
    assert update == output


def test_update_attendance_new_day() -> None:
    """Testing a dict with multiple elements and updates a new key and value."""
    input = {'Monday': ['Beyonce', 'Tommy'], 'Tuesday': ['James']}
    update = update_attendance(input, "Wednesday", "Beyonce")
    output = {'Monday': ['Beyonce', 'Tommy'], 'Tuesday': ['James'], 'Wednesday': ['Beyonce']}
    assert update == output