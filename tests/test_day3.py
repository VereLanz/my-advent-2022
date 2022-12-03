import pytest

from my_advent.day3 import prioritise_rucksacks as a
from my_advent.day3 import prioritise_badges as b

EXAMPLE_INPUT = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def test_example_a():
    example_result = 157
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 70
    assert b(EXAMPLE_INPUT) == example_result
