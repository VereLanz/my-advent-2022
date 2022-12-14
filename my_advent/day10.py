from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from my_advent import get_todays_puzzle, MyPuzzle


SCREEN_COLUMNS = 40


def sum_signal_strength_of_interest(inputs: list[str]) -> int:
    cycle_x = []
    x = 1
    for line in inputs:
        match line.split():
            case ["noop"]:
                cycle_x.append(x)
            case ["addx", value]:
                cycle_x.extend([x, x])
                x += int(value)
            
    signal_strength = 0    
    for c in range(19, 220, 40):  # idx needs to be 1 below cycle-of-interest number
        signal_strength += cycle_x[c] * (c + 1)
    return signal_strength


def draw_pixel(screen: np.ndarray, pixel: int, sprite: list[int]):
    if any([pixel - (i * SCREEN_COLUMNS) in sprite for i in range(6)]):
        row = pixel // SCREEN_COLUMNS
        column = pixel - (row * SCREEN_COLUMNS)
        screen[row][column] = 1


def draw_cycle_pixels(inputs: list[str], img_suffix: str = ""):
    screen = np.zeros(shape=(6, SCREEN_COLUMNS))
    sprite = [0, 1, 2]
    current_pixel = 0
    for line in inputs:
        match line.split():
            case ["noop"]:
                draw_pixel(screen, current_pixel, sprite)
                current_pixel += 1
            case ["addx", value]:
                draw_pixel(screen, current_pixel)
                current_pixel += 1
                draw_pixel(screen, current_pixel)
                current_pixel += 1
                for p in range(len(sprite)):
                    sprite[p] += int(value)

    plt.imshow(screen)
    plt.savefig(f"images/day10{img_suffix}.png")


def solve_a(puzzle: MyPuzzle):
    answer_a = sum_signal_strength_of_interest(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    draw_cycle_pixels(puzzle.input_lines)
    # this answer needs to be read from an image and manually entered!


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
