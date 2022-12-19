from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle, MyPuzzle


Coords = tuple[int]
CUBE_NEIGHBOURING = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1],
]


def find_neighbours(cube: Coords, cube_coords: list[Coords]) -> list[Coords]:
    neighbours = []
    for x, y, z in CUBE_NEIGHBOURING:
        candidate = (cube[0] + x, cube[1] + y, cube[2] + z)
        if candidate in cube_coords:
            neighbours.append(candidate)
    return neighbours
    
    
def find_droplet_surface_area(inputs: list[str]) -> int:
    cube_coords = [tuple(map(int, line.split(","))) for line in inputs]
    
    x_max = max([x for x, *_ in cube_coords])
    y_max = max([y for _, y, _ in cube_coords])
    z_max = max([z for *_, z in cube_coords])
    droplet_faces = np.zeros(shape=(x_max + 1, y_max + 1, z_max + 1))
    for cube in cube_coords:
        droplet_faces[cube] = 6 - len(find_neighbours(cube, cube_coords))

    return int(np.sum(droplet_faces))


def surrounded_by_blocks(
    cube: Coords, 
    cube_coords: list[Coords], 
    empty_cubes: list[Coords], 
    checked: list[Coords] = []
) -> int:
    if cube in checked:
        return 0
    checked.append(cube)
    
    neighbours = find_neighbours(cube, cube_coords)
    if len(neighbours) == 6:
        # surrounded by blocks
        return 6
    
    # TODO: how to handle empty space surrounded by more empty space but ultimately enclosed?
    # empty_neighbours = find_neighbours(cube, empty_cubes)
    return 0
    

def find_droplet_outer_surface_area(inputs: list[str]) -> int:
    cube_coords = [tuple(map(int, line.split(","))) for line in inputs]
    
    x_max = max([x for x, *_ in cube_coords])
    y_max = max([y for _, y, _ in cube_coords])
    z_max = max([z for *_, z in cube_coords])
    droplet_faces = np.zeros(shape=(x_max + 1, y_max + 1, z_max + 1))
    for cube in cube_coords:
        droplet_faces[cube] = 6 - len(find_neighbours(cube, cube_coords))
    all_faces = int(np.sum(droplet_faces))
        
    # find out which empty spaces are enclosed by cubes
    empty_cubes = set(map(tuple, np.argwhere(droplet_faces == 0).tolist()))
    empty_cubes = empty_cubes - set(cube_coords)
    enclosed_space_faces = 0
    for cube in empty_cubes:
        enclosed_space_faces += surrounded_by_blocks(cube, cube_coords, empty_cubes)
    
    return int(all_faces - enclosed_space_faces)


def solve_a(puzzle: MyPuzzle):
    answer_a = find_droplet_surface_area(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_droplet_outer_surface_area(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
