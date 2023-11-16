"""Test my zip function."""

__author__ = "730697392"

from lessons.zip import zip


def test_empty_dict():
    """Testing a dictionary with 0 elements for each value."""
    assert zip([], []) == {}


def test_list_1():
    """Testing a dictionary with 1 element for both values."""
    word_list = ["happy"]
    number_list = [1]
    expected_dict = {'happy': 1}
    assert zip(word_list, number_list) == expected_dict


def test_list_unequal():
    """Testing a list with 3 elements for both values."""
    word_list = ["happy", "birthday", "mom"]
    number_list = [1, 2, 3]
    expected_dict = {'happy': 1, 'birthday': 2, 'mom': 3}
    assert zip(word_list, number_list) == expected_dict