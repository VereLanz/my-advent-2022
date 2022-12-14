from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle


SAND_SOURCE = (0, 500)


class Sand:
    def __init__(self, start_point: tuple[int] = SAND_SOURCE):
        self.position = start_point
        self.has_dropped = False
        self.has_stopped = False
        
    def move(self, cave: np.ndarray):
        # assumes the free-falling line is not the outermost point
        if self.position[0] == cave.shape[0] - 1 \
           or self.position[1] == 0 \
           or self.position[1] == cave.shape[1] - 1:
            if not self.has_stopped:
                self.has_dropped = True
            return
        # empty spaces in cave are 0
        straight = (self.position[0] + 1, self.position[1])
        left  = (self.position[0] + 1, self.position[1] - 1)
        right = (self.position[0] + 1, self.position[1] + 1)
        if cave[straight] == 0:
            self.position = straight
        elif cave[left] == 0:
            self.position = left
        elif cave[right] == 0:
            self.position = right
        else:
            cave[self.position] = 2
            self.has_stopped = True
        

def parse_to_cave(inputs: list[str]) -> np.ndarray:
    rock_lines = []
    # attention: coords are FLIPPED here, for less confusing array access
    for line in inputs:
        rock_line = line.split(" -> ")
        rock_line = [(int(c.split(",")[1]), int(c.split(",")[0])) for c in rock_line]
        rock_lines.append(rock_line)
    hor_points = [coord[0] for lines in rock_lines for coord in lines]
    ver_points = [coord[1] for lines in rock_lines for coord in lines]
    hor_shape = max(hor_points) + 1
    ver_shape = max(max(ver_points), SAND_SOURCE[1]) + 1
    cave = np.zeros((hor_shape, ver_shape))
    
    # rocks are represented by value 1
    for lines in rock_lines:
        for i in range(len(lines) - 1):
            point_a_x, point_a_y = lines[i]
            point_b_x, point_b_y = lines[i + 1]
            coords_x = (min(point_a_x, point_b_x), max(point_a_x, point_b_x) + 1)
            coords_y = (min(point_a_y, point_b_y), max(point_a_y, point_b_y) + 1)
            cave[coords_x[0]:coords_x[1], coords_y[0]:coords_y[1]] = 1
            
    return cave


def drop_sand(cave: np.ndarray) -> bool:
    sand = Sand()
    while not sand.has_stopped:
        sand.move(cave)
        if sand.has_dropped:
            break
    return sand.has_dropped


def fill_cave_with_sand(inputs: list[str]) -> int:
    cave = parse_to_cave(inputs)
    sand_stacked = 0
    sand_dropped = False
    while not sand_dropped:
        sand_stacked += 1
        sand_dropped = drop_sand(cave)
        if sand_dropped:
            sand_stacked -= 1

    # create picture of result
    empty_columns = np.argwhere(np.all(cave[..., :] == 0, axis=0))
    print_cave = np.delete(cave, empty_columns, axis=1)
    plt.imshow(print_cave, interpolation='none')
    plt.savefig("day14.png")
    return sand_stacked


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = fill_cave_with_sand(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = b(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
