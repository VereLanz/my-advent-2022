from typing import Any

from aocd.models import Puzzle

YEAR = 2022


class MyPuzzle(Puzzle):
    def __init__(self, year: int, day: int):
        super().__init__(year=year, day=day)
        self.input_lines = self.input_data.splitlines()

    def submit_a(self, answer: Any):
        self.answer_a = answer

    def submit_b(self, answer: Any):
        self.answer_b = answer


def get_todays_puzzle(day: int, year: int = YEAR):
    my_puzzle = MyPuzzle(year=year, day=day)
    return my_puzzle
