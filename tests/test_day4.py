from my_advent.day4 import count_full_section_overlaps as a
from my_advent.day4 import count_section_overaps as b


EXAMPLE_INPUT = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def test_example_a():
    example_result = 2
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 4
    assert b(EXAMPLE_INPUT) == example_result
