"""EX04 - Utils."""

__Author__ = "730697392"


def all(numbers: list[int], real_numb: int) -> bool:
    """Checks if the integers in the list matches the chosen integer."""
    integer: int = 0
    if len(numbers) == 0: 
        return False
    else:
        while integer < len(numbers):
            if numbers[integer] != real_numb:
                return False
            integer += 1
        return True


def max(input: list[int]) -> int:
    """Evaluates the max integer value in the list and displays an error if there is no integer."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    max_integer = input.pop()
    integer: int = 0
    while integer < len(input):
        current = input.pop()
        if current > max_integer:
            max_integer = current
    integer += 1
    return max_integer


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Checks if the integers in the first list matches the integers in the second list."""
    if len(l1) != len(l2):
        return False
    while len(l1) > 0:
        if l1.pop() != l2.pop():
            return False
    return True