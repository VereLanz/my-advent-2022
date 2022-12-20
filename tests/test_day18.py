from my_advent.day18 import find_droplet_surface_area as a
from my_advent.day18 import find_droplet_outer_surface_area as b


EXAMPLE_INPUT = [
    "2,2,2",
    "1,2,2",
    "3,2,2",
    "2,1,2",
    "2,3,2",
    "2,2,1",
    "2,2,3",
    "2,2,4",
    "2,2,6",
    "1,2,5",
    "3,2,5",
    "2,1,5",
    "2,3,5",
]
MORE_EXAMPLE_INPUT = [
    "1,1,1",
    "2,1,1",
    "3,1,1",
    "4,1,1",
    "5,1,1",
    "6,1,1",
    "1,2,1",
    "2,2,1",
    "3,2,1",
    "4,2,1",
    "5,2,1",
    "6,2,1",
    "1,3,1",
    "2,3,1",
    "3,3,1",
    "4,3,1",
    "5,3,1",
    "6,3,1",
    "1,1,2",
    "2,1,2",
    "3,1,2",
    "4,1,2",
    "5,1,2",
    "6,1,2",
    "1,2,2",
    "6,2,2",
    "1,3,2",
    "2,3,2",
    "3,4,2",  # changed from "3,3,2", = moved one cube to create +1 hole
    "4,3,2",
    "5,3,2",
    "6,3,2",
    "1,1,3",
    "2,1,3",
    "3,1,3",
    "4,1,3",
    "5,1,3",
    "6,1,3",
    "1,2,3",
    "2,2,3",
    "3,2,3",
    "4,2,3",
    "5,2,3",
    "6,2,3",
    "1,3,3",
    "2,3,3",
    "3,3,3",
    "4,3,3",
    "5,3,3",
    "6,3,3",
]


def test_example_a():
    example_result = 64
    assert a(EXAMPLE_INPUT) == example_result
    assert a(MORE_EXAMPLE_INPUT) == 116  # 108 without my addition


def test_example_b():
    example_result = 58
    assert b(EXAMPLE_INPUT) == example_result
    assert b(MORE_EXAMPLE_INPUT) == 94  # 90 without my addition
