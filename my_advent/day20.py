from math import copysign
from pathlib import Path

import numpy as np
from tqdm import tqdm

from my_advent import get_todays_puzzle, MyPuzzle


POI = [1000, 2000, 3000]  # "positions of interest" after 0
DECRYPTION_KEY = 811_589_153


def move_idx_entry(
    idx: int, 
    mixing_movement: int, 
    new_positions: np.ndarray, 
    n_entries: int
) -> np.ndarray:
    current_position = new_positions[idx]
    
    # movement wraps around at the end, i.e. goes backward
    if current_position + mixing_movement >= n_entries:
        actual_movement = mixing_movement - (n_entries - 1)
    # movement wraps around at the beginning, i.e. goes forward
    elif current_position + mixing_movement < 0:
        actual_movement = mixing_movement + (n_entries - 1)
    # movement stays in list, i.e. moves forward or backward without change
    else:
        actual_movement = mixing_movement
    
    # adjust others' positions accordingly
    # take care not to move indices to overlap -> otherwise searching duplicates!
    if actual_movement > 0:
        walk = range(current_position + 1, current_position + actual_movement + 1)
        for passed_idx in walk:
            old_idx_of_passed = np.where(new_positions == passed_idx)[0][0]
            new_positions[old_idx_of_passed] = passed_idx - 1
    elif actual_movement < 0:
        walk_backwards = range(
            current_position - 1, current_position + actual_movement - 1, -1
        )
        for passed_idx in walk_backwards:
            old_idx_of_passed = np.where(new_positions == passed_idx)[0][0]
            new_positions[old_idx_of_passed] = passed_idx + 1
        
    new_positions[idx] = current_position + actual_movement
    return new_positions


def decode_mixed_list(inputs: list[str]) -> int:
    encoded_values = list(map(int, inputs))
    n_entries = len(encoded_values)
    new_positions = np.arange(n_entries)
        
    # carry out movements, adjusting for wrapping and each other's movements
    for idx, value in tqdm(enumerate(encoded_values)):
        mixing_movement = int(copysign(abs(value) % (n_entries - 1), value))
        new_positions = move_idx_entry(idx, mixing_movement, new_positions, n_entries)
        
    # find values at 0 index + POI (attention to wrap) for the answer
    zero_new_idx = new_positions[encoded_values.index(0)]
    coordinates_key = 0
    for position in POI:
        lookup_idx = zero_new_idx + (position % n_entries)
        if lookup_idx >= n_entries:
            lookup_idx -= n_entries
        old_idx_translation = np.where(new_positions == lookup_idx)[0][0]
        coordinates_key += encoded_values[old_idx_translation]
    return coordinates_key


def decode_seriously_mixed_list(inputs: list[str]) -> int:
    encoded_values = np.array(list(map(int, inputs)))
    n_entries = len(encoded_values)
    new_positions = np.arange(n_entries)
    
    # multiply everything by the decryption key 
    encoded_values *= DECRYPTION_KEY
    # carry out movements 10 times, adjusting for wrapping and each other's movements
    for _ in range(10):
        for idx, value in tqdm(enumerate(encoded_values)):
            mixing_movement = int(copysign(abs(value) % (n_entries - 1), value))
            new_positions = move_idx_entry(
                idx, mixing_movement, new_positions, n_entries
            )
        
    # find values at 0 index + POI (attention to wrap) for the answer
    zero_index = np.where(encoded_values == 0)[0][0]
    zero_new_idx = new_positions[zero_index]
    coordinates_key = 0
    for position in POI:
        lookup_idx = zero_new_idx + (position % n_entries)
        if lookup_idx >= n_entries:
            lookup_idx -= n_entries
        old_idx_translation = np.where(new_positions == lookup_idx)[0][0]
        coordinates_key += encoded_values[old_idx_translation]
    return coordinates_key


def solve_a(puzzle: MyPuzzle):
    answer_a = decode_mixed_list(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = decode_seriously_mixed_list(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
