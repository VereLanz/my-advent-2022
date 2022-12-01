import pytest

from my_advent.day1 import a as a
from my_advent.day1 import b as b

EXAMPLE_INPUT = [
    0,
]


@pytest.skip
def test_example_one():
    example_result = 0
    assert a(EXAMPLE_INPUT) == example_result


@pytest.skip
def test_example_two():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
