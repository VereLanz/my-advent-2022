import pytest

from my_advent.day_template import a as a
from my_advent.day_template import b as b

EXAMPLE_INPUT = [
    0,
]


@pytest.mark.skip
def test_example_a():
    example_result = 0
    assert a(EXAMPLE_INPUT) == example_result


@pytest.mark.skip
def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
