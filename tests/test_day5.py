from my_advent.day5 import reorganise_stacks as a
from my_advent.day5 import reorganise_stacks_multiple as b


EXAMPLE_INPUT = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_example_a():
    example_result = "CMZ"
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = "MCD"
    assert b(EXAMPLE_INPUT) == example_result
