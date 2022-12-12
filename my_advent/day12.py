from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle


STEP_DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    

# adapted from a recursive grid search found on stackoverflow
def find_paths_recursive(
    grid: np.ndarray, 
    target: tuple[int], 
    current_path: list[tuple[int]] = [(0, 0)], 
    solutions: list[list[tuple[int]]] = []
):
    last_cell = current_path[-1]
    
    for x_step, y_step in STEP_DIRECTIONS:
        new_step = (last_cell[0] + x_step, last_cell[1] + y_step)
        
        # skip if new cell is not in grid
        if any([new_step[0] < 0, new_step[1] < 0, new_step[0] >= grid.shape[0], new_step[1] >= grid.shape[1]]):
            continue
        # skip if new cell was already visited
        if new_step in current_path:
            continue
        # skip if new cell is more than 1 bigger than last
        if grid[new_step] > grid[last_cell] + 1:
            continue
        
        current_path_copy = current_path.copy()
        current_path_copy.append(new_step)

        # if goal is reached, it's a solution; if not, continue searching
        if new_step == target:
            solutions.append(current_path_copy)
            print("solution found...")
            break
        find_paths_recursive(grid, target, current_path_copy, solutions)
        
    return solutions


def find_shortest_hike_up(inputs: list[str]) -> int:
    height_grid = np.array([list(line) for line in inputs], dtype=object)
    # save start and target position
    start = np.where(height_grid == "S")
    end = np.where(height_grid == "E")
    height_grid[start] = "a"
    height_grid[end] = "z"
    # change specifiers to height-values
    letters_to_int = np.vectorize(lambda x: ord(x) - 96)
    height_grid = letters_to_int(height_grid)
    
    solutions = find_paths_recursive(height_grid, end)
    # start is in the path, but does not count as step -> len-1
    return min([len(s) - 1 for s in solutions])


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = find_shortest_hike_up(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = b(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    solve_a(my_puzzle)
    # solve_b(my_puzzle)
