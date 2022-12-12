from pathlib import Path
from typing import Optional

import numpy as np
from tqdm import tqdm

from my_advent import get_todays_puzzle, MyPuzzle


STEP_DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    

def parse_height_map(inputs: list[str]) -> np.ndarray:
    height_grid = np.array([list(line) for line in inputs], dtype=object)
    # save start and target position
    start = np.where(height_grid == "S")
    end = np.where(height_grid == "E")
    height_grid[start] = "a"
    height_grid[end] = "z"
    # change specifiers to height-values
    letters_to_int = np.vectorize(lambda x: ord(x) - 96)
    height_grid = letters_to_int(height_grid)
    return height_grid, (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))
    
    
def get_neighbours(point: tuple[int]) -> list[tuple[int]]:
    neighbours = []
    for x_step, y_step in STEP_DIRECTIONS:
        new_point = (point[0] + x_step, point[1] + y_step)
        neighbours.append(new_point)
    return neighbours


def breadth_first_hike(
    grid: np.ndarray, 
    start: tuple[int],
    target: tuple[int],
    hike_direction: str = "up"
) -> Optional[dict[tuple[int]]]:
    nodes = {start: None}  # value is key node's parent
    if hike_direction == "up":
        # can only go to points max 1 higher
        point_possible = lambda current, next: grid[current] + 1 < grid[next]
    elif hike_direction == "down":
        # can only go to points max 1 lower
        point_possible = lambda current, next: grid[current] - 1 > grid[next]
    
    visited_points = [start]
    queue = [start]
    while queue:
        current_point = queue.pop()
        if current_point == target:
            return nodes
        for neighbour in get_neighbours(current_point):
            # skip if new point is not in grid
            if any([
                neighbour[0] < 0, 
                neighbour[1] < 0, 
                neighbour[0] >= grid.shape[0], 
                neighbour[1] >= grid.shape[1]
               ]):
                continue
            # skip if new point was already visited
            if neighbour in visited_points:
                continue
            # skip if point not reachable (dep on hike_direction)
            if point_possible(current_point, neighbour):
                continue
            
            visited_points.append(neighbour)
            nodes[neighbour] = current_point
            queue.insert(0, neighbour)
    return None


def find_shortest_hike_up(inputs: list[str]) -> int:
    height_grid, start, end = parse_height_map(inputs)
    
    nodes = breadth_first_hike(height_grid, start, end)
    path = [end]
    parent = end
    while parent != start:
        parent = nodes[parent]
        path.append(parent)
    return len(path) - 1  # start point not included
    

def parse_scenic_height_map(inputs: list[str]) -> np.ndarray:
    height_grid = np.array([list(line) for line in inputs], dtype=object)
    # save start and target position
    start = np.where(height_grid == "S")
    peak = np.where(height_grid == "E")
    height_grid[start] = "a"
    height_grid[peak] = "z"
    
    lowest = np.where(height_grid == "a")
    scenic_goals = []
    for goal_x, goal_y in zip(lowest[0], lowest[1]):
        scenic_goals.append((goal_x, goal_y))
    
    # change specifiers to height-values
    letters_to_int = np.vectorize(lambda x: ord(x) - 96)
    height_grid = letters_to_int(height_grid)
    return height_grid, (int(peak[0]), int(peak[1])), scenic_goals


def find_scenic_hike_up(inputs: list[str]) -> int:
    height_grid, peak, scenic_goals = parse_scenic_height_map(inputs)
    paths = []
    for goal in tqdm(scenic_goals):
        nodes = breadth_first_hike(height_grid, peak, goal, hike_direction="down")
        if not nodes:
            continue
        parent = goal
        path = [parent]
        while parent != peak:
            parent = nodes[parent]
            path.append(parent)
        paths.append(path)
    return min([len(p) - 1 for p in paths])  # start point not included


def solve_a(puzzle: MyPuzzle):
    answer_a = find_shortest_hike_up(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_scenic_hike_up(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    solve_b(my_puzzle)
