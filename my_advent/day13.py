from functools import cmp_to_key
from pathlib import Path
from typing import Union

from my_advent import get_todays_puzzle, MyPuzzle


# nice solution from colleague LB
def compare_packs(left: Union[list, int], right: Union[list, int]) -> int:
    """
    Compare left and right (recursively), returning:
    number < 0 if left is smaller
    0 if they are equal
    number > 0 if right is smaller
    """
    match (left, right):
        case int(left), int(right):
            return left - right
        case int(left), right:
            return compare_packs([left], right)
        case left, int(right):
            return compare_packs(left, [right])
        case left, right:
            # zip stops if any list reaches its end (or is empty to begin with)
            for left_val, right_val in zip(left, right):
                comparison = compare_packs(left_val, right_val)
                if comparison != 0:
                    return comparison
            # list length as tiebreaker, if one side is longer than the other
            return len(left) - len(right)
    # should never be reached, but is a catchall
    return 0


def find_right_order_pairs(inputs: list[str]) -> int:
    packet_pairs = "\n".join(inputs).split("\n\n")
    right_order_pairs = []
    for idx, pair in enumerate(packet_pairs, start=1):
        if "sudo" in pair:  # i will eval...
            return 0
        packets = pair.split("\n")
        left, right = eval(packets[0]), eval(packets[1])  # i saw the input, it's fine
        if compare_packs(left, right) < 0:
            right_order_pairs.append(idx)
    return sum(right_order_pairs)


def find_decoder_key(inputs: list[str]) -> int:
    decoder_packs = [[[2]], [[6]]]
    packets = [eval(i) for i in inputs if i and not "sudo" in i] + decoder_packs
    packets.sort(key=cmp_to_key(compare_packs))
    return (packets.index(decoder_packs[0]) + 1) * (packets.index(decoder_packs[1]) + 1)


def solve_a(puzzle: MyPuzzle):
    answer_a = find_right_order_pairs(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_decoder_key(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
