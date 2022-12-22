from math import copysign
from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


POI = [1000, 2000, 3000]  # positions after 0


def move_idx_entry(
    idx: int, 
    mixing_movement: dict[int, int], 
    new_positions: dict[int, int], 
    n_entries: int
) -> dict:
    current_movement = mixing_movement[idx]
    current_position = new_positions.get(idx, idx)
    
    # movement wraps around at the end, i.e. goes backward
    if current_position + current_movement >= n_entries:
        actual_movement = current_movement - (n_entries - 1)
    # movement wraps around at the beginning, i.e. goes forward
    elif current_position + current_movement < 0:
        actual_movement = current_movement + (n_entries - 1)
    # movement stays in list, i.e. moves forward without change
    else:
        actual_movement = current_movement
    
    print(actual_movement)
    # adjust others' positions accordingly
    # take care not to move indices to overlap -> otherwise searching duplicates!
    if actual_movement > 0:
        for passed_idx in range(current_position + 1, current_position + actual_movement + 1):
            old_idx_of_passed = list(new_positions.values()).index(passed_idx)
            new_positions[old_idx_of_passed] = passed_idx - 1
    elif actual_movement < 0:
        for passed_idx in range(current_position - 1, current_position + actual_movement - 1, -1):
            old_idx_of_passed = list(new_positions.values()).index(passed_idx)
            new_positions[old_idx_of_passed] = passed_idx + 1
        
    new_positions[idx] = current_position + actual_movement
    print(new_positions, end="\n\n")
    return new_positions


def decode_mixed_list(inputs: list[str]) -> int:
    encoded_values = list(map(int, inputs))
    print(encoded_values)
    n_entries = len(encoded_values)
    mixing_movement = dict()
    new_positions = dict()
    for i, entry in enumerate(encoded_values):
        new_positions[i] = i
        mixing_movement[i] = int(copysign(abs(entry) % (n_entries - 1), entry))
        
    # carry out movements, adjusting for wrapping and each other's movements
    for idx in mixing_movement.keys():
        print(idx)
        new_positions = move_idx_entry(idx, mixing_movement, new_positions, n_entries)
        
    # find values at 0 index + POI (could probably wrap) for the answer
    zero_idx = encoded_values.index(0)
    zero_new_idx = zero_idx + mixing_movement[zero_idx]
    coordinates_key = 0
    print(new_positions.values())
    print(zero_new_idx)
    for position in POI:
        lookup_idx = zero_new_idx + (position % (n_entries - 1))
        if lookup_idx >= n_entries:
            lookup_idx -= n_entries
        old_idx_translation = list(new_positions.keys())[list(new_positions.values()).index(lookup_idx)]
        coordinates_key += encoded_values[old_idx_translation]
    return coordinates_key


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = decode_mixed_list(puzzle.input_lines)
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
