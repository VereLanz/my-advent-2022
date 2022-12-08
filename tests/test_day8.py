from my_advent.day8 import count_visible_trees as a
from my_advent.day8 import find_highest_scenic_score as b


EXAMPLE_INPUT = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]


def test_example_a():
    example_result = 21
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 8
    assert b(EXAMPLE_INPUT) == example_result
