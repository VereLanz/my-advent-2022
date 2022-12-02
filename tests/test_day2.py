import pytest

from my_advent.day2 import calculate_points_for_strategy as a
from my_advent.day2 import b as b

EXAMPLE_INPUT = [
    "A Y",
    "B X",
    "C Z",
]


def test_example_a():
    example_result = 15
    assert a(EXAMPLE_INPUT) == example_result


@pytest.mark.skip
def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
