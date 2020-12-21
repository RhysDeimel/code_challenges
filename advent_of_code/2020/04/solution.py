import re
from dataclasses import dataclass


@dataclass(frozen=True)
class SimplePassport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: int
    cid: int = None


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @property
    def byr(self):
        return self._byr

    @byr.setter
    def byr(self, value):
        if value < "1920" or value > "2002":
            raise ValueError("Byr is not valid")
        self._byr = value

    @property
    def iyr(self):
        return self._iyr

    @iyr.setter
    def iyr(self, value):
        if value < "2010" or value > "2020":
            raise ValueError("Iyr is not valid")
        self._iyr = value

    @property
    def eyr(self):
        return self._eyr

    @eyr.setter
    def eyr(self, value):
        if value < "2020" or value > "2030":
            raise ValueError("Eyr is not valid")
        self._eyr = value

    @property
    def hgt(self):
        return self._hgt

    @hgt.setter
    def hgt(self, value):
        unit = value[-2:]
        height = value[:-2]
        if unit == "cm":
            if "150" <= height <= "193":
                self._hgt = value
                return
        elif unit == "in":
            if "59" <= height <= "76":
                self._hgt = value
                return
        
        raise ValueError("Hgt is not valid")

    @property
    def hcl(self):
        return self._hcl

    @hcl.setter
    def hcl(self, value):
        if re.search('^#[1-9a-f]{6}$', value) != None:
            self._hcl = value
        else:
            raise ValueError("Hcl is not valid")


    @property
    def ecl(self):
        return self._ecl

    @ecl.setter
    def ecl(self, value):
        allowed_values = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        if value in allowed_values:
            self._ecl = value
        else:
            raise ValueError("Ecl is not valid")

    @property
    def pid(self):
        return self._pid
    
    @pid.setter
    def pid(self, value):
        if re.search('^[0-9]{9}$', value) != None:
            self._pid = value
        else:
            raise ValueError("Pid is not valid")


def get_inputs(file):
    with open(file, "r") as fd:
        passports = fd.read().rstrip().split("\n\n")
        return [passport.replace("\n", " ") for passport in passports]


def format_inputs(inputs):
    split = [
        [passport_data.split(":") for passport_data in item.split()] for item in inputs
    ]
    return [dict(item) for item in split]


def program_one(inputs):
    passports = format_inputs(inputs)

    valid_passports = []
    for item in passports:
        try:
            valid_passports.append(SimplePassport(**item))
        except TypeError:
            pass

    return len(valid_passports)


def program_two(inputs):
    passports = format_inputs(inputs)

    valid_passports = []
    for item in passports:
        try:
            valid_passports.append(Passport(**item))
        except (TypeError, ValueError):
            pass

    return len(valid_passports)


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    print(f"Part two solution: {program_two(inputs)}")
