
CODES = {
    1: add,
    2: multiply,
}

def get_inputs(file):
    with open(file, "r") as fd:
        number_string = fd.read().split(",")
        return [int(num) for num in number_string]


def add(ints, position):
    pass

def multiply():
    pass


def run_intcode(ints):
    # position = 0
    # total_len = len(ints)
    # if position > total_len:
    #     return
    pass



if __name__ == "__main__":
    inputs = get_inputs("input.txt")

    # init according to instructions
    inputs[1] = 12
    inputs[2] = 2


    print(f"Part one solution: {inputs[0]}")
