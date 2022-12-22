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
    # from shifting, some movements could again have become LONGER than the list
    current_movement = int(
        copysign(abs(current_movement) % (n_entries - 1), current_movement)
    )
    
    # movement wraps around at the end, i.e. goes backward
    if idx + current_movement >= n_entries:
        actual_movement = current_movement - (n_entries - 1)
        # adjust all influenced indices via their movements 
        for passed_idx in range(idx + actual_movement, idx):
            mixing_movement[passed_idx] += 1
    # movement wraps around at the beginning, i.e. goes forward
    elif idx + current_movement < 0:
        actual_movement = current_movement + (n_entries - 1)
        # adjust all influenced indices via their movements 
        for passed_idx in range(idx + 1, idx + actual_movement + 1):
            mixing_movement[passed_idx] -= 1
    # movement stays in list, i.e. moves forward without change
    else:
        actual_movement = current_movement
        # adjust all influenced indices via their movements 
        for passed_idx in range(idx + 1, idx + actual_movement + 1):
            mixing_movement[passed_idx] -= 1
            
    mixing_movement[idx] = actual_movement
    print(mixing_movement, end="\n\n")
    return mixing_movement


def decode_mixed_list(inputs: list[str]) -> int:
    encoded_values = list(map(int, inputs))
    print(encoded_values)
    n_entries = len(encoded_values)
    mixing_movement = dict()
    for i, entry in enumerate(encoded_values):
        mixing_movement[i] = int(copysign(abs(entry) % (n_entries - 1), entry))
    # adjust movements for wrapping and each other's movements
    new_positions = dict()
    for idx in mixing_movement.keys():
        print(idx)
        move_idx_entry(idx, mixing_movement, n_entries)
        
   # new_positions = dict()
   # # create lookup with new indices after movement
   # for old_idx, movement in mixing_movement.items():
   #     # key is new index, value is old index
   #     print(old_idx, movement, old_idx + movement)
   #     new_positions[old_idx + movement] = old_idx
        
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
