def get_inputs(file):
    with open(file, "r") as fd:
        lines = fd.read().splitlines()
        return [int(line) for line in lines]


def simple_calc_module_fuel(mass):
    return (mass // 3) - 2


def calc_module_fuel(mass):
    fuel = (mass // 3) - 2

    if fuel <= 0:
        return 0
    else:
        return calc_module_fuel(fuel) + fuel


def solution(modules, f):
    total_fuel = 0
    for module in modules:
        total_fuel += f(module)

    return total_fuel


if __name__ == "__main__":
    inputs = get_inputs("input.txt")

    print(f"Part one solution: {solution(inputs, simple_calc_module_fuel)}")
    print(f"Part two solution: {solution(inputs, calc_module_fuel)}")
