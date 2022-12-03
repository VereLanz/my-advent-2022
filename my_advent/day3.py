from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle

LOWER_OFFSET = ord("a") - 1   # a - z ->  1 - 26
UPPER_OFFSET = ord("A") - 27  # A - Z -> 27 - 52


def find_rucksack_priority(contents: str) -> int:
    median = int(len(contents) / 2)
    # exactly one letter will be in both halves
    misplaced: str = set(contents[:median]).intersection(set(contents[median:])).pop()
    if misplaced.isupper():
        return ord(misplaced) - UPPER_OFFSET
    return ord(misplaced) - LOWER_OFFSET
        

def prioritise_rucksacks(inputs: list[str]) -> int:
    priorities = [find_rucksack_priority(rucksack) for rucksack in inputs]
    return sum(priorities)

def find_badge_priority(group_contents: list[str]) -> int:
    contents = [set(c) for c in group_contents]
    # exactly one letter appears in each of the three strings (possibly more than once)
    group_item = contents[0].intersection(contents[1]).intersection(contents[2]).pop()
    if group_item.isupper():
        return ord(group_item) - UPPER_OFFSET
    return ord(group_item) - LOWER_OFFSET

def prioritise_badges(inputs: list[str]) -> int:
    group_length = 3
    priorities = []
    for i in range(0, len(inputs), group_length):
        group = inputs[i : i + group_length]
        priorities.append(find_badge_priority(group))
    return sum(priorities)


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
