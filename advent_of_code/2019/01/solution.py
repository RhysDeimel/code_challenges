def get_inputs(file):
    with open(file, "r") as fd:
        lines = fd.read().splitlines()
        return [int(line) for line in lines]


def simple_calc_module_fuel(mass):
    return (mass // 3) - 2


def soultion_part_one(modules):
    total_fuel = 0
    for module in modules:
        total_fuel += simple_calc_module_fuel(module)

    print(f"Part one solution: {total_fuel}")
    return total_fuel


# def calc

if __name__ == "__main__":
    soultion_part_one(get_inputs("input.txt"))
