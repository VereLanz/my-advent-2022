from my_advent.day21 import translate_monkey_numbers as a
from my_advent.day21 import b as b


EXAMPLE_INPUT = [
    "root: pppw + sjmn",
    "dbpl: 5",
    "cczh: sllz + lgvd",
    "zczc: 2",
    "ptdq: humn - dvpt",
    "dvpt: 3",
    "lfqf: 4",
    "humn: 5",
    "ljgn: 2",
    "sjmn: drzm * dbpl",
    "sllz: 4",
    "pppw: cczh / lfqf",
    "lgvd: ljgn * ptdq",
    "drzm: hmdt - zczc",
    "hmdt: 32",
]


def test_example_a():
    example_result = 152
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
