from pathlib import Path

import numpy as np
from scipy.ndimage import binary_fill_holes

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
   

def find_enclosed_spaces(cube_coords: list[Coords]) -> set[Coords]:
    # grid with all solid cubes = 1
    x_coords = set([x for x, *_ in cube_coords])
    y_coords = set([y for _, y, _ in cube_coords])
    z_coords = set([z for *_, z in cube_coords])
    cube_grid = np.zeros(
        shape=(max(x_coords) + 1, max(y_coords) + 1, max(z_coords) + 1)
    )
    for cube in cube_coords:
        cube_grid[cube] = 1
    
    # holes in 2D for x layers walked
    x_holes = []
    for x in x_coords:
        x_layer = cube_grid[x, :, :]
        holes = binary_fill_holes(x_layer) - x_layer
        hole_coords = np.argwhere(holes == 1).tolist()
        x_holes += [(x, y, z) for y, z in hole_coords if (x, y, z) not in cube_coords]
    # holes in 2D for y layers walked
    y_holes = []
    for y in y_coords:
        y_layer = cube_grid[:, y, :]
        holes = binary_fill_holes(y_layer) - y_layer
        hole_coords = np.argwhere(holes == 1).tolist()
        y_holes += [(x, y, z) for x, z in hole_coords if (x, y, z) not in cube_coords]
    # holes in 2D for z layers walked
    z_holes = []
    for z in z_coords:
        z_layer = cube_grid[:, :, z]
        holes = binary_fill_holes(z_layer) - z_layer
        hole_coords = np.argwhere(holes == 1).tolist()
        z_holes += [(x, y, z) for x, y in hole_coords if (x, y, z) not in cube_coords]
    # if holes are enclosed in all 2D planes, they are 3D holes as well
    return set(x_holes) & set(y_holes) & set(z_holes)
    

def find_droplet_outer_surface_area(inputs: list[str]) -> int:
    cube_coords = [tuple(map(int, line.split(","))) for line in inputs]
    # all non-solid-neighboured surfaces
    all_faces = 0
    for cube in set(cube_coords):
        all_faces += 6 - len(find_neighbours(cube, cube_coords))
        
    # find out which spaces are enclosed by solid cubes
    enclosed_spaces = find_enclosed_spaces(cube_coords)
    # get all the solid faces that enclosed holes touch
    enclosed_space_faces = 0
    for space in enclosed_spaces:
        enclosed_space_faces += 6 - len(find_neighbours(space, enclosed_spaces))
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
