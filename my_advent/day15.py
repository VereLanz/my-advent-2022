from pathlib import Path

from shapely.geometry import Polygon
from shapely.ops import unary_union
from tqdm import tqdm

from my_advent import get_todays_puzzle, MyPuzzle


class Sensor:
    def __init__(self, position: tuple[int], beacon: tuple[int]):
        self.position = position
        self.beacon_position = beacon
        self.calc_coverage_distance()
        self.calc_covered_lines()
    
    def calc_coverage_distance(self):
        # manhatten distance from beacon
        x_dist = abs(self.position[0] - self.beacon_position[0])
        y_dist = abs(self.position[1] - self.beacon_position[1])
        self.coverage_distance = x_dist + y_dist

    def calc_covered_lines(self):
        lines = list(range(
            self.position[1] - self.coverage_distance, 
            self.position[1] + self.coverage_distance + 1
        ))
        self.covered_lines = lines
        
    def calc_coverage_in_line(self, loi: int):
        covered_points = []
        x_range = self.coverage_distance - abs(self.position[1] - loi)
        for x in range(-x_range, x_range + 1):
            covered_points.append((self.position[0] + x, loi))
        self.loi_coverage = covered_points


def parse_sensor_points(inputs: list[str]) -> list[Sensor]:
    sensors = []
    for line in tqdm(inputs):
        s_xy, b_xy = line.replace("Sensor at x=", "").split(": closest beacon is at x=")
        s_x, s_y = s_xy.split(", y=")
        b_x, b_y = b_xy.split(", y=")
        sensor = Sensor((int(s_x), int(s_y)), (int(b_x), int(b_y)))
        sensors.append(sensor)
    return sensors

    
def rule_out_locations(inputs: list[str], line_of_interest: int) -> int:
    sensors = parse_sensor_points(inputs)
    beacons = [s.beacon_position for s in sensors]
    
    sensors_of_interest = [s for s in sensors if line_of_interest in s.covered_lines]
    covered_points = []
    for sensor in tqdm(sensors_of_interest):
        sensor.calc_coverage_in_line(line_of_interest)
        covered_points += sensor.loi_coverage
        
    ruled_out = [p for p in covered_points if p not in beacons]
    return len(set(ruled_out))


# for part 2, colleague LB had a very nice solution with shapely
def parse_sensor_polygons(inputs: list[str]) -> list[Polygon]:
    sensor_polygons = []
    for line in inputs:
        s_xy, b_xy = line.replace("Sensor at x=", "").split(": closest beacon is at x=")
        s_x, s_y = map(int, s_xy.split(", y="))
        b_x, b_y = map(int, b_xy.split(", y="))
        coverage_distance = abs(s_x - b_x) + abs(s_y - b_y)
        s = Polygon([
            (s_x, s_y - coverage_distance), 
            (s_x - coverage_distance, s_y), 
            (s_x, s_y + coverage_distance), 
            (s_x + coverage_distance, s_y)
        ])
        sensor_polygons.append(s)
    return sensor_polygons


def calc_tuning_frequency(x: int, y: int) -> int:
    return int(x * 4_000_000 + y)


def find_distress_frequency(inputs: list[str]) -> int:
    sensor_polygons = parse_sensor_polygons(inputs)
    sensor_coverage = unary_union(sensor_polygons)
    # there should be only one hole in the unioned polygons, get its center point
    empty_point_x, empty_point_y = sensor_coverage.interiors[0].centroid.coords[0]
    return calc_tuning_frequency(empty_point_x, empty_point_y)


def solve_a(puzzle: MyPuzzle):
    answer_a = rule_out_locations(puzzle.input_lines, line_of_interest=2_000_000)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = find_distress_frequency(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
