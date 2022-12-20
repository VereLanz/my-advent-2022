from my_advent.day19 import a as a
from my_advent.day19 import b as b


EXAMPLE_INPUT = [
    "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
    "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.", 
]


def test_example_a():
    example_result = 33
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
