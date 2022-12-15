from pathlib import Path

from tqdm import tqdm

from my_advent import get_todays_puzzle, MyPuzzle


MIN_DISTRESS_COORD = 0
MAX_DISTRESS_COORD = 4_000_000


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
            
    def calc_coverage_in_restricted_line(self, loi: int, x_limit: int):
        covered_points = []
        x_range = self.coverage_distance - abs(self.position[1] - loi)
        x_lower = max(self.position[0] - abs(x_range), MIN_DISTRESS_COORD)
        x_upper = min(self.position[0] + abs(x_range), x_limit)
        for x in range(x_lower, x_upper + 1):
            covered_points.append((x, loi))
        self.loi_coverage_restricted = covered_points
        
    def cover_points(self, x: int, y: int) -> list[tuple[int]]:
        points = []
        pos_x, pos_y = self.position
        for i in range(-x, x + 1):
            points.append((pos_x + i, pos_y + y))
            points.append((pos_x + i, pos_y - y))
        return points
        
    def calc_full_coverage(self):
        covered = []
        for d in range(self.coverage_distance + 1):
            x = self.coverage_distance - d
            y = d
            # add points between position -x+y to +x+y and -x,-y to +x-y
            covered += self.cover_points(x, y)
        self.coverage = list(set(covered))


def parse_sensor_points(inputs: list[str]) -> list[Sensor]:
    sensors = []
    for line in tqdm(inputs):
        s_xy, b_xy = line.replace("Sensor at x=", "").split(": closest beacon is at x=")
        s_x, s_y = s_xy.split(", y=")
        b_x, b_y = b_xy.split(", y=")
        sensor = Sensor((int(s_x), int(s_y)), (int(b_x), int(b_y)))
        sensors.append(sensor)
    return sensors
  
  
def calc_tuning_frequency(x: int, y: int) -> int:
    return x * 4_000_000 + y 

    
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


def find_distress_frequency(inputs: list[str], max_coord: int = MAX_DISTRESS_COORD) -> int:
    sensors = parse_sensor_points(inputs)
    covered_points = []
    # TODO: the theory seems sound, but this is not scaling to 4 Mio!
    for sensor in tqdm(sensors):
        for line in range(MIN_DISTRESS_COORD, max_coord + 1):
            sensor.calc_coverage_in_restricted_line(line, max_coord)
            covered_points += sensor.loi_coverage_restricted
    
    # TODO: find a better way to determine the MISSING one in covered_points
    full_grid = []
    for x in range(MIN_DISTRESS_COORD, max_coord + 1):
        for y in range(MIN_DISTRESS_COORD, max_coord + 1):
            full_grid.append((x, y))
    
    (empty_point, ) = set(full_grid) - set(covered_points)
    return calc_tuning_frequency(empty_point[0], empty_point[1])


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
    solve_b(my_puzzle)
