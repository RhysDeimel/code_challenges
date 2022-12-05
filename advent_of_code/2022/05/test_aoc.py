import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


@pytest.fixture
def input():
    with open("input.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    crates, moves = list(example1)
    assert crates == [[" ", "D", " "], ["N", "C", " "], ["Z", "M", "P"]]
    assert moves == [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]


def test_parse_input(input):
    # explicit test for input because crate space is larger
    crates, _ = list(input)
    assert crates == [
        ["N", " ", " ", "C", " ", "Z", " ", " ", " "],
        ["Q", "G", " ", "V", " ", "S", " ", " ", "V"],
        ["L", "C", " ", "M", " ", "T", " ", "W", "L"],
        ["S", "H", " ", "L", " ", "C", "D", "H", "S"],
        ["C", "V", "F", "D", " ", "D", "B", "Q", "F"],
        ["Z", "T", "Z", "T", "C", "J", "G", "S", "Q"],
        ["P", "P", "C", "W", "W", "F", "W", "J", "C"],
        ["T", "L", "D", "G", "P", "P", "V", "N", "R"],
    ]


def test_part1_example1(example1):
    assert solutions.part1(example1) == "CMZ"


def test_part2_example1(example1):
    assert solutions.part2(example1) == "MCD"
