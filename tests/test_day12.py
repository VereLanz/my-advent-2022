from my_advent.day12 import find_shortest_hike_up as a
from my_advent.day12 import find_scenic_hike_up as b


EXAMPLE_INPUT = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]


def test_example_a():
    example_result = 31
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 29
    assert b(EXAMPLE_INPUT) == example_result
