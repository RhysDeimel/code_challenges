from dataclasses import dataclass


@dataclass(frozen=True)
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: int
    cid: int = None


def get_inputs(file):
    with open(file, "r") as fd:
        passports = fd.read().rstrip().split("\n\n")
        return [passport.replace("\n", " ") for passport in passports]


def program_one(inputs):
    cleaned = [
        [passport_data.split(":") for passport_data in item.split()] for item in inputs
    ]
    passports = [dict(item) for item in cleaned]

    valid_passports = []
    for item in passports:
        try:
            valid_passports.append(Passport(**item))
        except TypeError:
            pass

    return len(valid_passports)


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    # print(f"Part two solution: {program_two(inputs)}")
