def get_inputs(file):
    with open(file, "r") as fd:
        lines = fd.read().splitlines()
        return [int(line) for line in lines]

def calc_module_fuel(mass):
    return (mass // 3) - 2


def main(modules):
    total_fuel = 0
    for module in modules:
        total_fuel += calc_module_fuel(module)

    print(total_fuel)
    return total_fuel


if __name__ == "__main__":
    main(get_inputs("input.txt"))
