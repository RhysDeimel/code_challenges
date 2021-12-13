import solutions
import pytest


@pytest.fixture
def example1():
    with open("example1.txt") as fd:
        puzzle_input = fd.read()

    return solutions.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [
        [
            (
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ),
            ("fdgacbe", "cefdb", "cefbgd", "gcbe"),
        ],
        [
            (
                "edbfga",
                "begcd",
                "cbg",
                "gc",
                "gcadebf",
                "fbgde",
                "acbgfd",
                "abcde",
                "gfcbed",
                "gfec",
            ),
            ("fcgedb", "cgb", "dgebacf", "gc"),
        ],
        [
            (
                "fgaebd",
                "cg",
                "bdaec",
                "gdafb",
                "agbcfd",
                "gdcbef",
                "bgcad",
                "gfac",
                "gcb",
                "cdgabef",
            ),
            ("cg", "cg", "fdcagb", "cbg"),
        ],
        [
            (
                "fbegcd",
                "cbd",
                "adcefb",
                "dageb",
                "afcb",
                "bc",
                "aefdc",
                "ecdab",
                "fgdeca",
                "fcdbega",
            ),
            ("efabcd", "cedba", "gadfec", "cb"),
        ],
        [
            (
                "aecbfdg",
                "fbg",
                "gf",
                "bafeg",
                "dbefa",
                "fcge",
                "gcbea",
                "fcaegb",
                "dgceab",
                "fcbdga",
            ),
            ("gecf", "egdcabf", "bgf", "bfgea"),
        ],
        [
            (
                "fgeab",
                "ca",
                "afcebg",
                "bdacfeg",
                "cfaedg",
                "gcfdb",
                "baec",
                "bfadeg",
                "bafgc",
                "acf",
            ),
            ("gebdcfa", "ecba", "ca", "fadegcb"),
        ],
        [
            (
                "dbcfg",
                "fgd",
                "bdegcaf",
                "fgec",
                "aegbdf",
                "ecdfab",
                "fbedc",
                "dacgb",
                "gdcebf",
                "gf",
            ),
            ("cefg", "dcbef", "fcge", "gbcadfe"),
        ],
        [
            (
                "bdfegc",
                "cbegaf",
                "gecbf",
                "dfcage",
                "bdacg",
                "ed",
                "bedf",
                "ced",
                "adcbefg",
                "gebcd",
            ),
            ("ed", "bcgafe", "cdgba", "cbgef"),
        ],
        [
            (
                "egadfb",
                "cdbfeg",
                "cegd",
                "fecab",
                "cgb",
                "gbdefca",
                "cg",
                "fgcdab",
                "egfdb",
                "bfceg",
            ),
            ("gbdfcae", "bgc", "cg", "cgb"),
        ],
        [
            (
                "gcafb",
                "gcf",
                "dcaebfg",
                "ecagb",
                "gf",
                "abcdeg",
                "gaef",
                "cafbge",
                "fdbac",
                "fegbdc",
            ),
            ("fgae", "cfgab", "fg", "bagce"),
        ],
    ]


def test_part1_example1(example1):
    assert solutions.part1(example1) == 26


def test_part2_example1(example1):
    assert solutions.part2(example1) == 61229
