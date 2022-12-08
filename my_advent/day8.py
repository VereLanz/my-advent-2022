from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle


def count_visible_trees(inputs: list[str]) -> int:
    tree_heights = np.ma.array([list(line) for line in inputs], mask=False).astype(int)
    # go line by line (ignoring first and last)
    for row_idx, row in enumerate(tree_heights.data[1:-1], start=1):
        # for each inner number check if bigger than max to left OR max to right
        for tree_idx, tree in enumerate(row[1:-1], start=1):
            if tree > max(row[:tree_idx]) or tree > max(row[tree_idx + 1:], default=9):
                tree_heights[row_idx][tree_idx] = np.ma.masked
            # columns view only necesseray if not already visible
            else:
                column = tree_heights.T[tree_idx].data
                if tree > max(column[:row_idx]) or \
                   tree > max(column[row_idx + 1:], default=9):
                    tree_heights[row_idx][tree_idx] = np.ma.masked
    border_trees = sum(tree_heights.shape) * 2 - 4
    return np.sum(tree_heights.mask) + border_trees


def find_highest_scenic_score(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = count_visible_trees(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_highest_scenic_score(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
