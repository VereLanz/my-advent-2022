from my_advent.day9 import check_tail_movement as a
from my_advent.day9 import check_long_tail_movement as b


EXAMPLE_INPUT = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]

BIGGER_EXAMPLE_INPUT = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20",
]

def test_example_a():
    example_result = 13
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 1
    assert b(EXAMPLE_INPUT) == example_result
    

def test_example_b_bigger():
    example_result = 36
    assert b(BIGGER_EXAMPLE_INPUT) == example_result
