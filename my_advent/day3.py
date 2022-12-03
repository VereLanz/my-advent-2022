from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


LOWER_OFFSET = ord("a") - 1  # a - z ->  1 - 26
UPPER_OFFSET = ord("A") - 27  # A - Z -> 27 - 52


def get_priority(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - UPPER_OFFSET
    return ord(letter) - LOWER_OFFSET


def find_rucksack_priority(contents: str) -> int:
    median = len(contents) // 2
    # exactly one letter will be in both halves
    misplaced: str = set(contents[:median]).intersection(set(contents[median:])).pop()
    return get_priority(misplaced)


def prioritise_rucksacks(inputs: list[str]) -> int:
    priorities = map(find_rucksack_priority, inputs)
    return sum(priorities)


def find_badge_priority(group_contents: list[str]) -> int:
    contents = [set(c) for c in group_contents]
    # exactly one letter appears in each of the three strings (possibly more than once)
    group_item = contents[0].intersection(contents[1]).intersection(contents[2]).pop()
    return get_priority(group_item)


def prioritise_badges(inputs: list[str]) -> int:
    group_length = 3
    priority_sum = 0
    for i in range(0, len(inputs), group_length):
        group = inputs[i : i + group_length]
        priority_sum += find_badge_priority(group)
    return priority_sum


def solve_a(puzzle: MyPuzzle):
    answer_a = prioritise_rucksacks(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = prioritise_badges(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
