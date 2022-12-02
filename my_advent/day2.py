from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


POINTS = {
    "A": 1,  # O Rock
    "B": 2,  # O Paper
    "C": 3,  # O Scissors
    "X": 1,  # Y Rock
    "Y": 2,  # Y Paper
    "Z": 3,  # Y Scissors
}
WINNING_COMBOS = [
    "AY",
    "BZ",
    "CX",
]


def get_rps_score(opponent: str, you: str) -> int:
    your_score = POINTS[you]
    # a tie
    if POINTS[you] == POINTS[opponent]:
        your_score += 3
    # you win
    elif opponent + you in WINNING_COMBOS:
        your_score += 6
    # else is lose, +0
    return your_score

def calculate_points_for_strategy(inputs: list[str]) -> int:
    your_scores = [get_rps_score(*inp.split()) for inp in inputs]
    return sum(your_scores)


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = calculate_points_for_strategy(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = b(puzzle.input_lines)
    # puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
