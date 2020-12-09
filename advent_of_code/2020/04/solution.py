from dataclasses import dataclass


@dataclass(frozen=True)
class Pssport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: int
    cid: int = None


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
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

#     @eyr.setter
#     def eyr(self, value):
#         pass

#     @hgt.setter
#     def hgt(self, value):
#         pass

#     @hcl.setter
#     def hcl(self, value):
#         pass

#     @ecl.setter
#     def ecl(self, value):
#         pass

#     @pid.setter
#     def pid(self, value):
#         pass

#     @cid.setter
#     def cid(self, value):
#         pass


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
            valid_passports.append(Pssport(**item))
        except TypeError:
            pass

    return len(valid_passports)


def program_two(inputs):
    pass


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    print(f"Part two solution: {program_two(inputs)}")
