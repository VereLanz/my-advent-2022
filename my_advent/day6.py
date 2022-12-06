from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


def check_buffer_length(data: str, marker_check: int = 4) -> int:
    counter = marker_check
    marker_found = False
    while not marker_found:
        part = data[counter - marker_check : counter]
        if len(part) == len(set(part)):
            buffer_length = counter
            marker_found = True
        counter += 1
    return buffer_length


def find_packet_marker(inputs: list[str]) -> int:
    buffer_length = check_buffer_length(inputs[0])
    return buffer_length


def find_message_marker(inputs: list[str]) -> int:
    buffer_length = check_buffer_length(inputs[0], marker_check=14)
    return buffer_length


def solve_a(puzzle: MyPuzzle):
    answer_a = find_packet_marker(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_message_marker(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
