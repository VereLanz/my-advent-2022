from collections import defaultdict
from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


DISK_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000


def get_folder_sizes(inputs: list[str]) -> list[int]:
    folder_chain = []
    folders = defaultdict(int)
    for line in inputs:
        match line.split():
            case ["$", "cd", ".."]:
                folder_chain.pop()
            case ["$", "cd", folder]:
                folder_chain.append(folder)
            case ["$", "ls"]:
                continue
            case ["dir", _]:
                continue
            case [size, _]:
                for i in range(1, len(folder_chain) + 1):
                    folders["".join(folder_chain[:i])] += int(size)
    return folders


def get_small_folders(inputs: list[str]) -> int:
    folders = get_folder_sizes(inputs)
    return sum([f for f in folders.values() if f <= 100_000])


def free_up_space(inputs: list[str]) -> int:
    folders = get_folder_sizes(inputs)
    needed_space = UPDATE_SIZE - (DISK_SIZE - folders["/"])
    delete_size = min([f for f in folders.values() if f >= needed_space])
    return delete_size


def solve_a(puzzle: MyPuzzle):
    answer_a = get_small_folders(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = free_up_space(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
