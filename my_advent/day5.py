from pathlib import Path
import re

from my_advent import get_todays_puzzle, MyPuzzle


def read_stack_grid(grid: list[str]) -> list[str]:
    stacks_number = int(grid[-1].strip().split()[-1])
    stacks = [""] * stacks_number
    for line in grid[:-1]:
        for i, spot in enumerate(range(1, len(line), 4)):
            stacks[i] += line[spot].strip()
    stacks = [s[::-1] for s in stacks]
    return stacks


def move_stacks(
    stacks: list[str], movement: list[int], single: bool = True
) -> list[str]:
    match = re.search(r"move (\d+) from (\d+) to (\d+)", movement)
    amount, source, target = [int(match.group(i)) for i in range(1, 4)]
    if single:
        stacks[target - 1] += stacks[source - 1][-amount:][::-1]
    else:
        stacks[target - 1] += stacks[source - 1][-amount:]
    stacks[source - 1] = stacks[source - 1][:-amount]
    return stacks


def reorganise_stacks(inputs: list[str]) -> str:
    grid, movements = "\n".join(inputs).split("\n\n")
    stacks = read_stack_grid(grid.split("\n"))
    for movement in movements.split("\n"):
        stacks = move_stacks(stacks, movement)
    top_ones = "".join([s[-1] for s in stacks])
    return top_ones


def reorganise_stacks_multiple(inputs: list[str]) -> int:
    grid, movements = "\n".join(inputs).split("\n\n")
    stacks = read_stack_grid(grid.split("\n"))
    for movement in movements.split("\n"):
        stacks = move_stacks(stacks, movement, single=False)
    top_ones = "".join([s[-1] for s in stacks])
    return top_ones


def solve_a(puzzle: MyPuzzle):
    answer_a = reorganise_stacks(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = reorganise_stacks_multiple(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
