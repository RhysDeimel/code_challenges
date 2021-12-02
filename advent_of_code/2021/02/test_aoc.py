import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


def test_part1_example1(example1):
    assert solutions.part1(example1) == 150


def test_part2_example1(example1):
    assert solutions.part2(example1) == 900
