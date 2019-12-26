def get_inputs(file):
    with open(file, "r") as fd:
        number_string = fd.read().split(",")
        return [int(num) for num in number_string]


def add(mem, address):
    param_1, param_2, result_param = mem[address + 1: address + 4]
    mem[result_param] = mem[param_1] + mem[param_2]

def multiply(mem, address):
    param_1, param_2, result_param = mem[address + 1: address + 4]
    mem[result_param] = mem[param_1] * mem[param_2]


def program_one(mem):
    CODES = {
        1: add,
        2: multiply,
        99: False
    }
    prog_len = len(mem) - 1

    for i in range(0, prog_len, 4):
        f = CODES[mem[i]]
        if f:
            f(mem, i)
        else:
            break

def program_two(mem):
    pass



if __name__ == "__main__":
    inputs = get_inputs("input.txt")

    # init according to instructions
    inputs[1] = 12
    inputs[2] = 2

    program_one(inputs)

    print(f"Part one solution: {inputs[0]}")
