import copy
import pytest
import solution as s

p1_test_input = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
    "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
    "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
]

p2_test_input = [
    "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
    "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007",
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
    "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
]

formatted_input = [
    {
        "hcl": "#888785",
        "hgt": "164cm",
        "byr": "2001",
        "iyr": "2015",
        "cid": "88",
        "pid": "545766238",
        "ecl": "hzl",
        "eyr": "2022",
    }
]


class TestUnit:
    def test_get_inputs(self):
        result = s.get_inputs("input.txt")
        assert (
            result[0]
            == "ecl:hzl byr:1926 iyr:2010 pid:221225902 cid:61 hgt:186cm eyr:2021 hcl:#7d3b0c"
        )
        assert result[-1] == "byr:2000 ecl:hzl eyr:2029 iyr:2011 hcl:#866857 hgt:74in"

    def test_format_inputs(self):
        given = p2_test_input[-2:-1] # slice because I want a list
        expected = copy.deepcopy(formatted_input)
        assert s.format_inputs(given) == expected

    def test_Passport_checks_byr(self):
        valid_byr = ("1920","2002")
        invalid_byr = ("1919","2003")

        given = copy.deepcopy(formatted_input[0])
        given["byr"] = valid_byr[0]

        p = s.Passport(**given)
        assert p.byr in valid_byr
        p.byr = valid_byr[1]
        assert p.byr in valid_byr

        with pytest.raises(ValueError):
            p.byr = invalid_byr[0]
        with pytest.raises(ValueError):
            p.byr = invalid_byr[1]


    def test_Passport_checks_iyr(self):
        valid_iyr = ("2010","2020")
        invalid_iyr = ("2009","2021")

        given = copy.deepcopy(formatted_input[0])
        given["iyr"] = valid_iyr[0]

        p = s.Passport(**given)
        # assert valid_iyr[0] <= p.iyr <= valid_iyr[1]
        assert p.iyr == valid_iyr[0]
        p.iyr = valid_iyr[1]
        assert p.iyr == valid_iyr[1]

        with pytest.raises(ValueError):
            p.iyr = invalid_iyr[0]
        with pytest.raises(ValueError):
            p.iyr = invalid_iyr[1]

    def test_Passport_checks_eyr(self):
        valid_eyr = ("2020","2030")
        invalid_eyr = ("2019", "2031")

        given = copy.deepcopy(formatted_input[0])
        given["eyr"] = valid_eyr[0]

        p = s.Passport(**given)
        assert p.eyr == valid_eyr[0]
        p.eyr = valid_eyr[1]
        assert p.eyr == valid_eyr[1]

        with pytest.raises(ValueError):
            p.eyr = invalid_eyr[0]
        with pytest.raises(ValueError):
            p.eyr = invalid_eyr[1]

    def test_Passport_checks_hgt(self):
        valid_hgt = ("150cm", "193cm", "59in", "76in")
        invalid_hgt = ("149cm", "194cm", "58in", "77in", "22")

        given = copy.deepcopy(formatted_input[0])
        p = s.Passport(**given)

        for value in valid_hgt:
            p.hgt = value
            assert p.hgt == value

        for value in invalid_hgt:
            with pytest.raises(ValueError):
                p.hgt = value

    def test_Passport_checks_hcl(self):
        valid_hcl = ("#123abc", "#623a2f", "#a97842", "#888785")
        invalid_hcl = ("#123abz", "123abc", "dab227", "74454a", "#123abcc")

        given = copy.deepcopy(formatted_input[0])
        p = s.Passport(**given)

        for value in valid_hcl:
            p.hcl = value
            assert p.hcl == value

        for value in invalid_hcl:
            with pytest.raises(ValueError):
                p.hcl = value

    def test_Passport_checks_ecl(self):
        valid = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        invalid = ("bmb", "asdasd", "", "123")

        given = copy.deepcopy(formatted_input[0])
        p = s.Passport(**given)

        for value in valid:
            p.ecl = value
            assert p.ecl == value

        for value in invalid:
            with pytest.raises(ValueError):
                p.ecl = value

    def test_Passport_checks_pid(self):
        valid = ("000000001", "087499704", "896056539", "545766238", "093154719")
        invalid = ("0123456789", "186cm", "02157", "3556412378")

        given = copy.deepcopy(formatted_input[0])
        p = s.Passport(**given)

        for value in valid:
            p.pid = value
            assert p.pid == value

        for value in invalid:
            with pytest.raises(ValueError):
                p.pid = value

    def test_Passport_handles_no_cid(self):
        given = copy.deepcopy(formatted_input[0])
        del given["cid"]
        s.Passport(**given)


class TestFunctional:
    def test_program_one(self):
        assert s.program_one(p1_test_input) == 2

    def test_program_two(self):
        assert s.program_two(p2_test_input) == 4
