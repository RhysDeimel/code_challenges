from collections import namedtuple


def get_inputs(file):
    with open(file, "r") as fd:
        return fd.read().splitlines()


def process_inputs(inputs):
    PassPol = namedtuple("PassPol", ["min", "max", "letter", "password"])
    results = []

    for line in inputs:
        a, b, password = line.split(" ")
        l_min, l_max = a.split("-")
        letter = b[0]

        results.append(
            PassPol(min=int(l_min), max=int(l_max), letter=letter, password=password)
        )

    return results


def program_one(inputs):
    items = process_inputs(inputs)
    valid_passwords = 0

    for item in items:
        occurances = item.password.count(item.letter)

        if item.min <= occurances <= item.max:
            valid_passwords += 1

    return valid_passwords


def program_two(inputs):
    items = process_inputs(inputs)
    valid_passwords = 0

    for item in items:
        first = item.password[item.min - 1] == item.letter
        second = item.password[item.max - 1] == item.letter

        if first ^ second:  # xor
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    inputs = get_inputs("input.txt")
    print(f"Part one solution: {program_one(inputs)}")
    print(f"Part two solution: {program_two(inputs)}")
