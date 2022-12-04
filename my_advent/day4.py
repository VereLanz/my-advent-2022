from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


def sectiony_fully_overlapping(sections: str) -> int:
    [a1, b1], [a2, b2] = [s.split("-") for s in sections.split(",")]
    section1 = set(range(int(a1), int(b1) + 1))
    section2 = set(range(int(a2), int(b2) + 1))
    if section1.issubset(section2) or section2.issubset(section1):
        return 1  # True
    return 0  # False


def count_full_section_overlaps(inputs: list[str]) -> int:
    overlaps = map(sectiony_fully_overlapping, inputs)
    return sum(overlaps)


def sectiony_overlapping(sections: str) -> int:
    [a1, b1], [a2, b2] = [s.split("-") for s in sections.split(",")]
    section1 = set(range(int(a1), int(b1) + 1))
    section2 = set(range(int(a2), int(b2) + 1))
    if section1.intersection(section2):
        return 1  # True
    return 0  # False


def count_section_overaps(inputs: list[str]) -> int:
    overlaps = map(sectiony_overlapping, inputs)
    return sum(overlaps)


def solve_a(puzzle: MyPuzzle):
    answer_a = count_full_section_overlaps(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = count_section_overaps(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
