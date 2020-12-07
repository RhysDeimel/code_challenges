import solution as s

test_input = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
    "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
    "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
]


class TestUnit:
    def test_get_inputs(self):
        result = s.get_inputs("input.txt")
        assert (
            result[0]
            == "ecl:hzl byr:1926 iyr:2010 pid:221225902 cid:61 hgt:186cm eyr:2021 hcl:#7d3b0c"
        )
        assert result[-1] == "byr:2000 ecl:hzl eyr:2029 iyr:2011 hcl:#866857 hgt:74in"


class TestFunctional:
    def test_program_one(self):
        assert s.program_one(test_input) == 2
