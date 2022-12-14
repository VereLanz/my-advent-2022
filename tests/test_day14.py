from my_advent.day14 import fill_cave_with_sand as a
from my_advent.day14 import b as b


EXAMPLE_INPUT = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9",
]


def test_example_a():
    example_result = 24
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
