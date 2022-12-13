from my_advent.day13 import find_right_order_pairs as a
from my_advent.day13 import find_decoder_key as b


EXAMPLE_INPUT = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]",
]


def test_example_a():
    example_result = 13
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 140
    assert b(EXAMPLE_INPUT) == example_result
