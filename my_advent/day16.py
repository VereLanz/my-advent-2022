from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


TIME_AVAILABLE = 30  # minutes = steps
    

class Valve:
    def __init__(self, name: str, flow_rate: int, neighbours: list[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours
        self.open = False
        # self.neighbours_weight
        
    def flow(self) -> int:
        if open:
            return self.flow_rate
        return 0
 
 
def parse_valves(inputs: list[str]) -> dict[Valve]:
    valves = {}
    for line in inputs:
        name, attributes = line.replace("Valve ", "").split(" has flow rate=")
        flow_rate, neighbours = attributes.split("; tunnels lead to valves ")
        valves[name] = Valve(name, int(flow_rate), neighbours.split(", "))
    return valves
    

def max_pressure_release(inputs: list[str]) -> int:
    valves = parse_valves(inputs)
    pressure_released = open_pressure = 0
    position = "AA"
    # currently all are closed
    valves_to_open = [v.name for v in valves.items() if v.flow_rate > 0]
    for i in range(TIME_AVAILABLE):
        pressure_released += open_pressure
        # find how to calculate which decision to take
        # something with flow_rate / (distance + 1) ?
        possible_routes = valves[position].neighbours
        # if step towards a valve
        # -> position = stepped towards
        # elif open valve
        # -> open_pressure += valves[position].flow_rate
    return pressure_released


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = max_pressure_release(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = b(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
