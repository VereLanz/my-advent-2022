import pytest

from my_advent.day1 import find_most_calories as a
from my_advent.day1 import find_top3_calories as b

EXAMPLE_INPUT = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


def test_example_a():
    example_result = 24000
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 45000
    assert b(EXAMPLE_INPUT) == example_result
