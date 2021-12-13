from collections import Counter


def parse(puzzle_input):
    data = []
    lines = [line for line in puzzle_input.rstrip().split("\n")]
    for line in lines:
        signal, output = line.split(" | ")
        signal = signal.split(" ")
        output = output.split(" ")

        data.append([tuple(signal), tuple(output)])

    return data


class Display:
    # I do not like this. Needs refactoring
    def __init__(self, signal, output):
        self.raw_signal = signal
        self.raw_output = output
        self.cipher = {}
        self.output = self._decode_output()

    def _find_five_segment(self, val):
        length = len(set(val) - self.cipher["4"])
        match length:
            case 2:
                l = len(set(val) - self.cipher["1"])
                match l:
                    case 3:
                        self.cipher["3"] = set(val)
                    case 4:
                        self.cipher["5"] = set(val)
            case 3:
                self.cipher["2"] = set(val)

    def _find_six_segment(self, val):
        length = len(set(val) - self.cipher["4"])
        match length:
            case 2:
                self.cipher["9"] = set(val)
            case 3:
                l = len(set(val) - self.cipher["1"])
                match l:
                    case 4:
                        self.cipher["0"] = set(val)
                    case 5:
                        self.cipher["6"] = set(val)

    def _unique_signals(self):
        for jumble in self.raw_signal:
            length = len(jumble)
            match length:
                case 2:
                    key = "1"
                case 3:
                    key = "7"
                case 4:
                    key = "4"
                case 7:
                    key = "8"
                case _:
                    continue

            val = set(jumble)
            self.cipher[key] = val

    def _other_signals(self):
        for jumble in self.raw_signal:
            length = len(jumble)
            match length:
                case 5:
                    self._find_five_segment(jumble)
                case 6:
                    self._find_six_segment(jumble)

    def _decode_output(self):
        self._unique_signals()
        self._other_signals()

        dct = {}
        for k, v in self.cipher.items():
            new_key = "".join(sorted(v))
            new_val = k
            dct[new_key] = new_val
        data = []
        for item in self.raw_output:
            val = "".join(sorted(item))
            data.append(dct[val])

        return data


def part1(data):
    displays = [Display(signal, output) for signal, output in data]

    count = Counter()
    for display in displays:
        count.update(display.output)

    return sum([count["1"], count["4"], count["7"], count["8"]])


def part2(data):
    displays = [Display(signal, output) for signal, output in data]
    outputs = [int("".join(display.output)) for display in displays]
    return sum(outputs)


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    print(f"Solution 1: {solution1}")
    print(f"Solution 2: {solution2}")


if __name__ == "__main__":
    with open("input.txt") as fd:
        puzzle_input = fd.read()

    solve(puzzle_input)
