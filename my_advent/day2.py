from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


POINTS = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

WINNING_COMBOS_A = [
    "AY",
    "BZ",
    "CX",
]


STRATEGY_B_LOOKUP = {
    "A": ["B", "A", "C"],  # Rock win, tie, lose
    "B": ["C", "B", "A"],  # Paper
    "C": ["A", "C", "B"],  # Scissors
}

STRATEGY_B = {
    "X": (2, 0),  # lose lookup_idx, points
    "Y": (1, 3),  # tie
    "Z": (0, 6),  # win
}

def get_rps_score(opponent: str, you: str) -> int:
    your_score = POINTS[you]
    # a tie
    if POINTS[you] == POINTS[opponent]:
        your_score += 3
    # you win
    elif opponent + you in WINNING_COMBOS_A:
        your_score += 6
    # else is lose, +0
    return your_score

def calculate_points_for_strategy(inputs: list[str]) -> int:
    your_scores = [get_rps_score(*inp.split()) for inp in inputs]
    return sum(your_scores)


def get_rps_strategy_score(opponent: str, your_plan: str) -> int:
    lookup_idx, your_score = STRATEGY_B[your_plan]
    your_score += POINTS[STRATEGY_B_LOOKUP[opponent][lookup_idx]]
    return your_score
    
def calculate_points_for_new_strategy(inputs: list[str]) -> int:
    your_scores = [get_rps_strategy_score(*inp.split()) for inp in inputs]
    return sum(your_scores)


def solve_a(puzzle: MyPuzzle):
    answer_a = calculate_points_for_strategy(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = calculate_points_for_new_strategy(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
