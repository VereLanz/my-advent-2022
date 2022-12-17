from itertools import repeat
from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle


STONES_WATCHED = 2022
CAVE_WIDTH = 7
STONE_PATTERNS = [
    np.array([[1, 1, 1, 1]]),
    np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
    np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
    np.array([[1], [1], [1], [1]]),
    np.array([[1, 1], [1, 1]]),
    
]


class Stone:
    def __init__(self, shape: np.ndarray, tower_height: int):
        self.shape = shape
        # 0 is the left wall, 0 is the floor
        self.width = np.array([3, 3 + self.shape.shape(1)])  # from left
        self.height = np.array(
            [tower_height + 4, tower_height + 4 + self.shape.shape(0)]
        )  # from floor
        self.falling = True
        
    def touching_ground(self, cave_outline):
        # TODO: how to work with the cave outline?
        pass
        

def next_stone_shape() -> np.ndarray:
    for stone_shape in repeat(STONE_PATTERNS):
        yield stone_shape
        
        
def next_gust(gust_pattern: list[str]) -> str:
    for gust in repeat(gust_pattern):
        yield gust
        

def predict_stone_tower_height(inputs: list[str]) -> int:
    gust_pattern = list(inputs[0])
    tower_height = 0
    cave_outline = np.zeros((6, CAVE_WIDTH))
    for _ in range(STONES_WATCHED):
        stone = Stone(next_stone_shape(), tower_height)
        while stone.falling:
            if next_gust(gust_pattern) == "<":
                # TODO: or touching another STONE!
                if stone.width[0] > 1:
                    stone.width -= 1
            else:
                # TODO: or touching another STONE!
                if stone.width[1] < CAVE_WIDTH:
                    stone.width += 1
            if stone.touching_ground(cave_outline):
                stone.falling = False
                # TODO: change cave_outline + tower_height
            else:
                stone.height -= 1
    return tower_height


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = predict_stone_tower_height(puzzle.input_lines)
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
