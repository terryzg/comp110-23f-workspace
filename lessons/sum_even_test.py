"""Testing my summation function."""

from lessons.sums_even import sums_even_list

def test_empty_sum():
    """sum_evens_list of empty list should be 0"""
    assert sums_even_list([]) == 0

def test_list_length_1():
    """Testing on a list with 1 element"""
    test_list: list[int] = [2]
    assert sums_even_list(test_list) == 2

def test_list_positives():
    """Testing sum on a list of positive integers"""
    test_list: list[int] = [1,2,3,4]
    assert sums_even_list(test_list) == 6