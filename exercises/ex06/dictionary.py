"""EX06 - Dictionaries."""

__Author__ = "730697392"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts a dict and returns a Keyerror if there is more than 1 of a key."""
    invert_dict: dict[str, str] = {}
    for i in input:
        invert_dict[input[i]] = i
    if len(input) != len(invert_dict):
        raise KeyError("You cannot have more than 1 of each key.")
    return invert_dict


def favorite_color(input: dict[str, str]) -> str:
    """Finds the value that appears most frequently."""
    color: dict[str, int] = {}
    numb: int = 0
    for i in input:
        if input[i] in color:
            color[input[i]] += 1
        else:
            color[input[i]] = 1
    for elem in color:
        if color[elem] > numb:
            numb = color[elem]
    for e in color:
        if color[e] == numb:
            return e
    return str


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in the input list by returning a dictionary."""
    count_dict: dict[str, int] = {}
    for i in input:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary that will organize each index into a list according to its first letter."""
    dictionary: dict[str, list[str]] = {}
    for i in input:
        first_letter = i[0].lower()
        if first_letter not in dictionary:
            dictionary[first_letter] = [i]
        else:
            dictionary[first_letter].append(i)
    return dictionary


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Returns a dictionary of updates the values based on the associated key."""
    if day in input:
        if student not in input[day]:
            input[day].append(student)
    else:
        input[day] = [student]
    return input
