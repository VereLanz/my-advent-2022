from my_advent.day20 import a as a
from my_advent.day20 import b as b


EXAMPLE_INPUT = [
    "1",
    "2",
    "-3",
    "3",
    "-2",
    "0",
    "4",
]


def test_example_a():
    example_result = 3
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
