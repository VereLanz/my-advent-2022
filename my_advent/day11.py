from dataclasses import dataclass
import math
import operator
from pathlib import Path
from typing import Callable

from tqdm import tqdm

from my_advent import get_todays_puzzle, MyPuzzle


INSPECTION_ROUNDS = 20
HUGE_INSPECTION_ROUNDS = 10_000
OPERATION_FUNCS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda x, y: int(operator.truediv(x, y)),
}
DOUBLE_OPERATION_FUNCS = {  # if operand y is also x, operand y will be set to 2
    "+": operator.mul,
    "-": lambda x, _: operator.sub(x, x),
    "*": operator.pow,
    "/": lambda x, _: int(operator.truediv(x, x)),
}


@dataclass
class Monkey:
    items_worry: list[int]
    operation: Callable
    operand: int
    test_divisor: int
    true_target: int
    false_target: int
    inspected_amount: int = 0
    
    def inspect_item(
        self, current_worry: int, relieved: bool = True, worry_reduction: int = 3
    ):
        current_worry = self.operation(current_worry, self.operand)
        self.inspected_amount += 1
        if relieved:
            return current_worry // worry_reduction
        return current_worry % worry_reduction
    
    def _find_target_monkey(self, current_worry: int):
        if current_worry % self.test_divisor == 0:
            return self.true_target
        return self.false_target
    
    def throw_item(self, current_worry: int):
        target = self._find_target_monkey(current_worry)
        del self.items_worry[0]
        return target
    
    
def parse_monkey_init(monkey_init: list[str]) -> Monkey:
    # simply with replacing string forms, could probably use regex
    worry_levels = monkey_init[0].strip().replace("Starting items: ", "").split(",")
    worry_levels = [int(w) for w in worry_levels]
    
    operate = monkey_init[1].strip().replace("Operation: new = old ", "").split()
    if operate[1].isdigit():
        operation = OPERATION_FUNCS[operate[0]]
        operand = int(operate[1])
    elif operate[1] == "old":
        operation = DOUBLE_OPERATION_FUNCS[operate[0]]
        operand = 2
    
    test_divisor = int(monkey_init[2].strip().replace("Test: divisible by ", ""))
    true_target = int(monkey_init[3].strip().replace("If true: throw to monkey ", ""))
    false_target = int(monkey_init[4].strip().replace("If false: throw to monkey ", ""))
    
    return Monkey(
        worry_levels, operation, operand, test_divisor, true_target, false_target
    )
    

def big_monkey_business(inputs: list[str]) -> int:
    # initialise monkeys
    monkeys: list[Monkey] = []
    for i in range(1, len(inputs), 7):
        monkey_init = inputs[i : i + 5]
        monkeys.append(parse_monkey_init(monkey_init))
    
    # for each monkey (20 rounds)
    for i in range(INSPECTION_ROUNDS):
        for monkey in monkeys:
            for item_worry in monkey.items_worry.copy():
                current_worry = monkey.inspect_item(item_worry)
                target = monkey.throw_item(current_worry)
                monkeys[target].items_worry.append(current_worry)
    
    monkey_business = sorted([m.inspected_amount for m in monkeys])[-2:]
    return operator.mul(*monkey_business)


def huge_monkey_business(inputs: list[str]) -> int:
    # initialise monkeys
    monkeys: list[Monkey] = []
    for i in range(1, len(inputs), 7):
        monkey_init = inputs[i : i + 5]
        monkeys.append(parse_monkey_init(monkey_init))
    # "find another way to keep your worry managable"
    lcm = math.lcm(*[m.test_divisor for m in monkeys])
    
    # for each monkey (10 000 rounds)
    for i in tqdm(range(HUGE_INSPECTION_ROUNDS)):
        for monkey in monkeys:
            for item_worry in monkey.items_worry.copy():
                current_worry = monkey.inspect_item(
                    item_worry, relieved=False, worry_reduction=lcm
                )
                target = monkey.throw_item(current_worry)
                monkeys[target].items_worry.append(current_worry)
    
    monkey_business = sorted([m.inspected_amount for m in monkeys])[-2:]
    return operator.mul(*monkey_business)


def solve_a(puzzle: MyPuzzle):
    answer_a = big_monkey_business(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = huge_monkey_business(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    # solve_a(my_puzzle)
    # solve_b(my_puzzle)
