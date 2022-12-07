from my_advent.day6 import find_packet_marker as a
from my_advent.day6 import find_message_marker as b


EXAMPLE_INPUT = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
]


def test_example_a():
    example_result = 7
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 19
    assert b(EXAMPLE_INPUT) == example_result
