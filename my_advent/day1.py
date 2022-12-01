from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


def find_most_calories(inputs: list[str]) -> int:
    current_largest = 0
    current_sum = 0
    for entry in inputs:
        if entry.isdigit():
            current_sum += int(entry)
        else:
            current_largest = max(current_sum, current_largest)
            current_sum = 0
    # last element might not be followed by non-digit
    current_largest = max(current_sum, current_largest)
    return current_largest


def find_top3_calories(inputs: list[str]) -> int:
    current_sum = 0
    sums = []
    for entry in inputs:
        if entry.isdigit():
            current_sum += int(entry)
        else:
            sums.append(current_sum)
            current_sum = 0
    # last element might not be followed by non-digit
    sums.append(current_sum)
    return sum(sorted(sums)[-3:])


def solve_a(puzzle: MyPuzzle):
    answer_a = find_most_calories(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_top3_calories(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
