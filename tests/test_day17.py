from my_advent.day17 import predict_stone_tower_height as a
from my_advent.day17 import predict_stone_tower_height_efficiently as b


EXAMPLE_INPUT = [
    ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>",
]


def test_example_a():
    example_result = 3068
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 1514285714288
    assert b(EXAMPLE_INPUT) == example_result
