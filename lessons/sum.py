"""Summing the elements of a list using different loops."""

__author__ = "730697392"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all the values in the list using while function."""
    i: int = 0
    total: float = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all the values in the list using for .. in .. function."""
    total: float = 0
    for numb in vals:
        total += numb
    return total


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all the values in the list using for .. in range .. function."""
    total: float = 0
    for numb in range(len(vals)):
        total += vals[numb]
    return total