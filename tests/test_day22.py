from my_advent.day22 import find_password_from_map as a
from my_advent.day22 import b as b


EXAMPLE_INPUT = [
    "        ...#",
    "        .#..",
    "        #...",
    "        ....",
    "...#.......#",
    "........#...",
    "..#....#....",
    "..........#.",
    "        ...#....",
    "        .....#..",
    "        .#......",
    "        ......#.",
    "",
    "10R5L5R10L4R5L5",
]


def test_example_a():
    example_result = 6032
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
