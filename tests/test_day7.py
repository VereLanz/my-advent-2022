from my_advent.day7 import get_small_folders as a
from my_advent.day7 import free_up_space as b


EXAMPLE_INPUT = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def test_example_a():
    example_result = 95437
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 24933642
    assert b(EXAMPLE_INPUT) == example_result
