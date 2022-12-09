import math
from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle


DIRECTION_DICT = {
    "L": -1,
    "R": +1,
    "U": +1j,
    "D": -1j,
}


def check_tail_movement(inputs: list[str]) -> int:
    movements = [line.split() for line in inputs]
    # with one trailing know, movement is always along the previous leading knot's path
    T = H = H_before = 0 + 0j
    tail_visited = [T]
    
    for direction, value in movements:
        move = DIRECTION_DICT[direction]
        for _ in range(int(value)):
            H_before = H
            H += move
            # check distance
            if abs(H - T) > math.sqrt(2):
                T = H_before
                tail_visited.append(T)
  
    return len(set(tail_visited))


def follow_move(vector: complex) -> complex:
    follow_real = 0 if vector.real == 0 \
        else math.copysign(vector.real / vector.real, vector.real)
    follow_imag = 0 if vector.imag == 0 \
        else math.copysign(vector.imag / vector.imag, vector.imag)
    return complex(follow_real, follow_imag)
    

def check_long_tail_movement(inputs: list[str]) -> int:
    movements = [line.split() for line in inputs]
    # it's always 10 knots, but the movement is now more irregular than with only 2
    knots = [0 + 0j] * 10
    tail_visited = [knots[-1]]
    
    for direction, value in movements:
        move = DIRECTION_DICT[direction]
        for _ in range(int(value)):
            knots[0] += move
            # check follow movement for each trailing knot after the previous one moves
            for i in range(len(knots) - 1):
                if abs(dist := (knots[i] - knots[i + 1])) > math.sqrt(2):
                    knots[i + 1] += follow_move(dist)
            tail_visited.append(knots[-1])
  
    return len(set(tail_visited))


def solve_a(puzzle: MyPuzzle):
    answer_a = check_tail_movement(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = check_long_tail_movement(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
