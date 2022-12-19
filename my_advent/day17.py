from itertools import cycle
from pathlib import Path
from typing import Generator

import numpy as np
from tqdm import tqdm

from my_advent import get_todays_puzzle, MyPuzzle


STONE_PATTERNS = [
    {0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j},  # ----
    {1 + 0j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 2j},  # +
    {0 + 0j, 1 + 0j, 2 + 0j, 2 + 1j, 2 + 2j},  # _|
    {0 + 0j, 0 + 1j, 0 + 2j, 0 + 3j},  # |
    {0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j},  # square
]
GUST_DIRECTIONS = {
    "<": -1 + 0j,
    ">": +1 + 0j,
}
DOWN = 0 - 1j
SPAWN_OFFSET = 2 + 4j
CAVE_WIDTH = 7


class Stone:
    def __init__(self, position: set[complex], cave_rocks: set[complex]):
        highest_rock = max([r.imag for r in cave_rocks]) * 1j
        self.position = {p + SPAWN_OFFSET + highest_rock for p in position}
        self.falling = True
        
    def move(self, direction: complex, cave_rocks: set[complex]):
        old_position = self.position
        self.position = {part + direction for part in self.position}
        if self._touching_rock(cave_rocks):
            # undo move
            self.position = old_position
            if direction == DOWN:
                # stone stops if down-obstacle
                self.falling = False
    
    def _touching_rock(self, cave_rocks: set[complex]) -> bool:
        # touching left wall, right wall, any other settled rock, or cave floor
        if any(part.real < 0 for part in self.position) or \
           any(part.real >= CAVE_WIDTH for part in self.position) or \
           len(cave_rocks & self.position) >= 1 or \
           any(part.imag < 0 for part in self.position):
               return True
        return False
        

def predict_stone_tower_height(inputs: list[str], stones_watched: int = 2022) -> int:
    gusts = cycle(list(inputs[0]))
    stone_shapes = cycle(STONE_PATTERNS)
    cave_rocks = {0 - 1j}  # one ground stone, floor is at -1
    for _ in tqdm(range(stones_watched)):
        stone = Stone(next(stone_shapes), cave_rocks)
        while stone.falling:
            stone.move(GUST_DIRECTIONS[next(gusts)], cave_rocks)
            stone.move(DOWN, cave_rocks)
        cave_rocks.update(stone.position)
    return int(max([r.imag for r in cave_rocks])) + 1  # count starts at 0


def drop_stones(
    stone_shapes: Generator[set[complex], None, None], 
    gusts: Generator[str, None, None], 
    stones_to_drop: int, 
    cave_rocks: set[complex] = {0 - 1j}
) -> list[int]:
    tower_heights = []  # floor height is -1
    for _ in tqdm(range(stones_to_drop)):
        stone = Stone(next(stone_shapes), cave_rocks)
        while stone.falling:
            stone.move(GUST_DIRECTIONS[next(gusts)], cave_rocks)
            stone.move(DOWN, cave_rocks)
        cave_rocks.update(stone.position)
        tower_heights.append(max([r.imag + 1 for r in cave_rocks]))  # height is y + 1
    return tower_heights


# taken from colleague LB
def find_repeating_height_pattern(
    values: list[int], min_length: int, max_length: int
) -> tuple[int]:
    """
    Find a sequence in the given list with a length between min_length and max_length
    which repeats at least 3 times:
    """
    print("finding pattern...")
    for i in range(len(values) - 3 * max_length):
        for length in range(min_length, max_length):
            if all(values[i : i + length] == values[i + length : i + 2 * length]) and \
               all(values[i + length : i + 2 * length] == \
                   values[i + 2 * length : i + 3 * length]):
                print("pattern found!")
                return i, length
    return None


def predict_stone_tower_height_efficiently(
    inputs: list[str], stones_watched: int = 1_000_000_000_000
) -> int:
    gusts = cycle(list(inputs[0]))
    stone_shapes = cycle(STONE_PATTERNS)
    # drop a managable but big enough amount to search for patterns
    heights = drop_stones(stone_shapes, gusts, stones_to_drop=10_000)
    # min and max length values come from experimentation...
    pattern_start, pattern_length = find_repeating_height_pattern(
        np.diff(heights), 10, 3000
    )
    pattern_height = heights[pattern_start + pattern_length] - heights[pattern_start]
    
    # "repeat pattern" for all coming blocks after pattern starts
    blocks_repeating_pattern = stones_watched - (pattern_start + 1)
    tower_height = (blocks_repeating_pattern // pattern_length) * pattern_height
    # add height from before the pattern starts
    tower_height += heights[pattern_start]
    # there might be blocks not fully running the pattern at the end
    remaining_blocks = blocks_repeating_pattern % pattern_length
    tower_height += heights[pattern_start + remaining_blocks] - heights[pattern_start]
        
    return int(tower_height)


def solve_a(puzzle: MyPuzzle):
    answer_a = predict_stone_tower_height(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = predict_stone_tower_height_efficiently(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
