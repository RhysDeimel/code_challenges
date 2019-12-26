def get_inputs(file):
    with open(file, "r") as fd:
        number_string = fd.read().split(",")
        return [int(num) for num in number_string]


def add(ints, position):
    pos1, pos2, result_pos = ints[position + 1: position + 4]
    ints[result_pos] = ints[pos1] + ints[pos2]

def multiply(ints, position):
    pos1, pos2, result_pos = ints[position + 1: position + 4]
    ints[result_pos] = ints[pos1] * ints[pos2]


def program_one(ints):
    CODES = {
        1: add,
        2: multiply,
        99: False
    }
    prog_len = len(ints) - 1

    for i in range(0, prog_len, 4):
        f = CODES[ints[i]]
        if f:
            f(ints, i)
        else:
            break




if __name__ == "__main__":
    inputs = get_inputs("input.txt")

    # init according to instructions
    inputs[1] = 12
    inputs[2] = 2

    program_one(inputs)

    print(f"Part one solution: {inputs[0]}")
